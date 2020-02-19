from drone.drone import Drone
from drone.area import Area
import os


class Overlord:

    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__)) + '/INPUT'
        self.instructions = None

    def take_instructions(self):
        input_path: str = str(input('Enter the full file path where we can get your desires\n'))
        if input_path is not None and not '.':
            self.path = input_path

        self.instructions = open(self.path, "r")

    def move_drones(self):
        if self.instructions is None:
            assert ValueError('There are no instructions for my Drones. Please ask for them')

        instructions = [x.replace('\n', '') for x in self.instructions]
        (height, width) = instructions[0].split(' ')
        area = Area(int(height), int(width))

        movements = instructions[1:]
        drone = None
        for i in range(len(movements)):
            if i % 2 == 0:
                (position_x, position_y, orientation) = movements[i].split(' ')
                drone = Drone(int(position_x), int(position_y), orientation, area)
            else:
                yield drone.move_with_instructions(movements[i])


if __name__ == '__main__':
    print('Welcome to the Yellowstone Park')
    print("I'm the Drone overlord. Let's have some fun")

    overlord = Overlord()
    overlord.take_instructions()
    movements = overlord.move_drones()
    if movements is not None:
        print('So here are the final positions of the minions:')
        for movement in movements:
            print(movement)
    else:
        print('It seems the minions are sleeping...')

    print('')
    print('We already finished... Hail to the Drone!')

