def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{i}*{j}")

multiplication_table(5)
