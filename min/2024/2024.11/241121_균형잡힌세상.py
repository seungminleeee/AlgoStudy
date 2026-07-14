while True:
    text = input()
    if text == ".":
        break

    arr = []
    check = True

    for i in text:
        if i == "(" or i == "[":
            arr.append(i)
        elif i == ")":
            if len(arr) != 0 and arr[-1] == "(":
                arr.pop()
            else:
                check = False
                break
        elif i == "]":
            if len(arr) != 0 and arr[-1] == "[":
                arr.pop()
            else:
                check = False
                break
        elif i == ".":
            break

    if len(arr) == 0 and check:
        ans = "yes"
    else:
        ans = "no"

    print(ans)