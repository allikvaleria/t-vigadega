#1 Вариант


#1 Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n елок. Изображение одной елки имеет размер 4×9 символов, между двумя соседними елками также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последней елки. Для упрощения рисования скопируйте елку из примера в среду разработки. Елки должны простоложиться горизонтально.

#   /V\    
#  / V \
# / V V \  
#/VV V VV\    

#2 Перемножить все не чётные значения в диапазоне от 0 до введенного пользователем числа(R);

#3 Дано N чисел. Найти количество положительных чисел среди них; N рандомное число

#4 Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

#5 Найти сумму ряда чисел от A до B. Полученный результат вывести на экран;


#1
#n=int(input("Vali arv 1 kuni 9 :"))
#for i in range(n):
#    print("   /V\    ")
#    print("  / V \   ")
#    print(" / V V \  ")
#    print("/VV V VV\ ")
#    print()


#1 töö vigadega
while True: 
    try:
        mitu=int(input("Mitu tk: "))
        if 1<=mitu<10:
            break
    except ValueError:
        print("Vale tüüp")

for i in range(mitu):
    print(' /V\ '.center(10,' '),end="")
print()
for i in range(mitu):
    print(' / V \ '.center(10,' '),end="")
print()
for i in range(mitu):
    print(' / V V \ '.center(10,' '),end="")
print()
for i in range(mitu):
    print('/VV V VV\ '.center(10,' '),end="")
print()


##2
#R=int(input("Sisesta arv :"))
#if R%2==0:
#    for i in range(0,R):
#        R+=1
#        print(R)
#while True:
#    R+=1
#    print("vale")
#    break



##4
#num = int(input("Sisesta naturaalarv: "))
#paarisarv = 0
#paaritu_arv = 0

#while num > 0:
#    a = num % 10
#    if a % 2 == 0:
#         paarisarv+= 1
#    else:
#         paaritu_arv+= 1
#    num //= 10
#print("Paarisarvude arv:", paarisarv)
#print("Paaritu arv:", paaritu_arv)

#4var 5zadacha
while True: 
    try:
        K=int(input("Mitu kotlet sul on?: "))
        if K>0: break
    except ValueError:
        print("Vale tüüp")
while True: 
    try:
        M=int(input("Mitu kotleti ühel pannil?: "))
        if M>0: break
    except ValueError:
        print("Vale tüüp")
pann=0
while K>M:
        K-=M 
        pann+=1
        print(f"praetud: {pann} tk")
        if K<M:
            pann+=1
            print(f"praetud: {pann} tk")
print(f"Kooku oli praetud: {pann} panni")
print()



#5var 2zadacha
from random import *
N=25
kesk1=0
kesk2=0
for i in range(N):
    h1=randint(1,5)
    h2=randint(1,5)
    kesk1+=h1 
    kesk2+=h2 
kesk1/=N 
kesk2/=N 
print(f"keskmine hinne 1 klassis on {kesk1}")
print(f"keskmine hinne 2 klassis on {kesk2}")



#5var 4zadacha
from random import *
sum_num=0
sum_km=0
for i in range(12):
    num=randint(1000,100000)
    km=randint(1,1000)
    sum_num+=num 
    sum_km+=km 
    print(f"{i+1}. maakond. \nElanikud: {num}. Pindala: {km}\n Kokku: {sum_num},{sum_km}")
vastus=sum_num/sum_km
print(f"{vastus:.3f}") #:.3f - округление до 3 знаков (f - формат числа float)
