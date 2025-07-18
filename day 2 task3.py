def is_valid_name(name):
    return name.isalpha() and len(name.strip()) > 1 and not name.startswith(" ")

def is_valid_email(email):
    try:
        email = email.strip()
        local, domain = email.split("@")
        if not local or not local[0].isalpha():
            return False
        if '.' not in domain:
            return False
        domain_name, extension = domain.rsplit('.', 1)
        if not domain_name.isalpha() or not extension.isalpha():
            return False
        if len(domain_name) < 2 or len(extension) < 2:
            return False
        return True
    except ValueError:
        return False

def collect_user_data():
    for _ in range(2):
        name = input("Enter your name: ").strip()
        if is_valid_name(name):
            break
        print("Invalid name. Please enter again.")
    else:
        print("Too many invalid attempts for name.")
        return

    for _ in range(2):
        email = input("Enter your email: ").strip()
        if is_valid_email(email):
            break
        print("Invalid email format. Try again.")
    else:
        print("Too many invalid attempts for email.")
        return

    print(f"Name accepted: {name}")
    print(f"Email accepted: {email}")

collect_user_data()
