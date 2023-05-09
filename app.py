# -*- coding: utf-8 -*-
"""
Created on Mon May  8 22:56:52 2023

@author: debna
"""

import streamlit as st
import numpy as np
import pickle
from pickle import load
from sklearn.ensemble import GradientBoostingClassifier

lr = load(open('E:/LiveProject/Default of credit card/gbc_creditcard.pickle', 'rb'))

st.title("[Predict Credit Card Defaulters]")



X1 = st.slider("[Amount of the given credit (NT dollar)]", 10000, 50000, 1000000)

X2 = st.radio("[Select Your Gender]", ["Male", "Female"])
if X2 == "Male":
    X2 = 1
else:
    X2 = 2

X3 = st.radio("[Select Your Education]", ["graduate school", "university","high school","others","10thstd","12thstd","bachaler"])
if X3 == "graduate school":
    X3 = 1
elif X3 == "university":
    X3 = 2
elif X3 == "high school":
    X3 = 3
elif X3 == "others":
    X3 = 4
elif X3 == "10thstd":
    X3 = 5
elif X3 == "12thstd":
    X3 = 6
elif X3 == "bachaler":
    X3 = 7

X4 = st.radio("[Marital status]", ["married", "single","others","divorced"])
if X4 == "married":
    X4 = 1
elif X4 == "single":
    X4 = 2
elif X4 == "others":
    X4 = 3
elif X4 == "divorced":
    X4 = 4

X5 = st.slider("[Select Your Age]",18, 80, 30 )

X6 = st.radio("[repayment status in September, 2005]", ["Zero Bill","Paid duly","1 Month Delay","2 Months Delay","3 Months Delay",
                                                 "4 Months Delay","5 Months Delay","6 Months Delay","7 Months Delay","8 Months Delay",
                                                 "9 Months & Above Delay"])

if X6 == "Zero Bill":
    X6 = 0
elif X6 == "Paid duly":
    X6 = -1
elif X6 == "1 Month Delay":
    X6 = 1
elif X6 == "2 Months Delay":
    X6 = 2
elif X6 == "3 Months Delay":
    X6 = 3
elif X6 == "4 Months Delay":
    X6 == 4
elif X6 == "5 Months Delay":
    X6 = 5
elif X6 == "6 Months Delay":
    X6 = 6
elif X6 == "7 Months Delay":
    X6 = 7
elif X6 == "8 Months Delay":
    X6 = 8
elif X6 == "9 Months & Above Delay":
    X6 = 9

X7 = st.radio("[repayment status in August 2005]", ["Zero Bill","Paid duly","1 Month Delay","2 Months Delay","3 Months Delay",
                                                 "4 Months Delay","5 Months Delay","6 Months Delay","7 Months Delay","8 Months Delay",
                                                 "9 Months & Above Delay"])


if X7 == "Zero Bill":
    X7 = 0
elif X7 == "Paid duly":
    X7 = -1
elif X7 == "1 Month Delay":
    X7 = 1
elif X7 == "2 Months Delay":
    X7 = 2
elif X7 == "3 Months Delay":
    X7 = 3
elif X7 == "4 Months Delay":
    X7 == 4
elif X7 == "5 Months Delay":
    X7 = 5
elif X7 == "6 Months Delay":
    X7 = 6
elif X7 == "7 Months Delay":
    X7 = 7
elif X7 == "8 Months Delay":
    X7 = 8
elif X7 == "9 Months & Above Delay":
    X7 = 9

X8 = st.radio("[repayment status in July 2005]", ["Zero Bill","Paid duly","1 Month Delay","2 Months Delay","3 Months Delay",
                                                 "4 Months Delay","5 Months Delay","6 Months Delay","7 Months Delay","8 Months Delay",
                                                 "9 Months & Above Delay"])
if X8 == "Zero Bill":
    X8 = 0
elif X8 == "Paid duly":
    X8 = -1
elif X8 == "1 Month Delay":
    X8 = 1
elif X8 == "2 Months Delay":
    X8 = 2
elif X8 == "3 Months Delay":
    X8 = 3
elif X8 == "4 Months Delay":
    X8 == 4
elif X8 == "5 Months Delay":
    X8 = 5
elif X8 == "6 Months Delay":
    X8 = 6
elif X8 == "7 Months Delay":
    X8 = 7
