from __future__ import print_function
from __future__ import division
import sys

class Executer:
  def __init__(self, quadruplets, symbols_table, temporal_count):
    self.quadruplets = quadruplets
    self.symbols_table = symbols_table
    self.temporals = [None] * temporal_count
    self.program_counter = 0
    self.calls_stack = []

  def get_operator_value(self, operator):
    if type(operator) is str: 
      if operator[0] == '#':
        return self.temporals[int(operator[1:len(operator)])]
      return self.symbols_table[operator].value
    return operator

  def set_operator_value(self, operator, value):
    if operator[0] == '#':
      self.temporals[int(operator[1:len(operator)])] = value
    else:
      self.symbols_table[operator].value = eval(self.symbols_table[operator].type)(value)

  def add_op(self, operator_1, operator_2, result):
    operator_1 = self.get_operator_value(operator_1)
    operator_2 = self.get_operator_value(operator_2)
    self.set_operator_value(result, operator_1 + operator_2)

  def or_op(self, operator_1, operator_2, result):
    operator_1 = self.get_operator_value(operator_1)
    operator_2 = self.get_operator_value(operator_2)
    self.set_operator_value(result, operator_1 or operator_2)

  def sub_op(self, operator_1, operator_2, result):
    operator_1 = self.get_operator_value(operator_1)
    operator_2 = self.get_operator_value(operator_2)
    self.set_operator_value(result, operator_1 - operator_2)

  def mul_op(self, operator_1, operator_2, result):
    operator_1 = self.get_operator_value(operator_1)
    operator_2 = self.get_operator_value(operator_2)
    self.set_operator_value(result, operator_1 * operator_2)

  def div_op(self, operator_1, operator_2, result):
    operator_1 = self.get_operator_value(operator_1)
    operator_2 = self.get_operator_value(operator_2)
    self.set_operator_value(result, operator_1 / operator_2)

  def and_op(self, operator_1, operator_2, result):
    operator_1 = self.get_operator_value(operator_1)
    operator_2 = self.get_operator_value(operator_2)
    self.set_operator_value(result, operator_1 and operator_2)

  def mod_op(self, operator_1, operator_2, result):
    operator_1 = self.get_operator_value(operator_1)
    operator_2 = self.get_operator_value(operator_2)
    self.set_operator_value(result, operator_1 % operator_2)

  def lt_op(self, operator_1, operator_2, result):
    operator_1 = self.get_operator_value(operator_1)
    operator_2 = self.get_operator_value(operator_2)
    self.set_operator_value(result, operator_1 < operator_2)

  def le_op(self, operator_1, operator_2, result):
    operator_1 = self.get_operator_value(operator_1)
    operator_2 = self.get_operator_value(operator_2)
    self.set_operator_value(result, operator_1 <= operator_2)

  def eq_op(self, operator_1, operator_2, result):
    operator_1 = self.get_operator_value(operator_1)
    operator_2 = self.get_operator_value(operator_2)
    self.set_operator_value(result, operator_1 == operator_2)

  def ne_op(self, operator_1, operator_2, result):
    operator_1 = self.get_operator_value(operator_1)
    operator_2 = self.get_operator_value(operator_2)
    self.set_operator_value(result, operator_1 != operator_2)

  def gt_op(self, operator_1, operator_2, result):
    operator_1 = self.get_operator_value(operator_1)
    operator_2 = self.get_operator_value(operator_2)
    self.set_operator_value(result, operator_1 > operator_2)

  def ge_op(self, operator_1, operator_2, result):
    operator_1 = self.get_operator_value(operator_1)
    operator_2 = self.get_operator_value(operator_2)
    self.set_operator_value(result, operator_1 >= operator_2)

  def goto_op(self, jump):
    self.program_counter = jump - 1

  def gotofalse_op(self, operator, jump):
    operator = self.get_operator_value(operator)
    if not operator:
      self.program_counter = jump - 1

  def gototrue_op(self, operator, jump):
    operator = self.get_operator_value(operator)
    if operator:
      self.program_counter = jump - 1

  def gosub_op(self, jump):
    self.calls_stack.append(self.program_counter)
    self.program_counter = jump - 1

  def return_op(self):
    self.program_counter = self.calls_stack.pop() 

  def print_op(self, operator):
    if operator == '\n':
      print('')
    elif operator[0] == '"':
      print(operator[1:len(operator)-1], end= '')
    else:
      print(self.get_operator_value(operator), end= '')

  def input_op(self, operator):
    self.set_operator_value(operator, raw_input())

  def store_op(self, operator_1, operator_2):
    value = self.get_operator_value(operator_1)
    self.set_operator_value(operator_2, value)

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
    while self.program_counter < len(self.quadruplets):
      q = self.quadruplets[self.program_counter]
      self.instruction(q[0])(*q[1:len(q)])
      self.program_counter = self.program_counter + 1
    print('\n')
