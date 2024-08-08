def pascal_triangle(n):
  """Prints Pascal's triangle up to the specified number of rows.

  Args:
    n: The number of rows to print.
  """

  for i in range(n):
    # Calculate and print the current row
    row = [1]
    for j in range(1, i + 1):
      row.append(row[j - 1] * (i - j + 1) // j)
    print(' ' * (n - i), *row)

# Example usage
rows = 5
pascal_triangle(rows)
