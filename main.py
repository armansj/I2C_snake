import time
import random
from machine import Pin, ADC
from I2C_LCD import I2CLcd
from machine import I2C

i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
devices = i2c.scan()

joystick_x = ADC(Pin(26))
joystick_y = ADC(Pin(27))

if devices != []:
    lcd = I2CLcd(i2c, devices[0], 2, 16)

    snake = [(0, 0)]
    snake_dir = (1, 0)
    food = (random.randint(0, 15), random.randint(0, 1))
    game_over = False

    def display_game():
        lcd.clear()
        for segment in snake:
            lcd.move_to(segment[0], segment[1])
            lcd.putchar('_')
        lcd.move_to(food[0], food[1])
        lcd.putchar('X')

    def move_snake():
        global food, game_over

        head_x, head_y = snake[0]

        new_head_x = head_x + snake_dir[0]
        new_head_y = head_y + snake_dir[1]

        if new_head_x < 0:
            new_head_x = 15
        elif new_head_x > 15:
            new_head_x = 0

        if new_head_y < 0:
            new_head_y = 1
        elif new_head_y > 1:
            new_head_y = 0

        if (new_head_x, new_head_y) in snake:
            game_over = True
            return

        snake.insert(0, (new_head_x, new_head_y))

        if (new_head_x, new_head_y) == food:
            while food in snake:
                food = (random.randint(0, 15), random.randint(0, 1))
        else:
            snake.pop()

    def reset_game():
        global snake, snake_dir, food, game_over
        snake = [(0, 0)]
        snake_dir = (1, 0)
        food = (random.randint(0, 15), random.randint(0, 1))
        game_over = False

    while True:
        joystick_x_value = joystick_x.read_u16()
        joystick_y_value = joystick_y.read_u16()

        deadzone_min = 20000
        deadzone_max = 40000

        if joystick_x_value > deadzone_max and snake_dir != (-1, 0):  # Move right
            snake_dir = (1, 0)
        elif joystick_x_value < deadzone_min and snake_dir != (1, 0):  # Move left
            snake_dir = (-1, 0)
        elif joystick_y_value > deadzone_max and snake_dir != (0, -1):  # Move down
            snake_dir = (0, 1)
        elif joystick_y_value < deadzone_min and snake_dir != (0, 1):  # Move up
            snake_dir = (0, -1)

        if not game_over:
            move_snake()
            display_game()
        else:
            lcd.clear()
            lcd.move_to(0, 0)
            lcd.putstr("Game Over!")
            time.sleep(2)
            reset_game()

        time.sleep(0.3)

