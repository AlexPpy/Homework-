"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
from datetime import datetime
history=[['Дата', 'Сумма']]
wallet=0
def adding_to_wallet(wallet_1):
    wallet_1=wallet
    print(f'На вашем счету {wallet_1}')
    x=input(f'Введите сумму пополнения')
    wallet_1+=int(x)
    return wallet_1

def buy(wallet_b):
    print(f'На вашем счету:{wallet_b}')
    amaunt=int(input(f'Введите сумму покупки...'))
    purch=[]

    if amaunt>wallet_b:
        print('На вашем счету недостаточно денегб пополните счет')
        pass
    else:
        pay=wallet_b-amaunt
        print(f'На вашем счету осталось:{pay}')
        now=datetime.now()
        n=now.strftime("%d/%m/%y %I:%M")
        purch.append(n)
        purch.append(amaunt)
        history.append(purch)
        return pay


def history_purchase(history_b):
    print('История ваших покупок:')
    for i in history_b:
        print(i)


while True:

    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        wallet=adding_to_wallet(wallet)
        print(wallet)
        pass
    elif choice == '2':
        wallet=buy(wallet)

        pass
    elif choice == '3':
        history_purchase(history)
        pass
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
