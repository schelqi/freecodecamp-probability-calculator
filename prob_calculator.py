import copy
import random


# Consider using the modules imported above.

class Hat:

    def __init__(self, **balls):
        self.contents = list()
        for color, frequency in balls.items():
            self.contents.extend([color] * frequency)

    def draw(self, number_of_balls):

        random_draw = list()
        for i in range(number_of_balls):
            try:
                ball = random.choice(self.contents)
                random_draw.append(ball)
                self.contents.remove(ball)
            except IndexError:
                break
        return random_draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match = 0
    expected_match = list()
    for k, v in expected_balls.items():
        expected_match.extend([k] * v)

    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        random_draw = copy_hat.draw(num_balls_drawn)
        test = True
        for k,v in expected_balls.items():
            if random_draw.count(k) < v:
                test=False
                break

        if test:
            match += 1

    return match / num_experiments
