def digit_sum(number):

  digit_sum = 0
  while number > 0:
    digit = number % 10
    digit_sum += digit
    number //= 10

  return digit_sum


def max_digit_sum(numbers):

  max_sum = -1
  max_number = None

  for number in numbers:
    digit_sum = digit_sum(number)
    if digit_sum > max_sum:
      max_sum = digit_sum
      max_number = number

  return max_number