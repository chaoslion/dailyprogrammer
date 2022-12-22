# https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/?ref=share&ref_source=link

def time2word(value: str) -> str:
    
    # split on colon and convert to integers
    h, m = list(map(int, value.split(":")))

    nums_map = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eightteen",
        19: "nineteen",
    }

    hours_map = {
        0: "twelve",
        **nums_map,
    }

    min_threshold = {
        10: "oh",
        20: "teen",
        30: "twenty",
        40: "thirty",
        50: "fourty",
        60: "fifty",
    }

    # throw zero away (will be filtered out later)
    if m == 0:
        m = ""
    else:
        for threshold, value in min_threshold.items():
            if m < threshold:
                # substract to lookup the second part of the number
                m -= threshold - 10
                # no second part: just use the threshold value
                if m == 0:
                    m = value
                else:
                    # combine threshold value with lookup of the second part
                    m = f"{value} {nums_map[m]}"
                break

    result = [
        "It's",
        hours_map[h % 12],
        m,
        "am" if h < 12 else "pm",
    ]

    # combine parts and filter empty values
    return " ".join(filter(lambda x: x, result))
    

samples = {
    "00:00": "It's twelve am",
    "01:30": "It's one thirty am",
    "12:05": "It's twelve oh five pm",
    "14:01": "It's two oh one pm",
    "20:29": "It's eight twenty nine pm",
    "21:00": "It's nine pm",
}

print(
    all(
        time2word(sin) == sout for sin, sout in samples.items()
    )
)