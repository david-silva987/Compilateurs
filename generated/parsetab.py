
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "COMPARATOR DEF ELSE ENTER EQU FLOAT FOR IDENTIFIER IF ILLEGAL IN INT POINTS PRINT RANGE TAB WHILE programme : statement   programme : statement ENTER programme  statement : assignation\n\t\t\t\t\t\t| structure expression : INT\n\t\t| FLOAT \n\t\t| IDENTIFIER \n\t\t  statement : PRINT expression  expression : expression COMPARATOR expressionstructure : IF expression POINTS ENTER TAB programme '#' structure : DEF expression '(' ')' POINTS TAB programme '#'  structure : WHILE expression POINTS ENTER TAB programme '#' expression : '(' expression ')' expression : TAB expression assignation : IDENTIFIER EQU expression "
    
_lr_action_items = {'PRINT':([0,10,34,36,38,],[5,5,5,5,5,]),'IDENTIFIER':([0,5,7,8,9,10,15,16,17,22,34,36,38,],[6,14,14,14,14,6,14,14,14,14,6,6,6,]),'IF':([0,10,34,36,38,],[7,7,7,7,7,]),'DEF':([0,10,34,36,38,],[8,8,8,8,8,]),'WHILE':([0,10,34,36,38,],[9,9,9,9,9,]),'$end':([1,2,3,4,11,12,13,14,21,24,25,29,30,40,42,43,],[0,-1,-3,-4,-8,-5,-6,-7,-2,-14,-15,-9,-13,-10,-12,-11,]),'#':([2,3,4,11,12,13,14,21,24,25,29,30,37,39,40,41,42,43,],[-1,-3,-4,-8,-5,-6,-7,-2,-14,-15,-9,-13,40,42,-10,43,-12,-11,]),'ENTER':([2,3,4,11,12,13,14,24,25,26,28,29,30,40,42,43,],[10,-3,-4,-8,-5,-6,-7,-14,-15,31,33,-9,-13,-10,-12,-11,]),'INT':([5,7,8,9,15,16,17,22,],[12,12,12,12,12,12,12,12,]),'FLOAT':([5,7,8,9,15,16,17,22,],[13,13,13,13,13,13,13,13,]),'(':([5,7,8,9,12,13,14,15,16,17,19,22,24,29,30,],[15,15,15,15,-5,-6,-7,15,15,15,27,15,-14,-9,-13,]),'TAB':([5,7,8,9,15,16,17,22,31,33,35,],[16,16,16,16,16,16,16,16,34,36,38,]),'EQU':([6,],[17,]),'COMPARATOR':([11,12,13,14,18,19,20,23,24,25,29,30,],[22,-5,-6,-7,22,22,22,22,22,22,22,-13,]),'POINTS':([12,13,14,18,20,24,29,30,32,],[-5,-6,-7,26,28,-14,-9,-13,35,]),')':([12,13,14,23,24,27,29,30,],[-5,-6,-7,30,-14,32,-9,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programme':([0,10,34,36,38,],[1,21,37,39,41,]),'statement':([0,10,34,36,38,],[2,2,2,2,2,]),'assignation':([0,10,34,36,38,],[3,3,3,3,3,]),'structure':([0,10,34,36,38,],[4,4,4,4,4,]),'expression':([5,7,8,9,15,16,17,22,],[11,18,19,20,23,24,25,29,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement','programme',1,'p_programme_statement','parser4.py',11),
  ('programme -> statement ENTER programme','programme',3,'p_programme_recursive','parser4.py',15),
  ('statement -> assignation','statement',1,'p_statement','parser4.py',19),
  ('statement -> structure','statement',1,'p_statement','parser4.py',20),
  ('expression -> INT','expression',1,'p_expression_num_or_var','parser4.py',24),
  ('expression -> FLOAT','expression',1,'p_expression_num_or_var','parser4.py',25),
  ('expression -> IDENTIFIER','expression',1,'p_expression_num_or_var','parser4.py',26),
  ('statement -> PRINT expression','statement',2,'p_statement_print','parser4.py',31),
  ('expression -> expression COMPARATOR expression','expression',3,'p_expression_comp','parser4.py',35),
  ('structure -> IF expression POINTS ENTER TAB programme #','structure',7,'p_structure_if','parser4.py',39),
  ('structure -> DEF expression ( ) POINTS TAB programme #','structure',8,'p_structure_function','parser4.py',43),
  ('structure -> WHILE expression POINTS ENTER TAB programme #','structure',7,'p_structure_while','parser4.py',47),
  ('expression -> ( expression )','expression',3,'p_expression_paren','parser4.py',51),
  ('expression -> TAB expression','expression',2,'p_expression_tab','parser4.py',56),
  ('assignation -> IDENTIFIER EQU expression','assignation',3,'p_assign','parser4.py',60),
]
