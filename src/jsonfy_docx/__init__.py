



__version__ = "0.1.0"

from src.jsonfy_docx.types.fragment import documentPart
from typing import Union, Dict, Optional, Type, Any
from .elements import document
from .utils.set_options import set_options as __set_options__

# --------------------------------------------------
# Main API
# --------------------------------------------------
def simplify(doc: documentPart, options: Optional[Dict[str, Any]] = None):
    """
    Coerce Docx Documents to JSON
    """

    # SET OPTIONS
    _options: Dict[str, Any]
    if options:
        _options = dict(__default_options__, **options)
    else:
        _options = __default_options__

    __set_options__(_options)

    element_temp =  doc.element
    document_temp = document(element_temp)
    out = document_temp.to_json(doc, _options)


    return out



# --------------------------------------------------
# Default Options     默认选项
# --------------------------------------------------
__default_options__: Dict[str, Union[str, bool, int, float]] = {
    # general
    "friendly-names": True,
    # flattening special content
    "flatten-hyperlink": True,
    "flatten-smartTag": True,
    "flatten-customXml": True,
    "flatten-simpleField": True,
    "merge-consecutive-text": True,
    "flatten-inner-spaces": False,
    # possibly meaningful style:
    "include-paragraph-indent": True,
    "include-paragraph-numbering": True,
    # ignoring invisible things
    "ignore-joiners": True,
    "ignore-left-to-right-mark": False,
    "ignore-right-to-left-mark": False,
    "ignore-empty-table-description": True,
    "ignore-empty-table-caption": True,
    "ignore-empty-paragraphs": True,
    "ignore-empty-text": True,
    "remove-trailing-white-space": True,
    "remove-leading-white-space": True,
    # forms
    "use-checkbox-default": True,
    "greedy-text-input": True,
    "checkbox-as-text": False,
    "dropdown-as-text": False,
    "simplify-dropdown": True,
    "simplify-textinput": True,
    "simplify-checkbox": True,
    "flatten-generic-field": True,
    "trim-dropdown-options": True,
    # special symbols
    "empty-as-text": False,
    "symbol-as-text": True,
    "special-characters-as-text": True,
    "dumb-quotes": True,
    "dumb-hyphens": True,
    "dumb-spaces": True,
}
