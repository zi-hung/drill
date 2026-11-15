def average(scores: list[int]) -> int:
    return round(sum(scores) / len(scores), 1)


if __name__ == "__main__":
    print(f"自测: {average([1, 2, 3])}")

