import io
from collections import Counter
from typing import NamedTuple


class LetterSumResult(NamedTuple):

    word: str
    len: int


def lettersum(s: str) -> int:
    return sum(
        map(
            lambda x: ord(x) - ord("a") + 1,
            s.lower(),
        ),
        0,
    )


tests = {
    "": 0,
    "a": 1,
    "z": 26,
    "cab": 6,
    "excellent": 100,
    "microspectrophotometries": 317,
}

print(f"tests: {all(lettersum(test) == value for test, value in tests.items())}")

# BONUS
bonus_results = []

with io.open("e399-enable1.txt") as fenable1:
    enable1 = fenable1.read().splitlines()


# 1
bonus_results += [
    list(
        filter(
            lambda x: x.len == 319,
            map(
                lambda x: LetterSumResult(x, lettersum(x)),
                enable1,
            ),
        ),
    ),
]

# 2
bonus_results += [
    len(
        list(
            filter(
                lambda x: x % 2 != 0,
                map(
                    lettersum,
                    enable1,
                ),
            ),
        ),
    ),
]

lettersums_common = Counter(
    map(
        lettersum,
        enable1,
    ),
).most_common()

# 3
bonus_results += [
    (
        lambda x: f"len: {x[0]}, words: {x[1]}"
    )(
        lettersums_common[0],
    )    
]

for index, bonus in enumerate(bonus_results):
    print(f"bonus #{index}: {bonus}")
