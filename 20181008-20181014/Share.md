#http 自动跳 https
有些云服务器可以直接在域名解析的时候设置这项功能，但好多是没有这个服务的。那么我们怎么来做？

比如 nginx，当我监听到 80 端口有请求的时候直接转发到 https 上面。

1、重定向方式
具体重定向使用的 http code 可以有很多种。301，302，307 都可以，我喜欢 307，转发的时候会将所有参数也转发过去。

```
server {
    server_name *.touchpeak.net;
    listen 80;
    return 307 https://$host$request_uri;
}
```

2、重写规则

```
server {
    server_name *.touchpeak.net;
    listen  80;
      
    rewrite ^(.*)$  https://$host$1 permanent;  
}
```