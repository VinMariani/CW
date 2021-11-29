import json
import requests


class Player:
    def __init__(self, name, number, points=0, words=[]):
        self.name = name
        self.number = number
        self.points = points
        self.words = words

#player_one = Player()
#player_two = Player()

def print_report(player_one: Player, player_two: Player):
    print(
        f"Игра завершена!\nИгрок {player_one.number} - {player_one.name} заработал {player_one.points} очков\nИгрок {player_two.number} - {player_two.name} заработал {player_two.points} очков")
    if player_one.points > player_two.points:
        print(f"Выиграл игрок {player_one.name}!\nДанные записаны в файл")
    if player_one.points < player_two.points:
        print(f"Выиграл игрок {player_two.name}!\nДанные записаны в файл")
    if player_one.points == player_two.points and player_one.points > 0:
        print('Победила дружба!')
    if player_one.points == player_two.points == 0:
        print('Начните игру заново :)')

def game_starts(player_one = Player(name=input("Введите имя первого игрока: "), number=1,), player_two = Player(name=input("Введите имя второго игрока: "), number=2, )):
    return print(f"Привет, {player_one.name} и {player_two.name}!\nЕсли захотите выйти из игры - введите 'Stop'")
    '''Начало игры'''



def user_variants(): # НЕ РАБОТАЕТ
    return question.ask_question()
    round_number = 1
    return print(f'user_input = input(f"Вариант от игрока {player_one.name} - ")')
    return print(f"{user_input}")
    question.check_answer(user_input.lower())


class Question:
    def __init__(self, correct=True, asked_words=[], current_word="", game_is_on=True):
        self.asked_words = asked_words
        self.correct = correct
        self.current_word = current_word
        self.game_is_on = game_is_on

    def stop_game(self):
        '''выход из игры'''
        while self.game_is_on is True:
            if user_input.lower() == "stop":
                print("Oops... Будем ждать вас снова")
                self.game_is_on is False
            break

    def ask_question(self):
        '''вывод вопроса'''
        if len(game) > len(self.asked_words):
            for new_word in game.keys():
                if new_word not in self.asked_words:
                    self.asked_words.append(new_word)
                    self.current_word = new_word
                    return print(f"Ваше слово на эту игру: {new_word}")
        else:
            print(f"Вопросы закончились!")

    def check_answer(self, player_answer, player_one: Player, player_two: Player):
        '''проверка ответа'''
        self.player_answer = player_answer
        if self.player_answer in game[self.current_word] and self.player_answer not in player_one.words and self.player_answer not in player_two.words:
            self.correct = True
            return print("Слово принято!")
        else:
            print("Нет такого слова или вы повторяетесь")
        if question.correct is True:
            player_one.points += len(user_input.lower())
            player_one.words.append(user_input.lower())



def load_questions(url: str = "https://jsonkeeper.com/b/UEQV"):
    response = requests.get("https://jsonkeeper.com/b/UEQV")
    game = response.json()
    return game




game = load_questions()
question = Question()
user_input = ""

game_starts()


while user_input.lower() != "stop" and len(game) > len(question.asked_words):
    user_variants()


    #########

    print_report(player_one, player_two)

    result_lib = {"users": {
        1: "",
        2: ""
    },
        "word": "",
        "words": ""
    }

    result_lib["users"][1] = player_one.name
    result_lib["users"][2] = player_two.name
    result_lib["word"] = str(question.current_word)
    result_lib["words"] = player_one.words

    with open('results.json', 'w', encoding='UTF-8') as res_file:
        json.dump(result_lib, res_file, ensure_ascii=False)