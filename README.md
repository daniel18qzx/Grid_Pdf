## 手邊方格紙剛好用完，要不自己做一個？

這項目的緣起只是因為早上忽然發現家中的方格紙沒了，外頭又再下大雨，閒閒沒事想說自己來尻一下順便練習 python 手感


## 項目目標
*   熟悉 Reportlab 的繪圖與 PDF 檔案匯出操作
*   熟悉物件導向，力求主程式簡單
*   熟悉項目資料夾架構
*   [範例](https://github.com/danielrapen3184/GridPdf/blob/master/MyGraphPaper.pdf)


## 使用語言

*   Python


## 我使用的工具

*   Sublime
*   Git
    *   Tower (Mac only)


## 學習需要能力/材料
### 強烈建議

*   家裡有印表機
*   有支持世大運
*   按這篇文章讚

### 有會更好

*   物件導向概念
*   基本 list 概念與操作方法
*   package 安裝方法
*   一點點程式邏輯拆解怎麼用一個 function 畫出主/副線框

## How to use it?

1.  [Open the GitHub repository](https://github.com/danielrapen3184/GridPdf)
2.  Fork it
3.  Clone it and create a copy on your computer
4.  Modify the settings.py file
6.  Run the main.py

## How to learn it?

1. Check the tutorial of reportlab package first, get to know how to create a canvas, put something on it and export it to the pdf file
2. Check how does the grid function works
3. Start to build the basic main python file: create a canvas > generate the grid > export
4. Use list .append() and while loop function to create the xlist/ylist (pls check out myfunc.py/xylist)
5. Because u would like to add a major grid in the end, so pls make sure the total numbers of both columns and rows u create can be divided by 5, the hint is trying to use the for loop inside the while loop
6. Write a boolean variable into your fun, so that both major/minor grids can call it
7. Use xylist to draw a grid
8. Now u might find out the whole grid doesn't locate at the middle
9. Create the align() function to compute the right starting point, then pass the value to xylist[0]
10. Everything just done, but try to do more! Separate all the setting and canvas Spec from main.py

## Settings Attributes
```python
class Settings():

    def __init__(self):
        self.filename="MyGraphPaper" #no need to assign a file extention
        self.size=A4 #check the default setting below
        self.xgap=0.5 #in cm
        self.ygap=.5 #in cm
        self.footer="Copyright © 2017 Dan Project"

        #Minor line setting:
        self.colorMinor=pink #check the default setting below
        self.lineWidthMinor=1

        #Major line setting: if u dont want the major grid, set the majorLine=False
        self.majorLine=True
        self.colorMajor=pink #check the default setting below
        self.lineWidthMajor=2<div>

    <html lang="zh-Hant-CN">

</div>
```

* * *

### 推薦文章：

> https://www.google.com.tw/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwjI3M6wlPfVAhXNq5QKHbHiAfQQFggxMAE&url=https%3A%2F%2Fwww.reportlab.com%2Fdocs%2Freportlab-userguide.pdf&usg=AFQjCNGZMKURmDlJw9uZ_mAIXO5tlMI81g
> https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
> https://python.swaroopch.com/oop.html
> http://www.python-course.eu/object_oriented_programming.php