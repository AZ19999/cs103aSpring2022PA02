import pytest
from category import *
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



@pytest.mark.summarize_year_test
def test_summarizeYear():
    testCategory = Category("tracker.db")
    year = 2005
    con = sqlite3.connect('tracker.db')
    cur = con.cursor()
    cur.execute('''SELECT year, amount FROM categories
                       WHERE year=(?) LIMIT 5;
    ''',(year,))
    z = cur.fetchall()
    con.commit()
    con.close()
    z = to_cat_dict(z)
    y = testCategory.summarizeyear(2005)
    assert z == y