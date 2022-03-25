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