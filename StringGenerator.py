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

    def inputStringGenerator(self, string, indices):
        cumulative = string
        for x in indices:
            s = string[0:x + 1]
            s = s + cumulative
            s = s + string[x + 1:len(string)]
            string = s
            cumulative = s
        return string
