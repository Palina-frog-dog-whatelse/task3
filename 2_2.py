def sr6():
    n, m = map(int, input().split())
    ans = []
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    for i in a:
        if i in b and i not in ans:
            ans.append(i)
    print(ans)
sr6()
