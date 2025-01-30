

# task 2

def dalinti(a, b):
    try:
        return a / b
    except Exception as e:
        return f'Dalyba is nulio negalima: {e}'

print(dalinti(10, 2))
print(dalinti(5, 0))
print(dalinti(8, 4))







