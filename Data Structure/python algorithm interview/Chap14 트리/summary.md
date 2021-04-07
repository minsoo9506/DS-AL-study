### 트리
- 그래프 vs 트리
  - 트리는 순환 구조를 갖지 않는 그래프
  - 트리에서 부모 노드는 단 하나, 루트도 하나

### 이진 트리
- 가장 널리 사용되는 트리는 이진트리와 이진탐색트리(BST)
- 일반적으로 트리라고 하면 대부분 이진트리를 의미
- 이진트리는 노드의 차수가 2이하인 트리

### 이진 탐색 트리
- 여기서 탐색이란 정렬되었다는 것을 의미한다.
- 노드의 왼쪽에는 작은 값, 오른쪽에는 같거나 큰 값이 위치한다.
- 장점은? 탐색이 $O(\log n)$

### 트리순회
- 그래프 순회의 한 형태로 트리 자료구조에서 각 노드를 정확히 한 번 방문하는 과정

```python
# 전위(Pre-Order) 순회 : NLR
def preorder(node):
  if node is None:
    return
  print(node.val)
  preorder(node.left)
  preorder(node.right)
# 중의(In-Order) 순회 : LNR
def inorder(node):
  if node is None:
    return
  inorder(node.left)
  print(node.val)
  inorder(node.right)
# 후위(Post-Order) 순회 : LRN
def postorder(node):
  if node in None:
    return
  postorder(node.left)
  postorder(node.right)
  print(node.val)
```

### Python 예시
- 이진트리 최대깊이
  - bfs
- 이진 트리의 직경
  - dfs
- 가장 긴 동일값의 경로
  - dfs
- 이진트리반전
  - 재귀, 큐, 스택
- 두 이진 트리 병합
  - 재귀
- 이진 트리 직렬화
  - bfs
- 균형 이진 트리
- 정렬된 배열의 이진 탐색 트리 변환
- 이진 탐색 트리를 더 큰 수 합계 트리로
- 이진 탐색 트리 합의 범위