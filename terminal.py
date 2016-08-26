class Terminal(object):

    """Docstring for Terminal. """

    def __init__(self):
        """TODO: to be defined1. """
        self.xMax = 11
        self.yMax = 21
        self.terminal = [['.' for i in range(self.yMax)] for j in range(self.xMax)]
        self.x = 0
        self.y = 0
        self.mode = 'o'

    def __str__(self):
        terminalString = ""
        for line in self.terminal:
            columnString = ""
            for column in line:
                columnString += column

            terminalString += columnString + "\n"

        terminalString += "\nmode: " + self.mode
        terminalString += "\ncursor: " + self.x.__str__() + "  " + self.y.__str__()

        return terminalString
