import json
import Whatsappcall

# Try to load existing data from a file
try:
    with open('user_data.json', 'r') as f:
        user_data = json.load(f)
except FileNotFoundError:
    # If the file doesn't exist, start with an empty dictionary
    user_data = {}

def store_data():
    user_id = input("Enter User ID: ")
    if user_id in user_data:
        print("User already exists.")
    else:
        value1 = input("Enter No1: ")
        value2 = input("Enter No2: ")
        value3 = input("Enter No3: ")
        user_data[user_id] = {'1': value1, '2': value2, '3': value3}
        # Write the updated data to the file
        with open('user_data.json', 'w') as f:
            json.dump(user_data, f)
def retrieve_data():
    user_id = input("Enter User ID: ")
    if user_id in user_data:
        print("choose (1,2 or 3)'",user_data[user_id])
        field = input("Enter field to print (or 'all' to print all fields): ")
        if field.lower() == 'all':
            print(user_data[user_id])
        elif field in user_data[user_id]:
            add_time=int(input("enter time:: "))
            Whatsappcall.phone_number(user_data[user_id][field])
            Whatsappcall.timer(add_time)
            print(user_data[user_id][field])
        else:
            print("Invalid field.")
    else:
        print("User not found.")

while True:
    print("\n1. Store Data\n2. Make Call\n3. Quit")
    option = input("Enter your option: ")
    if option == '1':
        store_data()
    elif option == '2':
        retrieve_data()
    elif option == '3':
        break
    else:
        print("Invalid option. Please try again.")
