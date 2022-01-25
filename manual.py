from Pair25ColorCode import*

def print_manual(formatString, printOnConsole):
  test_count = 0
  for i, major in enumerate(MAJOR_COLORS):
    for j, minor in enumerate(MINOR_COLORS):
      formatted_string = formatString((i * 5 + j), major, minor)
      printOnConsole(formatted_string)
      test_count += 1
  return test_count

def printOnConsole(formatted_string):
  print(formatted_string)

def formatString(index, major, minor):
  return f'{index} | {major} | {minor}'


if __name__ == '__main__':
    print_manual()
