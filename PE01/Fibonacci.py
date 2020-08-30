# #dynamic prg
# FibArray = [0,1] 
  
# def fibonacci(n): 
#     if n<0: 
#         print("Incorrect input") 
#     elif n<=len(FibArray): 
#         return FibArray[n-1] 
#     else: 
#         temp_fib = fibonacci(n-1)+fibonacci(n-2) 
#         FibArray.append(temp_fib) 
#         return temp_fib

# print(fibonacci(51))


#space optimization:
def modifiedFibo(index):
    first = 0
    second = 1
    if index == 0:
        return first
    elif index == 1:
        return second
    else:
        # print ("num: ", num, "result", ((num-2) + (num-1)))
        for i in range (2, index):
            third = first + second
            first = second
            second = third 
        return third
print(modifiedFibo(8))
# #original
# def modifiedFibo(num):
#     if num < 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         # print ("num: ", num, "result", ((num-2) + (num-1)))
#         return modifiedFibo((num-2)) + modifiedFibo((num-1))