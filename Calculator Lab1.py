#Kevin
#Calculator adding 2 value

sum = 0

while True:
    # 1.Input
    x1 = input("Type first number          : ") 
    x2 = input("Type second number         : ")
    op = input('Enter operator (+,-,*,/)   : ')

    # 2.Process
    if op == '+':
        sum = int(x1)+int(x2)
    elif op == '-':
        sum = int(x1)-int(x2)
    elif op == '*':
        sum = int(x1)*int(x2)
    elif op == '/':
        sum = int(x1)/int(x2)

    # 3. Output
    print(f"Sum                        : {sum}")
    res = input("Continue? (Yes/No)         : ")
    if res == "No":
        print("Exit")
        break;