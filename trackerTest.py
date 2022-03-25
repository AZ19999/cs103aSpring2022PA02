import pytest
from category import Category
from transactions import Transaction

@pytest.mark.delete_test
def test_delete():
    category.delete(5)
    
    
@pytest.mark.summarize_year_test
def test_summarizeYear():
    print("unimplented")