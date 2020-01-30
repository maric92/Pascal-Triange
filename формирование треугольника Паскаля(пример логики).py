def pascal_tringle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]

pascal_tringle(n = int(input('Введите количество строк  ')))