import random

def find_pairs(dividible_by):
    pairs = ""
    for x in range(1, int(dividible_by/2) + 1):
        for y in range(x + 1, dividible_by):
            if dividible_by % (x + y) == 0 and x != y:
                pairs = pairs + str(x) +  str(y)
    return pairs

first_number = random.randint(3, 20)
print('Число на первом камне:', first_number)
result_pairs = find_pairs(first_number)
print('Пары чисел, чтобы их сумма была кратна:', first_number)
print(result_pairs)

