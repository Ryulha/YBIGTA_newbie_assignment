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


import sys


"""
TODO:
- 일단 lib.py의 Trie Class부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    # 구현하세요!

    MOD = 1000000007

    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    names = input_data[1:1 + n]

    trie: Trie[int] = Trie()
    for name in names:
        # 이름을 정수 형태로 저장
        int_seq = [ord(c) - 65 for c in name]
        trie.push(int_seq)

    # 팩토리얼 배열 미리 구하기
    fact = [1] * 26
    for i in range(1, 26):
        fact[i] = (fact[i - 1] * i) % MOD

    # 경우의 수 계산
    answer = 1
    for node in trie:
        k = len(node.children)

        if node.is_end:
            k += 1
            
        if k > 0:
            answer = (answer * fact[k]) % MOD

    print(answer)

if __name__ == "__main__":
    main()