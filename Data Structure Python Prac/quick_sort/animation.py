import math
import random
from collections import UserList
from typing import List

from matplotlib import animation
from matplotlib import pyplot as plt

from quick_sort import quick_sort as sorting_algorithm

NUMBER_OF_ELEMENTS = 100
SUBPLOTS_PER_ROW = 3
SUBPLOTS_PER_COLUMN = 2
NUMBER_OF_SUBPLOTS = SUBPLOTS_PER_ROW * SUBPLOTS_PER_COLUMN
TIME_BETWEEN_FRAMES = 100  # min 1

random.seed(1)


class TrackingList(UserList[int]):
    """
    A list class that keeps track of changes to visualize sorting.

    `collections.UserList` provides a convenient wrapper around list objects.
    The underlying list is stored in `collections.UserList.data`.
    """

    def __init__(self, l):
        super().__init__(l)
        self.initial_list = l
        self.intermediate_states: List[List[int]] = [self.data[:]]

    def __setitem__(self, idx, value) -> None:
        """
        Changes the element on position `idx` to `value` and saves the new state
        of the list in `intermediate_states`.

        To avoid intermediate states in which some elements MIG th appear
        multiple times and some don't appear at all, we require the initial list
        to have only unique elements. This way we can check if all elements are
        present and thus know if we have a "valid" intermediate state.

        This version does not track if the ordering is changed. If the ordering
        after the change is the same as before we still have a valid new state.

        Args:
            idx: The position of the element to overwrite.
            value: The value of the new element.
        """
        super().__setitem__(idx, value)
        if set(self) == set(self.initial_list):
            self.intermediate_states.append(self.data[:])


def compare(intermediate_states: List[List[int]]):
    """Plots `NUMBER_OF_SUBPLOTS` intermediate states of the sorting process."""
    fix, axs = plt.subplots(SUBPLOTS_PER_COLUMN, SUBPLOTS_PER_ROW)
    for i in range(NUMBER_OF_SUBPLOTS):
        axs[i // SUBPLOTS_PER_ROW, i % SUBPLOTS_PER_ROW].bar(
            range(len(l)),
            intermediate_states[int((len(intermediate_states) - 1) / (NUMBER_OF_SUBPLOTS - 1) * i)],
            width=1,
        )
        axs[i // SUBPLOTS_PER_ROW, i % SUBPLOTS_PER_ROW].set_title(f"{i / (NUMBER_OF_SUBPLOTS - 1) * 100:.0f}%")
    plt.show()


def animate(intermediate_states: List[List[int]]):
    """Animates the sorting process. Colors in the moved items."""
    fig = plt.figure()
    bar = plt.bar(range(len(intermediate_states[0])), intermediate_states[0], width=1)
    plt.ylim(0, max(intermediate_states[0]))

    def _animate(arr):
        for i, b in enumerate(bar):
            if b.get_height() != arr[i]:
                b.set_color("r")
                b.set_height(arr[i])
            else:
                b.set_color("C0")
        return bar

    anim = animation.FuncAnimation(
        fig, _animate, frames=intermediate_states, interval=TIME_BETWEEN_FRAMES, blit=False, repeat=False
    )
    plt.show()


if __name__ == "__main__":
    # The list that will be sorted must have only unique items.
    l = list(range(1, NUMBER_OF_ELEMENTS))
    random.shuffle(l)
    tracking_list = TrackingList(l)

    sorting_algorithm(tracking_list)

    compare(tracking_list.intermediate_states)
    animate(tracking_list.intermediate_states)
