class Matrix:
    def __int__(self, a, b, c, d):
        self.matrix = [a, b, c, d]

    def __add__(self, other):
        tmp = []
        for i in range(len(self.matrix)):
            tmp.append(self.matrix[i] + other.matrix[i])
        return tmp

    # a =
    def __mul__(self, other):
        a = self.matrix[0] * other.matrix[0] + self.matrix[1] * other.matrix[2]
        b = self.matrix[0] * other.matrix[1] + self.matrix[1] * other.matrix[3]
        c = self.matrix[2] * other.matrix[1] + self.matrix[3] * other.matrix[3]
        d = self.matrix[2] * other.matrix[1] + self.matrix[3] * other.matrix[3]
        return Matrix(a, b, c, d)

    def __str__(self):
        return f"[{self.matrix[0]}{self.matrix[1]}; \n {self.matrix[2]}{self.matrix[3]}]"

    def __repr__(self):
        return f"Matrix({self.matrix[0]}, {self.matrix[1]}, {self.matrix[2]}, {self.matrix[3]})"