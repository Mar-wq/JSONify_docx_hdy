



__version__ = "1.0"

from typing import Union, Dict, Optional, Type, Any
from .elements import document
from .iterators.generic import build_iterators
from .textbook.book import Book
from .utils.set_options import parse_init


# --------------------------------------------------
# Main API
# --------------------------------------------------
def jsonfy_book(doc):
    parse_init(doc)
    book = Book(doc)
    return book.to_json()

