

import pytest
from category import *
from transactions import *


import pytest
from category import*
from transactions import *
@pytest.mark.delete_test
def test_delete():
    testCategory = Category("tracker.db")
    testRow = testCategory.select_one(5)
    testCategory.delete(5)
    testRow2 = testCategory.select_one(5)
    assert testRow != testRow2
    

@pytest.mark.summarize_date_test
def test_summarizeDate():
    testCategory = Category("tracker.db")
    date = 20050303
    con = sqlite3.connect('tracker.db')
    cur = con.cursor()
    cur.execute('''SELECT date, amount FROM categories
                       WHERE date=(?) LIMIT 5;
    ''',(date,))
    z = cur.fetchall()
    con.commit()
    con.close()
    z = to_cat_dict(z)
    y = testCategory.summarizeDate(20050303)
    assert z == y

@pytest.mark.summarize_category_test
def test_summarize_category():
    testCategory = Category("tracker.db")
    category = 'food'
    con = sqlite3.connect('tracker.db')
    cur = con.cursor()
    cur.execute('''SELECT category, amount FROM categories
                       WHERE category=(?) LIMIT 5;
        ''',(category,))
    z = cur.fetchall()
    con.commit()
    con.close()
    z = to_cat_dict(z)
    y = testCategory.summarizeDate(category)
    assert z == y

@pytest.mark.summarize_year_test


def test_addTransaction():
    testCategory = Category("tracker.db")
    testRow = testCategory.select_one(5)
    testCategory.addTransaction(3,4,5,6,7)
    assert testCategory.addTransaction(3,4,5,6,7)==testRow


def test_summarizeMonth():
    testCategory = Category("tracker.db")
    month = 200511

def test_summarizeYear():
    testCategory = Category("tracker.db")
    year = 2005

    con = sqlite3.connect('tracker.db')
    cur = con.cursor()
    cur.execute('''SELECT year, amount FROM categories
                       WHERE year=(?) LIMIT 5;

    ''',(month,))

    ''',(year,))

    z = cur.fetchall()
    con.commit()
    con.close()
    z = to_cat_dict(z)

    y = testCategory.summarizemonth(200511)
    assert z == y

def test_menu():
    assert True
    
    y = testCategory.summarizeyear(2005)
    assert z == y


    
