## day1
- 配置 pip 源
    windows: 
    直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下
    ```
    [global]
    index-url = https://mirrors.aliyun.com/pypi/simple/
    [install]
    trusted-host = https://mirrors.aliyun.com/pypi/simple/  

    ```
- 安装 fastapi
  ```
  pip install fastapi

  ```

- 安装 uvicorn
  ```
  pip install uvicorn

  ```
- hello world 

- api文档 http://127.0.0.1:8000/docs   
- 编辑文档  http://127.0.0.1:8000/redoc 

- 使用 .vscode launch.json 配置

## day2 
 - 用户新增查询restful接口
