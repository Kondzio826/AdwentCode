with open("2.txt", "r") as txt_file:
    passwords = txt_file.read()

count = 0
passwords = passwords.split("\n")

for passwd in passwords:
    password = passwd.split(":")
    string = password[1]
    letter = password[0][-1]
    minimal = int(password[0].split("-")[0])
    maximal = int(password[0].split("-")[1].split(" ")[0])
    if string.count(letter) >= minimal and string.count(letter) <= maximal:
        count +=1
print(count)

