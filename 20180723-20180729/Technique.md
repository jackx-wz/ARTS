# php 实现 websocket
> 几年前接触了 swoole，当时就迷上了，毕竟它解决了 PHP 的好几个大问题。常驻内存，C语言级别的效率，实现多种协议的服务器等等。想法是美好的，只是当时我用的版本比较低，好多功能都有 BUG 。现在重新捡起来发现已经发展得很好了。

```
$server = new swoole_websocket_server("0.0.0.0", 9501);

$server->on('open', function (swoole_websocket_server $server, $request) {
    echo "server: handshake success with fd{$request->fd}\n";
});

$server->on('message', function (swoole_websocket_server $server, $frame) {
    echo "receive from {$frame->fd}:{$frame->data},opcode:{$frame->opcode},fin:{$frame->finish}\n";
    $server->push($frame->fd, "this is server");
});

$server->on('close', function ($ser, $fd) {
    echo "client {$fd} closed\n";
});

$server->start();

```