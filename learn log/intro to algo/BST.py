class Null:
    def __str__():
        return ""
    
class BinaryTree:

    def __init__(self,item,left=Null,right=Null,parent=Null):
        self.item = item
        self.left = left
        self.right = right
        if self.left is not Null:
            self.left.parent = self
        if self.right is not Null:
            self.right.parent = self

    def is_BST(self):
        def check(node,pre):
            if node is Null:
                return True,pre
            
            is_bst_left,pre = check(node.left,pre)
            if not is_bst_left:
                return False,pre
            
            if pre is not None and node.item <= pre:
                print(f"{node.item} <= {pre}")
                return False,pre
            
            pre = node.item

            return check(node.right,pre)
        is_bst,_ = check(self,None)
        return is_bst

    def is_leaf(self):
        if self.left is Null and self.right is Null:
            return True

    def __str__(self):
        if self.is_BST():
            if self.is_leaf():
                return f" {self.item} "
            return f" {self.left.__str__()} " + f" {self.item} " + f" {self.right.__str__()} "
        return "发生错误"
    
def swap(node1,node2):
    i = node1.item
    node1.item = node2.item
    node2.item = i


def find_fir(tree):
    if tree.left is Null:
        return tree
    return find_fir(tree.left)

def find_las(tree):
    if tree.right is Null:
        return tree
    else:
        return find_las(tree.right)

def find_suc(tree):
    if tree.right is Null:
        if tree.parent.left is tree:
            return tree.parent
        else:
            return None
    else:
        return find_fir(tree.right)

def find_pre(tree):
    if tree.left is Null:
        if tree.parent.right is tree:
            return tree.parent
        else:
            return None
    else:
        return find_las(tree.left)
    

def insert_aft(node,item):
    if node.right is Null:
        node.right = BinaryTree(item)

    else:
        suc = find_suc(node)
        suc.left = BinaryTree(item)

def delete(node):
    if node.is_leaf():
        if node.parent.left == node:
            node.parent.left = Null
        else:
            node.parent.right = Null
    elif node.left is not Null:
        pre = find_pre(node)
        swap(node,pre)
        delete(pre)
    else:
        suc = find_suc(node)
        swap(node,suc)
        delete(suc)
#增删查找操作的时间复杂度均为O(h),其中h为二叉搜索树高度，由此可见，若想保持操作效率，实现平衡二叉树是很有必要的。
