import unittest, os, sys
import yolo_utils

class TestStringMethods(unittest.TestCase):
    def test_iou(self):
        # Import IoU calc function
        from yolo_utils import iou

        print("\n[Test] Testing IoU calculation")

        # Boxes not intersecting
        box1 = [2, 2, 2, 2]
        box2 = [7, 4, 2, 4]
        outcome = iou(box1, box2)
        print("Case 0: Expected outcome: 0,\tOutcome: ", outcome)
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
        try: outcome = iou(box1, box2)
        except Exception as e: print(e);
        print("Case 3: Expected outcome: 2,\tOutcome: ", outcome)
        if outcome != 2: self.fail("Case 3: Failed due to unexpected outcome")

        # Box1 inside box2
        box1 = [2.5, 2.5, 1, 2]
        box2 = [2, 2, 7, 5]
        outcome = iou(box1, box2)
        print("Case 4: Expected outcome: 2,\tOutcome: ", outcome)
        if outcome != 2: self.fail("Case 4: Failed due to unexpected outcome")

if __name__ == '__main__':
    # Run unittests
    unittest.main()