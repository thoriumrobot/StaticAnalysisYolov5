import ast
import tokenize
from scalpel.scalpel.cfg import CFGBuilder


# read file && test tokenize
with open('example_basic.py', 'r', encoding='utf8') as f: 
    src = f.read()
    token_src = tokenize.generate_tokens(f.readline)
    for token in token_src:
        print(token)

#print (type(src), src)
#print (type(token_src))

## test ast 
class GetAssignments(ast.NodeVisitor):
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            print (node.id, node.lineno)

tree = ast.parse(src, mode='exec')

print ("\n ---- AST TREE STARTED -----\n")
GetAssignments().visit(tree)
#print (type (tree) , tree, tree.lineno)

print ("\n ---- AST TREE END-----\n")

#print (ast.dump(tree))
'''
Module(
    body=[
        Expr(value=Constant(value='\nThis file services as an example of liner operation\n\n', kind=None)), 
        Import(names=[alias(name='numpy', asname='np')]), 
        Assign(targets=[Name(id='a', ctx=Store())], value=Constant(value=3, kind=None), type_comment=None), 
        Assign(targets=[Name(id='b', ctx=Store())], value=Constant(value=4, kind=None), type_comment=None), 
        Assign(targets=[Name(id='output', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='dot', ctx=Load()), args=[Name(id='a', ctx=Load()), Name(id='b', ctx=Load())], keywords=[]), type_comment=None), 
        Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Name(id='output', ctx=Load())], keywords=[]))
        ], 
    type_ignores=[]
    )
'''

## test scalpel
cfg = CFGBuilder().build_from_src(name='basic', src=src, flattened=False)
fun_cfg = cfg.functioncfgs.items()

print(type(cfg))
print (type(fun_cfg))

basic_cfg = None
for block in cfg:
    calls = block.get_calls()
    block_src = block.get_source()
    print (type(block), type(calls))
    print (calls)
    print (block_src)
    print (type(block_src))
