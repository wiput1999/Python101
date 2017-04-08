led = [
    [
        "xxxx",
        "x--x",
        "x--x",
        "x--x",
        "xxxx"
    ],
    [
        "---x",
        "---x",
        "---x",
        "---x",
        "---x"
    ],
    [
        "xxxx",
        "---x",
        "xxxx",
        "x---",
        "xxxx"
    ],
    [
        "xxxx",
        "---x",
        "xxxx",
        "---x",
        "xxxx"
    ],
    [
        "x--x",
        "x--x",
        "xxxx",
        "---x",
        "---x"
    ],
    [
        "xxxx",
        "x---",
        "xxxx",
        "---x",
        "xxxx"
    ],
    [
        "xxxx",
        "x---",
        "xxxx",
        "x--x",
        "xxxx"
    ],
    [
        "xxxx",
        "---x",
        "---x",
        "---x",
        "---x"
    ],
    [
        "xxxx",
        "x--x",
        "xxxx",
        "x--x",
        "xxxx"
    ],
    [
        "xxxx",
        "x--x",
        "xxxx",
        "---x",
        "xxxx"
    ]
]

s = input("Number : ")

for i in range(len(led[0])):
    for j in range(len(s)):
        a = int(s[j])
        print(led[a][i], "\t", end="")
    print()