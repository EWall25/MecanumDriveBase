import wpilib
import wpilib.drive

class Robot(wpilib.TimedRobot):
    
    def robotInit(self) -> None:
        fl_motor = wpilib.Spark(0)
        rl_motor = wpilib.Spark(1)
        fr_motor = wpilib.Spark(2)
        rr_motor = wpilib.Spark(3)
        self.drive = wpilib.drive.MecanumDrive(fl_motor, rl_motor, fr_motor, rr_motor)
        
        self.stick = wpilib.XboxController(0)

    def teleopPeriodic(self) -> None:
        # Get controller inputs
        fwd = -self.stick.getLeftY()
        right = self.stick.getLeftX()
        rot = self.stick.getRightX()

        # Move the robot chassis
        self.drive.driveCartesian(fwd, right, rot)
