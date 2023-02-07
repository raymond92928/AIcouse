from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
    
    def create_key(self, path):
        self.key = Fernet.generate_key()
        # print(self.key)
        pass
        
    def load_key(self, path):
        pass 
            
    def create_password_file(self, path, initial_values = None):
        self.password_file = path
        pass
        
            
    def load_password_file(self, path):
        self.password_file = path
        pass
                
    def add_password(self, site, password):
        self.password_dict[site] = password
        pass
    
    def get_password(self, site):
        return self.password_dict[site]

def main():
    password = {
        "email" : "123456",
        "facebook" : "012345",
        "instagram" : "my999"
    }
    
    pm = PasswordManager()
    print("""
    What do you want to do?
    (1) Create a new key
    (2) Load an existing key
    (3) Create new password file
    (4) Load existing password file
    (5) Add a new password
    (6) Get a password
    (q) Quit
    """)
    
    done = False
    
    while not done:
        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input("Enter path: ")
            pm.load_key(path)
        elif choice == "3":
            path = input("Enter path: ")
            pm.create_password_file(path, password)
        elif choice == "4":
            path = input("Enter path: ")
            pm.load_password_file(path)
        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        elif choice == "6":
            site = input("What site do you want: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif choice == "q":
            done = True
            print("Bye")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

