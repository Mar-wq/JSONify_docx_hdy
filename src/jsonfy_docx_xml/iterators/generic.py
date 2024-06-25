from ..types import xmlFragment
from docx.enum.style import WD_STYLE_TYPE
from typing import (
        Optional,
        Tuple,
        Type,
        Dict,
        Sequence,
        NamedTuple,
        NewType,
        Callable,
        Generator,
        List
)
from ..elements.base import el



FragmentIterator = NewType('FragmentIterator',
        Callable[[xmlFragment, Optional[str]], Generator[xmlFragment, None, None]])
#给Callable[[xmlFragment, Optional[str]], Generator[xmlFragment, None, None]]这种类型对象取了个别名
#叫做FragmentIterator



FragmentIterator = NewType('FragmentIterator',
        Callable[[xmlFragment, Optional[str]], Generator[xmlFragment, None, None]])

# CONSTANTS

class ElementHandlers(NamedTuple):
    """
    A convenience class
    """
    TAGS_TO_YIELD: Optional[Dict[str, Type[el]]]


ElementHandlers.__new__.__defaults__ = (None,)* 1


__definitions__: Dict[str, ElementHandlers] = {}
__built__: Dict[str, ElementHandlers] = {}
__styles__: Dict[str, WD_STYLE_TYPE.PARAGRAPH] = {}


def register_iterator(name: str,
                      TAGS_TO_YIELD: Dict[str, Type[el]] = None
                     ) -> None:
    """
    An opinionated iterator which ignores deleted and moved resources, and
    passes through in-line revision containers such as InsertedRun, and
    orientation elements like bookmarks, comments, and permissions
    """


    __definitions__[name] = ElementHandlers(
            TAGS_TO_YIELD
            )




def build_styleId_mapping(doc):
    # 获取所有样式
    styles = doc.styles

    # 创建样式ID到样式对象的映射字典

    for style in styles:
        if style.type == 1:  # 1 表示段落样式
            __styles__[style.style_id] = style

    # 输出样式字典（仅供调试）
    for style_id, style in __styles__.items():
        print(f"Style ID: {style_id}, Style Name: {style.name}")


def build_iterators() -> None:
    """
    Build the iterators for the current iteration
    """

    _resovled: List[str] = []
    def _resolve(x: str):

        if x in _resovled:
            return

        xdef = __definitions__[x]


        TAGS_TO_YIELD = dict(xdef.TAGS_TO_YIELD) if xdef.TAGS_TO_YIELD else {}




        __built__[x] = ElementHandlers(
                TAGS_TO_YIELD=TAGS_TO_YIELD,
                )

        _resovled.append(x)

    for name in __definitions__:
        _resolve(name)




def xml_iter(
        p: xmlFragment,
        name: str,            #表示处理器的名称。
        msg: Optional[str] = None) -> Generator[el, None, None]:
    """
    Iterates over an XML node yielding an appropriate element (el)
    """

    handlers = __built__[name]

    # INIT PHASE
    children = p.getchildren()
    if not children:
        return

    current: Optional[xmlFragment] = p.getchildren()[0]

    # ITERATION PHASE
    while current is not None:

        #如果当前标签在 TAGS_TO_YIELD 中，生成对应的元素, 如果当前标签在 TAGS_TO_NEST 中，递归调用 xml_iter 处理嵌套内容。
        if handlers.TAGS_TO_YIELD \
                and current.tag in handlers.TAGS_TO_YIELD:
            # Yield all math tags
            yield handlers.TAGS_TO_YIELD[current.tag](current)

        #移动到下一个兄弟节点
        current = current.getnext()

    return