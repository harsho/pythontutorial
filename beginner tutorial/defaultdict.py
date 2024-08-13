from collections import defaultdict


def default_Val():
    return "none"

d = defaultdict(default_Val)

d["1"] = 1
d["2"] = 2

print(d["1"])

