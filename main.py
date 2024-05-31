from task1 import good_num
from task2 import build_atm
from task3 import get_max_number

if __name__ == "__main__":
    string = input("Введите строку: ")
    good_num(string)
    n = int(input('Введите число n:'))
    k = int(input('Введите число k: '))
    L = [int(input()) for i in range(n)]
    print(build_atm(n, k, L))
    input_lst = input().split()
    print(get_max_number(input_lst))