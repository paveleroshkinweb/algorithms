def multiStringSearch1(bigString, smallStrings):
    searches = []
    for string in smallStrings:
        is_substring = string in bigString
        searches.append(is_substring)
    return searches


def multiStringSearch2(bigString, smallStrings):
    
    def build_from_i(string, i, tree):
        current_tree = tree
        for idx in range(i, len(string)):
            char = string[idx]
            if char not in current_tree:
                current_tree[char] = {}
            current_tree = current_tree[char]
        return tree

    def build_suffix_tree(string):
        tree = {}
        current_tree = tree
        for i in range(len(string)):
            char = string[i]
            tree[char] = build_from_i(string, i+1, tree)
        return tree


    def is_substring(tree, string):
        for char in string:
            if char not in tree:
                return False
            tree = tree[char]
        return True

    tree = build_suffix_tree(bigString)
    return [is_substring(tree, string) for string in smallStrings]


def multiStringSearch3(bigString, smallStrings):
    
    def build_tree(smallStrings):
        tree = {}
        for string in smallStrings:
            node = tree
            for idx in range(len(string)):
                char = string[idx]
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['*'] = string
        return tree

    matched = set()
    tree = build_tree(smallStrings)

    for i in range(len(bigString)):
        node = tree
        for idx in range(i, len(bigString)):
            char = bigString[idx]
            if char not in node:
                break
            node = node[char]
            if '*' in node:
                matched.add(node['*'])
    return [string in matched for string in smallStrings]

