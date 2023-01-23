#Create Function

# def welcome():
#     print("Good Morning!")
# welcome()

#Add 2 Numbers..

# def add(a,b):
#     total = a+b
#     print("a=%d b=%d" %(a,b))
#     print("The sum is:", total)
# add(20,30)


#Another

# def add(b,a):
#     total = a+b
#     print("a=%d b=%d" %(a,b))
#     print("The sum is:", total)
# add(a=15,b=10)


#Another One..


# def add(a=0, b=0):
#     total = a+b
#     print("a=%d b=%d" %(a,b))
#     print("The sum is:", total)
# add(10)


#Sum of a list number


def add(*a):
    total=0
    for i in a:
        total = total+i
    print("The sum is:", total)
add(10,20,30,40)


