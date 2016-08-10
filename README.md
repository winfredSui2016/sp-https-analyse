# Https全站加密工具

## virtualenv

这是 python 的虚拟环境, 用于解决python的依赖以及库的版本不一致问题。

### 安装 virtualenv:

```
[sudo] pip install virtualenv
```

### 创建 virtualenv:

```
virtualenv -p python3 env
```

参数说明:

* `-p python3`: 使用 python3 作为 virtualenv中的python解释器
* env: virtualenv 的存储目录, 存储python程序和依赖库

### 激活 virtualenv:

```
source env/bin/activate
```

参数说明:

* `env/bin/activate`: 是虚拟环境的设置, 使用source导入后会添加虚拟环境的bin到$PATH变量中, 之后当前session命令行中使用的就是virtualenv中的python了

### PyCharm中使用 virtualenv
`PyCharm` -> `Perferences` 菜单 或 `command + ,` -> `Project:{projectname}` -> `Project Interpreter` -> `Add local` -> 选择到virtualenv中的bin/python文件即可
