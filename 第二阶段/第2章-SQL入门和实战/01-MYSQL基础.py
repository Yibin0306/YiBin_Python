"""
在MySQL的命令行环境下，可以通过：
show databases;查看有哪些数据库
use数据库名使用某个数据库
show tables查看数据库内有哪些表
exit退出MySQL的命令行环境

SQL数据库的分类
数据定义：DDL（DataDefinition Language）
    库的创建删除、表的创建删除等
数据操纵： DML（Data Manipulation Language)
    新增数据、删除数据、修改数据等
数据控制：DCL （Data Control Language)
    新增用户、删除用户、密码修改、权限管理等
数据查询：DQL（Data Query Language)
    基于需求查询和计算数据

SQL语言特征
SQL语言，大小写不敏感
SQL可以单行或多行书写，最后以;号结束
SQL支持注释：
    单行注释：-- 注释内容（--后面一定要有一个空格)
    单行注释：# 注释内容 (#后面可以不加空格，推荐加上)
    多行注释：/*注释内容*/
字符串出现在SQL中，必须要用单引号

查看数据库 SHOW DATABASES;
使用数据库 USE数据库名称;
创建数据库CREATE DATABASE数据库名称[CHARSET UTF8];
删除数据库 DROP DATABASE数据库名称;
查看当前使用的数据库 SELECT DATABASE()；

DDL-表管理
查看有哪些表
SHOW TABLES; 注意：需要先选择数据库哦
删除表
DROP TABLE 表名称;
DROP TABLE IF EXISTS 表名称;
创建表
CREATE TABLE表名称（
列名称 列类型，
列名称 列类型，
...）
列类型有
int --整数
float --浮点数
varchar(长度) --文本，长度为数字，做最大长度限制
date --日期类型
timestamp --时间戳类型

条件判断：列 操作符 值
操作符：= < > <= >= != 等等

数据操纵： DML
INSERT 数据插入基础语法:
    INSERT INTO 表[(列1，列2,列N)］ VALUES(值1，值2，值N)[，（值1，值2，...值N)，（值1，值2，...值N)];
DELETE 数据删除基础语法:
    DELETE FROM 表名称 [WHERE 条件判断];
UPDATE 数据更新基础语法:
    UPDATE 表名 SET 列=值 [WHERE 条件判断];

数据查询：DQL
查询基础语法：
    SELECT 字段列表|* FROM 表
查询基础语法-过滤：
    SELECT 字段列表|* FROM 表 WHERE 条件判断
分组聚合基础语法:
    SELECT 字段|聚合函数 FROM 表 [WHERE 条件] GROUP BY 列
聚合函数有：
    SUM(列) 求和
    AVG(列) 求平均值
    MIN(列) 求最小值
    MAX(列) 求最大值
    COUNT(列|*) 求数量
结果排序基础语法：
    SELECT 列|聚合函数| * FROM 表
    WHERE ...
    GROUP BY ...
    ORDER BY ... [ASC|DESC](ASC表示从小到大，DESC表示从大到小)
结果分页限制基础语法：
    SELECT 列|聚合函数| * FROM 表
    WHERE ...
    GROUP BY ...
    ORDER BY ... [ASC|DESC]
    LIMIT n[, m]

执行顺序：FORM -> WHERE ->GROUP BY和聚合函数 -> STELE -> ORDER BY -> LIMIT
"""