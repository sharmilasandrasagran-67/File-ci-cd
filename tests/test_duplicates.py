import pytest
from scripts.duplicates import remove_duplicates

def test_remove_duplicates_basic():
    data = [1, 2, 2, 3]
    result = remove_duplicates(data)
    assert result == [1, 2, 3]

def test_remove_duplicates_empty():
    data = []
    result = remove_duplicates(data)
    assert result == []

def test_remove_duplicates_all_unique():
    data = [1, 2, 3, 4]
    result = remove_duplicates(data)
    assert result == [1, 2, 3, 4]

def test_remove_duplicates_all_duplicates():
    data = [5, 5, 5, 5]
    result = remove_duplicates(data)
    assert result == [5]
    
