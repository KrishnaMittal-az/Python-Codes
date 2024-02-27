import math

# a=1234598765432
# while(a>0):
#     last_digit=a%10
#     print(last_digit)
# 



# x = 10
# while (x<=20):
#     print(x)
#     x=x+2




# for ch in range(10 , 21 , 2):
# #     print(ch)




# n=int(input())
# reverse_digit=0
# while(n>0):
#     last_digit=n%10
#     reverse_digit=reverse_digit*10+last_digit
#     n=n//10
# print(reverse_digit)
# if(reverse_digit>n):
#     print("REVERSE BIG")
# elif(reverse_digit==n):
#     print("SAME")
# else:
#     print("Orignal")




# num = input("Enter a number: ")

# if num.isdigit():
#     num = int(num)
#     original_num = num
#     reversed_num = 0

#     while num > 0:
#         reversed_num = reversed_num * 10 + num % 10
#         num //= 10

#     if reversed_num > original_num:
#         print("reverse greater")
#     elif reversed_num < original_num:
#         print("reverse smaller")
#     else:
#         print("same")



# x , y = map(int,input().split(" "))
# if(x<y):
#     smaller = x
# else:
#     smaller = y
# for i in range(1 , smaller+1):
#     if((x%i==0)and(y%i==0)):
#         hcf = i
# print(hcf)



# answer = 1
# x = int(input())
# for ch in range(1,x+1):
#     answer= answer*ch
# print(x)



# answer = 1
# # n = int(input())
# # while(n>=1):
# #     answer = answer*n
# #     n = n - 1
# # print(answer)


# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*" , end=" ")
#     print()


# n = int(input())
# k = 2*n-2
# for ch in range(0, n):
#     for xy in range(0,k):
#         print(end = " ")
#     k = k-2
#     for lp in range(0 , ch+1):
#         print("*" , end = " ")
#     print()

# n = int(input())
# k = n-1
# for i in range(0,n):
#     for j in range(0,k):
#         print(end = " ")
#     k = k-1
#     for j in range(0 , i+1):
#         print("#", end = " ")
#     print()


# n = int(input())
# num1 = 0
# num2 = 1
# next_num=num2
# count = 1
# sum = 0
# while(count<=n):
#     print(next_num , end = " ")
#     count = count + 1
#     sum = sum +next_num
#     num1 , num2 = num2 , next_num
#     next_num = num1 + num2
# print()
# print(sum)



# n = int(input())
# n1 = 0
# n2 = 1
# l = [0,1]
# # print(n1 , n2 , end = " ")
# for i in range(2,n+10000):
#     n3 = n1 + n2
#     n1 , n2 = n2 , n3
#     l.append(n3)
# if(n in l):
#     print("Yes")
# else:
#     print("NO")
# # print( n3 )
# # print()




# num = int(input("Enter a number: "))

# a, b = 0, 1
# while a < num:
#     a, b = b, a + b

# if a == num:
#     print("this is a Fibonacci number.")
# else:
#     print( "this is not a Fibonacci number")



# n = int(input())
# if(n==0 or n==1):
#     print("Yes")
# else:
#     a = 0
#     b = 1
#     while(True):
#         c = a + b
#         a , b = b , c
#         if (c == n):
#             print("Yes")
#             break
#         elif (c > n):
#             print("No")
#             break



# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("*" , end = " ")
#     print()


# n = int(input())
# while(n>=0):
#     print("#", end = " ")
#     n = n-1
# print()
# while(n>=0):
#     print("#", end = " ")
#     n = n-




# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*" , end=" ")
#     print()




# n = int(input())
# for ch in range(n):
#     if(n%ch==0):
#         print("NO")
#     else:
#         print("Yes")




# n = int(input())

# prime_numbers = []
# num = 2

# while len(prime_numbers) < n:
#     prime = True
    
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             prime = False
#             break
    
#     if prime:
#         prime_numbers.append(num)
    
#     num += 1

# print(prime_numbers)





# Calculator

# x , y = map(int,input().split(" "))
# def sum(a,b):
#    print(a+b)
# def diff(a,b):
#     print(a-b)
# def product(a,b):
#     print(a*b)
# def quos(a,b):
#     print(a/b)
# print("Select the operators")
# op = input()
# if(op == "+"):
#     sum(x,y)
# elif(op == "-"):
#     diff(x,y)
# elif(op == "*"):
#     product(x,y)
# elif(op == "/"):
#     quos(x,y)
# else:
#     print("Invalid Operator selected")


# n= int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("@")
#     print()


# n=int(input())
# flag = True
# if n == 2:
#     print("Yes")
# else:
#     for a in range(2,n):
#         if(n%a==0):
#             print("No")
#             flag = False
#             break
# if(flag):
#     print("Yes")



# a=int(input("enter your percentage"))
# if(a>75):
#     print("you are eligible")
# elif(a==75):
#     print("you are eligible after 6 months")
# else:
#     print("you are not eligible")


