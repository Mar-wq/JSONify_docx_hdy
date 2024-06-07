"""
Iterate over containers (i.e. "things that can contain EG_BlockLevelElts")
"""
from docx.oxml.ns import qn
from .generic import register_iterator



# RANGE MARKUP

# BODY
register_iterator(
    "CT_Body", TAGS_TO_YIELD={}
)

