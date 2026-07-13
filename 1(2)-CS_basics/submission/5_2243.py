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


def main() -> None:
    # 구현하세요!
    
    input = sys.stdin.readline

    first_line = input()
    if not first_line:
        return
        
    n = int(first_line)
    
    MAX_FLAVOR = 1000000
    seg_tree = SegmentTree(MAX_FLAVOR)
    
    for _ in range(n):
        query = list(map(int, input().split()))
        
        # 1: 사탕을 꺼내는 경우 
        if query[0] == 1:
            k = query[1]
            # K번째 사탕을 찾아서 꺼내고 맛의 등급을 출력합니다.
            result_flavor = seg_tree.query_and_pop(k)
            print(result_flavor)
            
        # 2: 사탕을 넣거나 빼는 경우 
        else:
            flavor = query[1]
            diff = query[2]
            seg_tree.update(flavor, diff)


if __name__ == "__main__":
    main()