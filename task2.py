# \x1b[47;1m белый
# \x1b[40;1m черный

End = '\x1b[0m'
offs = ' '

for i in range(3):
    for i in range(8):
        print(f"\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 21}\x1b[40;1m{offs * 3}{End}", end='')
    print()
    for i in range(8):
        print(f"\x1b[47;1m{offs * 3}\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 15}\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 3}{End}", end='')
    print()
    for i in range(8):
        print(f"\x1b[47;1m{offs * 6}\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 9}\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 6}{End}", end='')
    print()
    for i in range(8):
        print(f"\x1b[47;1m{offs * 9}\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 3}\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 9}{End}", end='')
    print()
    for i in range(8):
        print(f"\x1b[47;1m{offs * 12}\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 12}{End}", end='')
    print()
    for i in range(8):
        print(f"\x1b[47;1m{offs * 9}\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 3}\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 9}{End}", end='')
    print()
    for i in range(8):
        print(f"\x1b[47;1m{offs * 6}\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 9}\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 6}{End}", end='')
    print()
    for i in range(8):
        print(f"\x1b[47;1m{offs * 3}\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 15}\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 3}{End}", end='')
    print()
    for i in range(8):
        print(f"\x1b[40;1m{offs * 3}\x1b[47;1m{offs * 21}\x1b[40;1m{offs * 3}{End}", end='')
    print()
