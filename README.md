# Focus
![](https://camo.githubusercontent.com/99d9bd01d6c06b87fe268f1daabf2ed978b1767f/68747470733a2f2f63692e6170707665796f722e636f6d2f6170692f70726f6a656374732f7374617475732f74667735377136656563697070736c352f6272616e63682f6d61737465723f7376673d74727565)

本文档用于帮助贡献者和用户在获取本项目的代码之后进行构建、编译和测试。

请注意，本文档和仓库中的所有内容，包括但不限于源代码文件、图片文件、字体文件(除非某些文件本身不开放源代码，那么这时应该遵循或分别遵循该一个或多个文件所遵循的许可证)，遵循[Apache License v2.0](http://www.apache.org/licenses/LICENSE-2.0.html "Apache License v2.0")发布。

### 下载
点击[此处](https://github.com/lenconda/focus/releases "此处")，获取最新版本的下载。

### 构建&编译
#### 前端代码
本项目采用Vue.JS作为前端框架，采用ElementUI作为前端UI框架。如果你希望运行或构建前端部分的代码，请预先搭建好Node.JS和NPM环境。

编译、运行或构建的流程大致如下：

``` bash
# install dependencies
npm install

# serve with hot reload at 0.0.0.0:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

如果你采用第一种方式，那么你将能在本机的`8080`端口访问应用程序，如果你采用第二或第三种方式，你将会在`/dist`目录下得到编译后的最终代码。

#### 后端代码
本项目采用Python作为后端,代码位于`/api`下，环境为Python 3.6，在运行之前，必须安装好以下模块：

```bash
pip install requests flask pymysql
```

完成之后，执行

```bash
/usr/bin/python ./EasyFlask.py
```

Python将会发起一个监听于TCP 3000端口，IP为`0.0.0.0`的进程，通过进一步配置实现前后端交流。

### 数据库

本项目采用MySQL作为默认数据库。

本项目提供一个SQL脚本文件，用于在任意MySQL服务器中导入本项目所需的数据库结构。该文件位于`/sql/focus.sql`。

##### 关于后端连接数据库

后端代码文件中连接数据库的代码片段位于`/api/dbIO.py`中，代码如下：

```python
host="localhost" 			 #数据库服务器地址
port=3306 					  #数据库端口
db="focus" 					 #数据库名称
user="root" 				    #数据库用户名
password="root" 		   #数据库密码
```

### 代理
在Web服务器中添加一个`/api`的路径，反向代理到`http://127.0.0.1:3000`即可完成API部署。
