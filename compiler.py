# coding=utf-8
import AST
from AST import addToClass

# opcodes de la SVM
#    PUSHC <val>     pushes the constant <val> on the stack
#    PUSHV <id>      pushes the value of identifier <id> on the stack
#    SET <id>        pops a value from the top of stack and sets <id>
#    PRINT           pops a value from the top of stack and print it
#    ADD,SUB,DIV,MUL pops 2 values from the top of stack and compute them
#    USUB            changes the sign of the number on the top of stack
#    JMP <tag>       jump to :<tag>
#    JIZ,JINZ <tag>  pops a value from the top of stack and jump to :<tag> if (not) zero

# chaque opération correspond à son instruction d'exécution de la machine SVM
operations = {
	'+' : 'ADD',
	'-' : 'SUB',
	'*' : 'MUL',
	'/' : 'DIV',
	'<' : 'NEGCOMP',
	'>' : 'POSCOMP'
}

def whilecounter():
	whilecounter.current += 1
	return whilecounter.current
whilecounter.current = 0

# noeud de programme
# retourne la suite d'opcodes de tous les enfants
@addToClass(AST.ProgramNode)
def compile(self):
	bytecode = ""
	for c in self.children:
		bytecode += c.compile()
	return bytecode

# noeud terminal
# si c'est une variable : empile la valeur de la variable
# si c'est une constante : empile la constante
@addToClass(AST.TokenNode)
def compile(self):
	bytecode = ""
	bytecode += "%s" % self.tok
	return bytecode

# noeud d'assignation de variable
# exécute le noeud à droite du signe =
# dépile un élément et le met dans ID
@addToClass(AST.AssignNode)
def compile(self):
	bytecode = ""
	if isinstance(self.children[1].tok,float):
		bytecode +="float"
	else:
		bytecode += "int"

	print(self.children[1].tok)
	bytecode += " %s" % self.children[0].tok+" = "
	bytecode += self.children[1].compile()
	bytecode +=";\n"
	return bytecode
	
# noeud d'affichage
# exécute le noeud qui suit le PRINT
# dépile un élément et l'affiche
@addToClass(AST.PrintNode)
def compile(self):
	bytecode = ""
	bytecode += "cout << "
	bytecode += self.children[0].compile()+";\n"

	return bytecode

# noeud d'opération arithmétique
# si c'est une opération unaire (nombre négatif), empile le nombre et l'inverse
# si c'est une opération binaire, empile les enfants puis l'opération
@addToClass(AST.OpNode)
def compile(self):
	bytecode = ""	
	bytecode += self.children[0].tok
	print(operations[self.op])
	for key,value in operations.items():
		if value == operations[self.op]:
			bytecode += key
	bytecode += self.children[1].tok



	return bytecode
	
# noeud de boucle while
# saute au label de la condition défini plus bas
# insère le label puis le corps du body
# insère le label puis le corps de la condition
# réalise un saut conditionnel sur le résultat de la condition (empilé)
@addToClass(AST.WhileNode)
def compile(self):
	counter = whilecounter()
	bytecode = ""
	bytecode += "while(%s) {" % self.children[0].tok
	bytecode +="\n"
	bytecode += "\t"+self.children[1].compile()
	bytecode+="}"
	return bytecode

# noeud de boucle while
# saute au label de la condition défini plus bas
# insère le label puis le corps du body
# insère le label puis le corps de la condition
# réalise un saut conditionnel sur le résultat de la condition (empilé)
@addToClass(AST.IfNode)
def compile(self):
	counter = whilecounter()
	bytecode = ""
	bytecode += "if(%s) {" % self.children[0].compile()
	bytecode +="\n"
	bytecode += "\t"+self.children[1].compile()
	bytecode+="}"
	return bytecode

if __name__ == "__main__":
    from parser4 import parse
    import sys, os
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    print(ast)
    compiled = ast.compile()
    name = os.path.splitext(sys.argv[1])[0]+'.vm'    
    outfile = open(name, 'w')
    outfile.write(compiled)
    outfile.close()
    print ("Wrote output to", name)