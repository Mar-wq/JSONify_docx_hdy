"""
Iterate over containers (i.e. "things that can contain EG_BlockLevelElts")
"""
from docx.oxml.ns import qn
from .generic import register_iterator
from ..elements.paragraph import paragraph
from ..elements.table import table

# RANGE MARKUP

# BODY
register_iterator(
    "CT_Body", TAGS_TO_YIELD={qn("w:p"): paragraph, qn("w:tbl"): table}
)

