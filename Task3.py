# TASK 3
#_________________________________________________________________
# ques. 1

n= int(input(" enter number upto which you  want to have fibbonacci series")
def fib(n):
      a=0
      b=1
      print(a)
      print (b)
       for i in range (2,n):
            c=a+b
             a=b
             a=c
            print(c)
fib(n)

#_________________________________________________________________

# ques. 2

#Let PQR be a triangle of sides PQ, QR, RP

a=int(input(" Enter length of PQ = "))
b=int(input(" Enter length of QR = "))
c=int(input(" Enter length of RP = "))

if a==b==c:
     print(" PQR is an equilateral triangle")
elif a !=b != c:
     print(" PQR is a scalene triangle")
else:
     print(" PQR is a isosceles triangle")

#_________________________________________________________________

# ques.3

m= int(input(" enter first number") 
n=  int(input(" enter second number ")
def gcp(m,n):
      p=1
       for u in range (1,m+1):
                  if m % u ==0 and n % u ==0:
                     p=u
                  else:
                     continue
        return p
print (gcp(m,n))

#_________________________________________________________________

# ques. 4

sum=0
for x in range (0,11,2):
    sum+=x
print(" sum of even numbers from 0 to 10 is ' {sum}' ")

#_________________________________________________________________


