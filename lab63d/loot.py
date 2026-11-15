import random
LOOT_TABLE = ["药水", "金币", "铁剑"]

def drop_loot(table: list[str], times: int) -> list[str]:
    result = []
    for _ in range(times):
        result.append(random.choice(table))
    return result

if __name__ == "__main__":
    print(f"自测: {drop_loot(["药水"], 2)}")

