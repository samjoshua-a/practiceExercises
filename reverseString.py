def reverse_string(word: str) -> str:
    index = 1
    reverse =""
    while index <= len(word):
        reverse += word[-index]
        index += 1
    return reverse

result = reverse_string("auhsoj")
print(result)