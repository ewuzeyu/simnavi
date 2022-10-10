# simnavi-简易导航页


simple navigation page


一个简单的导航页，侧边为目录，点击可跳转。每个网址单元格按钮可分为左右两部分，左边为在当前页面跳转（\_self），右边为在新标签页打开(\_blank)。

## 使用方法

在同目录下.yml文件中配置，col为侧边目录。
```
col:
 - 常用Common
 - 搜索Search
```
之后对应每个目录名字，后面依次填写网址信息，包括名字、描述和地址
```
常用Common:
 -
   name: Apple
   desc: Apple 苹果官网
   url: https://www.apple.com
 -
   name: Microsoft
   desc: 微软官网
   url: https://www.baidu.com
```

运行generator.py即可生成index.html文件，搭配global.css使用即可。
