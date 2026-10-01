# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
ML_IN_LITER = 1000


def classification_wno(bmi_value):  # Классификация по ВОЗ
    if (bmi_value < 16.0): 
        return 'Выраженный дефицит массы тела'
    elif (16.0 <= bmi_value <= 18.4):
        return 'Недостаточная масса тела'
    elif (18.5 <= bmi_value <= 24.9):
        return 'Нормальная масса тела'
    elif (25.0 <= bmi_value <= 29.9):
        return 'Избыточная масса тела (предожирение)'
    elif (30.0 <= bmi_value <= 34.9):
        return 'Ожирение I степени'
    elif (35.0 <= bmi_value <= 39.9):
        return 'Ожирение II степени'
    else:
        return 'Ожирение III степени (морбидное)'


def get_sufix_age(age):  # определение суфикса лет/год/года для возраста
    if ((age % 10 == 1) and (age % 100 != 11)):
        return 'год'
    elif ((age % 10 in [2, 3, 4]) and not (age % 100 in [12, 13, 14])):
        return 'года'
    else:
        return 'лет'

# 1. Приветствие
print('Вас приветствует цифровой фитнес-трекер')
print()

# 2. Знакомство
user_name = input('Введите Ваше имя:')
user_name = user_name.title() if user_name else 'АНОНИМ'

while True:
    try:
        user_age = int(input('Введите Ваш возраст:'))
        break
    except ValueError:
        print('Ошибка: введите пожалуйста, целое число лет.')

# 3. Сбор данных
while True:
    try:
        user_weight = float(input('Введите Ваш вес (в кг):'))
        break
    except ValueError:
        print('Ошибка: введите пожалуйста число (например 1.75)')

while True:
    try:
        user_height = float(input('Введите Ваш рост (в метрах):'))
        break
    except ValueError:
        print('Ошибка: введите пожалуйста число (например 1.75)')

# 4. Вычисление
bmi = user_weight / (user_height**2)  # расчёт индекса массы тела
bmi = round(bmi, 1)  # округление до одного знака после запятой
# Подсчет воды: вес * 30 мл
water_needed = user_weight * WATER_PER_KG
water_liters = water_needed / ML_IN_LITER

# 5. Вывод результата
print()
print(f'Отчет для пользователя: {user_name}  ({str(user_age)} {get_sufix_age(user_age)})')
print(f'Ваш Индекс Массы Тела: {bmi} ({classification_wno(bmi)})')
print(f'Рекомендуемая норма воды: {water_liters:.1f} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')
