class InputGenerator:
    X = ""
    Y = ""
    indices_x = []
    indices_y = []
    final_x = ""
    final_y = ""

    def __init__(self, strings):
        self.X = strings[0]
        self.Y = strings[1]

    def inputStringGenerator(self, str, indices):
        cummulative = str
        for x in indices:
            s = str[0:x + 1]
            s = s + cummulative
            s = s + str[x + 1:len(str)]
            str = s
            cummulative = s
        return str
