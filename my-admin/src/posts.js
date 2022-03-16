// in src/posts.js
import * as React from "react";
import {
    List, 
    Datagrid, 
    TextField, 
    ReferenceField, 
    EditButton,
    Edit,
    SimpleList,
    Create,
    SimpleForm,
    ReferenceInput,
    SelectInput,
    TextInput,
} from "react-admin";

const postFilters = [
    <TextInput source="q" label="Search"  alwaysOn />,
    <ReferenceInput source="userId" label="User" reference="users" allowEmpty>
        <SelectInput optionText="name"/>
    </ReferenceInput>,
];

export const PostList = props => (
    <List filters={postFilters} {...props}>
        {/* <Datagrid rowClick="edit">
        <TextField source="id" />
            <ReferenceField source="userId" reference="users">
                <TextField source="name" /></ReferenceField>
            <TextField source="title" />
            <EditButton/>
        </Datagrid> */}
        <SimpleList 
            primaryText={record => record.title}
            secondaryText={record=> `${record.views} views`}
            tertiaryText={record => new Date(record.published_at).toLocaleDateString()}
        />
    </List>
);

const PostTitle = ({record}) => {
    return <span>Post {record ? `"${record.title}"` : ''}</span>
}

export const PostEdit = props => (
    <Edit title={<PostTitle/>} {...props}>
        <SimpleForm>
            <ReferenceInput source="userId" reference="users">
                <SelectInput optionText="name"/>
            </ReferenceInput>
            <TextInput source="title" />
            <TextInput multiline source="body" />
        </SimpleForm>
    </Edit>
);

export const PostCreate = props => (
    <Create {...props}>
        <SimpleForm>
            <ReferenceInput source="userId" reference="users">
                <SelectInput optionText="name"/>
            </ReferenceInput>
            <TextInput source="title" />
            <TextInput multiline source="body" />
        </SimpleForm>
    </Create>
);