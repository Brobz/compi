
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ATTR_KWD BIGGER CLASS_KWD CLOSE_CURLY CLOSE_PARENTHESIS COLON COMMA CTE_F CTE_I CTE_S DERIVES_KWD DIFFERENT DOUBLE_EQUALS ELSE_KWD EQUALS FROM_KWD FWD_SLASH ID IF_KWD MAIN_KWD MINUS OPEN_CURLY OPEN_PARENTHESIS OR PLUS PROGRAM_KWD READ_KWD RETURN_KWD SEMI_COLON SMALLER STAR THEN_KWD TYPE UNTIL_KWD VARS_KWD WHILE_KWD WRITE_KWD PROGRAM : PROGRAM_KWD ID SEMI_COLON CLASS_STAR GLOBAL_VAR FUNC_DEF_STAR MAIN_KWD OPEN_PARENTHESIS CLOSE_PARENTHESIS OPEN_CURLY STATEMENT_STAR CLOSE_CURLY  CLASS_STAR : CLASS CLASS_STAR\n                   | empty  CLASS : CLASS_KWD ID SMALLER DERIVES_KWD TYPE BIGGER OPEN_CURLY CLASS_ATTR FUNC_DEF_STAR CLOSE_CURLY  CLASS_ATTR : ATTR_KWD OPEN_CURLY VAR_LIST_STAR CLOSE_CURLY  VAR_LIST_STAR : VAR_LIST VAR_LIST_STAR\n                      | empty  VAR_LIST : ID_LIST COLON TYPE SEMI_COLON  ID_LIST : ID ID_LIST_P  ID_LIST_P : COMMA ID ID_LIST_P\n                  | empty  GLOBAL_VAR : VAR_LIST_STAR  FUNC_DEF_STAR : FUNC_DEF FUNC_DEF_STAR\n                      | empty  FUNC_DEF : TYPE ID OPEN_PARENTHESIS FUNC_PARAM CLOSE_PARENTHESIS VARS OPEN_CURLY STATEMENT_STAR CLOSE_CURLY  FUNC_PARAM : VAR FUNC_PARAM_P\n                   | empty  FUNC_PARAM_P : COMMA VAR FUNC_PARAM_P\n                     | empty  VAR : ID COLON TYPE  VARS : VARS_KWD OPEN_CURLY VAR_LIST_STAR CLOSE_CURLY  STATEMENT_STAR : STATEMENT STATEMENT_STAR\n                       | empty  STATEMENT : ASSIGN\n                  | FUNC_RETURN\n                  | READ\n                  | WRITE\n                  | DECISION\n                  | REPETITION  ASSIGN : ID EQUALS EXPRESSION SEMI_COLON  EXP : TERM EXP_P  EXP_P : PLUS TERM EXP_P\n            | MINUS TERM EXP_P\n            | empty  EXPRESSION : EXP\n                   | EXP COMP EXP  COMP : BIGGER\n             | SMALLER\n             | DOUBLE_EQUALS\n             | DIFFERENT\n             | AND\n             | OR  FACTOR : OPEN_PARENTHESIS EXPRESSION CLOSE_PARENTHESIS\n               | FUNC_CALL\n               | ID\n               | CNST  CNST : CTE_S\n             | CTE_F\n             | CTE_I  TERM : FACTOR\n             | FACTOR STAR FACTOR\n             | FACTOR FWD_SLASH FACTOR  FUNC_CALL : ID OPEN_PARENTHESIS ARG_LIST CLOSE_PARENTHESIS  ARG_LIST : ID_LIST ARG_LIST_P\n                 | EXPRESSION ARG_LIST_P  ARG_LIST_P : COMMA ID_LIST ARG_LIST_P\n                   | COMMA EXPRESSION ARG_LIST_P\n                   | empty  FUNC_RETURN : RETURN_KWD EXPRESSION SEMI_COLON  READ : READ_KWD OPEN_PARENTHESIS ID_LIST CLOSE_PARENTHESIS SEMI_COLON  WRITE : WRITE_KWD OPEN_PARENTHESIS PRINTABLE CLOSE_PARENTHESIS SEMI_COLON  PRINTABLE : CNST PRINTABLE_P\n                  | EXPRESSION PRINTABLE_P  PRINTABLE_P : COMMA CNST PRINTABLE_P\n                    | COMMA EXPRESSION PRINTABLE_P\n                    | empty  DECISION : IF_KWD OPEN_PARENTHESIS EXPRESSION CLOSE_PARENTHESIS THEN_KWD OPEN_CURLY STATEMENT_STAR CLOSE_CURLY DECISION_P  DECISION_P : ELSE_KWD OPEN_CURLY STATEMENT_STAR CLOSE_CURLY DECISION_P\n                   | empty  REPETITION : CONDITIONAL_REP\n                   | UNCONDITIONAL_REP  CONDITIONAL_REP : WHILE_KWD OPEN_PARENTHESIS EXPRESSION CLOSE_PARENTHESIS OPEN_CURLY STATEMENT_STAR CLOSE_CURLY  UNCONDITIONAL_REP : FROM_KWD ID EQUALS EXPRESSION UNTIL_KWD EXPRESSION OPEN_CURLY STATEMENT_STAR CLOSE_CURLY empty :'
    
