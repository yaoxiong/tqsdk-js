#!/usr/bin/env python
#coding=utf-8

case = {
    "id": "ARBR",
    "cname": "人气意愿指标",
    "type": "SUB",
    "src": """
//该模型仅仅用来示范如何根据指标编写简单的模型
//用户需要根据自己交易经验，进行修改后再实际应用!!!
// //后为文字说明，编写模型时不用写出
AR : SUM(HIGH-OPEN,N)/SUM(OPEN-LOW,N)*100;//N个周期内的最高价减去开盘价的和与N个周期内的开盘价减去最低价的和的百分比
BR : SUM(MAX(0,HIGH-REF(CLOSE,1)),N)/SUM(MAX(0,REF(CLOSE,1)-LOW),N)*100;//取最高价减去一个周期前的收盘价的与0中的最大值，求和，取一个周期前的收盘价减去最低价与0中的最大值，求和，两个和的百分比
""",
    "params": [
        ("N", 2, 300, 26),
        ("M", 0, 100, 2),
        ("P", 0, 200, 120),
        ("Q", 0, 200, 30),
    ],
    "expected": """
    """,
}
