
## Check whether a number is Armstrong or not

def arm(num):

    t1=num
    order=0
    while t1>0:
        order+=1
        t1=t1//10

    temp=num
    sum=0
    while  temp>0:
        k=temp%10
        sum+=k**order
        temp=temp//10

    if sum==num:
        return True
    else: 
        return False

print("Enter the Number")
n=int(input())
print(arm(n))


## Prime Numbers in a range

def prime(l, u):
    for n in range(l, u + 1):
        count = 0
        for i in range(2, int(n ** 0.5) + 1):
            if (n % i == 0 ):
                count += 1
                break
        if count == 0 and n!=1:
            print(n)

print("Enter the Lower Limit")
l = int(input())
print("Enter the Upper Limit")
u = int(input())
print("The List of Numbers are:")
prime(l, u)



## sum of squares of first n square numbers
def squ(n):
    sm=0
    for i in range(1,n+1):
        sm=sm+(i*i)

    return sm

print("Enter the Number")
n=int(input())
print(squ(n))


## return ASCII code of a character
def asciiii(n):
        return ord(n)

print("Enter the Character")
n=(input())
print(asciiii(n))


## Compund Interest
def ci(p,r,t):
    amt=p*((1+r/100)**t)
    ci=amt-p
    print(ci)

ci(10000, 10.25, 5)


## CUBES OF n NATURAL numbers

def cub(n):
    sm=0
    for i in range(1,n+1):
        sm=sm+(i*i*i)

    return sm

print("Enter the Number")
n=int(input())
print(cub(n))


## Nth Fibonnaci Number

def fib(n):
    if n<=0:
        print("Incorrect Input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)    


print("Enter the Number")
n=int(input())
print(fib(n))


## First N Fibonnaci Numbers
def fib(n):
    a=0
    b=1
    i=0
    print(a)
    print(b)
    while i<=n-2:
        temp=b
        b=a+b
        a=temp
        i+=1
        print(b)

print("Enter the Number")
n=int(input())
fib(n)


## filter function

def odd(n):
    if n%2 == 1:
        return True
    else:
        return False
    
print(list(filter(odd,range(2,15))))


## Reducee function

from functools import reduce

def add(x, y):
    return x + y

nums = [1, 2, 3, 4, 5]

print(reduce(add, nums))

##lambda function
z=lambda x,y:x+y
print(z(5,3))

## Input a list and convert it to string
print("Enter the lis of numbers")
numms=list(input().split())
for i in range(len(numms)):
    numms[i]=int(numms[i])
print(numms)


## List Comprehension
nums=[1,2,3,4,5]
squares=[n**2 for n in nums]
print(squares)

# vowels in string
vowels="AEIOUaeiou"
s=input("Enter the string")
ns=""
for char in s:
    if char in vowels:
        ns=ns+char

print(ns)        


# Bubble sort

n= int(input("Enter how many numbers:"))
print("Enter the Numbers")
L=[]
for i in range (n):
    num=int(input())
    L.append(num)

for i in range (n):
    for j in range (n-1-i):
        if L[j]>L[j+1]:
            temp=L[j]
            L[j]=L[j+1]
            L[j+1]=temp

print("Sorted List:")
for i in range(n):
    print(L[i])



# Bubble sort alternate
def bubsort(a,n):
    for i in range(n):
        for j in range(n-1-i):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a

print("Bubble Sort!!!")
print("Enter how many Numbers to sort?")
n=int(input())
print("Enter the Numbers to sort:")
a=[]
for i in range (n):
    nums=int(input())
    a.append(nums)
print("Sorted List!!") 
bubsort(a,n)
print(a)       


##Third Largest Number in a List

print("Third Largest Number in a list")
print("Enter How many Numbers?")
n=int(input())
print("Enter the Numbers:")
l=[]
for i in range (n):
    nums=int(input())
    l.append(nums)
a=0
b=0
c=0
for i in range(n):
    temp=l[i]
    if temp>a:
        a=temp
for i in range(n):
    if (l[i]==a):
        l[i]=0
    temp=l[i]
    if temp>b:
        b=temp
for i in range(n):
    if(l[i]==b):
        l[i]=0
    temp=l[i]
    if temp>c:
        c=temp

print("Third largest number is",c)


##Reverse a List of Names without slicing

print("Names in a list")
print("Enter How many Names?")
n=int(input())
print("Enter the Names:")
l=[]
for i in range (n):
    nums=(input())
    l.append(nums)
left=0
right=len(l)-1
while(left<right):
    temp=l[left]
    l[left]=l[right]
    l[right]=temp
    left+=1
    right-=1

print(l)

## Sum of Numbers in a List
print("Sum of Numbers in a list")
print("Enter How many Numbers?")
n=int(input())
print("Enter the Numbers:")
l=[]
for i in range (n):
    nums=int(input())
    l.append(nums)
sum=0
for i in range (n):
    sum+=l[i]
   
print(sum)



##Largest Number in a list using max()
print("Sum of Numbers in a list")
print("Enter How many Numbers?")
n=int(input())
print("Enter the Numbers:")
l=[]
for i in range (n):
    nums=int(input())
    l.append(nums)

a=max(l)
print("The Largest number is",a)

##Largest Element in a list using sort() and pop()

print("Sum of Numbers in a list")
print("Enter How many Numbers?")
n=int(input())
print("Enter the Numbers:")
l=[]
for i in range (n):
    nums=int(input())
    l.append(nums)

l.sort()
a=l.pop()
print("The Largest number is",a)