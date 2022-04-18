class Token:
    def __init__(self, type: str, value: str, line: int, row: int):
        self.type = type
        self.value = value
        self.line = line
        self.row = row

    def __repr__(self):
        return 'Token({}, {})'.format(self.type, self.value)

    def __eq__(self, other): # type compare only
        return self.type == other.type

class Stack:
    def __init__(self):
        self.stack = []
        self.row = 0
        self.line = 0

    def push(self, item):
        self.stack.append(item)
    def peek(self, n=1):
        return self.stack[-n]
    def is_empty(self):
        return len(self.stack) == 0
    def __str__(self):
        return str(self.stack)
    def pop(self, n=1):
        buf = []
        for i in range(n):
            self.row += 1
            buf.append(self.stack.pop())
            if buf[-1].type == 'NewLine':
                self.line += 1
                self.row = 0
        if n==1:
            return buf[0]
        return buf


class State:
    def __init__(self):
        self.buffer = ''
    
class Text(State):
    def __init__(self):
        super().__init__()
        self.name = 'Text'

    def parse(self, stack):
        return stack.pop()

class Octo(State):
    def __init__(self):
        self.name = 'Octo'
        super().__init__()
        attributes = []
    
    def parse(self, stack):
        pass
    

class Plain(State): # root state
    def __init__(self):
        super().__init__()
        self.name = 'Plain'
    
    def parse(self, stack):
        # Titles
        if stack.peek_types(n=2)

        # SingleTick

        # Code Block

class Tokenizer:
    def __init__(self):
        self.tokens = []
        self.digits = [n for n in '0123456789']

    def scan(self, reader):
        while True:
            c = reader.read(1)
            if c == '': # EOF
                return self.tokens
            match c:
                case self.digits:
                    if self.tokens[-1].type == 'Digit':
                        self.tokens[-1].value += c
                    else:
                        self.tokens.append(Token('Digit', c))
                case '#': 
                    if self.tokens[-1].type == 'Octo':
                        self.tokens[-1].value += c
                    else:
                        self.tokens.append(Token('Octo', c))
                case ' ': self.tokens.append(Token('Space', c))
                case '\n': self.tokens.append(Token('Newline', c))
                case '.': self.tokens.append(Token('Dot', c))
                case '=': self.tokens.append(Token('Equal', c))
                case '`': 
                    if self.tokens[-1].type == 'Backtick':
                        self.tokens[-1].value += c
                    else:
                        self.tokens.append(Token('Backtick', c))
                case _:
                    if self.tokens[-1].type == 'Text':
                        self.tokens[-1].value += c
                    else:
                        self.tokens.append(Token('Text', c))

class Parser:
    '''
    BNF
    Plain ::= Text | Title | CodeBlock | SingleTick

    Title ::= Octo, Space, Text, NewLine
    CodeBlock ::= BackTick, NewLine, ANY+, NewLine, BackTick, NewLine
    '''
    def __init__(self):
        self.stack = Stack()
        self.body = ''
    def parse(self, tokens):
        tokens.reverse()
        self.stack.stack = tokens
        while not self.stack.is_empty():
            self.body += Plain().parse(self.stack)
        return self.body



def main(file_path):
    tokens = None
    tokenizer = Tokenizer()

    with open(file_path, 'r') as f:
        tokens = tokenizer.scan(f)

    return Parser().parse(tokens)

if __name__ == '__main__':
    print(main('test_files/single_title.md'))
    # main('test_files/lines_and_title.md')
    # main('test_files/h1_and_h2.md')
