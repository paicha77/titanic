# with open("titanic.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#
# print("Passengers:", len(lines) - 1)

# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         data = line.strip().split(",")
#         print(data)
#

# ramdeni gadarcha

# survived = died = 0

# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         Survived = line.split(",")[1]
#         if Survived == "1":
#             survived += 1
#         else:
#             died += 1
#
# print("Survived:", survived)
# print("Died:", died)

# gogo da kaci dayopa

# male = female = female_survived = 0
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         Sex = line.split(",")[4]
#         Survived = line.split(",")[1]
#
#         if Sex == "male":
#             male += 1
#         else:
#             female += 1
#             if Survived == "1":
#                 female_survived += 1
#
# print("Males:", male)
# print("Females:", female)
# print("Females survived:", female_survived)

# asaki

# ages = []
# under_18 = 0
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         Age = line.split(",")[5].strip()
#
#         if Age != "":
#             Age = float(Age)
#             ages.append(Age)
#
#             if Age < 18:
#                 under_18 += 1
#
# print("Under 18:", under_18)
# print("Average age:", sum(ages) / len(ages))

# meore asaki

# ages = []
# under_18 = 0

# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)  # skip header
#     for line in f:
#         # remove the comma inside the Name field
#         if '"' in line:
#             first_quote = line.find('"')
#             second_quote = line.find('"', first_quote + 1)
#             name = line[first_quote:second_quote + 1]
#             line = line.replace(name, name.replace(",", ""))
#
#         parts = line.strip().split(",")
#
#         Age = parts[5]
#
#         if Age != "":
#             Age = float(Age)
#             ages.append(Age)
#
#             if Age < 18:
#                 under_18 += 1
#
# print("Under 18:", under_18)
# print("Average age:", sum(ages) / len(ages))

# saxelebi da asaki

# names = []
# ages = []
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         parts = line.split(",")
#         names.append(parts[3])
#         if parts[5]:
#             ages.append(float(parts[5]))
#
# print(names)
# print(ages)

# names = []
# ages = []
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)  # skip header
#     for line in f:
#
#         # fix name comma problem
#         if '"' in line:
#             first = line.find('"')
#             second = line.find('"', first + 1)
#             name = line[first:second + 1]
#             line = line.replace(name, name.replace(",", ""))
#
#         parts = line.strip().split(",")
#
#         names.append(parts[3])
#
#         if parts[5] != "":
#             ages.append(float(parts[5]))
#
# print(names)
# print(ages)

# first class pessengers

# first_class = []
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         parts = line.split(",")
#         if parts[2] == "1":
#             first_class.append(parts[3])
#
# print(first_class)

# older then 60

# older_60 = []
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#
#         if '"' in line:
#             first = line.find('"')
#             second = line.find('"', first + 1)
#             name = line[first:second + 1]
#             line = line.replace(name, name.replace(",", ""))
#
#         parts = line.strip().split(",")
#
#         if parts[5] != "" and float(parts[5]) > 60:
#             older_60.append(parts[3])
#
# print(older_60)

# class passenger
#
# class_count = {}
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         pclass = line.split(",")[2]
#         class_count[pclass] = class_count.get(pclass, 0) + 1
#
# print(class_count)

# survived per class

# survivors_class = {}
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         parts = line.split(",")
#         pclass = parts[2]
#         survived = parts[1]
#
#         if survived == "1":
#             survivors_class[pclass] = survivors_class.get(pclass, 0) + 1
#
# print(survivors_class)

# oldes guy

oldest_age = 0
oldest_name = ""

with open("titanic.txt", "r", encoding="utf-8") as f:
    next(f)  # skip header
    for line in f:

        # fix comma inside Name
        if '"' in line:
            first = line.find('"')
            second = line.find('"', first + 1)
            name = line[first:second + 1]
            line = line.replace(name, name.replace(",", ""))

        parts = line.strip().split(",")

        if parts[5] != "":
            age = float(parts[5])
            if age > oldest_age:
                oldest_age = age
                oldest_name = parts[3]

print(oldest_name, oldest_age)










