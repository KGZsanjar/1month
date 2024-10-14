# Класс Computer
class Computer:
    def init(self, cpu: int, memory: int):
        self.__cpu = cpu
        self.__memory = memory

    # Геттеры и сеттеры
    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu: int):
        self.__cpu = cpu

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory: int):
        self.__memory = memory

    # Метод для вычислений
    def make_computations(self):
        return f"Результат вычислений: {self.cpu * self.memory}"

    # Магический метод str
    def str(self):
        return f"Computer(cpu: {self.cpu}, memory: {self.memory})"

    # Переопределение магических методов сравнения
    def eq(self, other):
        return self.memory == other.memory

    def ne(self, other):
        return self.memory != other.memory

    def lt(self, other):
        return self.memory < other.memory

    def le(self, other):
        return self.memory <= other.memory

    def gt(self, other):
        return self.memory > other.memory

    def ge(self, other):
        return self.memory >= other.memory


# Класс Phone
class Phone:
    def init(self, sim_cards_list: list):
        self.__sim_cards_list = sim_cards_list

    # Геттеры и сеттеры
    def get_sim_cards(self):
        return self.__sim_cards_list

    def set_sim_cards(self, sim_cards_list: list):
        self.__sim_cards_list = sim_cards_list

    # Метод для звонков
    def call(self, sim_card_number: int, call_to_number: str):
        sim_card = self.__sim_cards_list[sim_card_number - 1]
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")

    # Магический метод str
    def str(self):
        return f"Phone(sim_cards: {', '.join(self.__sim_cards_list)})"


# Класс SmartPhone, наследующий от Computer и Phone
class SmartPhone(Computer, Phone):
    def init(self, cpu: int, memory: int, sim_cards_list: list):
        Computer.init(self, cpu, memory)
        Phone.init(self, sim_cards_list)

    # Метод для GPS
    def use_gps(self, location: str):
        print(f"Построение маршрута до {location}")

    # Магический метод str
    def str(self):
        return f"SmartPhone(cpu: {self.get_cpu()}, memory: {self.get_memory()}, sim_cards: {', '.join(self.get_sim_cards())})"


# Создание объектов
computer = Computer(4, 16)
phone = Phone(['Beeline', 'Megacom'])
smartphone1 = SmartPhone(8, 32, ['O!', 'Beeline'])
smartphone2 = SmartPhone(6, 16, ['Megacom', 'O!'])

# Печать информации о каждом объекте
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Использование методов объектов
computer.make_computations()
phone.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Бишкек")
smartphone2.make_computations()

# Сравнение объектов
print(computer == smartphone2)
print(smartphone1 > smartphone2)