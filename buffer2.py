class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num
    
    def __sub__(self, other):
        return self.num - other.num
    
    def __mul__(self, other):
        return self.num * other.num

    def __eq__(self, other):
        return self.num == other.num

    def __lt__(self, other):
        return self.num < other.num


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)
print(n1 < n2)
print(n1 - n2)
print(n1 * n2)
print(n1 == n2)
