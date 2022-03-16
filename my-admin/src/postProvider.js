import { fetchUtils } from "react-admin";
import { stringify} from "query-string";

const apiUrl = "http://192.168.31.40:5001"
// const apiUrl ="https://jsonplaceholder.typicode.com";
// const httpClient = fetchUtils.fetchJson;

const authToken="123123";

const httpClient = (url, options = {}) => {
    if (!options.headers) {
        options.headers = new Headers({ 
        Accept: 'application/json'
    });
    }
  
    options.headers.set('Authorization', authToken);
    return fetchUtils.fetchJson(url, options)
};

export default {
    // 获取列表
    getList: async (resource, params) => {
        const { page, perPage } = params.pagination;
        const { field, order } = params.sort;
        const query = {
            sort: JSON.stringify([field, order]),
            range: JSON.stringify([(page - 1) * perPage, page * perPage - 1]),
            filter: JSON.stringify(params.filter),
        };
        const url = `${apiUrl}/${resource}?${stringify(query)}`;
        const {status, headers, body, json } = await httpClient(url);

        // console.log("status --->", status)
        // console.log("headers --->", headers.get("x-total-count"))
        // console.log("body --->", body)
        return ({
            data: json,
            total: parseInt(headers.get('x-total-count'))
        });
    },
    getOne: (resource, params) =>
        httpClient(`${apiUrl}/${resource}/${params.id}`).then(({ json }) => ({
            data: json,
        })),

    getMany: async (resource, params) => {
        const query = {
            filter: JSON.stringify({ id: params.ids }),
        };
        const url = `${apiUrl}/${resource}?${stringify(query)}`;
        const { json } = await httpClient(url);
        return ({ data: json });
    },

    getManyReference: async (resource, params) => {
        const { page, perPage } = params.pagination;
        const { field, order } = params.sort;
        const query = {
            sort: JSON.stringify([field, order]),
            range: JSON.stringify([(page - 1) * perPage, page * perPage - 1]),
            filter: JSON.stringify({
                ...params.filter,
                [params.target]: params.id,
            }),
        };
        const url = `${apiUrl}/${resource}?${stringify(query)}`;

        const { headers, json } = await httpClient(url);
        return ({
            data: json,
            total: parseInt(headers.get('content-range').split('/').pop(), 10),
        });
    },

    update: (resource, params) =>
        httpClient(`${apiUrl}/${resource}/${params.id}`, {
            method: 'PUT',
            body: JSON.stringify(params.data),
        }).then(({ json }) => ({ data: json })),

    updateMany: async (resource, params) => {
        const query = {
            filter: JSON.stringify({ id: params.ids}),
        };
        const { json } = await httpClient(`${apiUrl}/${resource}?${stringify(query)}`, {
            method: 'PUT',
            body: JSON.stringify(params.data),
        });
        return ({ data: json });
    },

    create: (resource, params) =>
        httpClient(`${apiUrl}/${resource}`, {
            method: 'POST',
            body: JSON.stringify(params.data),
        }).then(({ json }) => ({
            data: { ...params.data, id: json.id },
        })),

    delete: (resource, params) =>
        httpClient(`${apiUrl}/${resource}/${params.id}`, {
            method: 'DELETE',
        }).then(({ json }) => ({ data: json })),

    deleteMany: async (resource, params) => {
        const query = {
            filter: JSON.stringify({ id: params.ids}),
        };
        const { json } = await httpClient(`${apiUrl}/${resource}?${stringify(query)}`, {
            method: 'DELETE',
        });
        return ({ data: json });
    }
};