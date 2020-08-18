import random
character_set = "QWERTYUIOPASDFGHJKLZXCVBNM"


def random_word():

    answer = ""

    i = 0
    while i < 6:
        answer += random.choice(character_set)
        i += 1
    print(answer)


random_word()