# n=int(input())
# i=2
# while(i<n):
#     if(n%i==0):
#         print("not a prime no")
#         flag=False
#         break
# if(flag==True):
#     print("prime no")

            

# import math
# n = int(input())
# print(math.sqrt(n))


# def sqrt(x):
#     if(x == 0 or x == 1):
#         return x
#     i = 1
#     result = 1
#     while(result<=x):
#         i+=1
#         result = i*i
#     return i

# n = int(input())
# print(sqrt(n))



# def square_root(number, precision=0.0001, max_iterations=100):
#     guess = number / 2.0  

#     for i in range(max_iterations):
#         guess = (guess + number / guess) / 2  
#         if abs(number - guess * guess) < precision:
#             return guess  

#     return guess 


# number = float(input())
# result = square_root(number)
# print(f"The square root of {number} is approximately {result:.2f}")




# def square_root(number):
#     if number < 0:
#         raise ValueError("Cannot find the square root of a negative number")

#     result = 0
#     odd = 1

#     while number >= 0:
#         number -= odd
#         odd += 2
#         result += 1

#     return result - 1  


# number = int(input("Enter a number: "))
# result = square_root(number)
# print(f"The square root of {number} is approximately {result:.2f}")



# n = int(input())
# i = 2
# while(i*i<=n):
#     i+=0.01
# i = i - 0.01
# print(f"{i:.2f}")
# print(round(i,2))



# n = float(input())
# print("the ceil value is",math.ceil(n))
# print("the floor value is",math.floor(n))


# print(round(math.sqrt(int(input())),3))


# n = int(input())
# p = int(input("precision"))
# i = 0
# counter = 1
# for _ in range(p+1):
#     while(i*i<=n):
#         i+=counter
#     i-=counter
#     counter=counter/10
# print(round(i,p))




# n= int(input())
# count = 0
# num = 2
# while(count<n):
#     flag = True
#     for _ in range(2,num):
#         if(num%_==0):
#             flag=False
#             break
#     if flag==True:
#         print(num)
#         count+=1
#     num+=1


# n = int(input())
# summ = 0
# while(n>0):
#     k = n%10
#     summ+=k
#     n = n//10
# print(summ)



# cumulative_sum = 0
# numbers = []

# while True:
#     num = int(input())
#     cumulative_sum += num
#     if cumulative_sum < 0:
#         break
#     numbers.append(num)

# for num in numbers[:-1]:
#     print(num)


# cumulative_sum = 0
# numbers = []
# while True:
#     num = int(input())
#     cumulative_sum += num
#     numbers.append(num)
#     if cumulative_sum < 0:
#         break

# for i in numbers:
#     print(i)

# rem = 0
# k = int(input())
# while(k>0):
#     n = k%10
#     rev = rem*10+n
#     k = k //10
# print(k)


# lop=input()
# lop = int(lop)
# print(lop)
# reverse_digit=0
# while(lop>0):
#     last_digit=lop%10
#     reverse_digit=reverse_digit*10+last_digit
#     lop=lop//10
# print(reverse_digit)



# original=input()
# original= int(original)
# # print(lop)
# reverse_digit=0
# while(original>0):
#     last_digit=original%10
#     reverse_digit=reverse_digit*10+last_digit
#     original=original//10
# # print(lop)
# N = str(reverse_digit)

# odd = 0
# even = 0

# for xy in range(len(N)):
#     number = int(N[xy])
#     if xy % 2 == 0:  
#         even += number
#     else:  
#         odd += number

# print(even)
# print(odd)



# binary = input("Enter a binary number: ")
# decimal = 0
# power = 0

# for digit in reversed(binary):
#     if digit == '1':
#         decimal += 2 ** power
#     power += 1

# print("Decimal equivalent:", decimal)




# n = int(input())
# i = 0
# while(i<=n):
#     print(" " * (n-i) + "#" * i)
#     i+=1

# n = int(input())

# for row in range(1,n+1):
#     for space in range(1,n-row+1):
#         print(" " , end = " ")
#     for star in range(n-row+1 , n+1):
#         print("*",end = " ")
#     print()

# n = int(input())
# k = 1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end = " ")
#     print()

# n = int(input())
# k = 1
# while(k<n+1):
#     k = k+1
#     while(k , )


# rows = int(input())
# for i in range(0,rows):
#     for j in range(0,i):
#         print(end = " ")
#     for j in range(rows,0 ,-1):
#         print("#" , end = " ")
#     print()


# n = int(input())
# for i in range(n,0,-1):
#     for j in range(0 , n-i):
#         print(end = " ")
#     for j in range(0 , i):
#         print("#" , end = " ")
#     print()

#=========================================27/09/23==========================================


# name = input()
# age = int(input())
# print("his name is " + name + "and his age is" + str(age))

# print(f"his name is {name} and his age is {age}")

# print("his name is {} and his age is {}".format(name , age))

