from math import atan2

def calc_angle(line):
	"this function accepts line output of hough line transform and returns the skew angle"
	
	angle = 0
	for i in range(1, line.shape[0]):
		angle = angle + atan2((line[i][0][3] - line[i][0][1]), (line[i][0][2] - line[i][0][0]))
		
	angle = angle/line.shape[0]
	print "Angle Calculated"
	return angle
	
