print("Меня зовут Татьяна")
print("Мне 25 лет")
name = int(input("Привет, как твоё имя?: "))
print("Привет,", name, "добро пожаловать!")
age = int(input("Сколько тебе лет?: "))
print("Привет,", name)
age = int(input("Сколько тебе лет?: "))
if age > 18:
    print("Доступ открыт")
elif 18 < age < 20:
    print("Доступ ограничен")
else:
    print("Доступ закрыт")
