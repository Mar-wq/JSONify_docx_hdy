"""
Elements which inherit from EG_PContent
"""
from typing import Optional, Dict, List, Any, Sequence, Iterator
from . import el, container



class paragraph(container):
    """ 
    Represents a simple paragraph
    """

    __type__ = "CT_P"

    def to_json(
        self, doc, options: Dict[str, str], super_iter: Optional[Iterator] = None
    ) -> Dict[str, Any]:
        """Coerce a container object to JSON
        """
        out: Dict[str, Any] = super(paragraph, self).to_json(doc, options, super_iter)





        return out






