from Pair25ColorCode import*
from manual import *


def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = get_color_from_pair_number(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)


def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = get_pair_number_from_color(major_color, minor_color)
  assert(pair_number == expected_pair_number)

def test_print_manual():
  def format_string_stub(index, major, minor):
    return f'{index} | {major} | {minor}'

  def print_on_console_stub(formatted_string):
    print(formatted_string)

  return_value = print_manual(format_string_stub, print_on_console_stub)
  assert(return_value == 25)
