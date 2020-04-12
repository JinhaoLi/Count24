import random as r
import os

number = [0, 0, 0, 0]
countTool = ["+", "-", "*", "/"]
k = "("
z = ")"


# 计算两个数（param, param1）运算的结果，运算符op
def count_2_number(param, param1, op):
    if countTool[op] == "+":
        return param + param1
    if countTool[op] == "-":
        return param - param1
    if countTool[op] == "*":
        return param * param1
    if countTool[op] == "/" and param1 != 0 and param % param1 == 0:
        return param / param1
    else:
        return -9999


# 获得等于24的表达式 参数（param, param1, param2, param3）
# 计算4个数的所有得到24的表达式
def get_expression(param, param1, param2, param3):
    for op1 in range(4):
        front = count_2_number(param, param1, op1)
        for op2 in range(4):
            middle = count_2_number(param1, param2, op2)
            again1 = count_2_number(front, param2, op2)
            again2 = count_2_number(param, middle, op1)
            for op3 in range(4):
                last = count_2_number(param2, param3, op3)
                again3 = count_2_number(param1, last, op3)
                again4 = count_2_number(middle, param3, op2)

                # 5种不同的运算顺序得到的5种结果
                result1 = count_2_number(again1, param3, op3)
                result2 = count_2_number(again2, param3, op3)
                result3 = count_2_number(param, again3, op1)
                result4 = count_2_number(param, again4, op1)
                result5 = count_2_number(front, last, op2)

                if result1 == 24:
                    return k + k + str(param) + countTool[op1] + str(param1) + z + countTool[op2] + str(
                        param2) + z + countTool[op3] + str(param3) + "=24"
                if result2 == 24:
                    return k + str(param) + countTool[op1] + k + str(param1) + countTool[op2] + str(
                        param2) + z + z + countTool[op3] + str(param3) + "=24"
                if result3 == 24:
                    return str(param) + countTool[op1] + k + str(param1) + countTool[op2] + k + str(
                        param2) + countTool[op3] + str(param3) + z + z + "=24"
                if result4 == 24:
                    return str(param) + countTool[op1] + k + k + str(param1) + countTool[op2] + str(
                        param2) + z + countTool[op3] + str(param3) + z + "=24"
                if result5 == 24:
                    return k + str(param) + countTool[op1] + str(param1) + z + countTool[op2] + k + str(
                        param2) + countTool[op3] + str(param3) + z + "=24"
    return "null"


# 使用4个嵌套for循环列出排列组合
def count24():
    haveResult = 0
    for a in range(4):
        for b in range(4):
            if a == b:
                continue
            for c in range(4):
                if a == c or b == c:
                    continue
                for d in range(4):
                    if a == d or b == d or c == d:
                        continue
                    # print(str(number[a]) + "\t"
                    #       + str(number[b]) + "\t"
                    #       + str(number[c]) + "\t"
                    #       + str(number[d]) + "\t")
                    expr = get_expression(number[a], number[b], number[c], number[d])
                    if expr.__eq__("null"):
                        continue
                    else:
                        print(expr)
                        haveResult = 1
    if haveResult == 0:
        print("无解！")


# 等待用户输入 给出答案
def wait_for_input():
    cmdStr = input()
    count24()


while 1:  # 1代表 true ；0 代表 false
    print("请通过计算获得24:=======================================")
    for i in range(4):
        number[i] = 1 + (r.random() * 10).__int__()
        print(number[i])
    wait_for_input()
