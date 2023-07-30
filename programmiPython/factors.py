def get_factors(number):
  factors = []
  iteration_index = 1
  while iteration_index <= number :
    if number%iteration_index == 0 :
      factors.append(iteration_index)
    iteration_index += 1
  print(f'The factors of {number} are: {factors}')
  return factors

get_factors(7)