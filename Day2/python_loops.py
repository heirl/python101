my_dict = {'name': 'Athan', 'hobby': 'learning', 'pattern': 'time', 'day_part': 'morning', 'sleep': '12:30a.m', 'wake': '10:00a.m'}
# while len(my_dict)>1:
#     my_dict.popitem()
#     if len(my_dict)==3:
#         print(my_dict.items())
#         break

#Example to retrieve the elements in a dictionary using for loop and dict .items() method
for key,values in my_dict.items():
    print(f"The Key Value order is {key} : {values}")

#Using nested for loop 
sub=[1,2,3,4,5]
post=[1,2,3,4,5]
for i in sub:
    for j in post:
        print("\n You Recieved ")
        k = i*j
        while k>0:
            print("*",end=" ")
            k-=1
        print("Stars",end=" ")



    
