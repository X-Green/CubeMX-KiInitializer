class TreeNode(list):
    def __init__(self, name: str, values=list(), is_root=False):
        self.name = name
        self += values
        self.is_root = is_root

    def __str__(self):
        result = self.name
        for child in self:
            result += ("\n|" + str(child).replace("\n", "\n-"))
        return result


def parse_tree_string(target: str):
    kicad_obj = TreeNode("root", split_with_brackets_and_blanks(target), is_root=True)

    parse_subtree_string(kicad_obj)
    return kicad_obj


def parse_subtree_string(tree: TreeNode):
    for i in range(len(tree)):
        child = tree[i]
        if isinstance(child, str) and child.startswith("("):
            # this child is a subtree
            split_child = split_with_brackets_and_blanks(child[1: -1])
            tree[i] = TreeNode(split_child[0], split_child[1:])
            parse_subtree_string(tree[i])


def split_with_brackets_and_blanks(target: str):
    target = target.strip()
    bracket_count = 0
    result = list()
    pointer_bracket_out = 0
    pointer_bracket_in = 0
    for i in range(len(target)):
        c = target[i]
        if c == "(":
            if bracket_count == 0:
                result += target[pointer_bracket_out: i].split()
                pointer_bracket_in = i
            bracket_count += 1
        elif c == ")":
            bracket_count -= 1
            if bracket_count == 0:
                result.append(target[pointer_bracket_in: i + 1])
                pointer_bracket_out = i + 1
        elif i + 1 == len(target):
            result += target[pointer_bracket_out: i + 1].split()
    return result
