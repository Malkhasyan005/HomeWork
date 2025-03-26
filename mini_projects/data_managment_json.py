import json
import os

file_name = "data.json"

def load_data():
    if not os.path.exists(file_name):
        return []
    
    try:
        with open(file_name, 'r',encoding="utf-8") as fs:
            data = json.load(fs)
            return data
    except:
        return []
    
def save_data(data):
    with open(file_name, 'w', encoding="utf-8") as fs:
        json.dump(data, fs, indent=4)

def add_data():
    print("\n===== Add Data =====")
    print("Add Data")
    data = load_data()
    while True:
        key = input("Enter key (or press Enter to finish): ").strip()
        if data.get(key):
            print("Key already exists")
            return
        if not key:
            break
        val = input(f"Enter value for '{key}': ")
        if not val:
            print("Not Data entered!! ")
            return
        data[key] = val

        save_data(data)
        print("Data added successfully")

        
def retrieve_data():
    print("\n===== Retrieve Data =====")
    data = load_data()
    if not data:
        print('Data not found!')
        return

    for key, value in data.items():
        print(f'{key}: {value}')
    
    return True


def update_data():
    print("\n===== Update Data =====")
    data = load_data()
    
    flag = retrieve_data()

    if flag:
        key = input("Enter the key to update: ")
        if data.get(key) is None:
            print("Key not found! ")
            return
        
        new_val = input("Enter the new value: ")
        if not new_val:
            print("Empty input!")
            return 
        
        data[key] = new_val
        save_data(data)
        print("Data updated successfully")

def delete_data():
    print("\n===== Delete Data =====")
    data = load_data()

    flag = retrieve_data()

    if flag:
        key = input("Enter the key to delet! ")
        if data.get(key) is None:
            print("Key not found! ")
            return

        data.pop(key)
        save_data(data)
        print("Data deleted successfully")


def main():
    while True:
        print("\n===== JSON Data Management System =====")
        print("1. Add Data")
        print("2. Retrieve Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1': add_data()
        if choice == '2': retrieve_data()
        if choice == '3': update_data()
        if choice == '4': delete_data()
        if choice == '5':
            print("Exiting the program...")
            break

    
main()