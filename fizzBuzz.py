def fizz_buzz(num: int) -> list:
    output = []
    for _ in range(1, num+1):
        insert = ""
        if _%3==0:
            insert = "Fizz"
        if _%5==0:
            insert += "Buzz"
        if _%3!=0 and _%5!=0:
            insert=str(_)
        output.append(insert)
    return output

result = fizz_buzz(15)
print(result)