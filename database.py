import sqlite3
connection = sqlite3.connect("clients.db")
sql = connection.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, balance REAL);")
connection.commit()


choice = int(input('1-registr, 2-search by name, 3-search by phone, 4-add money, 5-снятие денег, 6-просмотр баланса, 7-подсчет вклада 8-личный кабинет'))


def calculate_balance(balance):
    calculate12 = (balance[0] * 1 * (365 / 365)) / 100
    print(f'процент вклада за 12месяцев {calculate12}')

def calculate_balance24(balance):
    calculate12 = (balance[0] * 1 * (365 / 365)) / 100 * 2
    print(f'процент вклада за 12месяцев {calculate12}')

def calculate_balance36(balance):
    calculate12 = (balance[0] * 1 * (365 / 365)) / 100 * 3
    print(f'процент вклада за 12месяцев {calculate12}')


if choice == 1:
    # ------ Ввод данных для регистрации ------
    client_name = input('введите имя: ')
    phone = input('введите свой номер телефона: ')
    deposit = int(input('введите сумму пополнения: '))

    # ------ Регистрация ------
    def register(name, phone, balance):
        sql.execute('INSERT INTO clients (name,phone,balance) VALUES(?, ?, ?);', (name, phone, balance))
        connection.commit()

    register(client_name, phone, deposit)

    # Показать данные таблицы
    print(f'Все данные таблицы: {sql.execute("SELECT * from clients").fetchall()}')

elif choice == 2:
    # ------ Ввод данных(имени) для поиска ------
    search_name = input('введите имя: ')

    def search(name):
        client_info = sql.execute('SELECT * FROM clients WHERE name=?;', (name,)).fetchone()
        print(f'id: {client_info[0]}, Имя клиента: {client_info[1]}, номер телефона: {client_info[2]}, баланс: {client_info[3]}')

    search(search_name);

elif choice == 3:
    # ------ Ввод данных(номера телефона) для поиска ------
    search_phone = input('введите номер: ')

    def search(phone):
        client_info = sql.execute('SELECT * FROM clients WHERE phone=?;', (phone,)).fetchone()
        print(f'id: {client_info[0]}, Имя клиента: {client_info[1]}, номер телефона: {client_info[2]}, баланс: {client_info[3]}')

    search(search_phone)

elif choice == 4:
    # ------ Ввод данных(имени) для поиска ------
    name = input('введите имя: ')
    amount = int(input('введите сумму пополнения: '))
    balance = sql.execute('SELECT balance FROM clients WHERE name=?;', (name,)).fetchone()

    def update_balance(name, amount, balance):
        sql.execute(f'UPDATE clients SET balance={balance[0] + amount}  WHERE name=?;', (name,))
        connection.commit()
        info = sql.execute('SELECT * FROM clients WHERE name=?;', (name,)).fetchone()
        print(f'Обновленные данные {info}')

    update_balance(name, amount, balance)

    print(f'Все данные таблицы: {sql.execute("SELECT * from clients").fetchall()}')
elif choice == 5:
    name = input('введите имя: ')
    amount = int(input('введите сумму снятия: '))
    balance = sql.execute('SELECT balance FROM clients WHERE name=?;', (name,)).fetchone()

    def withdrawal_balance(name, amount, balance):
        sql.execute(f'UPDATE clients SET balance={balance[0] - amount}  WHERE name=?;', (name,))
        connection.commit()
        info = sql.execute('SELECT * FROM clients WHERE name=?;', (name,)).fetchone()
        print(f'Обновленные данные {info}')

    withdrawal_balance(name, amount, balance)

    print(f'Все данные таблицы: {sql.execute("SELECT * from clients").fetchall()}')

elif choice == 6:
    name = input('введите имя: ')
    def watch_balance(name):
        client_info = sql.execute('SELECT * FROM clients WHERE name=?;', (name,)).fetchone()
        print(f'Баланс клиента {client_info[1]}:  {client_info[3]}')

    watch_balance(name);

elif choice == 7:
    name = input('введите имя: ')
    calculate = int(input('Посчитать процент вклада 1-12месяцев, 2-24месяца, 3-36месяцев '))
    balance = sql.execute('SELECT balance FROM clients WHERE name=?;', (name,)).fetchone()
    if calculate == 1:
        calculate_balance(balance)
    elif calculate == 2:
        calculate_balance24(balance)
    elif calculate == 3:
        calculate_balance36(balance)
    else:
        print('I dont understand you')

elif choice == 8:
    name = input('введите имя: ')
    info = sql.execute('SELECT * FROM clients WHERE name=?;', (name,)).fetchone()
    print(f'Баланс клиента {info[1]}:  {info[3]}, номер телефона: {info[2]}')

else:
    print('I dont understand you')







