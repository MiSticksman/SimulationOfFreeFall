from context import g


class FreeFall:

    def __init__(self, h0):
        self.h0 = h0
        self.h_values = []
        self.v_values = []

    def fall_time(self):
        t = abs(((2 * self.h0 / g) ** 0.5))
        return t

    @staticmethod
    def find_v(t):
        v = g * t
        return v

    def find_y(self, t):
        y = self.h0 - g * (t ** 2) / 2
        return y

    def calc_t_values(self):
        time = self.fall_time()
        t_values = []
        t = 0.
        while t <= time:
            t_values.append(t)
            v = self.find_v(t)
            self.v_values.append(v)
            h = self.find_y(t)
            self.h_values.append(h)
            t += 0.5
        return t_values
