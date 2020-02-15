__author__ = "Luis Manuel Angueira Blanco"
__email__ = "luis.manuel.angueira@gmail.com"

ORIENTATION = [
    'N',    # North
    'E',    # East
    'S',    # South
    'W'     # West
]


class Drone:
    """
    Drone with following movements:
    - Forward
    - Rotate Clockwise
    - Rotate Counterclockwise
    """
    def __init__(self, position_x, position_y, orientation):
        self.position_x = position_x
        self.position_y = position_y
        self.orientation = orientation

    def move(self, movement):
        """
        Moves the Drone
        :param movement: Movement to do
        :return:
        """
        if movement == "M":
            self._move_forward()
        elif movement == "R":
            self._rotate_clockwise()
        elif movement == "R":
            self._rotate_counterclockwise()

    def _move_forward(self):
        """
        Moves the Drone forward
        """
        if self.orientation == "N":
            self.position_y += 1
        elif self.orientation == "E":
            self.position_x += 1
        elif self.orientation == "S":
            self.position_y -= 1
        elif self.orientation == "W":
            self.position_x -= 1

    def _rotate_counterclockwise(self):
        """
        Rotates the Drone - Counterclockwise
        :return:
        """
        self._rotate(-1)

    def _rotate_clockwise(self):
        """
        Rotates the Drone - Clockwise
        :return:
        """
        self._rotate(1)

    def _rotate(self, positions):
        """
        Rotates the Drone n positions
        :param positions: Number of positions to rotate, positive (clockwise) or negative (counterclockwise)
        :return:
        """
        self.orientation = ORIENTATION[(ORIENTATION.index(self.orientation) + positions + self.orientation_positions)
                                       % self.orientation_positions]

    @property
    def current_orientation_index(self):
        return ORIENTATION.index(self.orientation)

    @property
    def orientation_positions(self):
        return len(ORIENTATION)
