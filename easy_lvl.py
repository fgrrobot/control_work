# 1A
mb = 200
print(f"в килобайтах: {mb * (2 ** 10)}")
print(f"в байтах: {mb * (2 ** 20)}")
print(f"в битах: {mb * (2 ** 20) * 8}")

# 2A
alphabet_len = 32
bit = 1
while alphabet_len > (2 ** bit):
  bit += 1
print(f"Количество информации в 100 символах: {bit * 100} бит")

# 3A
cool_list = [2, 3, 4, 4, 5, 6]

print(f"среднее арифмитическое крутого списка: {sum(cool_list) / len(cool_list)}")
