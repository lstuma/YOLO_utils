#include <stdlib.h>
#include <stdio.h>
#include <math.h>

double calc_iou(double* box1, double* box2)
{
	// Array type conversion + Conversion to midpoint anchor type
	double boxes[2][4];

    for(int i = 0; i < 2; i++) {
        double* box = i==0?box1:box2;
        // Calculate upper left corner
        boxes[i][0] = box[0] - box[2]/2.0;
        boxes[i][1] = box[1] - box[3]/2.0;
        // Calculate lower right corner
        boxes[i][2] = boxes[i][0] + box[2];
        boxes[i][3] = boxes[i][1] + box[3];
    }

	// Calculate IoU
	double iou_dim[2] = {0, 0};
    printf("\nIOU TESTO");
	for(int i=0; i < 2; i++) {
		int j = i+2;

		// Check cases

		// box1 inside box2
        if(boxes[0][i] >= boxes[1][i] && boxes[0][j] <= boxes[1][j])
            iou_dim[i] = boxes[0][j]-boxes[0][i];
        // box2 inside box1
        else if(boxes[1][i] >= boxes[0][i] && boxes[1][j] <= boxes[0][j])
            iou_dim[i] = boxes[1][j]-boxes[1][i];
        // box1 has left side in box2
        else if(boxes[1][i] <= boxes[0][i] && boxes[0][i] <= boxes[1][j])
            iou_dim[i] = boxes[2][j]-boxes[1][i];
        // box2 has left side in box1
        else if(boxes[0][i] <= boxes[1][i] && boxes[1][i] <= boxes[0][j])
            iou_dim[i] = boxes[1][i]-boxes[0][j];
        // boxes do not intersect
        }

    double iou = fabs(iou_dim[0] * iou_dim[1]);
	return iou;
}