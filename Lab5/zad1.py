import sqlite3


with sqlite3.connect('sales.db') as conn:
    cursor = conn.cursor()

    cursor.execute("select * from sales where product = 'Laptop'")
    rows = cursor.fetchall()
    print("a) Wyświetl tylko sprzedaż produktu „Laptop”")
    for row in rows:
        print(row)

    print("\n\n")

    print("b) Wyświetl dane tylko z dni 2025-05-07 i 2025-05-08")
    cursor.execute("select * from sales where date = '2025-05-07' or date = '2025-05-08'")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


    print("\n\n")

    print("c) Wyświetl tylko transakcje, w których cena jednostkowa przekracza 200 zł")
    cursor.execute("select * from sales where price >= 200")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


    print("\n\n")

    print("d) Oblicz łączną wartość sprzedaży dla każdego produkt")
    cursor.execute("select product, SUM(quantity * price) as suma from sales group by product")
    rows = cursor.fetchall()
    for row in rows:
        print(row)



    print("\n\n")

    print("e) Znajdź dzień z największą liczbą sprzedanych sztuk")
    cursor.execute("select * from (select date, sum(quantity) as ilosc from sales group by date) a order by ilosc desc limit 1")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

