# 1
# Write a Python function that takes a list as an argument and returns a new list
# with unique elements of the first list in the same order.
def u_list(x):
    u_list=list(set(x))
    return u_list

x=[1,3,4,1,5,5,6,6,3,4,6,8]
print(u_list(x))

# alternative
def u_list (x):
    main_list=list()
    for elt in x:
        if elt not in main_list:
            main_list.append(elt)
    return main_list
x=[1,3,4,1,5,5,6,6,3,4,6,8]
print(u_list(x))

# 2
# Write a Python function to check whether a number is perfect or not.
# The function should return True if the number is perfect and False otherwise.

def n_divisors(N):
    divisors = []
    for x in range(1, int(N / 2) + 1):
        if N % x == 0:
            divisors.append(x)
    return divisors

def perf_nber(N):
    div = n_divisors(N)
    if sum(div) == N:
        return True
    else:
        return False


N = 9
if perf_nber(N):
    print(f'{N} is a perfect number')
else:
    print(f'{N} is not a perfect number')


# 3
# Write a function that returns the factorial of a number n which is the function's argument.
def rand_number(n):
    if n<0:
        print('The argument must be greater than 0')
    elif n==0:
        return 1
    else:
        x=1
        while n>1:
            x*=n
            n-=1
        return x

n=4
print(rand_number(n))

# 4
# Create a function that takes an integer as an argument and returns True if it’s a prime number and False otherwise.

def n_prime(x):
    prime= True
    if x==1:
        return False
    n=1
    while n < x//2:
        n+=1
        if x%n==0:
           prime=False
           break
    return prime
x=2
print(n_prime(x))

# 5
# Using the function defined in the previous challenge find 5 prime numbers greater than 1,000,000

def n_prime(x):
    prime= True
    if x==1:
        return False
    n=1
    while n < x//2:
        n+=1
        if x%n==0:
           prime=False
           break
    return prime
prime= []
for n in range(100000,100000000):
    if n_prime(n):
        prime.append(n)
        if len(prime)==5:
            break
print(prime)

# 6
# Write a function called fibo that takes an integer greater than 10 as an argument
# and returns the Fibonacci series between 0 and the function's argument.

def fibo(a):
    x1, x2 = 0, 1
    if a<=10:
        return 'the argument must be greater than 10'
    while x1<=a:
        print(x1,'', end='')
        x1,x2=x2, x1+x2
a=158
print(fibo(a))

# 7 Write a function that takes a list as an argument and returns the Equilibrium Index of the list.
# If there isn't such an index it returns False.
def equi_index(my_list):
    for x in range(0,len(my_list)):
        if sum(my_list[:x]) == sum(my_list[x+1:]):
            return x
    return False

S=[2, 3, 10, 5]
print(equi_index(S))

# 8
# Change the solution of the previous challenge so that the function receives a
# string of numbers separated by a comma.

def equi_index(my_string):
    my_list = my_string.split(',')
    my_list = [int(i) for i in my_list]
    for x in range (0, len(my_list)):
        if sum(my_list[:x])==sum(my_list[x+1:]):
            return x
    return False
s='4,5,8,6,3'
print(equi_index(s))

# 9
# Define a function that draws a Christmas tree using asterisks (*).
# The function takes a single argument, which is the height of the tree.

# Example: by calling draw_tree(5) it will display:

# *
#
# ***
#
# *****
#
# *******
#
# *********

def draw_tree(height):
    for i in range (1, height+1):
        for j in range (height-i):
            print('', end='')
        for j in range(2*i-1):
           print('*', end='')
        print()
draw_tree(5)









