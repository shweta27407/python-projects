class Cookie:
    def __init__(self, color) -> None:
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print("Cookie one : ", cookie_one.get_color())
print("Cookie two : ", cookie_two.get_color())

cookie_two.set_color('red')
print("Cookie two : ", cookie_two.get_color())

print("#***********************")
# Understanding Pointers

num1 = 11
num2 = num1
print("Before num2 value is updated")
print("num1 : ", num1)
print("num2 : ", num2)

print("num1 points to : ", id(num1))
print("num2 points to: ", id(num2)) #points to the same address

num2 = 22

print("#***********************")
print("after num2 value is updated")
print("num1 : ", num1)
print("num2 : ", num2)

print("num1 points to : ", id(num1))
print("num2 points to: ", id(num2)) #points to the different address

# Pointers with Dictionaries
dict1 = {'value' : 11}
dict2 = dict1

print("#***********************")
print("Before dict2 value is updated")
print("dict1 : ", dict1)
print("dict2 : ", dict2)

print("dict1 points to : ", id(dict1))
print("dict2 points to: ", id(dict2)) #points to the same address

dict2['value'] = 22

print("#***********************")
print("aftwe dict2 value is updated")
print("dict1 : ", dict1)
print("dict2 : ", dict2)

print("dict1 points to : ", id(dict1))
print("dict2 points to: ", id(dict2)) #points to the same address