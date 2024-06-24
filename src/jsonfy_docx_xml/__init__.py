



__version__ = "1.0"

from typing import Union, Dict, Optional, Type, Any
from .elements import document
from .iterators.generic import build_iterators
from .textbook.book import Book
from .utils.set_options import set_options as __set_options__

# --------------------------------------------------
# Main API
# --------------------------------------------------
def jsonfy_book(doc):
    book = Book(doc)
    build_iterators()
    return book.to_json()

