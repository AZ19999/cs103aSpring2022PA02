import sqlite3
import csv

class Transaction:
    def __init__(self):
        self.one = 1
        con = sqlite3.connect('transactions.db')
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS transactions")
        cur.execute("CREATE TABLE IF NOT EXISTS transactions (item # int, amount int, category text, date text, description text)")
        con.commit()
        con.close()
        
        # load data
        csvfile = open('data/baby-names.csv','r')
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
        csvfile.close()

        # insert in table
        con = sqlite3.connect('transactions.db')
        cur = con.cursor()
        for d in data:
            cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",tuple(d.values()))
        con.commit()
        con.close()