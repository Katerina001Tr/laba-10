def errorCheck(n):                                                            #метод обработки ошибок 
    try:
        n = int(n)
    except Exception:
        return -1
    return n
N = - 1
while N == -1:                                                                   #цикл для ввода числа и обработка ошибок
    N = int(input('Введите натуральное число:\n'))
    if N<=0:
        print('Ошибка! Необходимо ввести натуральное число\n')
        N=-1
k=[64,32,16,8,4,2,1]                                                                 #список используемых купюр
print('Сумму можно выплатить:\n')
for i in k:                                                                          #поиск в списке нужных купюр и вывод их количества в консоль
    num=N//i
    N=N-(num*i)
    if num!=0:
        print(f'{num} куп. : номиналом {i} \n ')
    if N==0:
        break;
