# Проект FitLife - MVP версия 1.0


# 1. Знакомство
user_name = input("Как вас зовут?").strip()
user_name = user_name.title()

user_age = input("Сколько вам лет?")
user_age = int(user_age)
# Создаем переменную для окончания
year = ""

if 11 <= user_age % 100 <= 19:
    year = "лет"
elif user_age % 10 == 1:
    year = "год"
elif user_age % 10 in [2, 3, 4]:
    year = "года"
else:
    year = "лет"
# 2. Сбор данных
user_weight = input("Скажите свой вес (в кг)?")
user_weight = float(user_weight)

user_height = input("Скажите свой рост (в метрах)? Например 1.75-")
user_height = float(user_height)


# 3. Рассчет bmi (Индекс массы тела)
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
water_ml = user_weight * 30
water_needed = round((water_ml / 1000), 1)

# 4. Вывод красивого результата
print(" " * 30)
print(f"Отчет для пользователя: {user_name} {user_age} {year}")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_needed} л в день")
print(" " * 30)
print("Расчет окончен. Будьте здоровы!")
