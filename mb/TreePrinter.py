import AST


level = 0

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

def getBr():
    global level
    tmp = ""
    for l in xrange(level):
        tmp += "| "
    return tmp



class TreePrinter:

    

    @addToClass(AST.Node)
    def printTree(self):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Expresions)
    def printTree(self):
        ret = ""
        for e in self.exprs:
            ret += str(e)+"\n"
        return ret



    @addToClass(AST.BinExpr)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        level += 1
        ret += tmp +str(self.op) +"\n" + str(self.left) + "\n" + str(self.right)
        level -= 1
        return ret
 

    @addToClass(AST.BracExpr)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        ret += str(self.left)
        return ret



    @addToClass(AST.Const)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        ret = tmp + str(self.value)
        return ret

    @addToClass(AST.Integer)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        ret = tmp + str(self.value)
        return ret


    @addToClass(AST.Float)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        ret = tmp + str(self.value)
        return ret



    @addToClass(AST.String)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        ret = tmp + str(self.value)
        return ret



    @addToClass(AST.Variable)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        ret = tmp + str(self.ID)
        return ret

    @addToClass(AST.Assignment)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        level += 1
        ret = tmp + "=\n" + tmp + "| " +str(self.id)+ "\n"  + str(self.expr)
        level -= 1
        return ret


    @addToClass(AST.Condition)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        level += 1
        ret +=  tmp + str(self.op) + str(self.left)+  str(self.right)
        level -= 1
        return ret


    @addToClass(AST.While)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        level += 1
        ret += tmp + "WHILE\n"+ str(self.cond) + "\n" + str(self.stmt)
        level -= 1
        return ret


    @addToClass(AST.Repeate)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        level += 1
        ret += tmp + "REPEAT\n" + str(self.stmt) + tmp + "UNTIL\n" + str(self.cond)
        level -= 1
        return ret



    @addToClass(AST.Choice)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        level += 1
        if self.inst2 == None:
            ret += tmp + "IF\n" + str(self.cond) + "\n" +  str(self.inst1)
        else:
            ret += tmp + "IF\n" + str(self.cond) + "\n" + str(self.inst1) + tmp + "ELSE\n" + str(self.inst2)
        level -= 1
        return ret

    @addToClass(AST.Declarations)
    def printTree(self):
        ret = ""
        x = ""
        for d in self.decls:
             ret += x+str(d)
             x = "\n"
        return ret



    @addToClass(AST.Declaration)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        level += 1
        ret = tmp + "DECl\n" + str(self.val)
        level -= 1
        return ret

    @addToClass(AST.Inits)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        level += 1
        for i in self.inits:
             ret += tmp + "=\n" + str(i) + "\n"
        level -= 1
        return ret

    @addToClass(AST.Init)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        ret = tmp + str(self.id) + "\n" +str(self.val)
        return ret

    @addToClass(AST.Instructions)
    def printTree(self):
        ret = ""
        x = ""
        for i in self.instrs:
            ret += x + str(i) 
            x = "\n"
        return ret

    @addToClass(AST.ComInstructions)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        ret += str(self.decls) + str(self.instrs)
        return ret

    @addToClass(AST.Functions)
    def printTree(self):
        ret = ""
        x = ""
        for f in self.funcs:
             ret += x+str(f)
             x = "\n"
        return ret
     

    @addToClass(AST.Function)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        level += 1
        if self.args != None:
            ret += tmp+"FUNDEF\n| " + tmp +str(self.name) + "\n" + tmp + "| RET " + str(self.type) + "\n" + str(self.args) + str(self.instrs)
        else:
            ret += tmp+"FUNDEF\n| "+ tmp +str(self.name) + "\n" + tmp + "| RET " + str(self.type) + "\n" + tmp + "| VOID" +"\n" + str(self.instrs)
        level -= 1
        return ret

    @addToClass(AST.Print)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        level += 1
        ret += tmp + "PRINT\n" + str(self.expr)
        level -= 1
        return ret

    @addToClass(AST.Break)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        ret += tmp + "BREAK"
        return ret

    @addToClass(AST.Continue)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        ret += tmp + "CONTINUE"
        return ret

    @addToClass(AST.Return)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        level += 1
        ret += tmp + "RETURN\n" + str(self.ret) +"\n"
        level -= 1
        return ret

    @addToClass(AST.Arguments)
    def printTree(self):
        ret = ""
        for p in self.args:
            ret += str(p)+"\n"
        return ret

    @addToClass(AST.Argument)  
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        ret += tmp + "ARG " + str(self.id)
        return ret

    @addToClass(AST.CallArgument)  
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        ret += tmp + str(self.id)
        return ret

    @addToClass(AST.Call)
    def printTree(self):
        global level
        ret = ""
        tmp = getBr()
        level += 1
        if self.args != None:
            ret = tmp + "FUNCALL\n| " + tmp + str(self.name) + "\n" + str(self.args)
        else:
            ret = tmp + "FUNCALL\n| " + tmp + str(self.name) + "\n" + tmp +"| VOID\n"
        level -= 1
        return ret



    @addToClass(AST.Program)
    def printTree(self):
        return str(self.decls) + str(self.funcs) + str(self.insts)

