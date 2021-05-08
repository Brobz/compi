
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ATTR_KWD BIGGER CLASS_KWD CLOSE_CURLY CLOSE_PARENTHESIS COLON COMMA CTE_F CTE_I CTE_S DERIVES_KWD DIFFERENT DOUBLE_EQUALS ELSE_KWD EQUALS FOR_KWD FWD_SLASH ID IF_KWD MAIN_KWD MINUS NOT OPEN_CURLY OPEN_PARENTHESIS OR PLUS PROGRAM_KWD READ_KWD RETURN_KWD SEMI_COLON SMALLER STAR TYPE VARS_KWD WHILE_KWD WRITE_KWD PROGRAM : PROGRAM_KWD ID seen_program_id SEMI_COLON CLASS_STAR GLOBAL_VAR FUNC_DEF_STAR MAIN_KWD OPEN_PARENTHESIS CLOSE_PARENTHESIS OPEN_CURLY seen_main_kwd STATEMENT_STAR CLOSE_CURLY  seen_program_id : empty  seen_main_kwd : empty  CLASS_STAR : CLASS CLASS_STAR\n                   | empty  CLASS : CLASS_KWD ID SMALLER DERIVES_KWD TYPE BIGGER OPEN_CURLY CLASS_ATTR FUNC_DEF_STAR CLOSE_CURLY  CLASS_ATTR : ATTR_KWD OPEN_CURLY VAR_LIST_STAR CLOSE_CURLY  VAR_LIST_STAR : VAR_LIST VAR_LIST_STAR\n                      | empty  VAR_LIST : ID_LIST COLON TYPE SEMI_COLON  ID_LIST : ID ID_LIST_P  ID_LIST_P : COMMA ID ID_LIST_P\n                  | empty  READABLE_LIST : ID seen_readable READABLE_LIST_P  READABLE_LIST_P : COMMA ID seen_readable READABLE_LIST_P\n                  | empty  seen_readable  : empty  GLOBAL_VAR : VAR_LIST_STAR  FUNC_DEF_STAR : FUNC_DEF FUNC_DEF_STAR\n                      | empty  FUNC_DEF : TYPE ID seen_func_id OPEN_PARENTHESIS FUNC_PARAM CLOSE_PARENTHESIS seen_func_params VARS seen_func_vars OPEN_CURLY FUNC_STATEMENT_STAR CLOSE_CURLY  seen_func_id : empty  seen_func_params : empty  seen_func_vars : empty  FUNC_PARAM : VAR FUNC_PARAM_P\n                   | empty  FUNC_PARAM_P : COMMA VAR FUNC_PARAM_P\n                     | empty  VAR : ID COLON TYPE  VARS : VARS_KWD OPEN_CURLY VAR_LIST_STAR CLOSE_CURLY  FUNC_STATEMENT_STAR :       STATEMENT FUNC_STATEMENT_STAR\n                                |   FUNC_RETURN FUNC_STATEMENT_STAR\n                                |   empty  STATEMENT_STAR :  STATEMENT STATEMENT_STAR\n                       | empty  STATEMENT : ASSIGN SEMI_COLON\n                  | FUNC_CALL SEMI_COLON\n                  | READ SEMI_COLON\n                  | WRITE SEMI_COLON\n                  | DECISION\n                  | REPETITION  FOR_INCR_STATEMENT :    ASSIGN\n                              | FUNC_CALL\n                              | READ\n                              | WRITE  ASSIGN : ID seen_id EQUALS seen_equals EXPRESSION  seen_equals  : empty  EXP :   TERM seen_term EXP_P\n              | NOT seen_not EXP pop_not seen_term :   EXP_P : PLUS seen_term_op TERM seen_term EXP_P\n            | MINUS seen_term_op TERM seen_term EXP_P\n            | empty  seen_term_op :   EXPRESSION :   EXP\n                     | EXP COMP seen_comp_op EXPRESSION seen_comp  seen_comp : empty  seen_comp_op : empty  COMP : BIGGER\n             | SMALLER\n             | DOUBLE_EQUALS\n             | DIFFERENT\n             | AND\n             | OR  FACTOR :  OPEN_PARENTHESIS seen_open_parenthesis EXPRESSION CLOSE_PARENTHESIS seen_close_parenthesis\n                | NOT seen_not FACTOR pop_not\n                | FUNC_CALL\n                | ID seen_id\n                | CNST  pop_not : empty  seen_not : empty  seen_open_parenthesis : empty  seen_close_parenthesis : empty  seen_id :   seen_cte_i :   seen_cte_f :   seen_cte_s :   CNST : CTE_S seen_cte_s\n             | CTE_F seen_cte_f\n             | CTE_I seen_cte_i  TERM : FACTOR seen_factor TERM_P   TERM_P :    STAR seen_factor_op FACTOR seen_factor TERM_P\n                 |  FWD_SLASH seen_factor_op FACTOR seen_factor TERM_P\n                 |  empty  seen_factor :   seen_factor_op :   FUNC_CALL : ID seen_func_call_id OPEN_PARENTHESIS ARG_LIST CLOSE_PARENTHESIS  seen_func_call_id : empty  ARG_LIST : ID seen_arg ARG_LIST_P\n                 | EXPRESSION seen_arg ARG_LIST_P\n                 | FUNC_CALL seen_arg ARG_LIST_P\n                 | empty  ARG_LIST_P : COMMA ID seen_arg ARG_LIST_P\n                   | COMMA EXPRESSION seen_arg ARG_LIST_P\n                   | COMMA FUNC_CALL seen_arg ARG_LIST_P\n                   | empty  seen_arg :  FUNC_RETURN :   RETURN_KWD EXPRESSION SEMI_COLON\n                      | RETURN_KWD FUNC_CALL SEMI_COLON READ : READ_KWD OPEN_PARENTHESIS READABLE_LIST CLOSE_PARENTHESIS  WRITE : WRITE_KWD OPEN_PARENTHESIS PRINTABLE CLOSE_PARENTHESIS  PRINTABLE : EXPRESSION seen_printable PRINTABLE_P  PRINTABLE_P : COMMA EXPRESSION seen_printable PRINTABLE_P\n                    | empty  seen_printable  : empty  DECISION : IF_KWD OPEN_PARENTHESIS EXPRESSION CLOSE_PARENTHESIS seen_if_kwd OPEN_CURLY STATEMENT_STAR CLOSE_CURLY DECISION_P  DECISION_P : ELSE_KWD seen_else_kwd OPEN_CURLY STATEMENT_STAR CLOSE_CURLY\n                   | empty  seen_if_kwd : empty  seen_else_kwd : empty  REPETITION : CONDITIONAL_REP\n                   | UNCONDITIONAL_REP  CONDITIONAL_REP : WHILE_KWD seen_while_kwd OPEN_PARENTHESIS EXPRESSION CLOSE_PARENTHESIS seen_while_exp OPEN_CURLY STATEMENT_STAR CLOSE_CURLY  seen_while_kwd : empty  seen_while_exp : empty  UNCONDITIONAL_REP : FOR_KWD OPEN_PARENTHESIS ID seen_for_kwd EQUALS EXPRESSION seen_for_start_exp SEMI_COLON EXPRESSION seen_for_end_exp SEMI_COLON FOR_INCR_STATEMENT seen_for_incr_exp CLOSE_PARENTHESIS OPEN_CURLY STATEMENT_STAR CLOSE_CURLY  seen_for_kwd : empty  seen_for_incr_exp : empty seen_for_start_exp : empty  seen_for_end_exp : empty empty :'
    
