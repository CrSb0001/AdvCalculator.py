BASIC_MATH_INPUTS=set('123')
def bas_math_calc(s):
  while True:
    choice=input(f'Input:')
    val=set(f'{choice}')
    if val.issubset(BASIC_MATH_INPUTS)==True:
      return True
    else:
      print('That isn\'t an allowed input. Please try again.')
      continue
print(f'Which operation would you like to do?\n+-+--------------------+\n|1|Addition/Subtraction|\n+-+--------------------+\n|2|Multiplication      |\n+-+--------------------+\n|3|Division            |\n+-+--------------------+')
