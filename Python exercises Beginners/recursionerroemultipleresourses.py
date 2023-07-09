def fun(no):
    print(no)
    alist = []
    for i in range (0, 10000000, 1):
        alist.append("*")
    no = no +1
    fun(no)
fun(1)    
