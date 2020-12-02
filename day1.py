with open("1.txt.txt", "r") as file_:
    numbers = file_.read()

numbers = numbers.split("\n")
for number in numbers:
    for i in range(len(numbers)):
        for x in range(len(numbers)):
            wynik= int(number) + int(numbers[i]) + int(numbers[x])
            if wynik == 2020:
                answer = int(number)*int(numbers[i])*int(numbers[x])
print(answer)

