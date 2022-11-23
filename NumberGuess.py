import sys
import logging
from random import randint

logging.basicConfig(level = logging.INFO, filename = "sample.log", format = "%(asctime)s - %(levelname)s - %(message)s")

def input_natural(message):  # Метод обработки ввода натурального числа
    while True:
        try:
            number = int(input(f'Введите целое число (от 1 до {sys.maxsize}) {message}: '))
            # sys.maxsize - максимально возможное значение переменной типа integer в данной версии Python
            if number < 1:  # Одно из условий натурального числа
                logging.error(f'Ошибка. Некорректный ввод с консоли ненатурального числа: {number}')
                print('Ошибка ввода. Попробуйте еще раз\n')
                continue
            return number
        except ValueError:
            logging.error(f'Ошибка. Некорректный ввод с консоли')
            print('Ошибка ввода. Попробуйте еще раз\n')

def guess_number(n, k): # Метод ввода догадок пользователя по числу
    secret_number = randint(1, n)   # Генерация случайного числа от 1 до n
    logging.info(f'Программа сгенерировала число: {secret_number}')
    print (f'Программа сгенерировала число от 1 до {n}. У вас {k} попыток угадать\n')
    for i in range(k):  # Цикл ввода догадок (кол-во итераций = числу k)
        guess_number = input_natural('- ваша догадка')
        logging.info(f'Ввод с консоли числа (предположение сгенерированного): {guess_number}')
        if guess_number == secret_number:
            print(f'Вы угадали!\n')
            logging.info('Сообщение о том, что пользователь угадал число')
            return
        else:
            if i == k - 1:  # Сработает на последней итерации
                print(f'Попытки закончились!\n')
                logging.info('Сообщение о том, что у пользователя закончились попытки')
                return
            elif guess_number > secret_number:
                print('Ваше число больше сгенерированного. Попробуйте еще раз\n')
                logging.info('Сообщение о том, что введенное число больше сгенерированного числа')
            elif guess_number < secret_number:
                print('Ваше число меньше сгенерированного. Попробуйте еще раз\n')
                logging.info('Сообщение о том, что введенное число меньше сгенерированного числа')

logging.info('Запуск программы')

n = input_natural('- границу диапазона генерируемого числа')
logging.info(f'Ввод с консоли числа {n} - границы диапазона генерируемого числа')
k = input_natural('- кол-во попыток угадать это число')
logging.info(f'Ввод с консоли числа {k} - кол-ва попыток угадать сгенерированное число')
guess_number(n, k)

input('Работа программы завершена. Для выхода из консоли нажмите Enter')
logging.info('Завершение работы программы\n')
