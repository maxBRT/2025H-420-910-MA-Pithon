class Simple:
    def __init__(self):
        self.x = 10
        self.y = 20
        self.z = 30

    def get_x(self):
        return self.x
    def fizz_buzz(self, n: int):
        for i in range(1, n + 1):
            if i % 15 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)


obj = Simple()
obj.fizz_buzz(100)