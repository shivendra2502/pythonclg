#TASK 4
#********************************************************************
#que 1 --> Print even numbers in (1 to 50) using continue statement.

first, last = 1, 50

for x in range first, last+1):
     
       if x%2==1:
           continue

print("even numbers are :- ",x)

#____________________________________________________________________

#que 2 --> Print sum of digits of a number ........

num = int(input("enter a number :"))
sum = 0
while num > 0:
        d = num%10
        num = num//10
        sum += d

print ("sum of digits of number :-",sum)

#____________________________________________________________________

#que 3 --> To find median of three values.......

n1 = float(input("enter first number"))
n2 = float(input("enter second number"))
n3 = float(input ("enter third number"))

if n1>n2:
    
    if n1<n3:
        med =n1

   elif n2>n3:
       med = n2
   
   else:
       med = n3

else:
    
  if n1>n3:
      med =n1
  
  elif n2<n3:
      med = n2
  
  else:
      med = n3

print("Median is =", med)

#___________________________________________________________________
#******************thank you**************************************** 



















