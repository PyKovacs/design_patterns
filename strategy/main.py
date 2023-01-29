from typing import Protocol, List

class SelectionStrategy(Protocol):

	def execute(self, numbers: List[int]) -> List[int]:
		raise NotImplementedError


class FirstAndLastSelectionStrategy:

	def execute(self, numbers: List[int]) -> List[int]:
		return [numbers[0], numbers[-1]]


class EvenIndexSelectionStrategy:

	def execute(self, numbers: List[int]) -> List[int]:
		return numbers[1::2]


def select_numbers(numbers: List[int], selection_strategy: SelectionStrategy) -> List[int]:
	print('Selecting the numbers...')
	return selection_strategy.execute(numbers)

def main():
	numbers = input('Enter your numbers seperated by comma: ').split(',')
	strategy = EvenIndexSelectionStrategy()
	print(f'Selected numbers are: {select_numbers(numbers, strategy)}')

if __name__ == '__main__':
	main()
