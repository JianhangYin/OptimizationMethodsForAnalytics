from sympy import *


class SteepestDecent:

    MIN_STEP = 10 ** (-6)

    def __init__(self, initial_input, min_max, max_time):
        self.direction = []
        self.alpha = []
        self.input = [initial_input]
        self.function = None
        self.iteration_time = 0
        self.define_function()
        self.max_time = max_time
        self.min_max = min_max

    def define_function(self):
        x, y = symbols('x, y')
        # target function
        self.function = - (4 * x ** 2 - 2.54 * x + 6.654) / (2 * y ** 2) - 2 * log(2 * pi * y ** 2)

    def calculate_direction(self):
        direction_sign = 1 if self.min_max == 'max' else -1
        current_direction = []
        x, y = symbols('x, y')
        d_x = diff(self.function, x)
        d_y = diff(self.function, y)
        current_direction.append(direction_sign * d_x.subs({x: self.input[-1][0], y: self.input[-1][1]}))
        current_direction.append(direction_sign * d_y.subs({x: self.input[-1][0], y: self.input[-1][1]}))
        self.direction.append(current_direction)

    def calculate_alpha(self):
        x, y, alpha = symbols('x, y, alpha')
        lp_function = self.function.subs({x: self.input[-1][0] + alpha * self.direction[-1][0], y: self.input[-1][1] + alpha * self.direction[-1][1]})
        d_alpha = diff(lp_function, alpha)
        solved_alpha = [item for item in sorted(solve(d_alpha, alpha)) if item > 0]
        self.alpha.append(solved_alpha[0])

    def calculate_input(self):
        new_input = [self.input[-1][0] + self.alpha[-1] * self.direction[-1][0],
                     self.input[-1][1] + self.alpha[-1] * self.direction[-1][1]]
        self.input.append(new_input)

    def steep_decent_iteration(self):
        while self.max_time > self.iteration_time:
            self.calculate_direction()
            self.calculate_alpha()
            self.calculate_input()
            self.iteration_time += 1
        for item in self.input:
            print(item)
        for item in self.alpha:
            print(item)
        for item in self.direction:
            print(item)
        print(len(self.input), len(self.alpha), len(self.direction))


a = SteepestDecent([10, 10], 'max', 10)
a.steep_decent_iteration()






























