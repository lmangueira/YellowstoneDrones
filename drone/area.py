class Area:

    def __init__(self, height: int, width: int):
        """
        Area init
        :param height: Height - must be greater than zero
        :param width: Width - must be greater than zero
        """
        if height < 1:
            raise ValueError(f"Area height must be greater than zero. Value received {height}")
        if width < 1:
            raise ValueError(f"Area width must be greater than zero. Value received {width}")

        self.height = height
        self.width = width

    def valid_movement(self, position_x: int, position_y: int):
        """
        Checks whether a movement is valid or not.
        A valid movement is the one in the bounds.
        :param position_x: Movement final position - X-Axis
        :param position_y: Movement final position - Y-Axis
        :return:
        """
        return self.width >= position_x and self.height >= position_y
