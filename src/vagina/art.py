import math
import random

OUTER_PAIRS = [
    ("(", ")"),
    ("[", "]"),
    ("{", "}"),
    ("<", ">"),
    ("/", "\\"),
    ("\\", "/"),
]

INNER_MARKS = ["||", "<>", "()", "[]", "{}", "..", "::", ""]
FILL_SET = [" ", ".", "_", "~", ":"]


def _smooth(values, rounds=3):
    values = values[:]
    for _ in range(rounds):
        new_values = values[:]
        for i in range(1, len(values) - 1):
            new_values[i] = (values[i - 1] + values[i] + values[i + 1]) / 3
        values = new_values
    return values


def _make_profile(height, rng):
    amp = rng.uniform(8, 16)
    waist_y = rng.uniform(0.35, 0.65)
    waist_depth = rng.uniform(1.0, 4.5)
    top_taper = rng.uniform(0.5, 2.5)
    bottom_taper = rng.uniform(0.5, 2.5)

    profile = []
    for y in range(height):
        t = y / max(1, height - 1)

        base = math.sin(math.pi * t) * amp
        waist = math.exp(-((t - waist_y) ** 2) / rng.uniform(0.01, 0.03)) * waist_depth
        wiggle = (
            math.sin(t * math.pi * rng.uniform(2.0, 4.0)) * rng.uniform(0.0, 0.8)
            + math.sin(t * math.pi * rng.uniform(5.0, 8.0)) * rng.uniform(0.0, 0.3)
        )
        noise = rng.uniform(-0.5, 0.5)
        taper = (1 - t) * top_taper + t * bottom_taper

        width = base - waist - taper + wiggle + noise
        profile.append(max(2.0, width))

    return _smooth(profile, rounds=4)


def _build_middle(inner_width, rng):
    fill = rng.choice(FILL_SET)
    mode = rng.randint(0, 4)

    if mode == 0:
        return fill * inner_width

    if mode == 1:
        return "".join(rng.choice([fill, ".", " ", "~"]) for _ in range(inner_width))

    if mode == 2:
        token = rng.choice(INNER_MARKS)
        side = max(0, inner_width - len(token))
        left = "".join(rng.choice([fill, ".", " "]) for _ in range(side // 2))
        right = "".join(rng.choice([fill, ".", " "]) for _ in range(side - len(left)))
        return left + token + right

    if mode == 3:
        a = rng.choice([".", "~", "_", " "])
        b = rng.choice([".", "~", "_", " "])
        return "".join(a if i % 2 == 0 else b for i in range(inner_width))

    return "".join(rng.choice([" ", ".", ":", "_"]) for _ in range(inner_width))


def generate_art(height=24, center=34, seed=None):
    rng = random.Random(seed)

    left_edge, right_edge = rng.choice(OUTER_PAIRS)
    profile = _make_profile(height=height, rng=rng)

    lines = []

    top_count = rng.randint(1, 3)
    bottom_count = rng.randint(1, 3)

    for _ in range(top_count):
        w = rng.randint(2, 6)
        indent = " " * rng.randint(max(0, center - 2), center + 2)
        lines.append(
            indent
            + rng.choice(["/", "\\", "<", "("])
            + "." * w
            + rng.choice(["\\", "/", ">", ")"])
        )

    for half in profile:
        half_i = int(round(half))
        inner_w = max(4, half_i * 2)

        fold_left = rng.choice(["", left_edge, ""])
        fold_right = rng.choice(["", right_edge, ""])
        middle = _build_middle(inner_w, rng)

        indent = " " * max(0, center - half_i - len(fold_left))
        line = indent + left_edge + fold_left + middle + fold_right + right_edge
        lines.append(line.rstrip())

    for _ in range(bottom_count):
        w = rng.randint(2, 6)
        indent = " " * rng.randint(max(0, center - 2), center + 2)
        lines.append(
            indent
            + rng.choice(["/", "\\", "<", "("])
            + "_" * w
            + rng.choice(["\\", "/", ">", ")"])
        )

    return "\n".join(lines)
