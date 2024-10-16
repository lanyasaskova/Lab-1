line = ' ' * 25
SET_COLOR = '\x1b[48;5;'
END = '\x1b[0m'
CLEAR = "\033[H"
def draw_line(offset=0, length=25, color=196):
    line = ' ' * length
    print(f"{' ' * offset}{SET_COLOR}{color}m{line}{END}")
draw_line()
draw_line(color=231)
draw_line(color=27)
