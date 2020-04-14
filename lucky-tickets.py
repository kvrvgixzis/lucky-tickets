'''
    Подсчитать количество счатливых билетов в диапозоне от 000000 до 999999
    Билет является счатливым, если сумма первых трех чисел равна сумме последних
    ==============================================================================
    Правильный ответ: 55252 
'''

import datetime

def luckyTickets_first():
    # решение "на ходу"
    clt = 1
    for t in range (1000, 1000000):
        left = t // 1000
        right = t % 1000
        leftsum = sum(map(int, str(left)))
        rightsum = sum(map(int, str(right)))
        if leftsum == rightsum:
            clt+=1
    return clt

def luckyTickets_universal():
    # для билетов произвольной четной длинны
    count_lucky_tickets, lenth = 1, 1
    while lenth % 2 != 0 and lenth != 0:
        print("Введите длину билетов(четное число): ", end="")
        lenth = int(input())
    range_st = 1 * 10 ** (lenth // 2)
    range_end = 1 * 10 ** lenth
    lucky_tickets_list = [ticket for ticket in range (range_st, range_end) if sum(map(int, str(ticket // range_st))) == sum(map(int, str(ticket % range_st)))]
    count_lucky_tickets = len(lucky_tickets_list) + 1
    return count_lucky_tickets

def luckyTickets_inline():
    # в строку с длиной 6
    return len([t for t in range (1000, 1000000) if sum(map(int, str(t // 1000))) == sum(map(int, str(t % 1000)))]) + 1

def timer(fn):
    st = datetime.datetime.now()
    result = fn()
    time = datetime.datetime.now() - st
    print(f"Билетов: {result} Секунд: {time}")

if __name__ == "__main__":
    timer(luckyTickets_first)
    timer(luckyTickets_inline)
    
    print(luckyTickets_universal()) # с любой четной длиной
