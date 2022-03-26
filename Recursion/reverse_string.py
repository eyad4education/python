def reverse_string(string):
    if string == "":
        return ""
    return reverse_string(string[1:len(string)]) + string[0]

print(reverse_string("abcd"))
