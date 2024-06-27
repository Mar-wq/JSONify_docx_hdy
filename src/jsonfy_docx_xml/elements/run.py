from lxml import etree

from . import el, container
class run(container):
    __type__ = "run"

    def __init__(self, element):
        super().__init__(element)
        # 获取 run 对象的 XML 字符串
        xml_string = etree.tostring(element, encoding='unicode')

        # 解析 XML 字符串为 lxml 元素
        xml_element = etree.fromstring(xml_string)
        namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

        # 使用 xpath 查找属性
        b_element = xml_element.xpath('.//w:rPr/w:b', namespaces=namespaces)
        i_element = xml_element.xpath('.//w:rPr/w:i', namespaces=namespaces)
        sz_element = xml_element.xpath('.//w:rPr/w:sz', namespaces=namespaces)
        t_element = xml_element.xpath('.//w:t', namespaces=namespaces)
        if not t_element:
            return

        # 获取属性值
        # is_bold = True if b_element else False
        # is_italic = True if i_element else False
        # font_size = int(sz_element[0].get(
        #     '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')) / 2 if sz_element else None

        # 创建属性字典
        self.props = {}

        # 获取并添加属性值
        if b_element:
            self.props['bold'] = True
        if i_element:
            self.props['italic'] = True
        if sz_element:
            self.props['fontSize'] = int(
                sz_element[0].get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')) / 2
        if t_element:
            self.props['text'] = t_element[0].text


class commentReference(el):
    __type__ = "commentReference"

    def __init__(self, x):
        self.props = {}
        namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        rId = x.xpath('@w:id', namespaces=namespaces)[0]
        self.props['rId'] = rId
        print()


