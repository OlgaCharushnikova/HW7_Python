num_rows = int(input("Введите число строк: "))
num_columns = int(input("Введите число столбцов: "))
elements_list = list()

for i in range(num_rows + 1):
    for j in range(num_columns + 1):
        if i !=0 and j != 0:
            elements_list.append(i * j)
k = 0
while k < len(elements_list):
    print(*(elements_list[k : k + num_columns]))
    print(end = '\n')
    k = k + num_columns


          

# print_operation_table(operation, num_rows=6, num_columns=6)