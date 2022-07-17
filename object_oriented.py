import requests

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Elon", 50)

print(p1.name)
print(p1.age)

x = requests.get('https://query2.finance.yahoo.com/v8/finance/chart/%5EGSPC')

print(x.text)