class Node(object):
    def __str__(self):
        return self.printTree()

class Program(Node):
    def __init__(self, decl, func, inst):
         self.decls = decl
         self.funcs = func
         self.insts = inst

class BinExpr(Node):
    def __init__(self, left, op,right):
        self.op = op
        self.left = left
        self.right = right

class BracExpr(BinExpr):
    def __init__(self, expr):
        self.left = expr

class UnExpr(BinExpr):
    def __init__(self, expr):
        self.right = expr

class Expresions(Node):
    def __init__(self,exprs):
        self.exprs = [exprs]

class Const(Node):
    def __init__(self, const_type, value):
        self.type = const_type
        self.value = value

class Integer(Const):
     def __init__(self, value):
         self.type = const_type
         self.value = value

class Float(Const):
    def __init__(self, value):
        pass

class String(Const):
    def __init__(self, value):
        pass

class Variable(Node):
     def __init__(self, ID, name):
        self.ID = ID
        self.name = name

class Assignment(Node):
    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

class Condition(Node):
    def __init__(self, left, op,right):
        self.left = left
        self.op = op
        self.right = right

class While(Node):
    def __init__(self, cond, inst):
        self.cond = cond
        self.stmt = inst

class Repeate(Node):
    def __init__(self, cond, inst):
        self.cond = cond
        self.stmt = inst

class Choice(Node):
    def __init__(self, cond, inst1, inst2=None):
        self.cond = cond
        self.inst1 = inst1
        self.inst2 = inst2

class Declarations(Node):
    def __init__(self):
        self.decls = []

class Declaration(Node):
    def __init__(self, type,val):
        self.type = type
        self.id = id
        self.val = val

class Inits(Node):
    def __init__(self,init):
        self.inits = [init]

class Init(Node):
    def __init__(self,id,val):
        self.id = id
        self.val = val

class Instructions(Node):
    def __init__(self, instr):
        self.instrs = [instr]

class ComInstructions(Node):
    def __init__(self,decl,instr):
        self.decls = decl
        self.instrs = instr

class Functions(Node):
    def __init__(self):
        self.funcs = []

class Function(Node):
    def __init__(self, type, name,instr,args=None):
        self.type = type
        self.name = name
        self.args = args
        self.instrs = instr

class Print(Node):
    def __init__(self,expr):
        self.expr = expr

class Break(Node):
    def __init__(self):
        pass

class Continue(Node):
    def __init__(self):
        pass

class Arguments(Node):
    def __init__(self, arg):
         self.args = [arg]

class Return(Node):
    def __init__(self,ret):
        self.ret = ret

class Argument(Node):
    def __init__(self, type, id):
         self.type = type
         self.id = id

class CallArgument(Argument):
    def __init__(self, type, id):
         self.type = type
         self.id = id

class Call(Node):
    def __init__(self, name, args=None):
         self.name = name
         self.args = args


