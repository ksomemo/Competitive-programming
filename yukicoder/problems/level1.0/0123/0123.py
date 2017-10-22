def main():
    N, M = map(int, input().split())
    A = map(int, input().split())

    cards = list(range(1, N + 1))
    for a in A:
        pos = a - 1
        card = cards[pos]
        del cards[pos]
        cards.insert(0, card)

    print(cards[0])

if __name__ == '__main__':
    main()
