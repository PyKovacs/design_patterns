from typing import Protocol

class SelectionStrategy(Protocol):

	def execute(self, numbers: list[int]) -> list[int]:
		raise NotImplementedError


class FirstAndLastSelectionStrategy:

	def execute(self, numbers: list[int]) -> list[int]:
		return [numbers[0], numbers[-1]]


class EvenIndexSelectionStrategy:

	def execute(self, numbers: list[int]) -> list[int]:
		return numbers[1::2]


def select_numbers(numbers: list[int], selection_strategy: SelectionStrategy) -> list[int]:
	print('Selecting the numbers...')
	return selection_strategy.execute(numbers)

def main() -> None:
	numbers = list(map(int, input('Enter your numbers seperated by comma: ').split(',')))
	if isinstance(numbers, list) and [item for item in numbers if isinstance(item, int)]:
		strategy = EvenIndexSelectionStrategy()
		print(f'Selected numbers are: {select_numbers(numbers, strategy)}')

if __name__ == '__main__':
	main()
