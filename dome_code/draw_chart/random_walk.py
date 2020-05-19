from random import choice

class RandomWalk():
    """create a radom number"""
    def __init__(self,num_points = 5000):
        """initialize attribute of random_walk"""
        self.num_points = num_points

        # regulate all random start at (0,0)
        self.x_value = [0]
        self.y_value = [0]


    def fill_walk(self):
        """calculate all points involve in rand_walk"""
        # random walk until list is long enough
        while len(self.x_value) < self.num_points:
            # decide direction and step of the random walk list
            x_step = self.get_step()
            y_step = self.get_step()

            # refuse Step in place
            if x_step  == 0 and y_step == 0:
                continue

            # calculate value of next point
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)


    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance
        return step