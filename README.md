Snake Game on I2C LCD with Joystick Control
This project implements a simple snake game on a 16x2 I2C LCD screen, controlled by a joystick connected to a microcontroller. The snake moves in four directions (left, right, up, down) and wraps around the screen. The game ends when the snake collides with itself. A joystick is used to control the snake's movement, and the game restarts automatically after a game over.

Features:
Snake Game: A classic snake game where the snake grows as it eats food.
Joystick Control: A single joystick is used to move the snake up, down, left, and right.
Wrap-around: The snake reappears on the opposite side when it moves off the screen.
Game Restart: The game restarts automatically when the snake hits itself.
Hardware Requirements:
Raspberry Pi Pico (or any compatible microcontroller)
I2C LCD 16x2 Display
Joystick Module
Pinout:
VCC: 3.3V or 5V (depending on your microcontroller)
GND: Ground
X-Axis Output (VRx): Connected to ADC pin (e.g., ADC0)
Y-Axis Output (VRy): Connected to ADC pin (e.g., ADC1)
Pin Connections:
I2C LCD Connections:
SDA (I2C Data): Connect to Pin 14 on the Raspberry Pi Pico.
SCL (I2C Clock): Connect to Pin 15 on the Raspberry Pi Pico.
Joystick Connections:
VCC: 3.3V or 5V (based on your microcontroller)
GND: Ground
VRx (X-axis output): ADC Pin 26
VRy (Y-axis output): ADC Pin 27
