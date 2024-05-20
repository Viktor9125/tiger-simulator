import random


# класс тигра
class Tiger:
    def __init__(self):
        self.state = 'Выследить добычу'
        self.successful_attack_prob = 0.5
        self.x, self.y = 0, 0

    # это функция которая меняет состояние тигра
    def update_state(self, rabbits):
        if self.state == 'Выследить добычу':
            print('Тигр выслеживает добычу!')
            self.move_randomly()
            if any(self.is_near_rabbit(rabbit) for rabbit in rabbits):
                self.state = 'Атакавать добычу'
        elif self.state == 'Атакавать добычу':
            if random.random() < self.successful_attack_prob:
                print('Тигр успешно атаковал зайца!')

                for rabbit in rabbits:
                    if self.is_near_rabbit(rabbit):
                        rabbit.to_capture()

                self.state = 'Бежать домой'
            else:
                print('Тигр промахнулся!')
        elif self.state == 'Бежать домой':
            self.x, self.y = 0, 0

    # Эта функция двигает тигра в случайную клетку поля
    def move_randomly(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        self.x = max(0, min(self.x, 4))
        self.y = max(0, min(self.y, 4))

        # это функция определяет тигр рядом с зайцом

    def is_near_rabbit(self, rabbit):
        return abs(self.x - rabbit.x) <= 1 and abs(self.y - rabbit.y) <= 1

    def __str__(self):
        return f'Т (тигр): ({self.x}, {self.y})'


# класс зайца
class Rabbit:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.captured = False

    # Функция убирает зайца с поля
    def to_capture(self):
        self.captured = True

    def __str__(self):
        return f'З (заяц): ({self.x}, {self.y})'


# Функция выводит поле
def print_field(tiger, rabbits):
    field = []
    for _ in range(5):
        row = []
        for _ in range(5):
            row.append('.')
        field.append(row)

    field[tiger.x][tiger.y] = 'Т'
    for rabbit in rabbits:
        if not rabbit.captured:
            field[rabbit.x][rabbit.y] = 'З'
    for row in field:
        print(' '.join(row))
    print()


def main():
    tiger = Tiger()
    # 83 и 84 строки случайно определяют спавн зайца
    rabbit1 = Rabbit(random.randint(1, 4), random.randint(1, 4))
    rabbit2 = Rabbit(random.randint(1, 4), random.randint(1, 4))
    rabbits = [rabbit1, rabbit2]

    # цикл игры работает пока тигр не бежит домой
    while tiger.state != 'Бежать домой':
        print(tiger)
        for rabbit in rabbits:
            print(rabbit)
        print_field(tiger, rabbits)

        tiger.update_state(rabbits)

    print(tiger)
    for rabbit in rabbits:
        print(rabbit)

    tiger.update_state(rabbits)
    print_field(tiger, rabbits)
    if tiger.state == 'Бежать домой':
        print('Тигр вернулся домой.')


if __name__ == "__main__":
    main()
