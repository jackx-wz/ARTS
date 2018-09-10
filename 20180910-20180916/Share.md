# composer 创建自己的库
```
1、创建包文件夹 test
mkdir -p test/src

2、进入目录
cd test

3、初始化 git 仓库
git init

4、添加需要用到的类到 test/src
cp -r /neox/neox-backend/app/Library src/

5、初始化 composer,安装提示一直填下去
composer init

6、这个时候 src 和 composer.json 都准备好了

7、添加到已有的仓库
git remote add origin https://github.com/xxx/testcomp.git

8、添加命名空间到 composer.json
"autoload": {
    "psr-4": {
        "Fujitaro\\": "src/"
    }
}

9、提交代码
git add .
git commit -m "init composer neox/test"

10、进入需要用上面包的项目中
cd neox-backend

11、添加包地址
vi composer.json

"repositories": [
    {
        "type": "vcs",
        "url": "https://github.com/xxx/testcomp.git"
    }
]

12、安装包
composer require neox/test:dev-master

13、编写代码 a.php

<?php
require __DIR__ . '/vendor/autoload.php';
use Fujitaro\Library\Estate\Kit\Field;

echo Field::RENTAL_PRICE;
```
