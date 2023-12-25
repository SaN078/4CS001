#list with six even numbers!!
list_1 = [2,4,6,8,10,12]
print(list_1)
#list of vowel
list_2 = ['a','e','i','o','u']
print(list_2)

list_3 = [1,'Hello World',2.5,True]
print(list_3)



car_list = ['Supra', 'Ferrari', 'Honda Civic', 'Rolls Royce', 'MARUTI 800']

print(car_list[2])

new_car = 'Alto'
car_list.append(new_car)

print('New Car Collection: ', car_list)

car_list.insert(2,'BMW')

print("After business success: ",car_list)

del car_list[6]

print('While considering retirement from taxi business ',car_list)

car_list.remove('MARUTI 800')

print('After complete retirement ', car_list)



print(len(car_list))
print(list(car_list))
print(car_list.count(3))
print(car_list.pop(2))
car_list.reverse()
print(car_list)



list_4 = ['red','blue','green','yellow','black']
for i in list_4:
    print(i)

for i in range(len(list_4)):
    print(list_4[i])
    i+=1


i = 0
while i < len(list_4):
    print(list_4[i])
    i+=1
