import curses
import random
import time
import shutil

_size = shutil.get_terminal_size()
PADDLE_X = 1
PADDLE_H = 4

# Automatic Terminal window resize
H = max(8, min(20, _size.liness - 2))
W = max(20, min(40, _size.columns - 1))

def main(stdscr):
        curses.curs_set(0)
        stdscr.nodelay(True)
        stdscr.keypad(True)

        ball_x = W // 2
        ball_y = H // 2
        dx = random.choice([-1, 1])
        dy = random.choice([-1, 1])

        paddle_y = H // 2 - PADDLE_H // 2
        score = 0
        game_over = False
    def draw():
        stdscr.erase()
        for in range(X):
                try:
                        stdsrc.addch(0, x, '0')
                        stdsrc.addch()


