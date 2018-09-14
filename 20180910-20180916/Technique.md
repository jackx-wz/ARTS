# brew 升级 mysql 8 之后不能使用
在直接升级 mysql 之后，能够连接进去，但是一直不能 show databases

```
ERROR 1449 (HY000): The user specified as a definer ('mysql.infoschema'@'localhost') does not exist
```
这个问题是数据库软件升级了，数据库的数据也需要升级
```
/usr/local/opt/mysql/bin/mysql_upgrade -uroot -p
```


连接成功，但不能查询到数据
```
往这个文件中 /usr/local/etc/my.cnf 的 [mysqld] 中添加
default_authentication_plugin=mysql_native_password

重启数据库
sudo /usr/local/opt/mysql/support-files/mysql.server restart
```