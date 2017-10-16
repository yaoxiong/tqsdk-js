#!/usr/bin/env python
#coding=utf-8

case = {
    "id": "DKX",
    "cname": "多空线",
    "type": "MAIN",
    "src": """
//该模型仅仅用来示范如何根据指标编写简单的模型
//用户需要根据自己交易经验，进行修改后再实际应用!!!
// //后为文字说明，编写模型时不用写出
A:=(3*C+L+O+H)/6;//3倍收盘价与最高价、最低价、开盘价之和的均值。
B:(20*A+19*REF(A,1)+18*REF(A,2)+17*REF(A,3)+16*REF(A,4)+15*REF(A,5)+14*REF(A,6)+13*REF(A,7)+12*REF(A,8)+11*REF(A,9)+10*REF(A,10)+9*REF(A,11)+8*REF(A,12)+7*REF(A,13)+6*REF(A,14)+5*REF(A,15)+4*REF(A,16)+3*REF(A,17)+2*REF(A,18)+REF(A,20))/210;
//对A值做加权均值计算。
D:MA(B,M);//对B值做10周期平均计算。
""",
    "params": [
        ("M", 1, 100, 10),
    ],
    "expected": """
    """,
}
