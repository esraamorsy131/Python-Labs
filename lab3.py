#Question 1
l1 = [1,2,3,4,9,8]
l1.append(10)
print(l1)

#Question 2
l1.pop()
print(l1)

#Question 3
my_list = [5,1,0,6,-1,2]
my_list.sort()
print(my_list)

#Question 4
my_list.sort(reverse= True)
print(my_list)

#Question 5
tup1 = (1,2,3,4,"ahmed" , "Mona")
tup2 = ("yasmine" , "Eslam")
tup3 = tup1 + tup2
print(tup3)

# #Question 6 
y = dict(name="esraa" , age=25 , email="eng.esraamorsy2020@gmail.com")
print(y)

#Question 7
d1 = {"name":"ali", "age":30 , "grade":"b+"}
print(d1["name"])
print(d1.get("name"))

#Question 8
for i in d1.keys():
    print(d1.get(i))
    
#Question 9
def low(n1 , n2):
    print(n1 if n1 < n2 else n2)
    
low(10,50)


