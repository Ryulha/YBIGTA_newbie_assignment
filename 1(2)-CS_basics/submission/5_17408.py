from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    # 구현하세요!
    def __init__(self, size: int) -> None:
        """        
        Args:
            size (int): 값의 최대 범위 (사탕 맛의 최대 등급인 1,000,000)
        """
        node = 1
        while node < size:
            node *= 2
            
        self.node = node
        self.tree = [0] * (self.node * 2 + 1)

    def update(self, target: int, val: int) -> None:
        """
        Args:
            target (int): 사탕의 맛 등급 (리프 노드의 위치)
            val (int): 더하거나 뺄 사탕의 개수 (+값은 추가, -값은 꺼냄)
        """
        index = self.node + target
        self.tree[index] += val
        
        while index > 1:
            index //= 2
            # 부모 노드는 왼쪽 자식과 오른쪽 자식의 합
            self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

    def query_and_pop(self, count: int) -> int:
        """        
        Args:
            count (int): 찾고자 하는 사탕의 등급 순위 (K번째)
            
        Returns:
            int: 찾은 사탕의 맛 등급 (1 ~ 1,000,000)
        """
        index = 1 
        
        while index < self.node:
            index *= 2  
            
            # 왼쪽 자식 구간에 있는 사탕의 개수가 수정이가 찾는 순위(count)보다 작다면
            if self.tree[index] < count:
                count -= self.tree[index] 
                index += 1                 # 오른쪽 자식 노드로 이동
                
        flavor = index - self.node
        
        # 사탕을 꺼낸 후 트리에서 1개 감소
        self.update(flavor, -1)
        
        return flavor


import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


class Pair(tuple[int, int]):
    """
    힌트: 2243, 3653에서 int에 대한 세그먼트 트리를 만들었다면 여기서는 Pair에 대한 세그먼트 트리를 만들 수 있을지도...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        기본값
        이게 왜 필요할까...?
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        원본 수열의 값을 대응되는 Pair 값으로 변환하는 연산
        이게 왜 필요할까...?
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: Pair, b: Pair) -> 'Pair':
        """
        두 Pair를 하나의 Pair로 합치는 연산
        이게 왜 필요할까...?
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    # 구현하세요!
    pass


if __name__ == "__main__":
    main()