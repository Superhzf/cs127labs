cashback=76
value20=0
value10=0
value5=0
value1=0
value20=cashback//20
leftover=cashback%20
value10=leftover//10
leftover=leftover%10
value5=leftover//5
leftover=leftover%5
value1=leftover
print("The number of 20$ bills is {}".format(value20))
print("The number of 10$ bills is {}".format(value10))
print("The number of 5$ bills is {}".format(value5))
print("The number of 1$ bills is {}".format(value1))
