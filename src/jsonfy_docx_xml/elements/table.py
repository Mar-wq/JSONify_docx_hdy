from jsonfy_docx_xml.elements import container


class table(container):
    __type__ = "CT_Tbl"


class tr(container):
    __type__ = "CT_Tr"

class tc(container):
    __type__ = "CT_Tc"
    __props__ = ['text']