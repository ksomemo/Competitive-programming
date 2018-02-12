def main():
    SA = input()
    SB = input()
    SC = input()

    users = {
        "a": {"s": SA, "n": len(SA), "turn": 0},
        "b": {"s": SB, "n": len(SB), "turn": 0},
        "c": {"s": SC, "n": len(SC), "turn": 0},
    }

    name = "a"
    while True:
        user = users[name]

        user["turn"] += 1
        if user["turn"] > user["n"]:
            print(name.upper())
            return

        turn = user["turn"]
        name = user["s"][turn - 1]


if __name__ == '__main__':
    main()
