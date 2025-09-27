import numpy as np
# 1C
cool_list = [1, 2, 3]
print(f"среднее арифмитическое крутого списка: {sum(cool_list) / len(cool_list)}")
cool_list = np.array(cool_list)
print(f"Дисперсия крутого списка: {round(np.var(cool_list), 3)}")

# 2C
a = int(input("Введите количество символов в алфавите: "))
b = int(input("Введите длинну строки в символах: "))
c = int(input("Введите количество строк на странице: "))

def cool_function(alphabet_len, line_len, lines_in_side):
    bit = 1
    while alphabet_len > (2 ** bit):
        bit += 1
    return bit * 2 * line_len * lines_in_side
print(f"количество информации на листе: {cool_function(a, b, c)} бит")

# 3C
data = input("введите дату в формате дата.месяц.год: ")
data = data.split(".")
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if int(data[2]) % 4 == 0:
    days_in_months[1] = 29

if int(data[0]) > days_in_months[int(data[1])-1] and int(data[0]) <= 0:
    print("даты не существует")
else:

    print("дата существует")
