import random, math
from matplotlib import pyplot as plt
from matplotlib import animation

from bubble_sort import bubble_sort as sorting_algorithm


NUMBER_OF_ELEMENTS = 50
SUBPLOTS_PER_ROW = 3
SUBPLOTS_PER_COLUMN = 2
NUMBER_OF_SUBPLOTS = SUBPLOTS_PER_ROW * SUBPLOTS_PER_COLUMN
TIME_BETWEEN_FRAMES = 1  # min 1

random.seed(1)


class MyList(list[int]):
    def __init__(self, l):
        super().__init__(l)
        self.initial_list = l
        self.intermediate_states = [self[:]]

    def __setitem__(self, idx, value):
        super().__setitem__(idx, value)
        if set(self) == set(self.initial_list):
            self.intermediate_states.append(self[:])


def compare(arrays):
    fix, axs = plt.subplots(SUBPLOTS_PER_COLUMN, SUBPLOTS_PER_ROW)
    for i in range(NUMBER_OF_SUBPLOTS):
        axs[i // SUBPLOTS_PER_ROW, i % SUBPLOTS_PER_ROW].bar(range(len(l)), arrays[int((len(arrays) - 1) / (NUMBER_OF_SUBPLOTS - 1) * i)], width=1)
        axs[i // SUBPLOTS_PER_ROW, i % SUBPLOTS_PER_ROW].set_title(f"{i / (NUMBER_OF_SUBPLOTS - 1) * 100:.0f}%")
    plt.show()


def animate(arrays):
    fig = plt.figure()
    bar = plt.bar(range(len(arrays[0])), arrays[0], width=1)
    plt.ylim(0, max(arrays[0]))

    def _animate(arr):
        for i, b in enumerate(bar):
            if b.get_height() != arr[i]:
                b.set_color('r')
                b.set_height(arr[i])
            else:
                b.set_color('C0')
        return bar

    anim = animation.FuncAnimation(fig, _animate, frames=arrays, interval=TIME_BETWEEN_FRAMES, blit=False, repeat=False)
    plt.show()


if __name__ == "__main__":
    l = list(range(1, NUMBER_OF_ELEMENTS))
    random.shuffle(l)
    l = MyList(l)

    sorting_algorithm(l)

    compare(l.intermediate_states)
    animate(l.intermediate_states)