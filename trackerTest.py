import pytest

@pytest.mark.delete_test
def test_delete():
    testRow = category.select_one(5)
    category.delete(5)
    testRow2 = category.select_one(5)
    assert testRow != testRow2
    
@pytest.mark.summarize_year_test
def test_summarizeYear():
    year = 2005
    con = sqlite3.connect('tracker.db')
    cur = con.cursor()
    cur.execute('''SELECT year, amount FROM categories
                       WHERE year=(?) LIMIT 5;
    ''',(year,))
    z = cur.fetchall()
    con.commit()
    con.close()
    y = category.summarizeyear(2005)
    assert z == y