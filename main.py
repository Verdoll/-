import random


def rand_num():
    x = random.randint(1,100)
    return x

def rand_answer():
    x = random.randint(1,3)
    return x

def analize(x):
    aim = "idk"
    text = x.lower()
    dict = {
        "сколько":"number",
        "когда":"time",
        "любит":"love",
        "кто":"person",
        "где":"place",
        "во сколько":"time",
    }
    for key, value in dict.items():
        if key in text:
            aim = value
            break
    return aim

def answer(x):
    if x == "number":
        print('около', rand_num())

    elif x == "time":
        p_rand = rand_answer()
        if p_rand == 1:
            time = "лет"
        elif p_rand == 2:
            time = 'часов'
        elif p_rand == 3:
            time = 'минут'

        print('через', rand_num(), time)

    elif x == "love":
        p_rand = rand_answer()
        if p_rand == 1:
            print('любит на', rand_num(), '%')
        if p_rand == 2:
            print("все очень сложно")
        if p_rand == 3:
            print('обожает')

    elif x == "person":
        p_rand = rand_answer()
        if p_rand == 1:
            print('ты')
        if p_rand == 2:
            print('подруня')
        if p_rand == 3:
            print('я')

    elif x == "place":
        p_rand = rand_answer()
        if p_rand == 1:
            print('В России')
        if p_rand == 2:
            print('в', rand_num(), 'регионе')
        if p_rand == 3:
            print('рядом')

    else:
        p_rand = rand_answer()
        if p_rand == 1:
            print('скорее да')
        if p_rand == 2:
            print('50 на 50')
        if p_rand == 3:
            print('скорее нет')


print('Чтобы выйти нажмите 1')
while 1:
    question = input("Введите интересующий вопрос: ")
    if question != "1":
        answer(analize(question))
    else:
        break


