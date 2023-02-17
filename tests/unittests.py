import unittest, os, sys
import iou_utils

class TestStringMethods(unittest.TestCase):
    def test_iou(self):
        # Import IoU calc function
        from iou_utils import iou

        print("\n[Test] Testing IoU calculation")

        # Boxes not intersecting
        box1 = [2, 2, 2, 2]
        box2 = [7, 4, 2, 4]
        outcome = iou(box1, box2)
        print("Case 0: Expected outcome: 0,\tOutcome: ")
        if outcome != 0: self.fail("Case 0: Failed due to unexpected outcome")

        # Box2 intersecting with box1
        box1 = [2, 2, 3, 1]
        box2 = [3, 3, 1, 2]
        outcome = iou(box1, box2)
        print("Case 1: Expected outcome: 0.5,\tOutcome: ", outcome)
        if outcome != 0.5: self.fail("Case 1: Failed due to unexpected outcome")

        # Box2's left side same as box1's left side
        box1 = [2, 2, 3, 1]
        box2 = [1, 3, 1, 2]
        outcome = iou(box1, box2)
        print("Case 2: Expected outcome: 0.5,\tOutcome: ", outcome)
        if outcome != 0.5: self.fail("Case 2: Failed due to unexpected outcome")

        # Box2 inside box1
        box1 = [2, 2, 7, 5]
        box2 = [2.5, 2.5, 1, 2]
        outcome = iou(box1, box2)
        print("Case 3: Expected outcome: 2,\tOutcome: ", outcome)
        if outcome != 2: self.fail("Case 3: Failed due to unexpected outcome")

        # Box1 inside box2
        box1 = [2.5, 2.5, 1, 2]
        box2 = [2, 2, 7, 5]
        outcome = iou(box1, box2)
        print("Case 4: Expected outcome: 2,\tOutcome: ", outcome)
        if outcome != 2: self.fail("Case 4: Failed due to unexpected outcome")

    def test_nmax(self):
        # Import nmax suppression calc function
        from iou_utils import nmax

        print("\n[Test] Testing nmax suppression")

        # Basic funcionality
        box1 = [0.9, 3, 2, 4, 2, 1]
        box2 = [0.5, 2.5, 2, 2, 3, 1]
        box3 = [0.3, 2.75, 2, 3, 2, 1]
        outcome = nmax([box1, box2, box3])
        print(f"Case 0: Expected outcome: [[0.9, 3, 2, 4, 2, 1]],\tOutcome: {outcome}")
        if outcome != [[0.9, 3, 2, 4, 2, 1]]: self.fail("Case 0: Failed due to unexpected outcome")

        # IoU threshold
        box1 = [0.3, 3, 2, 4, 2, 1]
        box2 = [0.5, 12.5, 2, 2, 3, 1]
        box3 = [0.4, 2.75, 2, 3, 2, 1]
        outcome = nmax([box1, box2, box3])
        print(f"Case 1: Expected outcome: [[0.5, 12.5, 2, 2, 3, 1],..],\tOutcome: {outcome}")
        if outcome != [[0.5, 12.5, 2, 2, 3, 1], [0.4, 2.75, 2, 3, 2, 1]]: self.fail("Case 1: Failed due to unexpected outcome")

        # Differentiation between classes
        box1 = [0.9, 3, 2, 4, 2, 1]
        box2 = [0.5, 2.5, 2, 2, 3, 1]
        box3 = [0.7, 2.75, 2, 3, 2, 2]
        outcome = nmax([box1, box2, box3])
        print(f"Case 2: Expected outcome: [[0.9, 3, 2, 4, 2, 1],..],\tOutcome: {outcome}")
        if outcome != [[0.9, 3, 2, 4, 2, 1], [0.7, 2.75, 2, 3, 2, 2]]: self.fail("Case 2: Failed due to unexpected outcome")


if __name__ == '__main__':
    # Run unittests
    unittest.main()