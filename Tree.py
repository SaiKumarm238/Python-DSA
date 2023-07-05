# Tree is a Non-Linear Data Structure

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+= 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " "*self.get_level()*3
        prefix = spaces+ "|__" if self.parent else " "
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_tree():
    root = TreeNode("Tollywood")

    hero = TreeNode("Hero")
    hero.add_child(TreeNode("PK"))
    hero.add_child(TreeNode("AA"))
    hero.add_child(TreeNode("NTR"))
    hero.add_child(TreeNode("RC"))

    heroin = TreeNode("Heroins")
    heroin.add_child(TreeNode("Sam"))
    heroin.add_child(TreeNode("Anu"))
    heroin.add_child(TreeNode("Tam"))
    heroin.add_child(TreeNode("Poo"))

    comedian = TreeNode("Comedian")
    comedian.add_child(TreeNode("Bramhi"))
    comedian.add_child(TreeNode("Ali"))
    comedian.add_child(TreeNode("Venu"))
    comedian.add_child(TreeNode("Kishore"))

    root.add_child(hero)
    root.add_child(heroin)
    root.add_child(comedian)
    root.print_tree()


if __name__ == "__main__":
    build_tree()


