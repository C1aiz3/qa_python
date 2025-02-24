import pytest
from main import BooksCollector

@pytest.fixture
def test_book():
    return BooksCollector()