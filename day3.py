with open("3.txt","r") as _file:
    read = _file.read()

read = read.split("\n")
plane = 0
count = 0
flat = [1,3,5,7,1]
down = [1,1,1,1,2]
y=0
answer = 1
for x in flat:
    for i in read[::down[y]]:
        if i[plane%31] == ".":
            pass
        elif i[plane%31] == "#":
            count+=1
        plane+=x
    y+=1
    plane = 0
    answer = answer*count
    count = 0
print(answer)
    


    


    

