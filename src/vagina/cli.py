import argparse

from .art import generate_art


def build_parser():
    parser = argparse.ArgumentParser(
        prog="vagina",
        description="Procedural organic ASCII generator",
    )
    parser.add_argument("--height", type=int, default=24, help="Height of the generated art")
    parser.add_argument("--center", type=int, default=34, help="Horizontal center position")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducible output")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    print(generate_art(height=args.height, center=args.center, seed=args.seed))
