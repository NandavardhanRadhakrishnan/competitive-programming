# https://www.hackerrank.com/challenges/tree-huffman-decoding
# given root node of huffman tree and huffman encoded string print decoded string

def decodeHuff(root, s):
    temp = root
    for i in s:
        if i == "0":
            temp = temp.left
        elif i == "1":
            temp = temp.right
        if(temp.left == None) and (temp.right == None):
            print(temp.data, end='')
            temp = root