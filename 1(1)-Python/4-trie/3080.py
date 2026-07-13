from lib import Trie
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