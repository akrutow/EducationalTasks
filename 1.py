class Indenter:
    def __init__(self):
        self.level = -1

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.level -= 1

    def print(self, text):
        print('    ' * self.level + text)


with Indenter() as indent:
    indent.print('python')
    with indent:
        indent.print('beegeek')
        with indent:
            indent.print('stepik')
        indent.print('pygen')
    indent.print('bye-bye')