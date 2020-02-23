# 爬取豆瓣新书速递
保存书本封面和信息，并生成一个网页
## 运行
需要的第三方库
```
pip install requests
pip install lxml
```
标准库
```
import os
import time
import json
import webbrowser
```
## 如何保存
在当前py文件目录下创建一个时间格式的文件夹<br>
里面以书名创建文件夹，非法字符用"_"代替<br>
书名文件夹内保存封面图片和json文件<br>
json文件保存封面路径、书名、作者、出版时间、出版社、书本简介、豆瓣链接<br>
并根据回应的response生成一个网页方便阅读<br>