from typing import List, Tuple

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
result: List[Tuple] = list(map(lambda letter, number: (letter, number), letters, numbers))
print(result)
