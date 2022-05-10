"""23. Write a Python program to get the n (non-negative integer)
copies of the first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2."""

def sub_string_copy(str, n):
  given_len = 2
  if given_len > len(str):
    given_len = len(str)
  sub_str = str[:given_len]
  
  result = ""
  for i in range(n):
    result = result + sub_str
  return result

print(sub_string_copy('abcdef', 2))
print(sub_string_copy('p', 3));