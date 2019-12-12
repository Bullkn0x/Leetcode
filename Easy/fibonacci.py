import sys
# a=1
# b=2 then:
# b=a+b
# a=b
# 1,1,2,3,5,8,13
def fibSolve(n):
    solution=[]
    a,b= 1,1
    for x in range(n):
        solution.append(a)
        a,b = b, a+b
    print(solution)
print(fibSolve(13))
