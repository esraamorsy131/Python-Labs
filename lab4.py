
# #Question 1    
# x=[]  
# y = [1,2,3,4,5]

# for i in y:
#     x.append(i**2)
    
# print(x)

# #Qustion 2

# l =[1,1,2,5,8,5,2,6]
# s = set(l)
# print(s)

# #Question 3
# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# print(a)

# a = {1,2,3}
# a.add(10)
# print(a)

# d1 = {"name":"esraa" , "age":25}
# d2 = {"job":"Data analyst"}
# d1.update(d2)
# print(d1)

#Question 4
# l=[]
# t = (1,5,10,20,7,16)
# for i in t:
#     if i%2 == 0:
#         l.append(i)
#     a = tuple(l)
# print(a)   
        
#Question 5
my_list = []
for i in range(101):
    my_list.append(i)
print(my_list)

odds =[i for i in my_list if i%2 != 0]
print(odds)

odds_2 = set(odds)
print(odds_2)

odds_3 = {num : True for nym in my_list if i%2 != 0}

#Question 6
with open("names.text" , 'w')as file:
    file.write("esraa")
    
#Qustion 7
with open("names.text" , 'a')as file:
    file.write("\n" + "23/8/1997")
    
#Question 8
with open("names.text" , 'r')as file:
    for i in file:
        print(i)



    