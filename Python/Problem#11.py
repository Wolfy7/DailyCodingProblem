"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

# bruteforce
def find_strings(s, set_strings):
    prefix_strings = []
    for i in set_strings:
        if i.startswith(s):
            prefix_strings.append(i)
    return prefix_strings

print(find_strings("de", ["dog", "deer", "deal", "deas"]))

# trie or prefix tree
class Trie():
    def __init__(self):
        self.nodes = {}

    def insert(self, str):
        node = self.nodes
        for s in str:
            if s not in node:
                node[s] = {}
            node = node[s]
        node["$"] = True

    def find_strings_with_prefix(self, prefix):
        node = self._get_node(prefix)
        findings = []
        self._collect(node, prefix, findings)
        return [prefix + f for f in findings]


    def _collect(self, node, prefix, findings):

        for s, n in node.items():
            if s == "$":
                findings.append("".join(prefix))
            else:
                self._collect(n, prefix + s, findings)


    def _get_node(self, prefix):
        node = self.nodes
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return None
        return node


t = Trie()
t.insert("dog")
t.insert("deer")
t.insert("dees")
t.insert("deal")
t.insert("deas")
t.insert("dede")

print(t.find_strings_with_prefix("de"))