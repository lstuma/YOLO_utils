# YOLO_utils
A few utilities for the YOLO project implemented in C for extra speed

## How to use
```python
# Import Module
import yolo_utils

# Declare boxes for IoU Calculation
box1 = [2, 2, 3, 4]
box2 = [2, 3, 3, 4]

# Calculate Intersection over Union
intersec = iou(box1, box2)
```