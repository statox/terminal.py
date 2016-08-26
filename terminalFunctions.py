def clear(terminal):
    """ clear the entire screen; the cursor row and column do not change
    :returns: TODO

    """
    terminal.terminal = [['.' for i in range(terminal.yMax)] for j in range(terminal.xMax)]

def topLeft(terminal):
    """ Move the cursor to row 0, column 0; the image on the screen is not changed
    :returns: TODO

    """
    terminal.x = 0
    terminal.y = 0

def startOfCurrentLine(terminal):
    """ Move the cursor to the beginning of the current line; the cursor row does not change
    :returns: TODO

    """
    terminal.x = 0

def oneRowDown(terminal):
    """ Move the cursor down one row if possible; the cursor column does not change
    :returns: TODO

    """
    terminal.y += 1
    if (terminal.y > terminal.yMax):
        terminal.y = terminal.yMax-2

def oneRowUp(terminal):
    """ Move the cursor up one row, if possible; the cursor column does not change
    :returns: TODO

    """
    terminal.y -= 1
    if (terminal.y <= 0):
        terminal.y = 0

def oneColumnLeft(terminal):
    """ Move the cursor left one column, if possible; the cursor row does not change
    :returns: TODO

    """
    terminal.x -= 1
    if (terminal.x <= 0):
        terminal.x = 0

def oneColumnRight(terminal):
    """ Move the cursor right one column, if possible; the cursor row does not change
    :returns: TODO

    """
    terminal.x += 1
    if (terminal.x > terminal.xMax):
        terminal.x = terminal.xMax-2

def eraseCharacter(terminal):
    """ Erase characters to the right of, and including, the cursor column on the cursor's row;
        the cursor row and column do not change
    :returns: TODO

    """
    return "eraseCharacter"

def insertMode(terminal):
    """ Enter insert mode
    :returns: TODO

    """
    terminal.mode = 'i'

def overwriteMode(terminal):
    """ Enter overwrite mode
    :returns: TODO

    """
    terminal.mode = 'o'

def circumflex(terminal):
    """ Wite a circumflex (^) at the current cursor location, exactly as if it
        was not a special character; this is subject to the actions of the
        current mode (insert or overwrite) 
    :returns: TODO

    """
    addChar(terminal, '^')

def changeCoordinates(terminal, y, x):
    """ Move the cursor to the row and column specified;
    :returns: TODO

    """
    terminal.x = x
    terminal.y = y

def addChar(terminal, c):
    """ Insert a new character; this is subject to the actions of the current
        mode (insert or overwrite)
    :returns: TODO

    """
    if terminal.mode == 'o':
        terminal.terminal[terminal.y][terminal.x] = c.__str__()
        terminal.x += 1
    elif terminal.mode == 'i':
        line = terminal.terminal[terminal.y][terminal.x:terminal.xMax-2]
        terminal.terminal[terminal.y][terminal.x] = c.__str__()
        i=0
        for c in line:
            i+=1
            terminal.terminal[terminal.y][terminal.x+i] = c.__str__()
    else:
        # TODO : Raise exception
        print "C'est plante dans addChar. Mode inconnu"
