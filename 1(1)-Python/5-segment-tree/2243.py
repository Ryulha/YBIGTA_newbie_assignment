from lib import SegmentTree
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