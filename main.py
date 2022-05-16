from matplotlib import pyplot as plt


simulation = input("Free fall - input 1, of the body or movement of a body thrown vertically upwards - 2: ")
h0 = float(input("Initial height (in m): "))

fall = None
if simulation == "1":
    from free_fall import FreeFall
    fall = FreeFall(h0)
if simulation == "2":
    from upper import UpperFall
    v0 = float(input("Initial speed (in m/s): "))
    fall = UpperFall(h0, v0)


if __name__ == '__main__':

    fig = plt.figure("FreeFallSimulation", figsize=(10, 10))
    x = fall.calc_t_values()
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.set_title("the dependence of height on time on ")
    ax1.set_xlabel('time, s')
    ax1.set_ylabel('height, m')
    ax1.grid()
    ax1.plot(x, fall.h_values)

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.set_title("the dependence of speed on time on ")
    ax2.set_xlabel('time, s')
    ax2.set_ylabel("speed, m/s")
    ax2.grid()
    ax2.plot(x, fall.v_values)

    plt.show()
