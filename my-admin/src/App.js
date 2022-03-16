// in src/App.js

import * as React from "react";
import { Admin, Resource} from "react-admin";
import jsonServerProvider from "ra-data-json-server";
import { PostList, PostEdit, PostCreate} from "./posts";
import { UserList } from "./users";
import PostIcon from '@material-ui/icons/Book';
import UserIcon from '@material-ui/icons/Group';
import Dashboard from "./Dashboard";
import authProvider from "./authProvider";
import postProvider from "./postProvider";

// import { EditGuesser } from "react-admin";

// const dataProvider = jsonServerProvider("https://jsonplaceholder.typicode.com");
// const dataApi = jsonServerProvider("http://127.0.0.1:5001");
const App = () => (
  <Admin dataProvider={postProvider} dashboard={Dashboard} authProvider={authProvider}>
    <Resource name="posts" list={PostList} edit={PostEdit} create={PostCreate} icon={PostIcon}/>
    {/* <Resource name="users" list={UserList} icon={UserIcon}/> */}
  </Admin>
);

export default App;

