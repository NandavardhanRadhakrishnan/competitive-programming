# https://www.hackerrank.com/challenges/is-binary-search-tree
# given a root node check if the tree is a binary search tree or not

# i dont how this code works but the algo is simple and should work without any hacks, but supporting code is hidden and cant be debugged

def check_binary_search_tree_(root,mini=-1e9,maxi=1e9):
    if root==None:
        return True
    if root.data<=mini or root.data>=maxi:
        return False
    l=check_binary_search_tree_(root.left,mini,root.data)
    r=check_binary_search_tree_(root.right,root.data,maxi)
    return l and r