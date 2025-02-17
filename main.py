import sqlite_lib as sl
from Customer import Customer


def main():

    sl.connection("customers.db")

    sl.run_query_update('''
    CREATE TABLE IF NOT EXISTS Customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        address TEXT NOT NULL,
        mobile TEXT NOT NULL);
    ''')

    def insert_customer(customer):
        sl.run_query_update('''
           INSERT INTO Customers (first_name, last_name, address, mobile)
           VALUES (?, ?, ?, ?);
           ''', (customer.first_name, customer.last_name, customer.address, customer.mobile))

    def print_all_customers() -> list[Customer]:
        result = sl.run_query_select('''
            SELECT * FROM Customers;
        ''');

        list_result = []
        for customer in result:
            new_customer = Customer(customer['id'], customer['first_name'], customer['last_name'],
                                    customer['address'], customer['mobile'])
            list_result.append(new_customer)
        return list_result

    customer1 = Customer(None,'John', 'Doe', 'Bazel 15 Tel Aviv', '050-555-5555')
    customer2 = Customer(None, 'Jane', 'Smith', 'Moria 100 Haifa', '050-666-6666')

    insert_customer(customer1)
    insert_customer(customer2)

    customer_list = print_all_customers()
    print(customer_list)
    print(customer_list[0] == customer_list[1])
    print(customer_list[0] != customer_list[1])
    print(hash(customer_list[0]))
    print(hash(customer_list[1]))

    sl.close()


if __name__ == "__main__":
    main()
