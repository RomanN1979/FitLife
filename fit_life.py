# Проект FitLife - MVP версия 1.0


print('Вас приветствует цифровой фитнес-трекер')
print()
# 1. Знакомство
user_name=input('Введите Ваше имя:')
user_name=user_name.title() #Начать с заглавной буквы

while True:
    try:
        user_age=int(input('Введите Ваш возраст:'))
        break
    except ValueError:
        print('Ошибка: введите пожалуйста, целое число лет.')
# 2. Сбор данных        
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


bmi = user_weight/(user_height**2) # расчёт индекса массы тела
bmi = round(bmi,1) # округление до одного знака после запятой
# Подсчет воды: вес * 30 мл
water_needed = user_weight*30
water_liters = water_needed/1000

# определение суфикса лет/год/года для возраста
suffix = 'лет'  # по умолчанию
if ((user_age % 10 == 1) and (user_age % 100 != 11)):
    suffix = 'год'
elif ((user_age % 10 in [2, 3, 4]) and not (user_age % 100 in [12, 13, 14])):
    suffix = 'года'

# 4. Вывод красивого результата
print('')
print('Отчет для пользователя:',user_name,'('+str(user_age),'г.)')
print('Ваш Индекс Массы Тела:',bmi)
print(f"Рекомендуемая норма воды: {water_liters:.1f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")