import re
from typing import Callable

def generator_numbers(text: str):
  position = 0
  text_slice = text
  
  while True:
    if position >= len(text_slice) - 1:
      break

    text_slice = text_slice[position:]
    match = re.search(r'(^|\s)(\d+(?:\.\d+)?)(\s|$)', text_slice)
    
    if match == None:
      break
    
    position = match.end() - 1
    result = float(match.group().strip())
    yield result


def sum_profit(string: str, func: Callable[[str], float]) -> float:
  sum = 0
  for res in func(string):
    sum += res
    print(res, sum)

  return round(sum, 2)


text = "100.45 Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими 27 27.45 надходженнями 27 sd 27.45 і 324.00 доларів. 12.2"
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
