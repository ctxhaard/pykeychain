#!/usr/bin/env python3

import curses

def main(stdscr):
    stdscr.clear()
    wincmd = curses.newwin(1,curses.COLS-1,curses.LINES-1,0)
    winlist = curses.newwin(curses.LINES-2,curses.COLS-1,0,curses.COLS-1)
    wincmd.addstr('Insert your password:',curses.A_REVERSE)
    wincmd.refresh()
    curses.echo()
    # note: non so perche' la app esce subito...
    stdscr.getstr(curses.COLS-1,0,15)    

if __name__ == '__main__':
    curses.wrapper(main)

