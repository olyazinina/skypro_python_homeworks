rate_as_str = input("Оцените работу оператора от 1 до 5:") 
rate = int(rate_as_str) 

if(rate<1):
    rate = 1

if(rate > 5):
    rate = 5

print(rate)

feedback = ''

if rate == 1:
    feedback = input("Что не понравилось больше всего?")
elif rate == 2:
        feedback = input("Расскажите, что нам улучшить?")
elif rate == 3:
    feedback = input("Вы нагловаты")
elif rate == 4:
    feedback = input("Ну и вам не хворать")
else:
     feedback = input("За что похвалить оператора?")

print(feedback)