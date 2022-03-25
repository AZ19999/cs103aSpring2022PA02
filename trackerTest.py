
import pytest
from category import*
from transactions import *
@pytest.mark.delete_test
def test_delete():
    category.delete(5)
    
    
@pytest.mark.summarize_year_test


def test_addTransaction():
    testCategory = Category("tracker.db")
    testRow = testCategory.select_one(5)
    testCategory.addTransaction(3,4,5,6,7)
    assert testCategory.addTransaction(3,4,5,6,7)==testRow


def test_summarizeMonth():
    testCategory = Category("tracker.db")
    month = 200511
    con = sqlite3.connect('tracker.db')
    cur = con.cursor()
    cur.execute('''SELECT year, amount FROM categories
                       WHERE year=(?) LIMIT 5;
    ''',(month,))
    z = cur.fetchall()
    con.commit()
    con.close()
    z = to_cat_dict(z)
    y = testCategory.summarizemonth(200511)
    assert z == y

def test_menu():
    assert True
    