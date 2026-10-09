ClassmateNames = ["Josh", "Eugene", "Quandale Dingle", "Yolanda", "Mike", "Emre"]
print(ClassmateNames, len(ClassmateNames))
print(ClassmateNames[0], ClassmateNames[5])
print(ClassmateNames[0:3])
ClassmateNames.append("farts")
print(ClassmateNames[6])
ClassmateNames.remove("farts")
print(ClassmateNames.sort())
dictionary = {
    "Teacher1": "Hates teaching,",
    "Mathematics Teacher": "Likes doing math",
    "Mr.Subsitute": "He doesnt care",
    "Science Maniac": "The FDA does not like him"
}

print(dictionary)
dictionary["Mathematics Teacher"]="mathmaniacs@maniacteacher.lol"
dictionary["Teacher1"]="sudo apt install loves teaching"
print(dictionary)
list = ["1", "2", "3", "4"]
name = ["Mike", "Micheal", "Efran", "Stevens"]
list1 = dict(zip(list, name))
print(list1)
