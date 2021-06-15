from .categories import CATEGORIES
from .yatzy import Player, YatzyGame

def test_chance_scores_sum_of_all_dice():
    assert 15 == CATEGORIES.chance.score((2, 3, 4, 5, 1))
    assert 16 == CATEGORIES.chance.score((3, 3, 4, 5, 1))


def test_yatzy_scores_50():
    assert 50 == CATEGORIES.yatzy.score((4, 4, 4, 4, 4))
    assert 50 == CATEGORIES.yatzy.score((6, 6, 6, 6, 6))
    assert 0 == CATEGORIES.yatzy.score((6, 6, 6, 6, 3))


def test_1s():
    assert 1 == CATEGORIES.ones.score((1, 2, 3, 4, 5))
    assert 2 == CATEGORIES.ones.score((1, 2, 1, 4, 5))
    assert 0 == CATEGORIES.ones.score((6, 2, 2, 4, 5))
    assert 4 == CATEGORIES.ones.score((1, 2, 1, 1, 1))


def test_2s():
    assert 4 == CATEGORIES.twos.score((1, 2, 3, 2, 6))
    assert 10 == CATEGORIES.twos.score((2, 2, 2, 2, 2))


def test_threes():
    assert 6 == CATEGORIES.threes.score((1, 2, 3, 2, 3))
    assert 12 == CATEGORIES.threes.score((2, 3, 3, 3, 3))


def test_fours_test():
    assert 12 == CATEGORIES.fours.score((4, 4, 4, 5, 5))
    assert 8 == CATEGORIES.fours.score((4, 4, 5, 5, 5))
    assert 4 == CATEGORIES.fours.score((4, 5, 5, 5, 5))


def test_fives():
    assert 10 == CATEGORIES.fives.score((4, 4, 4, 5, 5))
    assert 15 == CATEGORIES.fives.score((4, 4, 5, 5, 5))
    assert 20 == CATEGORIES.fives.score((4, 5, 5, 5, 5))


def test_sixes_test():
    assert 0 == CATEGORIES.sixes.score((4, 4, 4, 5, 5))
    assert 6 == CATEGORIES.sixes.score((4, 4, 6, 5, 5))
    assert 18 == CATEGORIES.sixes.score((6, 5, 6, 6, 5))


def test_one_pair():
    assert 6 == CATEGORIES.pairs.score((3, 4, 3, 5, 6))
    assert 10 == CATEGORIES.pairs.score((5, 3, 3, 3, 5))
    assert 12 == CATEGORIES.pairs.score((5, 3, 6, 6, 5))


def test_two_pair():
    assert 16 == CATEGORIES.two_pairs.score((3, 3, 5, 4, 5))
    assert 18 == CATEGORIES.two_pairs.score((3, 3, 6, 6, 6))
    assert 0 == CATEGORIES.two_pairs.score((3, 3, 6, 5, 4))
    assert 0 == CATEGORIES.two_pairs.score((3, 1, 6, 5, 4))


def test_three_of_a_kind():
    assert 9 == CATEGORIES.three_of_a_kind.score((3, 3, 3, 4, 5))
    assert 15 == CATEGORIES.three_of_a_kind.score((5, 3, 5, 4, 5))
    assert 9 == CATEGORIES.three_of_a_kind.score((3, 3, 3, 3, 5))


def test_four_of_a_knd():
    assert 12 == CATEGORIES.four_of_a_kind.score((3, 3, 3, 3, 5))
    assert 20 == CATEGORIES.four_of_a_kind.score((5, 5, 5, 4, 5))
    assert 12 == CATEGORIES.four_of_a_kind.score((3, 3, 3, 3, 3))
    assert 0 == CATEGORIES.four_of_a_kind.score((3, 3, 3, 2, 1))


def test_small_straight():
    assert 30 == CATEGORIES.small_straight.score((1, 2, 3, 4, 5))
    assert 30 == CATEGORIES.small_straight.score((2, 3, 4, 5, 1))
    assert 0 == CATEGORIES.small_straight.score((1, 2, 2, 4, 5))
    assert 30 == CATEGORIES.small_straight.score((1, 2, 3, 4, 6))


def test_large_straight():
    assert 40 == CATEGORIES.large_straight.score((6, 2, 3, 4, 5))
    assert 40 == CATEGORIES.large_straight.score((2, 3, 4, 5, 6))
    assert 0 == CATEGORIES.large_straight.score((1, 2, 2, 4, 5))


def test_full_house():
    assert 25 == CATEGORIES.full_house.score((6, 2, 2, 2, 6))
    assert 0 == CATEGORIES.full_house.score((2, 3, 4, 5, 6))


def test_player():
    test_pos = 3
    player = Player(test_pos)
    assert player.points == 0
    assert player.position == test_pos
    player_categories_names = player.categories.keys()
    for category_name in CATEGORIES._fields:
        assert category_name in player_categories_names
    assert all([val is False for val in player.categories.values()])


def test_game():
    game = YatzyGame(5)
    assert len(game.players) == 5
    assert sorted(player.position for  player in game.players) == [1, 2, 3, 4, 5]
