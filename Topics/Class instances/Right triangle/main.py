class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = self.check_and_get_area()
        # calculate the area here

    def check_and_get_area(self):
        if self.c ** 2 == self.a ** 2 + self.b ** 2:
            return self.a * self.b / 2
        else:
            return 'Not right'


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
new_triangle = RightTriangle(input_c, input_a, input_b)

print(new_triangle.area)