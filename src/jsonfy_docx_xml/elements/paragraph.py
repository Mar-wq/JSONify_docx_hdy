"""
Elements which inherit from EG_PContent
"""
from typing import Optional, Dict, List, Any, Sequence, Iterator

from more_itertools import peekable

from . import el, container


class paragraph(container):
    """ 
    Represents a simple paragraph
    """

    __type__ = "paragraph"

    def to_json(self, doc) -> Dict[str, Any]:
        """Coerce a container object to JSON
        """

        out = super().to_json(doc)
        if 'VALUE' in out:
            runs = out['VALUE']
            merge_runs = self.merge_runs(runs)
            out['VALUE'] = merge_runs

        return out

    # 定义了run块所需要的属性过后，合并属性相同的run，形成更大的run，便于阅读和解析
    def merge_runs(self, runs):
        merge_runs = []
        index = 0

        while index < len(runs):
            next_index = index + 1
            while self.has_text_attribute(runs[index]) and next_index < len(runs) and self.has_text_attribute(runs[next_index]) and self.compare_run(runs[index], runs[next_index]):
                runs[index]['text'] += runs[next_index]['text']
                next_index += 1

            merge_runs.append(runs[index])
            index = next_index  # 更新 index 跳过已经合并的部分

        return merge_runs

    def compare_run(self, run1, run2):
        # 复制字典，删除特定键
        dict1_filtered = {key: value for key, value in run1.items() if key != 'text'}
        dict2_filtered = {key: value for key, value in run2.items() if key != 'text'}

        # 比较过滤后的字典
        return dict1_filtered == dict2_filtered

    def has_text_attribute(self, run):
        return 'text' in run


class commentRangeStart(el):
    __type__ = "commentRangeStart"

class commentRangeEnd(el):
    __type__ = "commentRangeEnd"