# Проект FitLife - MVP версия 1.0


# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную user_age
user_name = input("Как вас зовут?")
user_name = user_name.title()

user_age = input("Сколько вам лет?")
user_age = int(user_age)

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75)
user_weight = input("Скажите свой вес (в кг)?")
user_weight = float(user_weight)

user_height = input("Скажите свой рост (в метрах)? Например 1.75-")
user_height = float(user_height)


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_ml = user_weight * 30
water_needed = round((water_ml / 1000), 1)

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(" " * 30)
print(f"Отчет для пользователя: {user_name} {user_age} лет")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_needed} л. в день")
print(" " * 30)
print("Расчет окончен. Будьте здоровы!")
