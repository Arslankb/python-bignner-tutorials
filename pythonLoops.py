#While Loop

# val=int(input("Enter the number multiple of 7: "))
# while val%7 !=0 :
#     val = int(input("Enter the number multiple of 7: "))
# else :
#     print("%d is a multiple of 7" %val)


#For Loop

# x=[1,4,3,"Simplilearn"]
# for i in x:
#     print(i)

# x="simplilearn"
# for i in x:
#     print(i)


# Nested Foor Loop

# x=[[1,2,3],['a','b','c']]
#
# for i in x:
#     for j in i:
#         print(j, end="")
#     print()


#Loop Control Statement

# x="Hey there. how are you?"
#
# for i in x:
#     if i == ".":
#         break
#     print(i, end="")


#Continue Statement


# x=[2,3,6,78,43,9]
# for i in x:
#     if i>10:
#         continue
#     print(i)





#FOR LOOP IN DETAILED

#Even Numbers
# for i in range(0,21,2):
#     print(i)


#Sum of even Numbers

# sum=0
# for i in range(0,21):
#     if i%2==0 :
#         sum = sum+i
# print(sum)


#Pattern

# n =int(input("Enter a Number: "))
# # for i in range(1, n+1):
# #     for j in range(1, i+1):
# #         print(j, end='')
# #     print()



#While Loop

# i=1
# while i<=10:
#     print("Simplilearn")
#     i = i+1

#SUM
# sum=0
# i=1
# while i<=10:
#     if i%2==0:
#         sum = sum+i
#     i = i+1
# print(sum)


#Reverse a Number

# n=int(input("Enter a number: "))
#
# nr=0
#
# while n%10 !=0:
#     c=n%10
#     nr=nr *10 +c
#     n=n//10
# print(nr)


#Length of a List...

# x=[1,2.3,"simplilearn"]
# length=0
# i=0
# try:
#     while x[i]:
#         length = length+1
#         i = i+1
# except IndexError:
#     print(length)


#NESTED WHILE LOOP...


# n=int(input("Enter a Number: "))
# i=1
#
# while i<=n:
#     j=1
#     while j<=i:
#         print(i, end='')
#         j=j+1
#     i=i+1
#     print()


#Guess a Number...


import random
nump = random.randint(1000,9999)
n=int(input("Enter a 4 digit number: "))

while n!=10:
    num=nump
    cor=0
    while num%10 :
        numc = num%10
        nc = n%10
        num = num//10
        n = n//10
        if numc==nc:
            cor = cor+1
    if cor==4:
        print("Congrats! You guessed it right.")
        break
    else:
        print("%d digit were guessed right." %cor)
        n = int(input("Enter a 4 digit number: "))
else:
    print("You quit the game!")