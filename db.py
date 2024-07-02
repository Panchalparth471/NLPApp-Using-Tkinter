import json

class Database:
    
    def add_data(self, name, email, password):
        try:
            with open('mydb.json', 'r') as rf:
                database = json.load(rf)
        except FileNotFoundError:
            print("File not found. Ensure the file exists.")
            return 0
        except json.JSONDecodeError:
            print("Invalid JSON format in the file.")
            return 0
        
        if email in database:
            return 0
        else:
            database[email] = [name, password]
            with open("mydb.json", 'w') as f:
                json.dump(database, f, indent=4)
            return 1
    
    def login(self, email, password):
        try:
            with open('mydb.json', 'r') as rf:
                database = json.load(rf)
        except FileNotFoundError:
            print("File not found. Ensure the file exists.")
            return -1
        except json.JSONDecodeError:
            print("Invalid JSON format in the file.")
            return -1
        
        if email not in database:
            return -1
        
        saved_password = database[email][1]
        if password == saved_password:
            return 1
        else:
            print("Incorrect password.")
            return 0
