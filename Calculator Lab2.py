#
# Kevin
# Calculator Lab2
#

# 1. Function
def cal(x1, x2, op):
    if op == '+':
        return int(x1) + int(x2)
    elif op == '-':
        return int(x1) - int(x2)
    elif op == '*':
        return int(x1) * int(x2)  
    elif op == '/':
        return int(x1) / int(x2)

# 2.Input
x1 = input("Type x1     : ") 
x2 = input("Type x2     : ")
op = input("Operator    : ")

# 3. Output
sum = cal(x1, x2, op)
print(f"Sum         : {sum}")