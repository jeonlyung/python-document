import turtle as t

# 그래프를 그릴 x 좌표 범위
x_min = -5
x_max = +5

# 그래프를 그릴 y 좌표 범위
y_min = -5
y_max = +5

#그래프를 그릴 간격
space = 0.1

#그릴 함수의 리스트
func_list = ["y=x*x", "y=abs(x)", "y=0.5*x + 1"]

#좌표 설정, 거북이 속도, 선굵기
t.setworldcoordinates(x_min,y_min,x_max,y_max)
t.speed(0)
t.pensize(2)

#x축 그리기
t.up()
t.goto(x_min, 0)
t.down()
t.goto(x_max, 0)


#y축 그리기
t.up()
t.goto(0, y_min)
t.down()
t.goto(0, y_max)

#그래프 그리기
t.color("green")
for func in func_list:  #func_list에 있는 함수를 하나씩 그립니다.
    x = x_min           #x_min부터 계산을 시작합니다.
    exec(func)          #수식을 계산합니다.(x값으로 y값 구하기
    t.up()
    t.goto(x,y)         #계산된 좌표로 이동합니다.
    t.down()

    while x <= x_max:
        x = x + space   #space 만큼 x를 증가
        exec(func)      #수식을 계산
        t.goto(x,y)    #계산된 좌표로 이동
    
    
    



