def roman_to_int(roman_number):
  """Converts a Roman numeral to an integer.

  Args:
    roman_number: A string representing a Roman numeral.

  Returns:
    The integer value of the Roman numeral.
  """
  roman_numeral_dict = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000,
      "IV": 4,
      "IX": 9,
      "XL": 40,
      "XC": 90,
      "CD": 400,
      "CM": 900,
  }

  total = 0
  i = 0
  while i < len(roman_number):
    current_value = roman_numeral_dict[roman_number[i]]
    next_value = None
    if i + 1 < len(roman_number):
      next_value = roman_numeral_dict[roman_number[i + 1]]

    if next_value and current_value < next_value:
      total -= current_value
    else:
      total += current_value
    i += 1

  return total


