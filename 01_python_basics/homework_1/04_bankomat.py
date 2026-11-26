amount = float(input("Введіть суму: ").replace(",", "."))
amount = round(amount * 100)

banknotes = [50000, 20000, 10000, 5000, 2000, 1000, 500]
coins = [200, 100, 50, 20, 10, 5, 2, 1]

banknotes_total = 0
coins_total = 0

print("\nСклад суми:")

for nominal in banknotes + coins:
    count = amount // nominal
    amount = amount % nominal

    if count > 0:
        print(count, "x", nominal / 100)

        if nominal in banknotes:
            banknotes_total += count
        else:
            coins_total += count

print("\nКількість банкнот:", banknotes_total)
print("Кількість монет:", coins_total)
