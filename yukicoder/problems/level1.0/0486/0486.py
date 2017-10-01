def main():
    S = input()

    #e = S.find("OOO")
    #w = S.find("XXX")

    for i in range(len(S)):
        if S[i:i + 3] == "OOO":
            print("East")
            return
        if S[i:i + 3] == "XXX":
            print("West")
            return
    print("NA")

if __name__ == '__main__':
    main()