elif X8 == "8 Months Delay":
    X8 = 8
elif X8 == "9 Months & Above Delay":
    X8 = 9

X9 = st.radio("[repayment status in June 2005]", ["Zero Bill","Paid duly","1 Month Delay","2 Months Delay","3 Months Delay",
                                                 "4 Months Delay","5 Months Delay","6 Months Delay","7 Months Delay","8 Months Delay",
                                                 "9 Months & Above Delay"])
if X9 == "Zero Bill":
    X9 = 0
elif X9 == "Paid duly":
    X9 = -1
elif X9 == "1 Month Delay":
    X9 = 1
elif X9 == "2 Months Delay":
    X9 = 2
elif X9 == "3 Months Delay":
    X9 = 3
elif X9 == "4 Months Delay":
    X9 == 4
elif X9 == "5 Months Delay":
    X9 = 5
elif X9 == "6 Months Delay":
    X9 = 6
elif X9 == "7 Months Delay":
    X9 = 7
elif X9 == "8 Months Delay":
    X9 = 8
elif X9 == "9 Months & Above Delay":
    X9 = 9

X10 = st.radio("[repayment status in May 2005]", ["Zero Bill","Paid duly","1 Month Delay","2 Months Delay","3 Months Delay",
                                                 "4 Months Delay","5 Months Delay","6 Months Delay","7 Months Delay","8 Months Delay",
                                                 "9 Months & Above Delay"])
if X10 == "Zero Bill":
    X10 = 0
elif X10 == "Paid duly":
    X10 = -1
elif X10 == "1 Month Delay":
    X10 = 1
elif X10 == "2 Months Delay":
    X10 = 2
elif X10 == "3 Months Delay":
    X10 = 3
elif X10 == "4 Months Delay":
    X10 == 4
elif X10 == "5 Months Delay":
    X10 = 5
elif X10 == "6 Months Delay":
    X10 = 6
elif X10 == "7 Months Delay":
    X10 = 7
elif X10 == "8 Months Delay":
    X10 = 8
elif X10 == "9 Months & Above Delay":
    X10 = 9

X11 = st.radio("[repayment status in April 2005]", ["Zero Bill","Paid duly","1 Month Delay","2 Months Delay","3 Months Delay",
                                                 "4 Months Delay","5 Months Delay","6 Months Delay","7 Months Delay","8 Months Delay",
                                                 "9 Months & Above Delay"])
if X11 == "Zero Bill":
    X11 = 0
elif X11 == "Paid duly":
    X11 = -1
elif X11 == "1 Month Delay":
    X11 = 1
elif X11 == "2 Months Delay":
    X11 = 2
elif X11 == "3 Months Delay":
    X11 = 3
elif X11 == "4 Months Delay":
    X11 == 4
elif X11 == "5 Months Delay":
    X11 = 5
elif X11 == "6 Months Delay":
    X11 = 6
elif X11 == "7 Months Delay":
    X11 = 7
elif X11 == "8 Months Delay":
    X11 = 8
elif X11 == "9 Months & Above Delay":
    X11 = 9

X12 = st.slider("[bill statement in September 2005]", -165580,550000, 964511)
X13 = st.slider("[bill statement in August 2005]", -69777,590000, 983931)
X14 = st.slider("[bill statement in July 2005]", -157264,650000, 1664089)
X15 = st.slider("[bill statement in June 2005]", -170000,500000, 891586)
X16 = st.slider("[bill statement in May 2005]", -81334,550000, 927171)
X17 = st.slider("[bill statement in April 2005]", -339603,550000, 961664)

X18 = st.slider("[amount paid in September 2005]", 0,350000, 873552)
X19 = st.slider("[amount paid in August 2005]", 0,350000, 1684259)
X20 = st.slider("[amount paid in July 2005]", 0,350000, 896040)
X21 = st.slider("[amount paid in June 2005]", 0,350000, 621000)
X22 = st.slider("[amount paid in May 2005]", 0,250000, 426529)
X23 = st.slider("[amount paid in April 2005]", 0,280000, 426529)



if st. button("Predict"):
    query_point = np. array([X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23])
    query_point = query_point. reshape(1, -1)
    prediction = lr.predict(query_point)
    if prediction == 1:
        st.success("The person will default 😥!")
    else:
        st.error("The person will not defaul 😊!")
























