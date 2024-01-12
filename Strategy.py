from abc import ABC, abstractmethod
from typing import List


# Strategy Interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, dataset: List[int]) -> List[int]:
        pass


# Concrete strategies
class AscendingSortStrategy(SortStrategy):
    def sort(self, dataset: List[int]) -> List[int]:
        return sorted(dataset)


class DescendingSortStrategy(SortStrategy):
    def sort(self, dataset: List[int]) -> List[int]:
        return sorted(dataset, reverse=True)


class CustomSortStrategy(SortStrategy):
    def sort(self, dataset: List[int]) -> List[int]:
        return sorted(dataset, key=lambda x: -x)


class SortContext:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, dataset: List[int]) -> List[int]:
        return self._strategy.sort(dataset)


# Client code
if __name__ == "__main__":
    data = [8, 69, 420, 1, 5, 6]

    # Using ascending sort strategy
    context = SortContext(AscendingSortStrategy())
    print("Ascending Sort:", context.sort(data))

    # Changing strategy to descending sort
    context.set_strategy(DescendingSortStrategy())
    print("Descending Sort:", context.sort(data))

    # Changing strategy to custom sort
    context.set_strategy(CustomSortStrategy())
    print("Custom Sort:", context.sort(data))
