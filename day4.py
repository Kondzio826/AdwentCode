with open("4.txt","r") as _file:
    read = _file.read()
read = read.split("\n\n")
ver = {
"byr" : [1920,2002],
"iyr" : [2010,2020],
"eyr" : [2020 ,2030],
"hgt" : {"cm" : [150,193], "in": [59,76]},
"hcl" : "", # followed by exactly six characters 0-9 or a-f.
"ecl" : ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
"pid" : ""  #a nine-digit number, including leading zeroes.
}
count = 0
for passport in read:
    passport = passport.replace(" ","\n")
    passport = passport.split("\n")
    check = {}
    for element in passport:
        element = element.split(":")
        check[element[0]] = element[1]
    try:
        check.pop("cid")
    except KeyError:
        pass
    if ver.keys() == check.keys():
        if int(check["byr"]) >= ver["byr"][0] and int(check["byr"]) <= ver["byr"][1]:
            if int(check["iyr"]) >= ver["iyr"][0] and int(check["iyr"]) <= ver["iyr"][1]:
                if int(check["eyr"]) >= ver["eyr"][0] and int(check["eyr"]) <= ver["eyr"][1]:
                    if check["ecl"] in ver["ecl"]:
                        if len(check["hcl"]) == 7 and check["hcl"][0] == "#":
                            if len(check["pid"]) == 9:
                                if check["hgt"][-2:] == "cm" or check["hgt"][-2:] == "in":
                                    try:
                                        if check["hgt"][-2:] == "cm":
                                            if int(check["hgt"][0:3]) >= 150 and int(check["hgt"][0:3]) <= 193:
                                                count+=1
                                        
                                        if check["hgt"][-2:] == "in":
                                            if int(check["hgt"][0:2]) >= 59 and int(check["hgt"][0:2]) <= 76:
                                                count+=1
                                    except ValueError:
                                        pass

print(count)