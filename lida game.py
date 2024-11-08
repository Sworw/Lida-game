import random

class Hero:
    def __init__(self, health, energy, money, mood):
        self.health = health
        self.energy = energy
        self.money = money
        self.mood = mood

    def display_status(self):
        print(f"Здоровье: {self.health}, Энергия: {self.energy}, Деньги: {self.money}, Настроение: {self.mood}")

    def apply_outcome_changes(self, outcome):
        self.health += outcome.get('health', 0)
        self.energy += outcome.get('energy', 0)
        self.money += outcome.get('money', 0)
        self.mood += outcome.get('mood', 0)

    def is_alive(self):
        return self.health > 0 and self.energy > 0


class Event:
    def __init__(self, description, yes_outcome, no_outcome):
        self.description = description
        self.yes_outcome = yes_outcome
        self.no_outcome = no_outcome

    def present_event(self, hero):
        print(f'\nСобытие: {self.description}')
        choice = input('Да, или нет?: ').lower()

        if choice == 'да':
            hero.apply_outcome_changes(self.yes_outcome)
        elif choice == 'нет':
            hero.apply_outcome_changes(self.no_outcome)
        else:
            print('Введите "да" или "нет".')

        hero.display_status()

hero = Hero(50, 50, 50, 50)

events = [

    Event(
        "Вы нашли остатки обломков космического корабля. Исследовать его?",
        yes_outcome={"health": -10, "energy": -5, "money": 5},
        no_outcome={"mood": -5}
    ),
    Event(
        "Ядовитая лоза свисает с дерева и цепляется за вашу руку. Срезать её?",
        yes_outcome={"health": -10, "energy": -5},
        no_outcome={"health": -15}
    ),
    Event(
        "Вы столкнулись с диким инопланетным животным. Попробовать приручить?",
        yes_outcome={"health": -20, "mood": 10},
        no_outcome={"energy": -5}
    ),
    Event(
        "Ваше укрытие обрушилось под весом обильного дождя. Починить его?",
        yes_outcome={"health": -5, "energy": -15},
        no_outcome={"mood": -10}
    ),
    Event(
        "Вы находите затопленную пещеру. Попробовать проплыть через неё?",
        yes_outcome={"health": -15, "energy": -10},
        no_outcome={"mood": -5}
    ),
    Event(
        "На вас внезапно нападают мелкие, но агрессивные твари. Сбежать?",
        yes_outcome={"energy": -10, "health": -5},
        no_outcome={"health": -15}
    ),
    Event(
        "Вы набрели на древний монолит, излучающий странные вибрации. Коснуться?",
        yes_outcome={"health": -20, "mood": 15},
        no_outcome={"mood": -5}
    ),
    Event(
        "Вам на пути встречается хищное растение. Пройти осторожно?",
        yes_outcome={"energy": -5, "health": -10},
        no_outcome={"health": -20}
    ),
    Event(
        "Ваши запасы пищи начинают портиться. Съесть их сейчас?",
        yes_outcome={"health": -10, "energy": 10},
        no_outcome={"mood": -10}
    ),
    Event(
        "Вы вдыхаете странный аромат с цветущего поля. Останьтесь или уйти?",
        yes_outcome={"health": -15, "mood": 5},
        no_outcome={"energy": -5}
    ),
    Event(
        "Во время ночного отдыха вас кусает неизвестное насекомое. Уйти отсюда?",
        yes_outcome={"energy": -10, "health": -5},
        no_outcome={"health": -15}
    ),
    Event(
        "Внезапно земля под ногами начала дрожать. Найти безопасное место?",
        yes_outcome={"energy": -10, "mood": -5},
        no_outcome={"health": -20}
    ),
    Event(
        "Вы попали в зону высокой радиации. Уйти быстро?",
        yes_outcome={"energy": -15, "health": -10},
        no_outcome={"health": -25}
    ),
    Event(
        "Неожиданно сильный ветер сбивает вас с ног. Зацепиться за что-то?",
        yes_outcome={"health": -10, "energy": -5},
        no_outcome={"health": -15}
    ),
    Event(
        "Ваш фонарь выходит из строя в глубокой пещере. Найти выход в темноте?",
        yes_outcome={"energy": -10, "mood": -5},
        no_outcome={"health": -10}
    ),
    Event(
        "Вы находите ловушку с острыми шипами. Исследовать её на предмет сокровищ?",
        yes_outcome={"health": -15, "money": 10},
        no_outcome={"mood": -5}
    ),
    Event(
        "Вы ощущаете жуткий холод. Пытаться согреться?",
        yes_outcome={"energy": -5, "mood": -5},
        no_outcome={"health": -15}
    ),
    Event(
        "На вас сваливается грязевая лавина. Уйти, не тратя силы?",
        yes_outcome={"energy": -5, "mood": -10},
        no_outcome={"health": -10, "energy": -10}
    ),
    Event(
        "Вы теряете равновесие на скользком мосту. Удержаться за поручни?",
        yes_outcome={"health": -10},
        no_outcome={"health": -20, "energy": -5}
    ),
    Event(
        "Ваше оборудование перегревается. Остановиться и охладить его?",
        yes_outcome={"energy": -10},
        no_outcome={"health": -15}
    ),
    Event(
        "Вы наткнулись на странное свечение вдалеке. Подойти поближе?",
        yes_outcome={"mood": 5, "energy": -5},
        no_outcome={"mood": -2}
    ),
    Event(
        "Нашли заброшенный лагерь с припасами. Обследовать?",
        yes_outcome={"money": 10, "energy": 10},
        no_outcome={"mood": -3}
    ),
    Event(
        "Вы случайно наступили на ядовитое растение. Наблюдать за состоянием?",
        yes_outcome={"health": -15, "mood": -5},
        no_outcome={"health": -10}
    ),
    Event(
        "Во время поиска пищи вы находите странные ягоды. Попробовать их?",
        yes_outcome={"health": -20, "mood": 5},
        no_outcome={"mood": -5}
    ),
    Event(
        "Сильная пыльная буря поднялась внезапно. Найти укрытие?",
        yes_outcome={"health": -10, "energy": -15},
        no_outcome={"health": -20}
    ),
    Event(
        "Вы подскользнулись на мокрой скале и повредили ногу. Отдохнуть и перевязать?",
        yes_outcome={"health": -10, "energy": -10},
        no_outcome={"health": -20, "mood": -5}
    ),
    Event(
        "Вас укусило неизвестное насекомое. Принять меры?",
        yes_outcome={"health": -10, "mood": -5},
        no_outcome={"health": -20}
    ),
    Event(
        "Резкая перемена температуры вызвала озноб. Согреться у костра?",
        yes_outcome={"energy": -5, "mood": 5},
        no_outcome={"health": -15, "mood": -10}
    ),
    Event(
        "Вы находите загадочные грибы, но они могут быть ядовитыми. Съесть?",
        yes_outcome={"health": -20, "energy": 10},
        no_outcome={"mood": -5}
    ),
    Event(
        "Вы наткнулись на трещину в земле, откуда идет ядовитый газ. Убежать?",
        yes_outcome={"energy": -10, "health": -5},
        no_outcome={"health": -15, "mood": -5}
    ),
    Event(
        "Ваше тело ослаблено после долгого перехода. Отдохнуть или идти дальше?",
        yes_outcome={"energy": -5},
        no_outcome={"health": -10, "energy": -5}
    ),
    Event(
        "На пути вы находите зловещую темную воду. Попробовать на вкус?",
        yes_outcome={"health": -25, "energy": 5},
        no_outcome={"mood": -5}
    ),
    Event(
        "В лесу вы слышите странные звуки. Остановиться и обследовать?",
        yes_outcome={"health": -5, "energy": -10, "mood": -5},
        no_outcome={"mood": -5}
    ),
    Event(
        "Ваше оборудование случайно дало сильный разряд. Проверить его?",
        yes_outcome={"health": -10, "energy": -5},
        no_outcome={"health": -20}
    ),
    Event(
        "Резкий солнечный свет обжигает кожу. Остаться под солнцем?",
        yes_outcome={"health": -15, "mood": -5},
        no_outcome={"energy": -5}
    ),
    Event(
        "Вы находите источник воды, но он мутный. Пить?",
        yes_outcome={"health": -15, "energy": 10},
        no_outcome={"mood": -10}
    ),
    Event(
        "Вы подбираете необычный камень, но он радиоактивен. Оставить его?",
        yes_outcome={"health": -20},
        no_outcome={"mood": -5}
    ),
    Event(
        "На вашем пути появляется ядовитое облако. Быстро проскочить?",
        yes_outcome={"energy": -10, "health": -5},
        no_outcome={"health": -15, "mood": -5}
    ),
    Event(
        "Вы касаетесь незнакомого растения, и вас обжигает. Оставить его?",
        yes_outcome={"health": -10},
        no_outcome={"health": -15, "energy": -5}
    ),
    Event(
        "Вас укусил странный инопланетный комар. Остаться на месте?",
        yes_outcome={"health": -10},
        no_outcome={"mood": -5}
    ),
    Event(
        "Внезапный удар молнии вблизи. Вы слегка обожглись. Продолжить путь?",
        yes_outcome={"health": -10, "energy": -5},
        no_outcome={"health": -20}
    ),
    Event(
        "В ночи вы слышите странные шорохи. Подойти к источнику звука?",
        yes_outcome={"health": -15, "mood": -10},
        no_outcome={"mood": -5}
    )
    # Добавьте другие события без лишних ключей
]

def play_game(hero, events):
    print(f'\nТы согласилась отправиться в неизвестную точку вселенной за безумную сумму земной валюты,\nДумаю, ты полагала, что это будет случайная точка на земле...\nТак вышло что ты оказалась на другой планете и у тебя нет варината вернуться, хотя... всё может быть...')
    while hero.is_alive():
        event = random.choice(events)
        event.present_event(hero)

        if not hero.is_alive():
            print("Вы проиграли. Ваш герой погиб.")
            break

# Запуск игры
play_game(hero, events)