_lr_action_items = {'PROGRAM_KWD':([0,],[2,]),'$end':([1,85,],[0,-1,]),'ID':([2,6,7,8,9,10,14,17,20,25,39,42,44,50,51,55,61,67,68,72,73,81,87,88,89,90,91,92,93,96,100,102,103,106,111,120,124,126,127,136,137,141,142,143,144,145,146,147,149,150,160,168,172,174,175,177,178,183,184,189,191,192,194,197,205,206,210,211,212,232,237,240,241,248,252,254,263,265,266,272,273,280,284,286,],[3,-121,11,-121,-5,18,11,-4,29,32,-10,45,-121,59,-3,45,59,-40,-41,-111,-112,11,-36,-37,-38,-39,105,114,114,121,-6,-121,128,-121,-121,114,11,114,-47,114,-72,-121,-59,-60,-61,-62,-63,-64,114,-71,59,201,114,114,-58,-54,-54,-86,-86,114,59,59,221,222,114,114,114,114,59,-121,59,-98,-99,114,-121,114,-106,-108,-113,59,59,-107,59,-116,]),'SEMI_COLON':([3,4,5,33,63,64,65,66,109,110,112,113,114,115,116,117,118,133,138,148,151,152,153,154,155,162,164,176,179,180,181,182,185,202,204,207,208,209,215,219,220,221,226,227,229,230,231,233,234,235,238,239,247,249,250,251,258,259,260,261,262,267,270,271,],[-121,6,-2,39,87,88,89,90,-55,-50,-85,-67,-74,-69,-77,-76,-75,-100,-101,-121,-121,-68,-78,-79,-80,-46,-87,-48,-53,-121,-85,-81,-84,-121,-121,-49,-70,-66,-121,240,241,-74,-65,-73,-56,-57,-50,-50,-85,-85,254,-119,-121,-121,-121,-121,-51,-121,-52,-82,-83,-121,273,-120,]),'CLASS_KWD':([6,8,100,],[10,10,-6,]),'TYPE':([6,7,8,9,12,13,14,15,17,23,26,27,34,39,52,57,100,125,216,],[-121,-121,-121,-5,25,-18,-121,-9,-4,25,-8,33,40,-10,76,25,-6,-7,-21,]),'MAIN_KWD':([6,7,8,9,12,13,14,15,17,22,23,24,26,31,39,100,216,],[-121,-121,-121,-5,-121,-18,-121,-9,-4,30,-121,-20,-8,-19,-10,-6,-21,]),'COMMA':([11,29,47,76,79,105,108,109,110,112,113,114,115,116,117,118,128,130,131,134,135,139,140,148,151,152,153,154,155,163,164,165,166,176,179,180,181,182,185,201,202,203,204,207,208,209,222,223,224,225,226,227,228,229,230,231,233,234,235,242,243,244,247,249,250,251,258,259,260,261,262,],[20,20,55,-29,55,-121,-121,-55,-50,-85,-67,-74,-69,-77,-76,-75,-74,-97,-67,168,-17,172,-105,-121,-121,-68,-78,-79,-80,197,-87,197,197,-48,-53,-121,-85,-81,-84,-121,-121,-121,-121,-49,-70,-66,-74,-97,-67,168,-65,-73,172,-56,-57,-50,-50,-85,-85,197,197,197,-121,-121,-121,-121,-51,-121,-52,-82,-83,]),'COLON':([11,16,19,21,29,35,45,],[-121,27,-11,-13,-121,-12,52,]),'CLOSE_CURLY':([14,15,23,24,26,31,39,44,50,51,57,60,61,62,67,68,72,73,80,81,86,87,88,89,90,101,124,125,160,161,190,191,192,193,212,216,217,218,236,237,240,241,252,253,263,265,266,272,274,280,284,285,286,],[-121,-9,-121,-20,-8,-19,-10,-121,-121,-3,-121,85,-121,-35,-40,-41,-111,-112,100,-121,-34,-36,-37,-38,-39,125,-121,-7,-121,195,216,-121,-121,-33,-121,-21,-31,-32,252,-121,-98,-99,-121,266,-106,-108,-113,-121,280,-107,-121,286,-116,]),'SMALLER':([18,109,110,112,113,114,115,116,117,118,128,131,148,151,152,153,154,155,164,176,179,180,181,182,185,202,207,208,209,220,221,222,224,226,227,231,233,234,235,247,249,250,251,258,259,260,261,262,],[28,143,-50,-85,-67,-74,-69,-77,-76,-75,-74,-67,-121,-121,-68,-78,-79,-80,-87,-48,-53,-121,-85,-81,-84,-121,-49,-70,-66,-67,-74,-74,-67,-65,-73,-50,-50,-85,-85,-121,-121,-121,-121,-51,-121,-52,-82,-83,]),'DERIVES_KWD':([28,],[34,]),'OPEN_PARENTHESIS':([30,32,37,38,59,69,70,71,74,75,83,84,92,93,94,95,102,103,106,111,114,120,126,127,128,136,137,141,142,143,144,145,146,147,149,150,172,174,175,177,178,183,184,189,194,197,205,206,210,211,221,222,232,248,254,],[36,-121,42,-22,-121,91,92,93,-121,96,103,-88,106,106,120,-114,-121,106,-121,-121,-121,106,106,-47,-121,106,-72,-121,-59,-60,-61,-62,-63,-64,106,-71,106,106,-58,-54,-54,-86,-86,106,106,106,106,106,106,106,-121,-121,-121,106,106,]),'CLOSE_PARENTHESIS':([36,42,46,47,48,54,56,76,79,99,103,104,105,107,108,109,110,112,113,114,115,116,117,118,119,128,129,130,131,132,133,134,135,138,139,140,148,151,152,153,154,155,157,162,163,164,165,166,167,169,170,171,173,176,179,180,181,182,185,196,198,199,200,201,202,203,204,207,208,209,222,223,224,225,226,227,228,229,230,231,233,234,235,242,243,244,245,246,247,249,250,251,255,256,257,258,259,260,261,262,275,276,277,278,279,281,282,],[41,-121,53,-121,-26,-25,-28,-29,-121,-27,-121,133,-121,138,-121,-55,-50,-85,-67,-74,-69,-77,-76,-75,156,-74,164,-97,-67,-92,-100,-121,-17,-101,-121,-105,-121,-121,-68,-78,-79,-80,188,-46,-121,-87,-121,-121,-14,-16,202,-102,-104,-48,-53,-121,-85,-81,-84,-89,-96,-90,-91,-121,-121,-121,-121,-49,-70,-66,-74,-97,-67,-121,-65,-73,-121,-56,-57,-50,-50,-85,-85,-121,-121,-121,-15,-103,-121,-121,-121,-121,-93,-94,-95,-51,-121,-52,-82,-83,-121,-42,-43,-44,-45,283,-118,]),'BIGGER':([40,109,110,112,113,114,115,116,117,118,128,131,148,151,152,153,154,155,164,176,179,180,181,182,185,202,207,208,209,220,221,222,224,226,227,231,233,234,235,247,249,250,251,258,259,260,261,262,],[43,142,-50,-85,-67,-74,-69,-77,-76,-75,-74,-67,-121,-121,-68,-78,-79,-80,-87,-48,-53,-121,-85,-81,-84,-121,-49,-70,-66,-67,-74,-74,-67,-65,-73,-50,-50,-85,-85,-121,-121,-121,-121,-51,-121,-52,-82,-83,]),'OPEN_CURLY':([41,43,58,97,98,122,123,156,186,187,188,195,213,214,264,268,269,283,],[44,49,81,-121,124,160,-24,-121,212,-109,-121,-30,237,-115,-121,272,-110,284,]),'READ_KWD':([44,50,51,61,67,68,72,73,87,88,89,90,160,191,192,212,237,240,241,252,263,265,266,272,273,280,284,286,],[-121,69,-3,69,-40,-41,-111,-112,-36,-37,-38,-39,69,69,69,69,69,-98,-99,-121,-106,-108,-113,69,69,-107,69,-116,]),'WRITE_KWD':([44,50,51,61,67,68,72,73,87,88,89,90,160,191,192,212,237,240,241,252,263,265,266,272,273,280,284,286,],[-121,70,-3,70,-40,-41,-111,-112,-36,-37,-38,-39,70,70,70,70,70,-98,-99,-121,-106,-108,-113,70,70,-107,70,-116,]),'IF_KWD':([44,50,51,61,67,68,72,73,87,88,89,90,160,191,192,212,237,240,241,252,263,265,266,272,280,284,286,],[-121,71,-3,71,-40,-41,-111,-112,-36,-37,-38,-39,71,71,71,71,71,-98,-99,-121,-106,-108,-113,71,-107,71,-116,]),'WHILE_KWD':([44,50,51,61,67,68,72,73,87,88,89,90,160,191,192,212,237,240,241,252,263,265,266,272,280,284,286,],[-121,74,-3,74,-40,-41,-111,-112,-36,-37,-38,-39,74,74,74,74,74,-98,-99,-121,-106,-108,-113,74,-107,74,-116,]),'FOR_KWD':([44,50,51,61,67,68,72,73,87,88,89,90,160,191,192,212,237,240,241,252,263,265,266,272,280,284,286,],[-121,75,-3,75,-40,-41,-111,-112,-36,-37,-38,-39,75,75,75,75,75,-98,-99,-121,-106,-108,-113,75,-107,75,-116,]),'ATTR_KWD':([49,],[58,]),'VARS_KWD':([53,77,78,],[-121,98,-23,]),'EQUALS':([59,82,121,158,159,],[-74,102,-121,189,-117,]),'RETURN_KWD':([67,68,72,73,87,88,89,90,160,191,192,240,241,252,263,265,266,280,286,],[-40,-41,-111,-112,-36,-37,-38,-39,194,194,194,-98,-99,-121,-106,-108,-113,-107,-116,]),'NOT':([92,93,102,103,106,111,120,126,127,136,137,141,142,143,144,145,146,147,149,150,172,174,175,177,178,183,184,189,194,197,205,206,210,211,232,248,254,],[111,111,-121,111,-121,-121,111,111,-47,111,-72,-121,-59,-60,-61,-62,-63,-64,111,-71,111,111,-58,-54,-54,-86,-86,111,111,111,232,232,232,232,-121,232,111,]),'CTE_S':([92,93,102,103,106,111,120,126,127,136,137,141,142,143,144,145,146,147,149,150,172,174,175,177,178,183,184,189,194,197,205,206,210,211,232,248,254,],[116,116,-121,116,-121,-121,116,116,-47,116,-72,-121,-59,-60,-61,-62,-63,-64,116,-71,116,116,-58,-54,-54,-86,-86,116,116,116,116,116,116,116,-121,116,116,]),'CTE_F':([92,93,102,103,106,111,120,126,127,136,137,141,142,143,144,145,146,147,149,150,172,174,175,177,178,183,184,189,194,197,205,206,210,211,232,248,254,],[117,117,-121,117,-121,-121,117,117,-47,117,-72,-121,-59,-60,-61,-62,-63,-64,117,-71,117,117,-58,-54,-54,-86,-86,117,117,117,117,117,117,117,-121,117,117,]),'CTE_I':([92,93,102,103,106,111,120,126,127,136,137,141,142,143,144,145,146,147,149,150,172,174,175,177,178,183,184,189,194,197,205,206,210,211,232,248,254,],[118,118,-121,118,-121,-121,118,118,-47,118,-72,-121,-59,-60,-61,-62,-63,-64,118,-71,118,118,-58,-54,-54,-86,-86,118,118,118,118,118,118,118,-121,118,118,]),'DOUBLE_EQUALS':([109,110,112,113,114,115,116,117,118,128,131,148,151,152,153,154,155,164,176,179,180,181,182,185,202,207,208,209,220,221,222,224,226,227,231,233,234,235,247,249,250,251,258,259,260,261,262,],[144,-50,-85,-67,-74,-69,-77,-76,-75,-74,-67,-121,-121,-68,-78,-79,-80,-87,-48,-53,-121,-85,-81,-84,-121,-49,-70,-66,-67,-74,-74,-67,-65,-73,-50,-50,-85,-85,-121,-121,-121,-121,-51,-121,-52,-82,-83,]),'DIFFERENT':([109,110,112,113,114,115,116,117,118,128,131,148,151,152,153,154,155,164,176,179,180,181,182,185,202,207,208,209,220,221,222,224,226,227,231,233,234,235,247,249,250,251,258,259,260,261,262,],[145,-50,-85,-67,-74,-69,-77,-76,-75,-74,-67,-121,-121,-68,-78,-79,-80,-87,-48,-53,-121,-85,-81,-84,-121,-49,-70,-66,-67,-74,-74,-67,-65,-73,-50,-50,-85,-85,-121,-121,-121,-121,-51,-121,-52,-82,-83,]),'AND':([109,110,112,113,114,115,116,117,118,128,131,148,151,152,153,154,155,164,176,179,180,181,182,185,202,207,208,209,220,221,222,224,226,227,231,233,234,235,247,249,250,251,258,259,260,261,262,],[146,-50,-85,-67,-74,-69,-77,-76,-75,-74,-67,-121,-121,-68,-78,-79,-80,-87,-48,-53,-121,-85,-81,-84,-121,-49,-70,-66,-67,-74,-74,-67,-65,-73,-50,-50,-85,-85,-121,-121,-121,-121,-51,-121,-52,-82,-83,]),'OR':([109,110,112,113,114,115,116,117,118,128,131,148,151,152,153,154,155,164,176,179,180,181,182,185,202,207,208,209,220,221,222,224,226,227,231,233,234,235,247,249,250,251,258,259,260,261,262,],[147,-50,-85,-67,-74,-69,-77,-76,-75,-74,-67,-121,-121,-68,-78,-79,-80,-87,-48,-53,-121,-85,-81,-84,-121,-49,-70,-66,-67,-74,-74,-67,-65,-73,-50,-50,-85,-85,-121,-121,-121,-121,-51,-121,-52,-82,-83,]),'PLUS':([110,112,113,114,115,116,117,118,128,131,148,151,152,153,154,155,164,181,182,185,202,208,209,220,221,222,224,226,227,231,233,234,235,247,249,250,251,259,261,262,],[-50,-85,-67,-74,-69,-77,-76,-75,-74,-67,177,-121,-68,-78,-79,-80,-87,-85,-81,-84,-121,-70,-66,-67,-74,-74,-67,-65,-73,-50,-50,-85,-85,177,177,-121,-121,-121,-82,-83,]),'MINUS':([110,112,113,114,115,116,117,118,128,131,148,151,152,153,154,155,164,181,182,185,202,208,209,220,221,222,224,226,227,231,233,234,235,247,249,250,251,259,261,262,],[-50,-85,-67,-74,-69,-77,-76,-75,-74,-67,178,-121,-68,-78,-79,-80,-87,-85,-81,-84,-121,-70,-66,-67,-74,-74,-67,-65,-73,-50,-50,-85,-85,178,178,-121,-121,-121,-82,-83,]),'STAR':([112,113,114,115,116,117,118,128,131,151,152,153,154,155,164,181,202,208,209,220,221,222,224,226,227,234,235,250,251,259,],[-85,-67,-74,-69,-77,-76,-75,-74,-67,183,-68,-78,-79,-80,-87,-85,-121,-70,-66,-67,-74,-74,-67,-65,-73,-85,-85,183,183,-121,]),'FWD_SLASH':([112,113,114,115,116,117,118,128,131,151,152,153,154,155,164,181,202,208,209,220,221,222,224,226,227,234,235,250,251,259,],[-85,-67,-74,-69,-77,-76,-75,-74,-67,184,-68,-78,-79,-80,-87,-85,-121,-70,-66,-67,-74,-74,-67,-65,-73,-85,-85,184,184,-121,]),'ELSE_KWD':([252,],[264,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'seen_program_id':([3,],[4,]),'empty':([3,6,7,8,11,12,14,23,29,32,42,44,47,50,53,57,59,61,74,79,81,97,102,103,105,106,108,111,114,121,124,128,134,139,141,148,151,156,160,163,165,166,180,181,188,191,192,201,202,203,204,212,215,221,222,225,228,232,237,242,243,244,247,249,250,251,252,259,264,267,272,275,284,],[5,9,15,9,21,24,15,24,21,38,48,51,56,62,78,24,84,62,95,56,15,123,127,132,135,137,140,150,84,159,15,84,169,173,175,179,185,187,193,198,198,198,208,208,214,193,193,135,227,140,230,62,239,84,84,169,173,150,62,198,198,198,179,179,185,185,265,208,269,271,62,282,62,]),'CLASS_STAR':([6,8,],[7,17,]),'CLASS':([6,8,],[8,8,]),'GLOBAL_VAR':([7,],[12,]),'VAR_LIST_STAR':([7,14,81,124,],[13,26,101,161,]),'VAR_LIST':([7,14,81,124,],[14,14,14,14,]),'ID_LIST':([7,14,81,124,],[16,16,16,16,]),'ID_LIST_P':([11,29,],[19,35,]),'FUNC_DEF_STAR':([12,23,57,],[22,31,80,]),'FUNC_DEF':([12,23,57,],[23,23,23,]),'seen_func_id':([32,],[37,]),'FUNC_PARAM':([42,],[46,]),'VAR':([42,55,],[47,79,]),'seen_main_kwd':([44,],[50,]),'FUNC_PARAM_P':([47,79,],[54,99,]),'CLASS_ATTR':([49,],[57,]),'STATEMENT_STAR':([50,61,212,237,272,284,],[60,86,236,253,274,285,]),'STATEMENT':([50,61,160,191,192,212,237,272,284,],[61,61,191,191,191,61,61,61,61,]),'ASSIGN':([50,61,160,191,192,212,237,272,273,284,],[63,63,63,63,63,63,63,63,276,63,]),'FUNC_CALL':([50,61,92,93,103,120,126,136,149,160,172,174,189,191,192,194,197,205,206,210,211,212,237,248,254,272,273,284,],[64,64,113,113,131,113,113,113,113,64,113,113,113,64,64,220,224,113,113,113,113,64,64,113,113,64,277,64,]),'READ':([50,61,160,191,192,212,237,272,273,284,],[65,65,65,65,65,65,65,65,278,65,]),'WRITE':([50,61,160,191,192,212,237,272,273,284,],[66,66,66,66,66,66,66,66,279,66,]),'DECISION':([50,61,160,191,192,212,237,272,284,],[67,67,67,67,67,67,67,67,67,]),'REPETITION':([50,61,160,191,192,212,237,272,284,],[68,68,68,68,68,68,68,68,68,]),'CONDITIONAL_REP':([50,61,160,191,192,212,237,272,284,],[72,72,72,72,72,72,72,72,72,]),'UNCONDITIONAL_REP':([50,61,160,191,192,212,237,272,284,],[73,73,73,73,73,73,73,73,73,]),'seen_func_params':([53,],[77,]),'seen_id':([59,114,128,221,222,],[82,152,152,152,152,]),'seen_func_call_id':([59,114,128,221,222,],[83,83,83,83,83,]),'seen_while_kwd':([74,],[94,]),'VARS':([77,],[97,]),'READABLE_LIST':([91,],[104,]),'PRINTABLE':([92,],[107,]),'EXPRESSION':([92,93,103,120,126,136,172,174,189,194,197,254,],[108,119,130,157,162,170,203,204,215,219,223,267,]),'EXP':([92,93,103,120,126,136,149,172,174,189,194,197,254,],[109,109,109,109,109,109,180,109,109,109,109,109,109,]),'TERM':([92,93,103,120,126,136,149,172,174,189,194,197,205,206,254,],[110,110,110,110,110,110,110,110,110,110,110,110,231,233,110,]),'FACTOR':([92,93,103,120,126,136,149,172,174,189,194,197,205,206,210,211,248,254,],[112,112,112,112,112,112,181,112,112,112,112,112,112,112,234,235,259,112,]),'CNST':([92,93,103,120,126,136,149,172,174,189,194,197,205,206,210,211,248,254,],[115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,]),'seen_func_vars':([97,],[122,]),'seen_equals':([102,],[126,]),'ARG_LIST':([103,],[129,]),'seen_readable':([105,201,],[134,225,]),'seen_open_parenthesis':([106,],[136,]),'seen_printable':([108,203,],[139,228,]),'COMP':([109,],[141,]),'seen_term':([110,231,233,],[148,247,249,]),'seen_not':([111,232,],[149,248,]),'seen_factor':([112,181,234,235,],[151,151,250,251,]),'seen_cte_s':([116,],[153,]),'seen_cte_f':([117,],[154,]),'seen_cte_i':([118,],[155,]),'seen_for_kwd':([121,],[158,]),'seen_arg':([128,130,131,222,223,224,],[163,165,166,242,243,244,]),'READABLE_LIST_P':([134,225,],[167,245,]),'PRINTABLE_P':([139,228,],[171,246,]),'seen_comp_op':([141,],[174,]),'EXP_P':([148,247,249,],[176,258,260,]),'TERM_P':([151,250,251,],[182,261,262,]),'seen_if_kwd':([156,],[186,]),'FUNC_STATEMENT_STAR':([160,191,192,],[190,217,218,]),'FUNC_RETURN':([160,191,192,],[192,192,192,]),'ARG_LIST_P':([163,165,166,242,243,244,],[196,199,200,255,256,257,]),'seen_term_op':([177,178,],[205,206,]),'pop_not':([180,181,259,],[207,209,209,]),'seen_factor_op':([183,184,],[210,211,]),'seen_while_exp':([188,],[213,]),'seen_close_parenthesis':([202,],[226,]),'seen_comp':([204,],[229,]),'seen_for_start_exp':([215,],[238,]),'DECISION_P':([252,],[263,]),'seen_else_kwd':([264,],[268,]),'seen_for_end_exp':([267,],[270,]),'FOR_INCR_STATEMENT':([273,],[275,]),'seen_for_incr_exp':([275,],[281,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> PROGRAM_KWD ID seen_program_id SEMI_COLON CLASS_STAR GLOBAL_VAR FUNC_DEF_STAR MAIN_KWD OPEN_PARENTHESIS CLOSE_PARENTHESIS OPEN_CURLY seen_main_kwd STATEMENT_STAR CLOSE_CURLY','PROGRAM',14,'p_program','main.py',189),
  ('seen_program_id -> empty','seen_program_id',1,'p_seen_program_id','main.py',195),
  ('seen_main_kwd -> empty','seen_main_kwd',1,'p_seen_main_kwd','main.py',200),
  ('CLASS_STAR -> CLASS CLASS_STAR','CLASS_STAR',2,'p_class_star','main.py',204),
  ('CLASS_STAR -> empty','CLASS_STAR',1,'p_class_star','main.py',205),
  ('CLASS -> CLASS_KWD ID SMALLER DERIVES_KWD TYPE BIGGER OPEN_CURLY CLASS_ATTR FUNC_DEF_STAR CLOSE_CURLY','CLASS',10,'p_class','main.py',208),
  ('CLASS_ATTR -> ATTR_KWD OPEN_CURLY VAR_LIST_STAR CLOSE_CURLY','CLASS_ATTR',4,'p_class_attr','main.py',211),
  ('VAR_LIST_STAR -> VAR_LIST VAR_LIST_STAR','VAR_LIST_STAR',2,'p_var_list_star','main.py',214),
  ('VAR_LIST_STAR -> empty','VAR_LIST_STAR',1,'p_var_list_star','main.py',215),
  ('VAR_LIST -> ID_LIST COLON TYPE SEMI_COLON','VAR_LIST',4,'p_var_list','main.py',222),
  ('ID_LIST -> ID ID_LIST_P','ID_LIST',2,'p_id_list','main.py',226),
  ('ID_LIST_P -> COMMA ID ID_LIST_P','ID_LIST_P',3,'p_id_list_p','main.py',232),
  ('ID_LIST_P -> empty','ID_LIST_P',1,'p_id_list_p','main.py',233),
  ('READABLE_LIST -> ID seen_readable READABLE_LIST_P','READABLE_LIST',3,'p_readable_list','main.py',240),
  ('READABLE_LIST_P -> COMMA ID seen_readable READABLE_LIST_P','READABLE_LIST_P',4,'p_readable_list_p','main.py',244),
  ('READABLE_LIST_P -> empty','READABLE_LIST_P',1,'p_readable_list_p','main.py',245),
  ('seen_readable -> empty','seen_readable',1,'p_seen_readable','main.py',248),
  ('GLOBAL_VAR -> VAR_LIST_STAR','GLOBAL_VAR',1,'p_global_var','main.py',254),
  ('FUNC_DEF_STAR -> FUNC_DEF FUNC_DEF_STAR','FUNC_DEF_STAR',2,'p_func_def_star','main.py',261),
  ('FUNC_DEF_STAR -> empty','FUNC_DEF_STAR',1,'p_func_def_star','main.py',262),
  ('FUNC_DEF -> TYPE ID seen_func_id OPEN_PARENTHESIS FUNC_PARAM CLOSE_PARENTHESIS seen_func_params VARS seen_func_vars OPEN_CURLY FUNC_STATEMENT_STAR CLOSE_CURLY','FUNC_DEF',12,'p_func_def','main.py',265),
  ('seen_func_id -> empty','seen_func_id',1,'p_seen_func_id','main.py',270),
  ('seen_func_params -> empty','seen_func_params',1,'p_seen_func_params','main.py',274),
  ('seen_func_vars -> empty','seen_func_vars',1,'p_seen_func_vars','main.py',282),
  ('FUNC_PARAM -> VAR FUNC_PARAM_P','FUNC_PARAM',2,'p_func_param','main.py',292),
  ('FUNC_PARAM -> empty','FUNC_PARAM',1,'p_func_param','main.py',293),
  ('FUNC_PARAM_P -> COMMA VAR FUNC_PARAM_P','FUNC_PARAM_P',3,'p_func_param_p','main.py',301),
  ('FUNC_PARAM_P -> empty','FUNC_PARAM_P',1,'p_func_param_p','main.py',302),
  ('VAR -> ID COLON TYPE','VAR',3,'p_var','main.py',310),
  ('VARS -> VARS_KWD OPEN_CURLY VAR_LIST_STAR CLOSE_CURLY','VARS',4,'p_vars','main.py',314),
  ('FUNC_STATEMENT_STAR -> STATEMENT FUNC_STATEMENT_STAR','FUNC_STATEMENT_STAR',2,'p_func_statement_star','main.py',319),
  ('FUNC_STATEMENT_STAR -> FUNC_RETURN FUNC_STATEMENT_STAR','FUNC_STATEMENT_STAR',2,'p_func_statement_star','main.py',320),
  ('FUNC_STATEMENT_STAR -> empty','FUNC_STATEMENT_STAR',1,'p_func_statement_star','main.py',321),
  ('STATEMENT_STAR -> STATEMENT STATEMENT_STAR','STATEMENT_STAR',2,'p_statement_star','main.py',325),
  ('STATEMENT_STAR -> empty','STATEMENT_STAR',1,'p_statement_star','main.py',326),
  ('STATEMENT -> ASSIGN SEMI_COLON','STATEMENT',2,'p_statement','main.py',329),
  ('STATEMENT -> FUNC_CALL SEMI_COLON','STATEMENT',2,'p_statement','main.py',330),
  ('STATEMENT -> READ SEMI_COLON','STATEMENT',2,'p_statement','main.py',331),
  ('STATEMENT -> WRITE SEMI_COLON','STATEMENT',2,'p_statement','main.py',332),
  ('STATEMENT -> DECISION','STATEMENT',1,'p_statement','main.py',333),
  ('STATEMENT -> REPETITION','STATEMENT',1,'p_statement','main.py',334),
  ('FOR_INCR_STATEMENT -> ASSIGN','FOR_INCR_STATEMENT',1,'p_for_incr_statement','main.py',337),
  ('FOR_INCR_STATEMENT -> FUNC_CALL','FOR_INCR_STATEMENT',1,'p_for_incr_statement','main.py',338),
  ('FOR_INCR_STATEMENT -> READ','FOR_INCR_STATEMENT',1,'p_for_incr_statement','main.py',339),
  ('FOR_INCR_STATEMENT -> WRITE','FOR_INCR_STATEMENT',1,'p_for_incr_statement','main.py',340),
  ('ASSIGN -> ID seen_id EQUALS seen_equals EXPRESSION','ASSIGN',5,'p_assign','main.py',343),
  ('seen_equals -> empty','seen_equals',1,'p_seen_equals','main.py',347),
  ('EXP -> TERM seen_term EXP_P','EXP',3,'p_exp','main.py',351),
  ('EXP -> NOT seen_not EXP pop_not','EXP',4,'p_exp','main.py',352),
  ('seen_term -> <empty>','seen_term',0,'p_seen_term','main.py',356),
  ('EXP_P -> PLUS seen_term_op TERM seen_term EXP_P','EXP_P',5,'p_exp_p','main.py',362),
  ('EXP_P -> MINUS seen_term_op TERM seen_term EXP_P','EXP_P',5,'p_exp_p','main.py',363),
  ('EXP_P -> empty','EXP_P',1,'p_exp_p','main.py',364),
  ('seen_term_op -> <empty>','seen_term_op',0,'p_seen_term_op','main.py',367),
  ('EXPRESSION -> EXP','EXPRESSION',1,'p_expression','main.py',371),
  ('EXPRESSION -> EXP COMP seen_comp_op EXPRESSION seen_comp','EXPRESSION',5,'p_expression','main.py',372),
  ('seen_comp -> empty','seen_comp',1,'p_seen_comp','main.py',375),
  ('seen_comp_op -> empty','seen_comp_op',1,'p_seen_comp_op','main.py',380),
  ('COMP -> BIGGER','COMP',1,'p_comp','main.py',384),
  ('COMP -> SMALLER','COMP',1,'p_comp','main.py',385),
  ('COMP -> DOUBLE_EQUALS','COMP',1,'p_comp','main.py',386),
  ('COMP -> DIFFERENT','COMP',1,'p_comp','main.py',387),
  ('COMP -> AND','COMP',1,'p_comp','main.py',388),
  ('COMP -> OR','COMP',1,'p_comp','main.py',389),
  ('FACTOR -> OPEN_PARENTHESIS seen_open_parenthesis EXPRESSION CLOSE_PARENTHESIS seen_close_parenthesis','FACTOR',5,'p_factor','main.py',394),
  ('FACTOR -> NOT seen_not FACTOR pop_not','FACTOR',4,'p_factor','main.py',395),
  ('FACTOR -> FUNC_CALL','FACTOR',1,'p_factor','main.py',396),
  ('FACTOR -> ID seen_id','FACTOR',2,'p_factor','main.py',397),
  ('FACTOR -> CNST','FACTOR',1,'p_factor','main.py',398),
  ('pop_not -> empty','pop_not',1,'p_pop_not','main.py',401),
  ('seen_not -> empty','seen_not',1,'p_seen_not','main.py',415),
  ('seen_open_parenthesis -> empty','seen_open_parenthesis',1,'p_seen_open_parenthesis','main.py',419),
  ('seen_close_parenthesis -> empty','seen_close_parenthesis',1,'p_seen_close_parenthesis','main.py',423),
  ('seen_id -> <empty>','seen_id',0,'p_seen_id','main.py',427),
  ('seen_cte_i -> <empty>','seen_cte_i',0,'p_seen_cte_i','main.py',432),
  ('seen_cte_f -> <empty>','seen_cte_f',0,'p_seen_cte_f','main.py',437),
  ('seen_cte_s -> <empty>','seen_cte_s',0,'p_seen_cte_s','main.py',443),
  ('CNST -> CTE_S seen_cte_s','CNST',2,'p_cnst','main.py',450),
  ('CNST -> CTE_F seen_cte_f','CNST',2,'p_cnst','main.py',451),
  ('CNST -> CTE_I seen_cte_i','CNST',2,'p_cnst','main.py',452),
  ('TERM -> FACTOR seen_factor TERM_P','TERM',3,'p_term','main.py',457),
  ('TERM_P -> STAR seen_factor_op FACTOR seen_factor TERM_P','TERM_P',5,'p_term_p','main.py',460),
  ('TERM_P -> FWD_SLASH seen_factor_op FACTOR seen_factor TERM_P','TERM_P',5,'p_term_p','main.py',461),
  ('TERM_P -> empty','TERM_P',1,'p_term_p','main.py',462),
  ('seen_factor -> <empty>','seen_factor',0,'p_seen_factor','main.py',466),
  ('seen_factor_op -> <empty>','seen_factor_op',0,'p_seen_factor_op','main.py',471),
  ('FUNC_CALL -> ID seen_func_call_id OPEN_PARENTHESIS ARG_LIST CLOSE_PARENTHESIS','FUNC_CALL',5,'p_func_call','main.py',476),
  ('seen_func_call_id -> empty','seen_func_call_id',1,'p_seen_func_call_id','main.py',480),
  ('ARG_LIST -> ID seen_arg ARG_LIST_P','ARG_LIST',3,'p_arg_list','main.py',486),
  ('ARG_LIST -> EXPRESSION seen_arg ARG_LIST_P','ARG_LIST',3,'p_arg_list','main.py',487),
  ('ARG_LIST -> FUNC_CALL seen_arg ARG_LIST_P','ARG_LIST',3,'p_arg_list','main.py',488),
  ('ARG_LIST -> empty','ARG_LIST',1,'p_arg_list','main.py',489),
  ('ARG_LIST_P -> COMMA ID seen_arg ARG_LIST_P','ARG_LIST_P',4,'p_arg_list_p','main.py',492),
  ('ARG_LIST_P -> COMMA EXPRESSION seen_arg ARG_LIST_P','ARG_LIST_P',4,'p_arg_list_p','main.py',493),
  ('ARG_LIST_P -> COMMA FUNC_CALL seen_arg ARG_LIST_P','ARG_LIST_P',4,'p_arg_list_p','main.py',494),
  ('ARG_LIST_P -> empty','ARG_LIST_P',1,'p_arg_list_p','main.py',495),
  ('seen_arg -> <empty>','seen_arg',0,'p_seen_arg','main.py',498),
  ('FUNC_RETURN -> RETURN_KWD EXPRESSION SEMI_COLON','FUNC_RETURN',3,'p_func_return','main.py',505),
  ('FUNC_RETURN -> RETURN_KWD FUNC_CALL SEMI_COLON','FUNC_RETURN',3,'p_func_return','main.py',506),
  ('READ -> READ_KWD OPEN_PARENTHESIS READABLE_LIST CLOSE_PARENTHESIS','READ',4,'p_read','main.py',509),
  ('WRITE -> WRITE_KWD OPEN_PARENTHESIS PRINTABLE CLOSE_PARENTHESIS','WRITE',4,'p_write','main.py',513),
  ('PRINTABLE -> EXPRESSION seen_printable PRINTABLE_P','PRINTABLE',3,'p_printable','main.py',517),
  ('PRINTABLE_P -> COMMA EXPRESSION seen_printable PRINTABLE_P','PRINTABLE_P',4,'p_printable_p','main.py',521),
  ('PRINTABLE_P -> empty','PRINTABLE_P',1,'p_printable_p','main.py',522),
  ('seen_printable -> empty','seen_printable',1,'p_seen_printable','main.py',525),
  ('DECISION -> IF_KWD OPEN_PARENTHESIS EXPRESSION CLOSE_PARENTHESIS seen_if_kwd OPEN_CURLY STATEMENT_STAR CLOSE_CURLY DECISION_P','DECISION',9,'p_decision','main.py',530),
  ('DECISION_P -> ELSE_KWD seen_else_kwd OPEN_CURLY STATEMENT_STAR CLOSE_CURLY','DECISION_P',5,'p_decision_p','main.py',535),
  ('DECISION_P -> empty','DECISION_P',1,'p_decision_p','main.py',536),
  ('seen_if_kwd -> empty','seen_if_kwd',1,'p_seen_if_kwd','main.py',539),
  ('seen_else_kwd -> empty','seen_else_kwd',1,'p_seen_else_kwd','main.py',543),
  ('REPETITION -> CONDITIONAL_REP','REPETITION',1,'p_repetition','main.py',550),
  ('REPETITION -> UNCONDITIONAL_REP','REPETITION',1,'p_repetition','main.py',551),
  ('CONDITIONAL_REP -> WHILE_KWD seen_while_kwd OPEN_PARENTHESIS EXPRESSION CLOSE_PARENTHESIS seen_while_exp OPEN_CURLY STATEMENT_STAR CLOSE_CURLY','CONDITIONAL_REP',9,'p_conditional_rep','main.py',554),
  ('seen_while_kwd -> empty','seen_while_kwd',1,'p_seen_while_kwd','main.py',561),
  ('seen_while_exp -> empty','seen_while_exp',1,'p_seen_while_exp','main.py',566),
  ('UNCONDITIONAL_REP -> FOR_KWD OPEN_PARENTHESIS ID seen_for_kwd EQUALS EXPRESSION seen_for_start_exp SEMI_COLON EXPRESSION seen_for_end_exp SEMI_COLON FOR_INCR_STATEMENT seen_for_incr_exp CLOSE_PARENTHESIS OPEN_CURLY STATEMENT_STAR CLOSE_CURLY','UNCONDITIONAL_REP',17,'p_unconditional_rep','main.py',571),
  ('seen_for_kwd -> empty','seen_for_kwd',1,'p_seen_for_kwd','main.py',587),
  ('seen_for_incr_exp -> empty','seen_for_incr_exp',1,'p_seen_for_incr_exp','main.py',593),
  ('seen_for_start_exp -> empty','seen_for_start_exp',1,'p_seen_for_start_exp','main.py',597),
  ('seen_for_end_exp -> empty','seen_for_end_exp',1,'p_seen_for_end_exp','main.py',602),
  ('empty -> <empty>','empty',0,'p_empty','main.py',615),
]