# print("his name is %s and his age is %d"%(name , age))


# x = input()
# print(x.lstrip())
# print(x.rstrip())
# print(x.strip())

# sen = "my name is Krishna Mittal"
# print(sen.split())
# print(sen.split("a"))

# st = input()
# print(st.replace("Krishna" , "Dhruv"))  
# print(st.replace("a" , "t")) 
# print(st.count("a"))

# n = int(input())
# for rows in range(0,n+1):
#     for star in range(1,rows+1):
#         print("*" , end = " ")
#     for space in range(1,n+1,-2):
#         print(" ",end=" ")
#     for star in range(1,rows):
#         print("*",end = " ")
#     print()

#<================================================29/09/23==============================================>

# class_ = ["krishna" , "aditya" , "ansh" , "kanhaiya" ]
# if("krishna" in class_):
#     print("YES")
# else:
#     print("NO")

# l = [1,2,3,4,5,6,7,8,9]
# print(len(l))

# l1 = [10,20,30]
# l2 = [40,50,60]
# l3 = l1 +l2
# print(l3)

# def CheckLeap(Year):  
#     if((Year % 400 == 0) or  
#         (Year % 100 != 0) and  
#         (Year % 4 == 0)):   
#             print("Given Year is a leap year")
#     else:  
#         print ("Given Year is not a leap Year")  
  
# Year = int(input("Enter the number: "))  
  
# CheckLeap(Year)





# n = int(input())
# l = []
# l1=[]
# for _ in range(n):
#     x = int(input())
#     l.append(x)
# t = int(input())
# for i in range(n,-1):
#     if(l[i]==t):
#         l1.append(l[i])
#     else:
#         x = -1





#<=======================================25/10/23=======================================>

# n = int(input())
# total = 0
# for i in range(n):
#     if(i%2==0)and (i%3==0):
#         total = total + i

# print(total)


# n = input()
# x=0
# l1 = ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U']
# for i in l1:
#     if(i in n):
#         x+=1
# print(x)


# list1 = list(map(int,input().split()))
# new_list = []
# # for i in list1:
#     # new_list.append(i*i) 

# for j in list1:
#     if(j%2!=0):
#         new_list.append(j*j)

# if(len(new_list)==0):
#     print("None")
# else:
#     for _ in new_list:
#         print(_ , end = " ")


# n = int(input("number of maximum values you want to find"))
# list1 = list(map(int,input().split()))

# x1 = float("-inf")
# x2 = float("-inf")
# x3 = float("-inf")

# for i in list1:
#     if(i>=x1):
#         x3 = x2
#         x2 = x1
#         x1 = i
#     elif(i>=x2):
#         x3 = x2
#         x2 = i
#     elif(i>=x3):
#         x3 = i

# print(x1)
# print(x2)
# print(x3)

#<====================================27/10/23========================================>

#take a list from user and generate all pair.

# list_1 = list(map(int,input().split(" ")))

# pairs_list = []
# for i in range(len(list_1)):
#   for j in range(i + 1, len(list_1)):
#     pairs_list.append((list_1[i] , list_1[j]))
#     # print(f"{list_1[i]} , {list_1[j]}")
# # print(pairs)
# for pairs in pairs_list :
#   print(pairs)
# # no of pairs is ^nC2 (permutaion and combination)


#if you have sorted array containing n digit integer and target integer t . design an algorith to count the number of pairs whose sum is equal to target t.give apython code

# l = [10,20,30,40,50,60]
# t = int(input())
# count = 0
# i = 0
# j = len(l)-1
# while i<j:
#     summ = l[i]+l[j]
#     if(summ == t):
#         print(f"{l[i]},{l[j]}")
#         i = i+1
#         j = j-1
#         count+=1
#     elif(summ > t):
#         j = j-1
#     elif(summ < t):
#         i = i+1
# print(count)

# import math
# input = list(map(int,input().split()))

# maxi = -math.inf
# mini = math.inf

# for i in range(len(input)):
#   if input[i] > maxi:
#     maxi = input[i]
#   if input[i] < mini:
#     mini = input[i]

# print("Maximum value:", maxi)
# print("Minimum value:", mini)


# l = list(map(int,input().split()))
# i = 0
# j = len(l)-1
# flag = True
# while(i<j):
#         if(l[i]!=l[j]):
#             print("NO")
#             flag = False
#             break
# if(flag == True):
#     print("YES") 

# take a list and print contigious part of the list(sub arrays)

# l = list(map(int,input().split()))
# # for i in range(len(l)):
# #     for j in range(i, len(l)):
# #         sublist = l[i:j+1]
# #         print(sublist)

# # 2nd method
# l = list(map(int,input().split()))
# max_sum = -math.inf
# for i in range(len(l)):
#     for j in range(i , len(l)):
#         c_sum = 0
#         for k in range(i,j+1):
#             c_sum += l[k]
#         if(c_sum>max_sum):
#             max_sum=c_sum
# print(max_sum)






