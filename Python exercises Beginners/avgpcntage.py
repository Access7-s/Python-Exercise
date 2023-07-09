a1=float(input("enter 1st assignment score "))
a2=float(input("enter 2nd assignment score "))
a3=float(input("enter 3rd assignment score "))
a4=float(input("enter 4th assignment score "))
a5=float(input("enter 5th assignment score "))
scores=a1+a2+a3+a4+a5
ttlscore=500
ovrlpcntge=(scores/ttlscore)*100
print(f"The overall grade as percentage is :{ovrlpcntge:.2f}%")
