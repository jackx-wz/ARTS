# php 的匿名函数
[匿名函数](http://php.net/manual/zh/functions.anonymous.php)

[静态匿名函数](http://php.net/manual/zh/functions.anonymous.php#functions.anonymous-functions.static)

> 在写 swoole 的时候发现类中的匿名函数，居然可以直接使用 $this 调用到外部类的对象，于是开始翻手册。发现如果是在类中的匿名函数在 php5.4 之后会直接绑定外部类的 $this。如果不想要它绑定使用静态匿名函数。

### 匿名函数绑定 $this
```
class Test{
    public $name = "amanda";

    public function take(){
        $age = 18;
        $callback = function(){
            var_dump($this, $age);
        };

        return $callback;
    }
}

$obj = new Test();
$obj->take()();

输出：
class Test#1 (1) {
  public $name =>
  string(6) "amanda"
}
NULL        //匿名函数使用不了外部的变量，只能使用 $this
```

### 匿名函数不绑定 $this
```
class Test{
    public $name = "amanda";

    public function take(){
        $age = 18;
        $callback = static function(){
            var_dump($this, $age);
        };

        return $callback;
    }
}

$obj = new Test();
$obj->take()();

输出：
PHP Fatal error:  Uncaught Error: Using $this when not in object context in
```