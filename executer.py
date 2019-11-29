import sys

class Executer:
  def __init__(self, quadruplets, symbols_table, temporal_count):
    self.quadruplets = quadruplets
    self.symbols_table = symbols_table
    self.temporals = [None] * temporal_count
    self.program_counter = 0

  def add_op(self, operator_1, operator_2, result):
    print(sys._getframe(0).f_code.co_name)

  def or_op(self, operator_1, operator_2, result):
    print(sys._getframe(0).f_code.co_name)

  def sub_op(self, operator_1, operator_2, result):
    print(sys._getframe(0).f_code.co_name)

  def mul_op(self, operator_1, operator_2, result):
    print(sys._getframe(0).f_code.co_name)

  def div_op(self, operator_1, operator_2, result):
    print(sys._getframe(0).f_code.co_name)

  def and_op(self, operator_1, operator_2, result):
    print(sys._getframe(0).f_code.co_name)

  def mod_op(self, operator_1, operator_2, result):
    print(sys._getframe(0).f_code.co_name)

  def lt_op(self, operator_1, operator_2, result):
    print(sys._getframe(0).f_code.co_name)

  def le_op(self, operator_1, operator_2, result):
    print(sys._getframe(0).f_code.co_name)

  def eq_op(self, operator_1, operator_2, result):
    print(sys._getframe(0).f_code.co_name)

  def ne_op(self, operator_1, operator_2, result):
    print(sys._getframe(0).f_code.co_name)

  def gt_op(self, operator_1, operator_2, result):
    print(sys._getframe(0).f_code.co_name)

  def ge_op(self, operator_1, operator_2, result):
    print(sys._getframe(0).f_code.co_name)

  def goto_op(self, jump):
    print(sys._getframe(0).f_code.co_name)

  def gotofalse_op(self, operator, jump):
    print(sys._getframe(0).f_code.co_name)

  def gototrue_op(self, operator, jump):
    print(sys._getframe(0).f_code.co_name)

  def gosub_op(self, jump):
    print(sys._getframe(0).f_code.co_name)

  def return_op(self, var):
    print(sys._getframe(0).f_code.co_name)

  def print_op(self, operator):
    print(sys._getframe(0).f_code.co_name)

  def input_op(self, operator):
    print(sys._getframe(0).f_code.co_name)

  def store_op(self, operator_1, operator_2):
    print(sys._getframe(0).f_code.co_name)

  def instruction(self, key):
    return {
      '=': self.store_op,
      '+': self.add_op,
      '||': self.or_op,
      '-': self.sub_op, 
      '*': self.mul_op, 
      '/': self.div_op,
      '&&': self.and_op, 
      '%': self.mod_op, 
      '<': self.lt_op, 
      '<=': self.le_op, 
      '==': self.eq_op, 
      '!=': self.ne_op, 
      '>': self.gt_op, 
      '>=': self.ge_op,
      'goto': self.goto_op,
      'gotofalso': self.gotofalse_op,
      'gototrue': self.gototrue_op,
      'gosub': self.gosub_op,
      'return': self.return_op,
      'print': self.print_op,
      'input': self.input_op
    }[key]

  def execute(self):
    print("Executing...")
    for q in self.quadruplets:
      print(q[0])
      print(self.instruction(q[0])(self, *q[1:len(q)-1]))
