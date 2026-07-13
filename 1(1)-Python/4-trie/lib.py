from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """
        # 구현하세요!
        
        node_index = 0  

        for element in seq:
            # 존재하는 자식 노드가 있는지 탐색
            for child_index in self[node_index].children:
                if self[child_index].body == element:
                    break
            # 일치하는 노드가 없다면 새로 생성
            else:
                child_index = len(self)
                self.append(TrieNode(body=element))
                self[node_index].children.append(child_index)

            node_index = child_index 

        self[node_index].is_end = True  

    # 구현하세요!