emails = ["ahmed@gmail.com", "ibrahim@iti.com", "ali@yahoo.com"]
def extract_domains(email_list):
    return list(map(lambda email: email.split('@')[1], email_list))
domains = extract_domains(emails)
print(domains)