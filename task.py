#Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
#print ('введите число N =>')
Number = int (input('введите число N =>\t'))
count=0
result=1
while count < Number:
    print (result,end=',')
    
    result*=-3
    count+=1


#****************************************************************
#Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
Line = str(input('введите строку =>\t'))
substring = str(input('введите подстроку =>\t'))
results = 0
for i in range(len(Line)):
    if Line[i:i+len(substring)] == substring:
        results += 1
print (results)

#*****************************************************************
#Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
print ('введите число N')
Number = int (input())

print(f'====================')
def SetNumbers(Number):

    result = 1
    count = 1

    for i in range (Number):
        result *= count
        print(result ,end=',')
        count +=1

SetNumbers(Number)


#**************************************
#Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 
#3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


print ("введите число N")
Number = int (input())
count=0
result=1
print ("---------------")
while count<Number:
    result+=3
    count+=1
    print(f"{count}:{result}")
   
#******************************************************************


#Подсчитать сумму цифр в вещественном числе.

print ('введите число N =>')
number = str (input())
a = str(number).replace(".", "")
x = int (str(a))
def SumNumber(x):
    result = 0
    while x > 0:
        result += x % 10
        x//=10
    return result
print(SumNumber(x))