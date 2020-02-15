__author__ = "Luis Manuel Angueira Blanco"
__email__ = "luis.manuel.angueira@gmail.com"

from unittest import TestCase
from drone.drone import Drone


class TestDrone(TestCase):

    def test_move_forward_N(self):
        drone = Drone(0, 0, "N")
        drone.move("M")
        self.assertEqual(1, drone.position_x)

    def test_move_forward_E(self):
        drone = Drone(0, 0, "E")
        drone.move("M")
        self.assertEqual(1, drone.position_y)

    def test_move_L(self):
        drone = Drone(0, 0, "N")
        drone.move("L")
        self.assertEqual("W", drone.orientation)

    def test_move_R(self):
        drone = Drone(0, 0, "N")
        drone.move("R")
        self.assertEqual("E", drone.orientation)

    def test_rotate_clockwise_N(self):
        drone = Drone(0, 0, "N")
        drone._rotate_clockwise()
        self.assertEqual("E", drone.orientation)

    def test_rotate_clockwise_E(self):
        drone = Drone(0, 0, "E")
        drone._rotate_clockwise()
        self.assertEqual("S", drone.orientation)

    def test_rotate_clockwise_S(self):
        drone = Drone(0, 0, "S")
        drone._rotate_clockwise()
        self.assertEqual("W", drone.orientation)

    def test_rotate_clockwise_W(self):
        drone = Drone(0, 0, "W")
        drone._rotate_clockwise()
        self.assertEqual("N", drone.orientation)

    def test_rotate_counterclockwise_N(self):
        drone = Drone(0, 0, "N")
        drone._rotate_counterclockwise()
        self.assertEqual("W", drone.orientation)

    def test_rotate_counterclockwise_E(self):
        drone = Drone(0, 0, "E")
        drone._rotate_counterclockwise()
        self.assertEqual("N", drone.orientation)

    def test_rotate_counterclockwise_S(self):
        drone = Drone(0, 0, "S")
        drone._rotate_counterclockwise()
        self.assertEqual("E", drone.orientation)

    def test_rotate_counterclockwise_W(self):
        drone = Drone(0, 0, "W")
        drone._rotate_counterclockwise()
        self.assertEqual("S", drone.orientation)

    def test_move_forward_N(self):
        drone = Drone(2, 2, "N")
        drone._move_forward()
        self.assertEqual(3, drone.position_y)

    def test_move_forward_E(self):
        drone = Drone(2, 2, "E")
        drone._move_forward()
        self.assertEqual(3, drone.position_x)

    def test_move_forward_S(self):
        drone = Drone(2, 2, "S")
        drone._move_forward()
        self.assertEqual(1, drone.position_y)

    def test_move_forward_W(self):
        drone = Drone(2, 2, "W")
        drone._move_forward()
        self.assertEqual(1, drone.position_x)

    def test_current_position_incorrect(self):
        drone = Drone(2, 2, "W")
        self.assertNotEqual("22W", drone.current_position)

    def test_move_drone_without_area_simple_movement(self):
        drone = Drone(3, 3, "E")
        instructions = "L"
        self.assertEqual("3 3 N", drone.move_with_instructions(instructions))

    def test_move_drone_without_area_middle(self):
        drone = Drone(3, 3, "E")
        instructions = "MMRMMRMRRM"
        self.assertEqual("5 1 E", drone.move_with_instructions(instructions))

    def test_move_drone_without_area_complex(self):
        drone = Drone(1, 2, "N")
        instructions = "LM LM LM LM ML ML ML ML MM"
        self.assertEqual("1 4 N", drone.move_with_instructions(instructions))