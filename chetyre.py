sequence = input("Необходимо ввести последовательность чисел: ")
numbers = sequence.split()
seen_numbers = set()
for number in numbers:
    if number in seen_numbers:
        print("Да")
    else:
        print("Нет")
        seen_numbers.add(number)
