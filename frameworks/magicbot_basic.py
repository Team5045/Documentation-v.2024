import wpilib
import phoenix5
from magicbot import MagicRobot
from phoenix5 import NeutralMode

#NOTE: Download and Installs for RoboRIO
# make sure imaging is up to date
'''
python -m robotpy installer download python
python -m robotpy installer install python
python -m robotpy installer download robotpy[phoenix5]
python -m robotpy installer install robotpy[phoenix5]
python -m robotpy installer download robotpy[rev]
python -m robotpy installer install robotpy[rev]

--------------- PERSONAL INSTALLS --------------------

pip install robotpy[phoenix5]
pip install robotpy[rev]
'''
# NOTE: Deployment instructions
'''
1. cd robot
2. python robot.py deploy --skip-tests (OPTION 1, with CD)
3. python robot/robot.py deploy --skip-tests (OPTION 2, without CD)
'''

BRAKE_MODE = NeutralMode(2)
COAST_MODE = NeutralMode(1)
# NOTE: Constants would go here, for example as above, the brake mode constants
class MyRobot(MagicRobot):


    def createObjects(self):
        '''Initializing sensors and motors would go here, as well as things like modules or DT systems'''
        pass

    def autonomousInit(self):
        '''Any functions that need to be run once when auton is enabled would go here'''
        pass
    
    def teleopInit(self):
        '''Any functions that need to be run once when teleop is enabled would go here'''
        pass

    def teleopPeriodic(self):
        '''Drivetrain and other teleop functions would go here'''
        pass


if __name__ == "__main__": # This block of code will actually run the robot code
    wpilib.run(MyRobot)   # So normally this file would need to be named "robot.py"