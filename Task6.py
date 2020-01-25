# TASK 6
#******************************************************************************************
# Que 1..


a_dict = {}

print(a_dict)
 
a_dict = {"1st element " : 5, "2nd element " : 6, "3rd element " : 7, "4th element " : 8, "5th element " : 9}

print(a_dict)

#*******************************************************************************************

#Que 2..

b_dict = {}


for i in range (1,11):

    b_dict[i] = i**2
    


print(b_dict) 

#********************************************************************************************


#Que 3...

c_dict = {1:1, 2:2, 3:3}

sum = 0

for i in c_dict:
    
    sum += c_dict[i] 
    


print("sum of values are" ,sum)   

#*******************************************************************************************

Que 4...
 
m_set = set(["Lily", "Rose", "Hibiscous"]) 

n_set = set(["Lotus", "Rose"])



set_u = m_set | n_set

print("union is ", set_u)



set_i = m_set & n_set

print("intersection is ", set_i)



set_d = m_set - set_i

print("set difference is ", set_d)   


#********************************************************************************************