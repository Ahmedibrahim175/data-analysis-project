def validate_email(email):
    if "@" in email:
        parts = email.split("@")
        if len(parts) == 2 and "." in parts[1]:
            return True
    raise ValueError("Invalid email.")

for i in range(3):
    email = input("Enter your email: ")
    try:
        if validate_email(email):
            print("Email is valid.")
            break
    except ValueError as error:
        print(error)
else:
    print("Failed after 3 tries.")
