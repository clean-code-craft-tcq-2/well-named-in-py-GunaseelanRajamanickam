from testlib import*

def print_manual():
  pair_number = 1
  for major_Color in MAJOR_COLORS:
    for minor_Color in MINOR_COLORS:
      print(pair_number, major_Color, minor_Color)
      pair_number += 1


if __name__ == '__main__':
    print_manual()