_lr_action_items = {'PROGRAM_KWD':([0,],[2,]),'$end':([1,76,],[0,-1,]),'ID':([2,4,5,6,7,8,12,15,18,23,35,36,44,48,53,55,56,57,58,59,60,61,65,66,68,75,82,89,90,91,92,94,95,98,100,101,102,103,104,105,106,107,109,110,112,113,115,122,125,127,141,154,157,158,162,163,168,174,175,176,178,180,181,182,184,185,],[3,-74,9,-74,-3,16,9,-2,27,30,39,-8,51,39,51,-24,-25,-26,-27,-28,-29,84,-70,-71,93,84,84,9,84,84,84,51,9,9,-59,84,-37,-38,-39,-40,-41,-42,84,84,84,84,134,84,-4,-30,84,134,-60,-61,51,84,51,-72,51,-74,-67,-69,-73,51,-74,-68,]),'SEMI_COLON':([3,31,78,79,80,81,83,84,85,86,87,88,99,108,111,128,129,130,131,132,133,138,139,150,151,152,],[4,36,100,-35,-74,-50,-44,-45,-46,-47,-48,-49,127,-31,-34,-36,-74,-74,-51,-52,-43,157,158,-32,-33,-53,]),'CLASS_KWD':([4,6,125,],[8,8,-4,]),'TYPE':([4,5,6,7,10,11,12,13,15,21,24,25,32,36,45,73,125,147,149,],[-74,-74,-74,-3,23,-12,-74,-7,-2,23,-6,31,37,-8,69,23,-4,-15,-5,]),'MAIN_KWD':([4,5,6,7,10,11,12,13,15,20,21,22,24,29,36,125,147,],[-74,-74,-74,-3,-74,-12,-74,-7,-2,28,-74,-14,-6,-13,-8,-4,-15,]),'COMMA':([9,17,19,27,33,41,69,72,79,80,81,83,84,85,86,87,88,108,111,118,119,128,129,130,131,132,133,134,136,137,150,151,152,159,160,164,165,],[18,-9,-11,18,-10,48,-20,48,-35,-74,-50,-44,-45,-46,-47,-48,-49,-31,-34,141,141,-36,-74,-74,-51,-52,-43,18,154,154,-32,-33,-53,141,141,154,154,]),'COLON':([9,14,17,19,27,33,39,],[-74,25,-9,-11,-74,-10,45,]),'CLOSE_PARENTHESIS':([9,17,19,27,33,34,35,40,41,42,47,49,69,72,79,80,81,83,84,85,86,87,88,96,108,111,114,116,117,118,119,120,121,128,129,130,131,132,133,134,135,136,137,140,142,143,150,151,152,153,155,156,159,160,164,165,166,167,171,172,],[-74,-9,-11,-74,-10,38,-74,46,-74,-17,-16,-19,-20,-74,-35,-74,-50,-44,-45,-46,-47,-48,-49,-18,-31,-34,133,138,139,-46,-74,144,145,-36,-74,-74,-51,-52,-43,-45,152,-74,-74,-62,-66,-63,-32,-33,-53,-54,-58,-55,-46,-74,-74,-74,-64,-65,-56,-57,]),'CLOSE_CURLY':([12,13,21,22,24,29,36,44,52,53,54,55,56,57,58,59,60,65,66,73,77,94,95,97,98,100,123,124,126,127,147,149,157,158,162,168,169,173,174,175,176,177,178,180,181,182,183,184,185,],[-74,-7,-74,-14,-6,-13,-8,-74,76,-74,-23,-24,-25,-26,-27,-28,-29,-70,-71,-74,-22,-74,-74,125,-74,-59,147,148,149,-30,-15,-5,-60,-61,-74,-74,174,176,-72,-74,-74,181,-67,-69,-73,-74,184,-74,-68,]),'SMALLER':([16,79,80,81,83,84,85,86,87,88,108,111,118,129,130,131,132,133,134,150,151,152,159,],[26,103,-74,-50,-44,-45,-46,-47,-48,-49,-31,-34,-46,-74,-74,-51,-52,-43,-45,-32,-33,-53,-46,]),'DERIVES_KWD':([26,],[32,]),'OPEN_PARENTHESIS':([28,30,61,62,63,64,67,75,82,84,90,91,92,101,102,103,104,105,106,107,109,110,112,113,115,122,134,141,154,163,],[34,35,82,89,90,91,92,82,82,115,82,82,82,82,-37,-38,-39,-40,-41,-42,82,82,82,82,82,82,115,82,82,82,]),'BIGGER':([37,79,80,81,83,84,85,86,87,88,108,111,118,129,130,131,132,133,134,150,151,152,159,],[43,102,-74,-50,-44,-45,-46,-47,-48,-49,-31,-34,-46,-74,-74,-51,-52,-43,-45,-32,-33,-53,-46,]),'OPEN_CURLY':([38,43,70,71,74,79,80,81,83,84,85,86,87,88,108,111,128,129,130,131,132,133,145,148,150,151,152,161,170,179,],[44,50,94,95,98,-35,-74,-50,-44,-45,-46,-47,-48,-49,-31,-34,-36,-74,-74,-51,-52,-43,162,-21,-32,-33,-53,168,175,182,]),'RETURN_KWD':([44,53,55,56,57,58,59,60,65,66,94,100,127,157,158,162,168,174,175,176,178,180,181,182,184,185,],[61,61,-24,-25,-26,-27,-28,-29,-70,-71,61,-59,-30,-60,-61,61,61,-72,61,-74,-67,-69,-73,61,-74,-68,]),'READ_KWD':([44,53,55,56,57,58,59,60,65,66,94,100,127,157,158,162,168,174,175,176,178,180,181,182,184,185,],[62,62,-24,-25,-26,-27,-28,-29,-70,-71,62,-59,-30,-60,-61,62,62,-72,62,-74,-67,-69,-73,62,-74,-68,]),'WRITE_KWD':([44,53,55,56,57,58,59,60,65,66,94,100,127,157,158,162,168,174,175,176,178,180,181,182,184,185,],[63,63,-24,-25,-26,-27,-28,-29,-70,-71,63,-59,-30,-60,-61,63,63,-72,63,-74,-67,-69,-73,63,-74,-68,]),'IF_KWD':([44,53,55,56,57,58,59,60,65,66,94,100,127,157,158,162,168,174,175,176,178,180,181,182,184,185,],[64,64,-24,-25,-26,-27,-28,-29,-70,-71,64,-59,-30,-60,-61,64,64,-72,64,-74,-67,-69,-73,64,-74,-68,]),'WHILE_KWD':([44,53,55,56,57,58,59,60,65,66,94,100,127,157,158,162,168,174,175,176,178,180,181,182,184,185,],[67,67,-24,-25,-26,-27,-28,-29,-70,-71,67,-59,-30,-60,-61,67,67,-72,67,-74,-67,-69,-73,67,-74,-68,]),'FROM_KWD':([44,53,55,56,57,58,59,60,65,66,94,100,127,157,158,162,168,174,175,176,178,180,181,182,184,185,],[68,68,-24,-25,-26,-27,-28,-29,-70,-71,68,-59,-30,-60,-61,68,68,-72,68,-74,-67,-69,-73,68,-74,-68,]),'VARS_KWD':([46,],[71,]),'ATTR_KWD':([50,],[74,]),'EQUALS':([51,93,],[75,122,]),'CTE_S':([61,75,82,90,91,92,101,102,103,104,105,106,107,109,110,112,113,115,122,141,154,163,],[86,86,86,86,86,86,86,-37,-38,-39,-40,-41,-42,86,86,86,86,86,86,86,86,86,]),'CTE_F':([61,75,82,90,91,92,101,102,103,104,105,106,107,109,110,112,113,115,122,141,154,163,],[87,87,87,87,87,87,87,-37,-38,-39,-40,-41,-42,87,87,87,87,87,87,87,87,87,]),'CTE_I':([61,75,82,90,91,92,101,102,103,104,105,106,107,109,110,112,113,115,122,141,154,163,],[88,88,88,88,88,88,88,-37,-38,-39,-40,-41,-42,88,88,88,88,88,88,88,88,88,]),'UNTIL_KWD':([79,80,81,83,84,85,86,87,88,108,111,128,129,130,131,132,133,146,150,151,152,],[-35,-74,-50,-44,-45,-46,-47,-48,-49,-31,-34,-36,-74,-74,-51,-52,-43,163,-32,-33,-53,]),'DOUBLE_EQUALS':([79,80,81,83,84,85,86,87,88,108,111,118,129,130,131,132,133,134,150,151,152,159,],[104,-74,-50,-44,-45,-46,-47,-48,-49,-31,-34,-46,-74,-74,-51,-52,-43,-45,-32,-33,-53,-46,]),'DIFFERENT':([79,80,81,83,84,85,86,87,88,108,111,118,129,130,131,132,133,134,150,151,152,159,],[105,-74,-50,-44,-45,-46,-47,-48,-49,-31,-34,-46,-74,-74,-51,-52,-43,-45,-32,-33,-53,-46,]),'AND':([79,80,81,83,84,85,86,87,88,108,111,118,129,130,131,132,133,134,150,151,152,159,],[106,-74,-50,-44,-45,-46,-47,-48,-49,-31,-34,-46,-74,-74,-51,-52,-43,-45,-32,-33,-53,-46,]),'OR':([79,80,81,83,84,85,86,87,88,108,111,118,129,130,131,132,133,134,150,151,152,159,],[107,-74,-50,-44,-45,-46,-47,-48,-49,-31,-34,-46,-74,-74,-51,-52,-43,-45,-32,-33,-53,-46,]),'PLUS':([80,81,83,84,85,86,87,88,118,129,130,131,132,133,134,152,159,],[109,-50,-44,-45,-46,-47,-48,-49,-46,109,109,-51,-52,-43,-45,-53,-46,]),'MINUS':([80,81,83,84,85,86,87,88,118,129,130,131,132,133,134,152,159,],[110,-50,-44,-45,-46,-47,-48,-49,-46,110,110,-51,-52,-43,-45,-53,-46,]),'STAR':([81,83,84,85,86,87,88,118,133,134,152,159,],[112,-44,-45,-46,-47,-48,-49,-46,-43,-45,-53,-46,]),'FWD_SLASH':([81,83,84,85,86,87,88,118,133,134,152,159,],[113,-44,-45,-46,-47,-48,-49,-46,-43,-45,-53,-46,]),'THEN_KWD':([144,],[161,]),'ELSE_KWD':([176,184,],[179,179,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'CLASS_STAR':([4,6,],[5,15,]),'CLASS':([4,6,],[6,6,]),'empty':([4,5,6,9,10,12,21,27,35,41,44,53,72,73,80,94,95,98,118,119,129,130,134,136,137,159,160,162,164,165,168,175,176,182,184,],[7,13,7,19,22,13,22,19,42,49,54,54,49,22,111,54,13,13,142,142,111,111,19,155,155,142,142,54,155,155,54,54,180,54,180,]),'GLOBAL_VAR':([5,],[10,]),'VAR_LIST_STAR':([5,12,95,98,],[11,24,124,126,]),'VAR_LIST':([5,12,95,98,],[12,12,12,12,]),'ID_LIST':([5,12,89,95,98,115,154,],[14,14,116,14,14,136,164,]),'ID_LIST_P':([9,27,134,],[17,33,17,]),'FUNC_DEF_STAR':([10,21,73,],[20,29,97,]),'FUNC_DEF':([10,21,73,],[21,21,21,]),'FUNC_PARAM':([35,],[40,]),'VAR':([35,48,],[41,72,]),'FUNC_PARAM_P':([41,72,],[47,96,]),'STATEMENT_STAR':([44,53,94,162,168,175,182,],[52,77,123,169,173,177,183,]),'STATEMENT':([44,53,94,162,168,175,182,],[53,53,53,53,53,53,53,]),'ASSIGN':([44,53,94,162,168,175,182,],[55,55,55,55,55,55,55,]),'FUNC_RETURN':([44,53,94,162,168,175,182,],[56,56,56,56,56,56,56,]),'READ':([44,53,94,162,168,175,182,],[57,57,57,57,57,57,57,]),'WRITE':([44,53,94,162,168,175,182,],[58,58,58,58,58,58,58,]),'DECISION':([44,53,94,162,168,175,182,],[59,59,59,59,59,59,59,]),'REPETITION':([44,53,94,162,168,175,182,],[60,60,60,60,60,60,60,]),'CONDITIONAL_REP':([44,53,94,162,168,175,182,],[65,65,65,65,65,65,65,]),'UNCONDITIONAL_REP':([44,53,94,162,168,175,182,],[66,66,66,66,66,66,66,]),'VARS':([46,],[70,]),'CLASS_ATTR':([50,],[73,]),'EXPRESSION':([61,75,82,90,91,92,115,122,141,154,163,],[78,99,114,119,120,121,137,146,160,165,170,]),'EXP':([61,75,82,90,91,92,101,115,122,141,154,163,],[79,79,79,79,79,79,128,79,79,79,79,79,]),'TERM':([61,75,82,90,91,92,101,109,110,115,122,141,154,163,],[80,80,80,80,80,80,80,129,130,80,80,80,80,80,]),'FACTOR':([61,75,82,90,91,92,101,109,110,112,113,115,122,141,154,163,],[81,81,81,81,81,81,81,81,81,131,132,81,81,81,81,81,]),'FUNC_CALL':([61,75,82,90,91,92,101,109,110,112,113,115,122,141,154,163,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'CNST':([61,75,82,90,91,92,101,109,110,112,113,115,122,141,154,163,],[85,85,85,118,85,85,85,85,85,85,85,85,85,159,85,85,]),'COMP':([79,],[101,]),'EXP_P':([80,129,130,],[108,150,151,]),'PRINTABLE':([90,],[117,]),'ARG_LIST':([115,],[135,]),'PRINTABLE_P':([118,119,159,160,],[140,143,166,167,]),'ARG_LIST_P':([136,137,164,165,],[153,156,171,172,]),'DECISION_P':([176,184,],[178,185,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> PROGRAM_KWD ID SEMI_COLON CLASS_STAR GLOBAL_VAR FUNC_DEF_STAR MAIN_KWD OPEN_PARENTHESIS CLOSE_PARENTHESIS OPEN_CURLY STATEMENT_STAR CLOSE_CURLY','PROGRAM',12,'p_program','main.py',160),
  ('CLASS_STAR -> CLASS CLASS_STAR','CLASS_STAR',2,'p_class_star','main.py',165),
  ('CLASS_STAR -> empty','CLASS_STAR',1,'p_class_star','main.py',166),
  ('CLASS -> CLASS_KWD ID SMALLER DERIVES_KWD TYPE BIGGER OPEN_CURLY CLASS_ATTR FUNC_DEF_STAR CLOSE_CURLY','CLASS',10,'p_class','main.py',169),
  ('CLASS_ATTR -> ATTR_KWD OPEN_CURLY VAR_LIST_STAR CLOSE_CURLY','CLASS_ATTR',4,'p_class_attr','main.py',172),
  ('VAR_LIST_STAR -> VAR_LIST VAR_LIST_STAR','VAR_LIST_STAR',2,'p_var_list_star','main.py',175),
  ('VAR_LIST_STAR -> empty','VAR_LIST_STAR',1,'p_var_list_star','main.py',176),
  ('VAR_LIST -> ID_LIST COLON TYPE SEMI_COLON','VAR_LIST',4,'p_var_list','main.py',178),
  ('ID_LIST -> ID ID_LIST_P','ID_LIST',2,'p_id_list','main.py',183),
  ('ID_LIST_P -> COMMA ID ID_LIST_P','ID_LIST_P',3,'p_id_list_p','main.py',189),
  ('ID_LIST_P -> empty','ID_LIST_P',1,'p_id_list_p','main.py',190),
  ('GLOBAL_VAR -> VAR_LIST_STAR','GLOBAL_VAR',1,'p_global_var','main.py',197),
  ('FUNC_DEF_STAR -> FUNC_DEF FUNC_DEF_STAR','FUNC_DEF_STAR',2,'p_func_def_star','main.py',200),
  ('FUNC_DEF_STAR -> empty','FUNC_DEF_STAR',1,'p_func_def_star','main.py',201),
  ('FUNC_DEF -> TYPE ID OPEN_PARENTHESIS FUNC_PARAM CLOSE_PARENTHESIS VARS OPEN_CURLY STATEMENT_STAR CLOSE_CURLY','FUNC_DEF',9,'p_func_def','main.py',204),
  ('FUNC_PARAM -> VAR FUNC_PARAM_P','FUNC_PARAM',2,'p_func_param','main.py',208),
  ('FUNC_PARAM -> empty','FUNC_PARAM',1,'p_func_param','main.py',209),
  ('FUNC_PARAM_P -> COMMA VAR FUNC_PARAM_P','FUNC_PARAM_P',3,'p_func_param_p','main.py',212),
  ('FUNC_PARAM_P -> empty','FUNC_PARAM_P',1,'p_func_param_p','main.py',213),
  ('VAR -> ID COLON TYPE','VAR',3,'p_var','main.py',216),
  ('VARS -> VARS_KWD OPEN_CURLY VAR_LIST_STAR CLOSE_CURLY','VARS',4,'p_vars','main.py',219),
  ('STATEMENT_STAR -> STATEMENT STATEMENT_STAR','STATEMENT_STAR',2,'p_statement_star','main.py',222),
  ('STATEMENT_STAR -> empty','STATEMENT_STAR',1,'p_statement_star','main.py',223),
  ('STATEMENT -> ASSIGN','STATEMENT',1,'p_statement','main.py',226),
  ('STATEMENT -> FUNC_RETURN','STATEMENT',1,'p_statement','main.py',227),
  ('STATEMENT -> READ','STATEMENT',1,'p_statement','main.py',228),
  ('STATEMENT -> WRITE','STATEMENT',1,'p_statement','main.py',229),
  ('STATEMENT -> DECISION','STATEMENT',1,'p_statement','main.py',230),
  ('STATEMENT -> REPETITION','STATEMENT',1,'p_statement','main.py',231),
  ('ASSIGN -> ID EQUALS EXPRESSION SEMI_COLON','ASSIGN',4,'p_assign','main.py',234),
  ('EXP -> TERM EXP_P','EXP',2,'p_exp','main.py',238),
  ('EXP_P -> PLUS TERM EXP_P','EXP_P',3,'p_exp_p','main.py',245),
  ('EXP_P -> MINUS TERM EXP_P','EXP_P',3,'p_exp_p','main.py',246),
  ('EXP_P -> empty','EXP_P',1,'p_exp_p','main.py',247),
  ('EXPRESSION -> EXP','EXPRESSION',1,'p_expression','main.py',259),
  ('EXPRESSION -> EXP COMP EXP','EXPRESSION',3,'p_expression','main.py',260),
  ('COMP -> BIGGER','COMP',1,'p_comp','main.py',265),
  ('COMP -> SMALLER','COMP',1,'p_comp','main.py',266),
  ('COMP -> DOUBLE_EQUALS','COMP',1,'p_comp','main.py',267),
  ('COMP -> DIFFERENT','COMP',1,'p_comp','main.py',268),
  ('COMP -> AND','COMP',1,'p_comp','main.py',269),
  ('COMP -> OR','COMP',1,'p_comp','main.py',270),
  ('FACTOR -> OPEN_PARENTHESIS EXPRESSION CLOSE_PARENTHESIS','FACTOR',3,'p_factor','main.py',275),
  ('FACTOR -> FUNC_CALL','FACTOR',1,'p_factor','main.py',276),
  ('FACTOR -> ID','FACTOR',1,'p_factor','main.py',277),
  ('FACTOR -> CNST','FACTOR',1,'p_factor','main.py',278),
  ('CNST -> CTE_S','CNST',1,'p_cnst','main.py',286),
  ('CNST -> CTE_F','CNST',1,'p_cnst','main.py',287),
  ('CNST -> CTE_I','CNST',1,'p_cnst','main.py',288),
  ('TERM -> FACTOR','TERM',1,'p_term','main.py',293),
  ('TERM -> FACTOR STAR FACTOR','TERM',3,'p_term','main.py',294),
  ('TERM -> FACTOR FWD_SLASH FACTOR','TERM',3,'p_term','main.py',295),
  ('FUNC_CALL -> ID OPEN_PARENTHESIS ARG_LIST CLOSE_PARENTHESIS','FUNC_CALL',4,'p_func_call','main.py',306),
  ('ARG_LIST -> ID_LIST ARG_LIST_P','ARG_LIST',2,'p_arg_list','main.py',309),
  ('ARG_LIST -> EXPRESSION ARG_LIST_P','ARG_LIST',2,'p_arg_list','main.py',310),
  ('ARG_LIST_P -> COMMA ID_LIST ARG_LIST_P','ARG_LIST_P',3,'p_arg_list_p','main.py',313),
  ('ARG_LIST_P -> COMMA EXPRESSION ARG_LIST_P','ARG_LIST_P',3,'p_arg_list_p','main.py',314),
  ('ARG_LIST_P -> empty','ARG_LIST_P',1,'p_arg_list_p','main.py',315),
  ('FUNC_RETURN -> RETURN_KWD EXPRESSION SEMI_COLON','FUNC_RETURN',3,'p_func_return','main.py',318),
  ('READ -> READ_KWD OPEN_PARENTHESIS ID_LIST CLOSE_PARENTHESIS SEMI_COLON','READ',5,'p_read','main.py',321),
  ('WRITE -> WRITE_KWD OPEN_PARENTHESIS PRINTABLE CLOSE_PARENTHESIS SEMI_COLON','WRITE',5,'p_write','main.py',324),
  ('PRINTABLE -> CNST PRINTABLE_P','PRINTABLE',2,'p_printable','main.py',328),
  ('PRINTABLE -> EXPRESSION PRINTABLE_P','PRINTABLE',2,'p_printable','main.py',329),
  ('PRINTABLE_P -> COMMA CNST PRINTABLE_P','PRINTABLE_P',3,'p_printable_p','main.py',333),
  ('PRINTABLE_P -> COMMA EXPRESSION PRINTABLE_P','PRINTABLE_P',3,'p_printable_p','main.py',334),
  ('PRINTABLE_P -> empty','PRINTABLE_P',1,'p_printable_p','main.py',335),
  ('DECISION -> IF_KWD OPEN_PARENTHESIS EXPRESSION CLOSE_PARENTHESIS THEN_KWD OPEN_CURLY STATEMENT_STAR CLOSE_CURLY DECISION_P','DECISION',9,'p_decision','main.py',339),
  ('DECISION_P -> ELSE_KWD OPEN_CURLY STATEMENT_STAR CLOSE_CURLY DECISION_P','DECISION_P',5,'p_decision_p','main.py',342),
  ('DECISION_P -> empty','DECISION_P',1,'p_decision_p','main.py',343),
  ('REPETITION -> CONDITIONAL_REP','REPETITION',1,'p_repetition','main.py',346),
  ('REPETITION -> UNCONDITIONAL_REP','REPETITION',1,'p_repetition','main.py',347),
  ('CONDITIONAL_REP -> WHILE_KWD OPEN_PARENTHESIS EXPRESSION CLOSE_PARENTHESIS OPEN_CURLY STATEMENT_STAR CLOSE_CURLY','CONDITIONAL_REP',7,'p_conditional_rep','main.py',350),
  ('UNCONDITIONAL_REP -> FROM_KWD ID EQUALS EXPRESSION UNTIL_KWD EXPRESSION OPEN_CURLY STATEMENT_STAR CLOSE_CURLY','UNCONDITIONAL_REP',9,'p_unconditional_rep','main.py',353),
  ('empty -> <empty>','empty',0,'p_empty','main.py',356),
]
