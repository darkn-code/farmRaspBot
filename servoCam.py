from PCA9685 import PCA9685
import time

def main(motor,angulo):

	pwm = PCA9685()
	pwm.setPWMFreq(50)

	pwm.setRotationAngle(motor,angulo)
	time.sleep(0.1)

	pwm.exit_PCA9685()

if __name__ == '__main__':
	motor = int(input("Que motor desea mover [0] o [1]? "))
	angulo = int(input("Que angulo desea (0-180)? "))
	main(motor,angulo)
