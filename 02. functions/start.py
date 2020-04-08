import copy
import random
# def sum():
#     print("function sum")


# sum()

# def sum(a, b):
#     print(a + b)


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# sum(a, b)


# global glob
# def sum(a=0, b=0):
#     glob = "Global vars"
#     if a > 0:
#         return a + b
#     else:
#         print("Test")
#         return 0


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# # res = sum(a, b)
# res = sum(a, b)
# print("Result = ", res)
# print(glob)

# def sum(*params):
#     res = 0
#     for item in params:
#         print(item)
#         res += item
#     return res


# result = sum(2, 5, 8, 1, 9, 4)
# print("Result => ", result)

# tmp = 10

# for i in range(1, tmp):
#     print(i)

# a = int(input("First number: "))
# b = int(input("Second number: "))


# def find_range(a, b):
#     res = 0
#     for i in range(a+1, b):
#         print("i = ", i)
#         res += i
#     return res


# result = find_range(a, b)
# print("Result => ", result)

# arr = [4, 6, 7, 8, 0, 5, 8, 3, 4, 8]
# # print(arr, "type => ", type(arr))
# # for i in arr:
# #     print(i)
# print("========================================>")
# arr[2] = 100
# # for i in arr:
# #     print(i)

# arr.append(99)
# print("========================================>")
# # arr[2] = 100
# # for i in arr:
# #     print(i)
# print("========================================>")
# arr.insert(2, 150)
# for i in arr:
#     print(i)

# arr.remove(4)
# print("========================================>")
# for i in arr:
#     print(i)

# print("index => ", arr.index(0))

# print("Arr len => ", len(arr))
# print("Count => ", arr.count(8))
# arr.pop()

# print("After pop => ")
# for i in arr:
#     print(i)

# print("Sort ========================================>")
# arr.sort()
# for i in arr:
#     print(i)


# print("Reverse ========================================>")
# arr.reverse()
# for i in arr:
#     print(i)

# print("Max => ", max(arr))
# print("Min => ", min(arr))

# arr = [4, 6, 7, 4, 5, 4, [55, 43, 34], 66, 44, "Works", True]
# print(arr)
# arr[6][1] = 90
# print(arr)

# person = ["Tom", "Bill", "Abram", "Steel", "Adam"]
# for i in person:
#     print(i)

# person.sort()
# for i in person:
#     print(i)

# numbers = []
# for i in range(30):
#     numbers.append(random.randint(-20, 30))
#     if numbers[i] < 0:
#         numbers[i] = -numbers[i]
#     print(numbers)


# lang = ["C++", "Python", "java Script", "C#", "Java", "PHP", "HTML", "CSS"]

# prog = lang
# print(prog)
# prog[0] = "Kotlin"
# print("Prog => ", prog)
# print("lang => ", lang)

# prog = copy.deepcopy(lang)
# prog[0] = "Kotlin"
# print("Prog => ", prog)
# print("lang => ", lang)

# part = lang[2:8:2]
# part = lang[:4]
# print(part)


# car = ("Bmw", "Renault", "VW", "Audi")
# print(car)

# for i in car:
#     print(i)

# print(car[-1])

# print(len(car))
# print("Audi count ", car.count("Audi"))

# i = 0
# while i < len(car):
#     print(car[i])
#     i += 1

# person = ("Bill", 34)

# name, age = person
# print("Name : ", name, "\nAge: ", age)

# countries = {
#     "UA": "Ukraine",
#     "US": "USA",
#     "BR": "Brasil"
# }

# for key, value in countries.items():
#     print(key, "====", value)

# countries.pop("BR")
# print("==============After=================")

# for key, value in countries.items():
#     print(key, "====", value)

# # for key in countries.keys():
# #     print(key)

# # for value in countries.values():
# #     print(value)

# # print(countries["UA"])
# print(countries.get("US"))
# countries["IT"] = "Italy"
# for key, value in countries.items():
#     print(key, "====", value)
