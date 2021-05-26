class Solution:
    def __init__(self, node):
        self.node = node

    def fail(self):
        return not self.node

    def steps(self):
        node = self.node
        steps = []

        while node and node.father:
            steps.append(node)
            node = node.father

        steps.append(node)

        return list(reversed(steps))

    def print(self):
        if self.fail():
            print('Não foi encontrado uma solução')

        steps = self.steps()

        for node in steps[:-1]:
            print(node.city, '-> ', end='')

        print(steps[-1].city, '||', 'Custo total:', self.node.total_cost())
