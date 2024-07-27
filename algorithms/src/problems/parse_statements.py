# parse statement: a2(a2(bc))3db -> aabcbcabcbcdddb

def build_tree_from_s(s):
    root = Tree('')
    idx = 0
    while idx < len(s):
        char = s[idx]
        if char.isdigit():
            child = build_tree_from_s(s[idx+2:])
            root.add_child(child, count=int(char))

            n_children = len(child.children)
            while idx < len(s) and n_children != 0:
                if s[idx] == ')':
                    n_children -= 1
                idx += 1

        elif char == ')':
            return root
        else:
            l = idx
            while idx < len(s) and (s[idx] != ')' and not s[idx].isdigit()):
               idx += 1
            sub_char = s[l:idx]
            subtree = Tree(sub_char)
            root.add_child(subtree)

    return root


def unzip_str(target_s):
    tree = build_tree_from_s(target_s)
    return tree.build_str_from_self()


class Tree:

    def __init__(self, root: str):
        self.root = root
        self.children = []

    def add_child(self, child, count=1):
        self.children.append((child, count))

    def build_str_from_self(self):
        res_str = self.root
        for child, count in self.children:
            res_str += child.build_str_from_self() * count
        return res_str
