

a = ord('a')

dict1 = {chr(a + i): i + 1 for i in range(20)}

letters = [chr((ord('a') + i)) for i in range(0, 20)]
numbers = [i for i in range(1, 21)]

print(letters)
print(numbers)


def func(list1, list2, length):
    return dict(zip(list1[:length], list2[:length]))


print(func(letters, numbers, 30))
