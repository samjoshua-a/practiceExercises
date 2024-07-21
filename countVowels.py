def count_vowels(word: str) -> int:
    count = 0
    for i in word.lower():
        if i in "aeiou":
            count += 1
    return count

result = count_vowels("beautiful")
print(result)