# 关系型数据库范式
关系型数据库设计有一些规范：第一范式，第二范式，第三范式，BC范式，第四范式，第五范式，一般都只用到前4个。

> 候选关键字：又叫候选关键码，可以通过它来唯一确定一条记录，可以是单个字段，也可以是多个字段的组合。

> 主键：又叫主码，是从候选关键字中选择出的一个

```
第一范式：所有字段不可再分

第二范式：没有非关键字字段对候选组合关键字的部分依赖

第三范式：第二范式基础上，没有非关键字对任何候选关键字的依赖

BC 范式：第三范式基础上，组合关键字字段之间也不能有依赖关系
```

规范标准:
1、插入异常：插入需要多次操作才是完整步骤，否则会引起数据不一致
2、更新异常：更新需要多次操作，否则会引起数据不一致
3、删除异常：删除需要多次操作，否则会引起数据不一致
4、冗余：重复数据的存储，占用大量空间还减低了操作效率