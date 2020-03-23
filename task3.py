class BracketsChecker:
    def __init__(self, input_line):
        self.input_line = input_line
        self.opened = '<({['
        self.closed = '>)}]'

    def is_opened(self, value):
        return value in self.opened

    def is_pair(self, a, b):
        return self.closed[self.opened.index(a)] == b

    def check(self):
        temporary = []
        for symbol in self.input_line:
            if symbol not in self.opened and symbol not in self.closed:
                return False
            elif self.input_line[0] in self.closed or len(self.input_line) % 2 != 0:
                return False
            else:
                if temporary is False:
                    temporary.append(symbol)
                elif self.is_opened(symbol):
                    temporary.append(symbol)
                else:
                    if self.is_pair(temporary.pop(), symbol) is False:
                        return False
        return True


b = BracketsChecker('({[<>]})')
print(b.check())

c = BracketsChecker(')()')
print(c.check())

d = BracketsChecker(')<>(')
print(d.check())

e = BracketsChecker('({[()(<>)]}<>)')
print(e.check())

f = BracketsChecker('({)}')
print(f.check())
