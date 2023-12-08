words = set()
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        words_list = line.split()
        words.update(words_list)
        
num_different_words = len(words)
print(f"Кол-во различных слов в тексте: {num_different_words}")
