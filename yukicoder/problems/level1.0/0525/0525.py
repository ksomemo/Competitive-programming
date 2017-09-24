def main():
    T = input()
    h, m = map(int, T.split(":"))
    m_plus5 = m + 5
    new_h = (h + m_plus5 // 60) % 24
    new_m = m_plus5 % 60
    print("{0}:{1:02d}".format(
        str(new_h).zfill(2),
        new_m)
    )

if __name__ == '__main__':
    main()
