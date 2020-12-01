with open("1.txt.txt", "r") as file_:
    numbers = file_.read()

numbers = numbers.split("\n")
for number in numbers:
    for i in range(len(numbers)):
        wynik= int(number) + int(numbers[i])
        if wynik == 2020:
            print(int(number)*int(numbers[i]))

