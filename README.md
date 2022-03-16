# pancake
reactjs admin

# prepare env

```
registry = https://registry.npm.taobao.org
```

# create a project

```
yarn create react-app my-admin
cd my-admin/
yarn add react-admin ra-data-json-server prop-types
yarn start
```

# docs


>host-address:port/<api-name>
使用Resource时，其name可以映射到<api-name>上，使用ListGuesser可以自动展示数据
```
    <Resource name="users" list={ListGuesser} />
```

> 使用ListGuesser可以快速的自适应并展示数据列表，但是在实际生产环境中还是需要自定义列表组件，可以通过查看console可以拿到ListGuesser给出的当前的列表定义;

> 使用 ReferenceField 可以引用关联数据


通过选择下拉输入

```
            <ReferenceInput source="userId" reference="users">
                <SelectInput optionText="name"/>
            </ReferenceInput>
```

#  to visit your data 

open a new chrome windows and then input `http://127.0.0.1:3000` 

see more: https://alfilatov.com/posts/run-chrome-without-cors/

```
open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security
```