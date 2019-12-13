
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "EQU FLOAT FOR IDENTIFIER IF IN INT PRINT RANGE programme : statement  programme : statement ';' programme  statement : assignation\n\t\t\t\t\t\t| expression expression : INT\n\t\t| FLOAT expression : '(' expression ')'  assignation : IDENTIFIER EQU expression "
    
_lr_action_items = {'IDENTIFIER':([0,9,],[5,5,]),'INT':([0,8,9,10,],[6,6,6,6,]),'FLOAT':([0,8,9,10,],[7,7,7,7,]),'(':([0,8,9,10,],[8,8,8,8,]),'$end':([1,2,3,4,6,7,12,13,14,],[0,-1,-3,-4,-5,-6,-2,-8,-7,]),';':([2,3,4,6,7,13,14,],[9,-3,-4,-5,-6,-8,-7,]),'EQU':([5,],[10,]),')':([6,7,11,14,],[-5,-6,14,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programme':([0,9,],[1,12,]),'statement':([0,9,],[2,2,]),'assignation':([0,9,],[3,3,]),'expression':([0,8,9,10,],[4,11,4,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement','programme',1,'p_programme_statement','parser4.py',11),
  ('programme -> statement ; programme','programme',3,'p_programme_recursive','parser4.py',15),
  ('statement -> assignation','statement',1,'p_statement','parser4.py',19),
  ('statement -> expression','statement',1,'p_statement','parser4.py',20),
  ('expression -> INT','expression',1,'p_expression_num_or_var','parser4.py',24),
  ('expression -> FLOAT','expression',1,'p_expression_num_or_var','parser4.py',25),
  ('expression -> ( expression )','expression',3,'p_expression_paren','parser4.py',29),
  ('assignation -> IDENTIFIER EQU expression','assignation',3,'p_assign','parser4.py',33),
]