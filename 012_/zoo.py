# Родительский класс Animal
class Animal:
    """Класс, представляющий животное."""

    def __init__(self, name, species):
        self._name = name  # Приватный атрибут
        self._species = species  # Приватный атрибут

    @property
    def name(self):
        """Геттер для имени животного."""
        return self._name

    @property
    def species(self):
        """Геттер для вида животного."""
        return self._species

    def feed(self):
        """Метод кормления, который должен быть переопределён в подклассах."""
        raise NotImplementedError ("Метод feed должен быть реализован в подклассах")

    def __repr__(self):
        return f"{self._name} is a {self._species}"


# Подкласс Mamal (млекопитающие)
class Mamal(Animal):
    """Класс, представляющий млекопитающих."""

    def __init__(self, name, fur_color):
        super().__init__(name, species="Mamal")
        self._fur_color = fur_color  # Приватный атрибут

    @property
    def fur_color(self):
        """Геттер для цвета шерсти."""
        return self._fur_color

    def feed(self):
        """Механизм кормления для млекопитающих."""
        print(f"{self.name} is fed with grass and meat.")

    def __repr__(self):
        return f"{self._name} is a {self._species} with {self._fur_color} fur"


# Подкласс Bird (птицы)
class Bird(Animal):
    """Класс, представляющий птиц."""

    def __init__(self, name, wing_span):
        super().__init__(name, species="Bird")
        self._wing_span = wing_span  # Приватный атрибут

    @property
    def wing_span(self):
        """Геттер для размаха крыльев."""
        return self._wing_span

    def feed(self):
        """Механизм кормления для птиц."""
        print(f"{self.name} is fed with seeds and insects.")

    def __repr__(self):
        return f"{self._name} is a {self._species} with a wingspan of {self._wing_span} meters"


# Подкласс Reptile (рептилии)
class Reptile(Animal):
    """Класс, представляющий рептилий."""

    def __init__(self, name, scale_type):
        super().__init__(name, species="Reptile")
        self._scale_type = scale_type  # Приватный атрибут

    @property
    def scale_type(self):
        """Геттер для типа чешуи."""
        return self._scale_type

    def feed(self):
        """Механизм кормления для рептилий."""
        print(f"{self.name} is fed with small mammals and insects.")

    def __repr__(self):
        return f"{self._name} is a {self._species} with {self._scale_type} scales"


# Класс Zoo для управления животными
class Zoo:
    """Класс для управления зоопарком."""

    def __init__(self, name):
        self._name = name  # Приватный атрибут
        self._animals = []  # Приватный список для хранения животных

    @property
    def name(self):
        """Геттер для имени зоопарка."""
        return self._name

    def add_animal(self, animal):
        """Добавить животное в зоопарк."""
        if isinstance(animal, Animal):
            self._animals.append(animal)
            print(f"{animal.name} was added to the zoo.")
        else:
            print("This is not a valid animal!")

    def remove_animal(self, animal):
        """Удалить животное из зоопарка."""
        if animal in self._animals:
            self._animals.remove(animal)
            print(f"{animal.name} was removed from the zoo.")
        else:
            print(f"{animal.name} is not in the zoo.")

    def list_animals(self):
        """Вывести список всех животных в зоопарке."""
        if self._animals:
            print(f"Animals in {self._name}:")
            for animal in self._animals:
                print(f"  - {animal}")
        else:
            print(f"No animals in {self._name}.")

    def get_animals_by_species(self, species):
        """Получить всех животных определённого вида."""
        result = [animal for animal in self._animals if animal.species == species]
        return result

    def count_animals(self):
        """Посчитать общее количество животных в зоопарке."""
        return len(self._animals)

    def feed_all_animals(self):
        """Кормление всех животных в зоопарке."""
        print(f"\nFeeding all animals in {self._name}:")
        for animal in self._animals:
            animal.feed()

# Программа main для демонстрации функционала
def main():
    # Создаём экземпляры животных
    simba = Mamal("Simba", "golden")
    eagle = Bird("Eagle", 2.3)
    snake = Reptile("Snake", "smooth")

    # Создаём экземпляр зоопарка
    my_zoo = Zoo("City Zoo")

    # Добавляем животных в зоопарк
    my_zoo.add_animal(simba)
    my_zoo.add_animal(eagle)
    my_zoo.add_animal(snake)

    # Список всех животных
    my_zoo.list_animals()

    # Получаем животных по виду
    print("\nMammals in the zoo:")
    mammals = my_zoo.get_animals_by_species("Mamal")
    for mammal in mammals:
        print(mammal)

    # Удаляем животное
    my_zoo.remove_animal(eagle)

    # Список после удаления
    my_zoo.list_animals()

    # Количество животных в зоопарке
    print(f"\nTotal animals in the zoo: {my_zoo.count_animals()}")

    # Покормим животных
    my_zoo.feed_all_animals()


# Запуск программы
if __name__ == "__main__":
    main()

