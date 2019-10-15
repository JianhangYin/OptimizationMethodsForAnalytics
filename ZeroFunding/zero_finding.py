from scipy.misc import derivative


class ZeroFunding:
    @staticmethod
    def bisection(func, low_bound, high_bound, min_distance):
        while abs(high_bound - low_bound) > min_distance:
            if func((low_bound + high_bound) / 2) > 0:
                high_bound = (low_bound + high_bound) / 2
            elif func((low_bound + high_bound) / 2) < 0:
                low_bound = (low_bound + high_bound) / 2
            else:
                break
        target_result = (low_bound + high_bound) / 2
        return low_bound, high_bound, target_result

    @staticmethod
    def newton(func, init_point, min_value):
        while abs(func(init_point)) > min_value:
            init_point = init_point - func(init_point) / derivative(func, init_point, min_value)
        return init_point

    @staticmethod
    def secant(func, first_point, second_point, min_value):
        while abs(func(second_point)) > min_value:
            func_dev = (func(second_point) - func(first_point)) / (second_point - first_point)
            first_point, second_point = second_point, second_point - func(second_point) / func_dev
        return second_point

    @staticmethod
    def regula_falsi(func, first_point, second_point, min_value):
        while abs(func(second_point)) > min_value:
            print(second_point)
            func_dev = (func(second_point) - func(first_point)) / (second_point - first_point)
            temp_point = second_point
            second_point = second_point - func(second_point) / func_dev
            first_point = first_point if func(first_point) * func(second_point) < 0 else temp_point
        return second_point
