from boxprint import box
import error_corrector as ec

print("""
888b    888          888    888      d8b                  
8888b   888          888    888      Y8P                  
88888b  888          888    888                           
888Y88b 888  .d88b.  888888 88888b.  888 88888b.   .d88b. 
888 Y88b888 d88""88b 888    888 "88b 888 888 "88b d88P"88b
888  Y88888 888  888 888    888  888 888 888  888 888  888
888   Y8888 Y88..88P Y88b.  888  888 888 888  888 Y88b 888
888    Y888  "Y88P"   "Y888 888  888 888 888  888  "Y88888
                                                       888
We sell everything...                             Y8b d88P
                                                   "Y88P" """)

print("Starting...")
ec.check_mysql()
ec.check_data()

box(["Please Log In"], width=20)
user = input("Select User [Customer/Admin]: ")

if user == "Customer":
    import customer
elif user == "Admin":
    import admin
else:
    print("User not defined")