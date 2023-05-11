# 大作业

基于chatpgt进行query分析构建自有知识体系的问答系统。

## 方案优点

1. 对于问答系统比较麻烦的问题就是需要分析query，识别出query里的实体和关系。使用chatgpt可以很容易的完成这个工作。

2. 基于本地知识图谱，解决chatgpt的“幻觉”问题。

## 方案简介

1. 使用neo4j构造一个电影的知识图谱。
![知识图谱](../imgs/kg.jpeg)

2. 使用chatgpt用来分析实体和关系。并构造出neo4j的查询语句。比如：
> **prompt：**
>
> **对下面的语句做实体和关系的分析，生成neo4j的查询语句：周星驰和冯小刚合演的电影有哪些？**

**chatgpt：**
```
实体： 
1. 周星驰 （Person） 
2. 冯小刚（Person） 
3. 电影（Movie） 

关系： 1. 合演（Acted_In） 

查询语句： 
MATCH (周星驰:Person)-[:Acted_In]->(电影:Movie)<-[:Acted_In]-(冯小刚:Person)  WHERE 周星驰.name = '周星驰' AND 冯小刚.name = '冯小刚'   RETURN DISTINCT 电影.title AS 合演电影列表
```

3.执行查询语句。去得结果返回：
![问答系统](../imgs/qa.jpeg)
