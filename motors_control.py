import time

def set_motor_speed(left_speed, right_speed):
    print(f"[MOTORS] Left motor speed: {left_speed}, Right motor speed: {right_speed}")

def smooth_speed_transition(start, end, steps=5):
    print(f"Transitioning from {start} to {end} in {steps} steps:")
    for i in range(steps + 1):
        speed = start + (end - start) * i / steps
        set_motor_speed(speed, speed)
        time.sleep(0.5)

# Пример запуска
if __name__ == "__main__":
    set_motor_speed(0, 0)
    smooth_speed_transition(0, 100)
    set_motor_speed(0, 0)
def manual_control():
    try:
        while True:
            left = int(input("Left speed: "))
            right = int(input("Right speed: "))
            set_motor_speed(left, right)
    except KeyboardInterrupt:
        print("Manual control stopped.")

# запуск
if __name__ == "__main__":
    choice = input("Smooth (s) or Manual (m)? ")
    if choice.lower() == "s":
        smooth_speed_transition(0, 100)
    else:
        manual_control()