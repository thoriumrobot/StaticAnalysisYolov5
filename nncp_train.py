import ast
import tokenize
from scalpel.scalpel.cfg import CFGBuilder

with open('./yolov5/train.py', 'r', encoding='utf8') as f: 
    src = f.read()

## test scalpel
# build CFG
cfg = CFGBuilder().build_from_src(name='basic', src=src, flattened=False)
fun_cfg = cfg.functioncfgs.items()

#print(type(cfg))
#print (type(fun_cfg))

# get the blocks and print only blocks that has calls to np or torch
for block in cfg:
    calls = block.get_calls()
    if 'torch' in calls or 'np.' in calls:
        print(block.at())   # print the 1st line number of the block
        print("\t", calls)  

# get the name of functions that are defined in the src code
basic_cfg = None
for (block_id, fun_name), fun_cfg in cfg.functioncfgs.items():
    #print (fun_name)
    if fun_name == "train":
        basic_cfg = fun_cfg

#print (type(fun_cfg), type(basic_cfg))
#if basic_cfg is not None:
#    basic_cfg.build_visual('png')