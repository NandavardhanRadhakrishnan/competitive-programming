# https://www.hackerrank.com/challenges/tree-top-view
# given a binary tree return the top view of the tree, as in what will be seen when seen from the top
# https://www.javatpoint.com/top-view-of-a-binary-tree

from collections import deque 
def topView(root):
    q = deque()
    q.append((root,0))
    d={}
    while q:
        node,num = q.popleft()
        d[num] = d.get(num,node.info)
        if node.left:
            q.append((node.left,num-1))
        if node.right:
            q.append((node.right,num+1))
    ans=[]
    for i in sorted(list(d.keys())):
        ans.append(d[i])
    print(*ans)