c1 = {"city": "Moscow", "temperature": 25, "wind": True}
c2 = {"city": "Kaliningrad", "temperature": 20, "wind": False}
c3 = {"city": "Kiyv", "temperature": 22, "wind": False}
db1 = {"Anton": c1, "Yuriy": c2, "Alexey": c3}
naming = input('Как вас зовут?')
print(db1.get(naming))
naming2 = input('Как вас зовут?')