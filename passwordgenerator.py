import random
import string
symbols='!@#$%^&*()_'
numbers='1234567890'
all_characters=string.ascii_lowercase+string.ascii_uppercase+symbols+numbers
length=int(input("Please enter the preferred length for your password: "))
password=random.sample(all_characters,length)
final_password=""
for i in password:
    final_password+=i
print(f"Your newly created password is {final_password}")