from random import randint, choice


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    def choose_defence(self, heroes_list):
        random_hero = choice(heroes_list)
        self.__defence = random_hero.ability

    def attack(self, heroes_list):
        for hero in heroes_list:
            if hero.health > 0:
                if type(hero) == Berserk and self.__defence != hero.ability:
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    @property
    def defence(self):
        return self.__defence

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes_list):
        pass

    def attack(self, boss):
        boss.health -= self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes_list):
        coeff = randint(2, 5)
        boss.health -= coeff * self.damage
        print(f'Warrior {self.name} hits critically {coeff * self.damage}.')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')

    def apply_super_power(self, boss, heroes_list):
        # TODO here will be implementation of boosting
        pass


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_DAMAGE')
        self.__blocked_damage = 0

    def apply_super_power(self, boss, heroes_list):
        boss.health -= self.blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} damages to boss.')

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


round_number = 0


def is_game_over(boss, heroes_list):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes_list:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def show_statistics(boss, heroes_list):
    print(f' ------------- ROUND {round_number} -------------')
    print(boss)
    for hero in heroes_list:
        print(hero)


def play_round(boss, heroes_list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes_list)
    boss.attack(heroes_list)
    for hero in heroes_list:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes_list)
    show_statistics(boss, heroes_list)


def start_game():
    boss = Boss(name='Minotavr', health=1000, damage=50)

    warrior_1 = Warrior(name='Asterix', health=290, damage=10)
    warrior_2 = Warrior(name='Obelix', health=280, damage=15)
    magic = Magic(name='Alice', health=270, damage=5)
    berserk = Berserk(name='Guts', health=220, damage=10)
    doc = Medic(name='Doc', health=200, damage=5, heal_points=15)
    assistant = Medic(name='Junior', health=300, damage=5, heal_points=5)

    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant]
    show_statistics(boss, heroes_list)

    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)



import random


# Класс героя
class Hero:
    def init(self, name, health, attack, special=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.special = special
        self.is_dead = False

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_dead = True
            print(f"{self.name} погиб!")

    def heal(self, health_points):
        self.health += health_points
        print(f"{self.name} восстановил {health_points} здоровья")

    def perform_attack(self, boss):
        if not self.is_dead:
            boss.take_damage(self.attack)
            print(f"{self.name} атаковал босса и нанес {self.attack} урона!")


class Boss:
    def init(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"Босс получил {damage} урона! Осталось здоровья: {self.health}")

    def attack_hero(self, hero):
        if not hero.is_dead:
            print(f"Босс атакует {hero.name}!")
            hero.take_damage(50)  # Урон босса фиксированный для примера



class Witcher(Hero):
    def init(self, health, attack):
        super().init("Witcher", health, attack)
        self.revive_used = False

    def take_damage(self, damage):
        super().take_damage(damage)
        if self.health <= 0 and not self.revive_used:
            self.revive_used = True
            print("Witcher отдал свою жизнь, чтобы воскресить первого погибшего героя!")
            # Логика воскрешения героя, передав ему здоровье Witcher.



class Magic(Hero):
    def init(self, health, attack, n):
        super().init("Magic", health, attack)
        self.n = n

    def buff_allies(self, heroes):
        for hero in heroes:
            if not hero.is_dead:
                hero.attack += self.n
                print(f"Magic увеличил атаку {hero.name} на {self.n}")



class Hacker(Hero):
    def init(self, health, attack, n):
        super().init("Hacker", health, attack)
        self.n = n
        self.turn_counter = 0

    def steal_health(self, boss, allies):
        if self.turn_counter % 2 == 0:  # Каждые два хода
            boss.take_damage(self.n)
            hero_to_heal = random.choice(allies)
            hero_to_heal.heal(self.n)
            print(f"Hacker украл {self.n} здоровья у босса и передал {hero_to_heal.name}")



class Thor(Hero):
    def init(self, health, attack):
        super().init("Thor", health, attack)

    def perform_attack(self, boss):
        if not self.is_dead:
            chance = random.randint(1, 100)
            if chance <= 25:
                print(f"Thor оглушил босса!")
                # Логика оглушения босса на 1 раунд
            else:
                super().perform_attack(boss)


class TrickyBastard(Hero):
    def init(self, health, attack):
        super().init("TrickyBastard", health, attack)
        self.fake_dead_round = random.randint(1, 5)  # Случайный раунд

    def perform_attack(self, boss, current_round):
        if current_round == self.fake_dead_round:
            print(f"{self.name} притворился мертвым в этом раунде!")
        else:
            super().perform_attack(boss)



heroes = [
    Witcher(health=200, attack=0),
    Magic(health=150, attack=30, n=5),
    Hacker(health=120, attack=20, n=10),
    Thor(health=180, attack=40),
    TrickyBastard(health=160, attack=25)
]

boss = Boss(name="Boss", health=1000)

rounds = 5
for i in range(1, rounds + 1):
    print(f"\n=== Раунд {i} ===")

    for hero in heroes:
        hero.perform_attack(boss)

    if boss.health <= 0:
        print("Босс повержен!")
        break

    boss.attack_hero(random.choice(heroes))



if isinstance(heroes[1], Magic):
    heroes[1].buff_allies(heroes)

if isinstance(heroes[2], Hacker):
    heroes[2].steal_health(boss, heroes)

start_game()
