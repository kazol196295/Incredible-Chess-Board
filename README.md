# Peripheral Project

This is a university project for the peripheral course of CSE.

## Overview

This project involves an Arduino-based system that uses various components such as a servo motor, ultrasonic sensor, and load cell. The system performs actions based on distance measurements from the ultrasonic sensor and weight measurements from the load cell.

## Components

- **Servo Motor**: Used to perform actions based on sensor input.
- **Ultrasonic Sensor**: Measures distance to detect objects.
- **Load Cell**: Measures weight to trigger actions based on weight thresholds.

## Features

- **Distance Measurement**: Uses an ultrasonic sensor to measure distance and trigger the servo motor when an object is within 20 cm.
- **Weight Measurement**: Uses a load cell to measure weight and trigger actions if the weight exceeds 400 grams.
- **Calibration and Storage**: Includes functionalities for calibration and storing calibration values in EEPROM.

## Code Explanation

The main logic of the project is implemented in `main.ino`. The `setup` function initializes the components, and the `loop` function continuously reads the sensor data and triggers the `pingpong` function based on the sensor readings.

## How to Use

1. Upload the `main.ino` file to your Arduino board.
2. Connect the components as described in the code comments.
3. Run the project and observe the actions based on distance and weight measurements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the university for providing the resources and guidance for this project.
