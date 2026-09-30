# Проект FitLife - MVP версия 1.0


# 1. Приветствие
print('Вас приветствует цифровой фитнес-трекер')
print()

# 2. Знакомство
user_name=input('Введите Ваше имя:')
user_name=user_name.title() if bool(user_name) else 'АНОНИМ'

while True:
    try:
        user_age=int(input('Введите Ваш возраст:'))
        break
    except ValueError:
        print('Ошибка: введите пожалуйста, целое число лет.')

# 3. Сбор данных    
while True:
    try:
        user_weight=float(input('Введите Ваш вес (в кг):'))
        break
    except ValueError:
        print('Ошибка: введите пожалуйста, число в качестве разделителя целой и дробной части используйте "." (точка)')

while True:
    try:
        user_height=float(input('Введите Ваш рост (в метрах, например 1.75):'))
        break
    except ValueError:
        print('Ошибка: введите пожалуйста, число в качестве разделителя целой и дробной части используйте "." (точка)')

# 4. Вычисление  
bmi = user_weight/(user_height**2) # расчёт индекса массы тела
bmi = round(bmi,1) # округление до одного знака после запятой
# Подсчет воды: вес * 30 мл
water_needed = user_weight*30
water_liters = water_needed/1000

# 5. Вывод красивого результата
print('')
print('Отчет для пользователя:',user_name,'('+str(user_age)+' г.)')
print('Ваш Индекс Массы Тела:',bmi)
print(f"Рекомендуемая норма воды: {water_liters:.1f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
