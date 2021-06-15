from abc import ABC
from collections import namedtuple
from typing import Dict, Tuple, Union

DieNamedTuple = namedtuple('die', ['value', 'index'])
CategoryNamedTuple = namedtuple('categories',
                                ['chance', 'yatzy',
                                 'ones', 'twos', 'threes', 'fours', 'fives', 'sixes',
                                 'pairs', 'two_pairs',
                                 'three_of_a_kind', 'four_of_a_kind',
                                 'small_straight', 'large_straight',
                                 'full_house'])


class CategoryImplementationError(Exception):
    pass


class Category(ABC):
    def __init__(self, category_name: str):
        self.name = category_name

    def score(self, dice_tuple: Tuple[int, int, int, int, int]) -> int:
        raise NotImplementedError


class ChanceCategory(Category):

    def score(self, dice_tuple: Tuple[int, int, int, int, int]) -> int:
        return sum(dice_tuple)


class YatzyCategory(Category):
    def score(self, dice_tuple: Tuple[int, int, int, int, int]) -> int:
        return 50 if len(set(dice_tuple)) == 1 else 0


class SumsCategory(Category):

    def __init__(self, category_name: str):
        """
        :param category_name: "sum:1", "sum:2", "sum:3", "sum:4", "sum:5", or "sum:6"
        """
        super().__init__(category_name)
        num_to_sum = category_name.split(':')[-1]
        if not num_to_sum.isdigit():
            raise CategoryImplementationError(
                f"expecting '{num_to_sum}' (from '{category_name}') to be a digit")
        self.num_to_sum = int(num_to_sum)

    def score(self, dice_tuple: Tuple[int, int, int, int, int]) -> int:
        return sum(filter(lambda x: x == self.num_to_sum, dice_tuple))


class PairCategory(Category):

    @staticmethod
    def get_highest_pair(
            dice_tuple: Union[Tuple[int, int, int], Tuple[int, int, int, int, int]]
    ) -> Tuple[DieNamedTuple, DieNamedTuple]:
        """

        :param dice_tuple: tuple of either 3 or 5 integers
        :return: Tuple representing the value and index of the highest pair in dice_tuple
        """

        # if there are no pairs, return 0
        default_return_value = (DieNamedTuple(value=0, index=-1), DieNamedTuple(value=0, index=-1))

        for possible_die_value in list(reversed(range(1, 7))):
            for idx, actual_die_value_i in enumerate(dice_tuple[:-1]):
                if actual_die_value_i == possible_die_value:
                    for j, actual_die_value_j in enumerate(dice_tuple[idx + 1:]):
                        jdx = j + idx + 1
                        if actual_die_value_i == actual_die_value_j:
                            return (DieNamedTuple(value=actual_die_value_i, index=idx),
                                    DieNamedTuple(value=actual_die_value_j, index=jdx))

        return default_return_value

    def score(self, dice_tuple: Tuple[int, int, int, int, int]) -> int:
        high_pair = self.get_highest_pair(dice_tuple)
        return sum(x.value for x in high_pair)


class TwoPairCategory(PairCategory):

    def score(self, dice_tuple: Tuple[int, int, int, int, int]) -> int:
        first_high_pair = self.get_highest_pair(dice_tuple)

        if first_high_pair[0].value == 0:
            return 0

        # if a high pair was found, remove the high pair values and find the next highest pair
        dice_list = list(dice_tuple)
        dice_list.remove(first_high_pair[0].value)
        dice_list.remove(first_high_pair[0].value)

        next_high_pair = self.get_highest_pair(tuple(dice_list))

        if next_high_pair[0].value == 0:
            return 0

        return sum(x.value for x in first_high_pair) + sum(x.value for x in next_high_pair)


class XOfAKind(Category):

    def __init__(self, category_name: str):
        """
        :param category_name: "kind:3", "kind:4"
        """
        super().__init__(category_name)
        num_of_a_kind = category_name.split(':')[-1]
        if not num_of_a_kind.isdigit():
            raise CategoryImplementationError(
                f"expecting '{num_of_a_kind}' (from '{category_name}') to be a digit")
        self.num_of_a_kind = int(num_of_a_kind)

    def score(self, dice_tuple: Tuple[int, int, int, int, int]) -> int:
        default_return_value = 0
        for die_value in dice_tuple:
            def filter_func(x, value=die_value):
                return x == value

            if len(list(filter(filter_func, dice_tuple))) >= self.num_of_a_kind:
                return self.num_of_a_kind * die_value

        return default_return_value


class Straight(Category):

    def __init__(self, category_name: str):
        """
        :param category_name: "straight:4", "straight:5"
        """
        super().__init__(category_name)
        big_or_small = category_name.split(':')[-1]
        if not big_or_small.isdigit() or big_or_small not in ['4', '5']:
            raise CategoryImplementationError(
                f"expecting '{big_or_small}' (from '{category_name}') to be a digit")
        self.big_or_small = int(big_or_small)

    def score(self, dice_tuple: Tuple[int, int, int, int, int]) -> int:
        sorted_set = sorted(set(dice_tuple))
        if len(set(dice_tuple)) < self.big_or_small:
            return 0

        num_skips = 0
        if self.big_or_small == 4 and len(sorted_set) == 5:
            num_skips = 1

        for curr_die, next_die in zip(sorted_set[:], sorted_set[1:]):
            if curr_die + 1 != next_die:
                if num_skips == 0:
                    return 0
                num_skips = num_skips - 1

        return 30 if self.big_or_small == 4 else 40


class FullHouse(Category):

    def score(self, dice_tuple: Tuple[int, int, int, int, int]) -> int:
        return 0 if len(set(dice_tuple)) > 2 else 25


CATEGORIES = CategoryNamedTuple(
    chance=ChanceCategory("chance"),
    yatzy=YatzyCategory("yatzy"),
    ones=SumsCategory("sum:1"),
    twos=SumsCategory("sum:2"),
    threes=SumsCategory("sum:3"),
    fours=SumsCategory("sum:4"),
    fives=SumsCategory("sum:5"),
    sixes=SumsCategory("sum:6"),
    pairs=PairCategory("pairs"),
    two_pairs=TwoPairCategory("two-pairs"),
    three_of_a_kind=XOfAKind("kind:3"),
    four_of_a_kind=XOfAKind("kind:4"),
    small_straight=Straight("straight:4"),
    large_straight=Straight("straight:5"),
    full_house=FullHouse("full-house")
)
