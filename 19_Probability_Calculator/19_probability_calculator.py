import copy
import random
from collections import Counter

# ===============================================


class Hat:
    def __init__(self, **args):
        self.contents = []
        for color, n in args.items():
            self.contents.extend([color for _ in range(n)])

    # -------------------------------------------

    def draw(self, number_of_balls):
        num_to_draw = min(number_of_balls, len(self.contents))

        drawn_balls = random.sample(self.contents, num_to_draw)

        for ball in drawn_balls:
            self.contents.remove(ball)

        return drawn_balls


# ===============================================


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)

        drawn_balls = hat_copy.draw(num_balls_drawn)

        fail = any(
            Counter(drawn_balls)[color] < count
            for color, count in expected_balls.items()
        )

        if not fail:
            successful_experiments += 1

    return successful_experiments / num_experiments

# ===============================================


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)

print(probability)
