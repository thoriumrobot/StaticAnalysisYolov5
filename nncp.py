import ast
import tokenize
from scalpel.scalpel.cfg import CFGBuilder

# dictionary to save all linear ops by annotated str
linear_ops = {}

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
            if (node.lineno-1) in linear_ops.keys():
                print (linear_ops[node.lineno-1])
                #linear_ops[node.lineno-1] in node
                # TODO: get the ops from code and comp it with op in annotation
                #print(node.attr)



# get the annotaiton from string. 
# only print str that has 'nncp'
class ConstantVisitor(ast.NodeVisitor):
    def visit_Constant(self,node):
        #print('Node type: Constant\nFields: ', node._fields, node.value, node.kind)
        if ( isinstance(node.value, str) and 'nncp' in node.value): 
            # TODO: check this value is valid before adding to dict. check if the value is part of the linear op hard list
            linear_ops[node.lineno] = node.value.split('nncp')[1].replace(' ', '')
            
        ast.NodeVisitor.generic_visit(self, node)



tree = ast.parse(src, mode='exec')

print ("\n ---- AST TREE STARTED -----\n")
ConstantVisitor().visit(tree)
#print (type (tree) , tree, tree.lineno)
print (linear_ops)

GetAssignments().visit(tree)

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
