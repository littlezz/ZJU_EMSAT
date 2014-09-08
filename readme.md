
to do
==========
1. 测试ajax  ----------------->done
2. 从无到有创建满课表  -------------->done
3. 测试ajax post
4. 测试部分有课的情况创建满课表
5. 测试选退课 ajax post 处理
6. 添加其他课表限制
7. 添加API,测试
8. 测试.


micro
-----------
- use attrgetter for supportkey --done
- use djangoajax
- 添加多重志愿

update
=========
support diffrent seasons! 9-6
修改`supportkey`即可修改返回的参数 9-8


required
==============

django1.7
--------------

抓取课程要添加的表
--------------------
```
startday = models.IntegerField()               #3
startcourse = models.IntegerField()            #1
firstcourse = models.CharField(max_length=20)  #3,1,2  means fri, the first and second
secondcourse = models.CharField(max_length=20)

season = models.CharField(max_length=10)
```

比如课程是周二3,4节 周四1,2节.    
`startday` 表示这周首次课是哪一天, 这里是 2 (周二)  
`startcourse` 是startday的第一节课 这里是2 (周二的第三节课,从0开始)  
`firstcourse` 字符串,形如 whichday,num1,num2, 表示首天的课程, 这里是 `2,2,3` (周二第3,4节)  
`secondcourse` 同上, 这里是`4,0,1` ,如果没用着为空.  

`season` 哪个学期,取值0-3 逗号隔开,比如秋冬 `2,3`, 春`0`  

抓课表的时候记得没有上课时间的,或者没有学期的课程直接过滤掉,不要写进数据库.

Note
=============

1. django 果真不适合一开始就有数据库,重新抓课程时记得加上新的表
2. 要兼容python2,束手束脚,后端的算法不好写,考虑:

    - api兼容py3?
    - 接着蛋疼?
    
    BAE 不支持python3.请问我可以说粗口么? 无语


choose
-------------
课表习惯从1 开始计数,但是table 结构从0开始,考虑:

- custom list 的 一些方法? 但是要考虑到py2的super感觉不好用.
- 让数据库也从0开始?

让所有都从0开始.

