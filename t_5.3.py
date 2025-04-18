import random as rand
import json
import string

firstname = rand.choice(string.ascii_uppercase) + ''.join(rand.choices(string.ascii_lowercase, k = rand.randint(1, 9)))
secondname = rand.choice(string.ascii_uppercase) + ''.join(rand.choices(string.ascii_lowercase, k = rand.randint(1, 14)))
somename = f"{firstname} {secondname}"
someage = rand.randint(1, 120)
someemail = ''.join(rand.choices(string.ascii_lowercase + string.digits, k = rand.randint(6, 30))) + "@example.com"
somepassword = ''.join(rand.choices(string.ascii_letters + string.digits + string.punctuation, k = 12))

data = {"name": somename, "age": someage, "email": someemail, "password": somepassword}
json_string = json.dumps(data, indent = 4)
with open("json.txt", "w+", encoding="utf-8") as f:
    f.write(json_string)
    f.seek(0)
    print(f.read())