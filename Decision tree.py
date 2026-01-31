import math
from collections import Counter

data = [
    {'a1':'True','a2':'Hot','a3':'High','Class':'No'},
    {'a1':'True','a2':'Hot','a3':'High','Class':'No'},
    {'a1':'False','a2':'Hot','a3':'High','Class':'Yes'},
    {'a1':'False','a2':'Cool','a3':'Normal','Class':'Yes'},
    {'a1':'False','a2':'Cool','a3':'Normal','Class':'Yes'},
    {'a1':'True','a2':'Cool','a3':'High','Class':'No'},
    {'a1':'True','a2':'Hot','a3':'High','Class':'No'},
    {'a1':'True','a2':'Hot','a3':'Normal','Class':'Yes'},
    {'a1':'False','a2':'Cool','a3':'Normal','Class':'Yes'},
    {'a1':'False','a2':'Cool','a3':'High','Class':'Yes'}
]

def entropy(rows):
    counts = Counter(r['Class'] for r in rows)
    total = len(rows)
    return -sum((c/total)*math.log2(c/total) for c in counts.values())

def info_gain(rows, attr):
    total_entropy = entropy(rows)
    subsets = {}
    for r in rows:
        subsets.setdefault(r[attr], []).append(r)
    return total_entropy - sum(
        (len(s)/len(rows)) * entropy(s) for s in subsets.values()
    )

def id3(rows, attrs):
    classes = [r['Class'] for r in rows]
    if len(set(classes)) == 1:
        return classes[0]
    if not attrs:
        return Counter(classes).most_common(1)[0][0]

    best = max(attrs, key=lambda a: info_gain(rows, a))
    tree = {best: {}}
    subsets = {}

    for r in rows:
        subsets.setdefault(r[best], []).append(r)

    for val, subset in subsets.items():
        tree[best][val] = id3(subset, [a for a in attrs if a != best])

    return tree

def print_tree(tree, prefix="", is_last=True):
    if not isinstance(tree, dict):
        print(prefix + ("└── " if is_last else "├── ") + tree)
        return

    attr = list(tree.keys())[0]
    print(prefix + attr)
    branches = list(tree[attr].items())

    for i, (val, subtree) in enumerate(branches):
        last = (i == len(branches) - 1)
        print(prefix + ("└── " if last else "├── ") + val)
        print_tree(
            subtree,
            prefix + ("    " if last else "│   "),
            last
        )

tree = id3(data, ['a1','a2','a3'])
print_tree(tree)
