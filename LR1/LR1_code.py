# ---- ЗАДАНИЕ № 1 ----
my_list = list(range(45, 6, -3))  # Список от 45 до 7 с шагом 3
print(f"1.  Список от 45 до 7: {my_list}")

# ---- ЗАДАНИЕ № 2 ----
my_set = {i for i in my_list if i % 2 == 0}  # Множество из четных элементов списка
count_odd = sum(1 for i in my_list if i % 2 != 0)  # Подсчет нечетных элементов строки
print(f'\n2.  Количество нечетных в списке - {count_odd}'
      f'\nМножество четных элементов: {my_set}')

# ---- ЗАДАНИЕ № 3 ----
my_list.extend(list(my_set))  # Добавление элементов множества в список
print(f"\n3.  Список после добавления множества: {my_list}")
my_set.update(my_list)  # Добавление элементов списка в множество
print(f"Множество после добавления списка: {my_set}")

# ---- ЗАДАНИЕ № 4 ----
# Перестановка двух соседних элементов
def swap_words(text):
    word = text.split()
    for i in range(0, len(word) - 1, 2):
        word[i], word[i + 1] = word[i + 1], word[i]
    return " ".join(word)  # Метод строки, который объединяет слова через пробел в единый текст

my_text_4 = "поменять местами соседние слова между собой"
#my_text_4 = input("Введите текст строки: ")
print(f"\n4.  Исходная срока: {my_text_4}")
print(f"Строка после транспозиции пар: {swap_words(my_text_4)}")

# ---- ЗАДАНИЕ № 5 ----
# Работа со словарем
def process_dict(sl):
    # Ключи с max и min длиной
    # sl.keys(): первый аргумент (max) — это то, среди чего мы ищем максимум
    # key = len: сравнение (max) по длине ключей
    max_key = max(sl.keys(), key = len)
    min_key = min(sl.keys(), key = len)
    # sl[max_key]: берет числовые значения, соответствующие этим ключам
    avg_val = (sl[max_key] + sl[min_key]) / 2
    print(f"Самый длинный ключ - '{max_key}'\nСамый короткий ключ - '{min_key}'")
    print(f"Среднее значение: {avg_val}")
    # filter: оставляет значения, длина которых >= avg_val
    # sl.items(): превращает словарь в список пар (картежей) (ключ, значение)
    result_dict = dict(filter(lambda item: len(item[0]) >= avg_val, sl.items()))
    return result_dict

my_dict = {"яблоко": 5, "банан": 5, "киви": 1, "апельсин": 8, "груша": 4}
print(f"\n5.  Исходный словарь: {my_dict}")
print(f"Итоговый словарь: {process_dict(my_dict)}")

# ---- ЗАДАНИЕ № 6 ---- 
def filter_capitalized_words(text):
    word = text.split()
    # Оставляет слова на большую букву
    filtered = list(filter(lambda w: w[0].isupper(), word))
    filtered.sort()
    return filtered



my_text_6 = "Россия Китай франция Германия италия Япония сша"
#my_text_6 = input("Введите текст строки: ")
print(f"\n6.  Исходная срока: {my_text_6}")
fn = filter_capitalized_words(my_text_6)
fn1 = [word.lower() for word in fn]
gn = list(fn).sort()
print(gn)

# ---- ЗАДАНИЕ № 7 ----
import random
# Симулятор подбрасывания монеты
def coin_simulation():
    data_rounds = []  # Список для хранения истории всех раундов (результаты и кол-во попыток)
    count_attempts = 0  # Переменная для подсчета ОБЩЕГО количества бросков за все 10 раундов
    for i in range(1, 11):
        sequence = []  # Список, куда будем записывать результаты бросков ТЕКУЩЕГО раунда
        attempts = 0  # Счетчик бросков для ТЕКУЩЕГО раунда
        while True:
            attempts += 1
            result = random.choice(["Орел", "Решка"])
            sequence.append(result)
            if len(sequence) >= 3:
                if sequence[-1] == sequence[-2] == sequence[-3]:  # Проверка совпадения последних 3-х бросков
                    break
        data_rounds.append((sequence, attempts))
        count_attempts += attempts
        # sequence[-3:]: срез, который позволяет взять только конец списка (последние 3 элмента)
        print(f"Раунд {i} - попытка: {attempts}; последние броски: {sequence[:]}")
    avg_attempts = count_attempts / 10
    print(f"\nСреднее количество попвток за 10 раундов: {avg_attempts}\n")

print("\n7.")
coin_simulation()