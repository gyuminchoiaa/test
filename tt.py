import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

c1 = st.radio('선의 폭을 선택하시오',['red','green','blue','orange'])
s1 = st.radio('선의 형태를 선택하시오',['-',':','-.','--'])

fig, ax = plt.subplots()


x = []
y = []
for i in range(-20,21,2):
    x.append(i)
    y.append(-2*i*i+3*i+5)

plt.plot(x,y,color=c1, linestyle=s1, marker='h')
st.pyplot(fig)

import sys
sys.exit()

fig, ax = plt.subplots()

# col = st.columns(3)
# with col[0]:
#     a = st.number_input('insert a', step = 1)
# with col[1]:
#     b = st.number_input('insert b', step = 1)    
# with col[2]:
#     c = st.number_input('insert c', step = 1)


# y = []
# for i in x:
#     y.append(a*i**2 + b*i + c)

# plt.plot(x,y)

# st.pyplot(fig)































# import time
# import random as r

 

# s1=1
# s2=2
# s3=3
# s4=4
# s5=5
# s1,s2,s3,s4,s5

# s=[1,2,3,4,5]
# s

# import turtle
# t = turtle.Turtle()
# t.left(90)
# # t.shape('turtle')
# # t.speed(1000)
  
# # t.pensize(5)


# def tree(length):
#         if length >5:
#                 t.forward(length)
#                 t.right(20)
#                 tree(length-15)
#                 t.left(40)
#                 tree(length-15)
#                 t.right(20)
#                 t.backward(length)
                
# t.color('green')
# t.speed(0)
# tree(90)
#                 # def shape(sh):
# #     for j in range(sh):
# #         t.forward(1+5*i)
# #         t.left(360/sh)
# # # sh=6
# # while True:
# #     for i in range(30):




#         # if i < 10:
#         #     shape(3)
#         # elif i < 20:
#         #     shape(4)
#         # elif i <30:
#         #     shape(5)
#         # for j in range(sh):
#         #     t.forward(1+5*i)
#         #     t.left(360/sh)
#         # t.forward(1+5*i)
#         # t.left(60)
#         # t.left(60)
      
        
        
       
#         # t.forward(1+5*i)
#         # t.left(90)
#         # t.forward(1+5*i)
#         # t.left(90)
#         # t.forward(1+5*i)
#         # t.left(90)
#         # t.forward(1+5*i)
#         # t.left(90)
#         # t.circle(1+5*i)
#         # t.color(r.random(),r.random(),r.random())
#         # t.goto(i*20, 0)






# turtle.done()





















# import turtle

# screen = turtle.Screen
# im1 = '호랑이-gif.htm'
# t1 = turtle.Turtle()
# t2 = turtle.Turtle()



# t1.shape('turtle')
# t2.shape('turtle')
    
    
# screen.addshape(im1)

# t1.penup()
# t1.shapesize(3)
# t1.pensize(5)
# t1.goto(-300,100)

# t2.penup()
# t2.shapesize(3)
# t2.pensize(5)
# t2.goto(-300,-100)

# t1.pendown()
# t2.pendown()
# t1.speed(1)
# t2.speed(1)



# for i in range(50):
#     d1=r.randint(1,30)
#     t1.forward(d1)
#     d2= r.randint(1,30)
#     t2.forward(d2)








# turtle.done()




# def square(x,y,lx,ly):
#     turtle.bgcolor('yellow')
#     t.width(5)
#     t.color('blue')
#     t.up()
#     t.goto(x,y)
#     t.down()
#     for i in range(2):
#         t.forward(lx)
#         t.left(90)
#         t.forward(ly)
#         t.left(90)



# square(-200,0,100,50)
# square(0,0,100,150)
# square(200,0,100,100)



# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(1000)
    
    


# turtle.done()







# colors=['red','purple','blue','yellow','orange','green','magenta']
# t.width(8)
# t.pencolor('purple')

# length=5
# for i in range(1000):
#     t.forward(length)
#     t.pencolor(colors[length%7])
#     t.right(45)
#     length += 1


# turtle.done()












# n=30
# ang=360/n



# for i in range(n):
#     t.circle(100)
#     t.left(ang)







# s=0
# for i in range(1,6,1):
#     # s=s+i
#     s+=i
#     s


# s=100
# if s >= 90:
#     '귀하의 점수는'+ str(s) +'점으로 :orange[A등급]입니다'
# elif s >=80:
#     '귀하의 점수는'+ str(s) +'점으로 :blue[B등급]입니다'
# elif s >=70:
#     '귀하의 점수는'+ str(s) +'점으로 :blue[C등급]입니다'
# elif s >=60:
#     '귀하의 점수는'+ str(s) +'점으로 :blue[D등급]입니다'
# elif s >=50:
#     '귀하의 점수는'+ str(s) +'점으로 :red[F등급]입니다'


# '7과 4의 연산'

# '덧셈', 7 + 4
# '뺄셈', 7 - 4
# '곱셈', 7 * 7
# '나눗셈', 7 / 4
# '몫', 7 // 4
# '나머지', 7 % 4
# '거듭제곱', 2 ** 4



# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(100)
    

# turtle.done()




