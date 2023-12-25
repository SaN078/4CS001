print('Welcome to list operation hall')
print('*'*20)

car_list = ['Supra', 'Ferrari', 'Honda Civic', 'Rolls Royce', 'MARUTI 800']

print('Enter 1 for Append, 2 for Insert, 3 for New list append, 4 for Modifying existing element, 5 for Deleting existing element, 6 for Deleting an existing element with its value, 7 for sorting and 8 to display the list')

user_input = int(input('Enter your Choice: '))

match user_input:
    case 1:
        user_append = input(" ::")
        car_list.append(user_append)
    case 2:
        user_insert = input("::")
        user_index = int(input("Index:: "))
        car_list.insert(user_index, user_insert)
    case 3:
        user_list = []
        limit = int(input("Enter your list limit"))
        for i in range(limit):
            element = input(f"Enter your element {i+1}")
            user_list.append(element)
        car_list += user_list
    case 4:
        user_index = int(input("Enter your index"))
        print(car_list[user_index])