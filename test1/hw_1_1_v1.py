import datetime
#Вариант 0

#print('Здравствуйте {} {}.'.format(input('Введите свою фамилию: '),input('Введите свое имя: ')))

#Вариант 1

surname_user = input('Введите свою фамилию: ')
name_user = input('Введите свое имя: ')
print('Здравствуйте {} {}.'.format(surname_user,name_user))
print('-'*40)
now = datetime.datetime.now()
DATE_2018_11_19 = datetime.datetime(2018,11,19)
birthday_dd_user = input('Введите День даты рождения: ')
birthday_mm_user = input('Введите Месяц даты рождения: ')
birthday_yy_user = input('Введите Год даты рождения: ')
birthday_user= datetime.datetime(int(birthday_yy_user),int(birthday_mm_user),int(birthday_dd_user))
# Кол-во времени между датами.
then = now - birthday_user
then_kyrs = DATE_2018_11_19 - birthday_user
print('''Колличество прожитых Вами лет - {}.
Колличество прожитых Вами месяцев - {}.'''.format(str(then.days//365),str(then.days//30)))
print('''Вы прожили до даты начала курса 19.11.2018 - 
    лет - {},
    месяцев -{}, 
    дней - {}.'''.format(str(then_kyrs.days//365),str(then_kyrs.days%365//30),str(then_kyrs.days%365%30)))
