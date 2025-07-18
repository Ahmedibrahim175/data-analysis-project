emails = ["ahmed@example.com","ahmed.com","ahmedser@.com","user@domain","data.iti@domain.com", "@ibrahim.com","ali@iti..com"," a.ibrahim@domain.com"]
def is_valid_email(email):
    email = email.strip()
    if " " in email:
        return False
    if email.count("@") != 1:
        return False
    user, domain = email.split("@")
    if not user or not domain:
        return False
    if "." not in domain:
        return False
    return True
valid_emails = list(filter(is_valid_email, emails))
print(valid_emails)
