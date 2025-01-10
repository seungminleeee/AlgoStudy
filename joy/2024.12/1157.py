word = input()
new_word = word.lower()
dict = {}
for i in new_word:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

lst = []
for i in dict.values():
    lst.append(i)

max_value = max(lst)
if lst.count(max_value) > 1:
    print('?')
else:
    for key, value in dict.items():
        if value == max_value:
            print(key.upper())
            break
