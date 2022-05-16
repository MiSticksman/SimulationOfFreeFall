from context import g


class UpperFall:

    def __init__(self, h0, v0):
        self.h0 = h0
        self.v0 = v0
        self.h_values = []
        self.v_values = []

    def find_time(self):
        t = 2 * self.v0 / g
        return t

    def find_v(self, t):
        v = self.v0 - g * t
        return v

    def find_y(self, t):
        h = self.h0 + self.v0 * t - g * (t ** 2) / 2
        return h

    def calc_t_values(self):
        time = self.find_time()
        t_values = []
        t = 0
        while t <= time:
            t_values.append(t)
            v = self.find_v(t)
            self.v_values.append(v)
            h = self.find_y(t)
            self.h_values.append(h)
            t += 0.5
        print(self.h_values)
        print(t_values)
        return t_values
