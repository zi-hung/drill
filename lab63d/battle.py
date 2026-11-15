import loot

def main():
    print(f"掉落 3 件: {loot.drop_loot(loot.LOOT_TABLE, 3)}")

if __name__ == "__main__":
    main()

