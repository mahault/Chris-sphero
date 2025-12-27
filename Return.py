import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

def run_segment(bolt, speed, heading, seconds):
    bolt.set_heading(int(heading) % 360)
    bolt.set_speed(int(speed))
    time.sleep(float(seconds))
    bolt.set_speed(0)
    time.sleep(0.15)

toy = scanner.find_toy()

with SpheroEduAPI(toy) as bolt:
    speed = 20
    side_seconds = 2.5
    heading = 0

    bolt.set_main_led(Color(0, 255, 0))

    # Build the triangle as a list of segments
    path = []
    heading = 0
    for _ in range(3):
        path.append((speed, heading, side_seconds))
        heading = (heading + 120) % 360

    # Execute triangle
    for spd, hdg, secs in path:
        run_segment(bolt, spd, hdg, secs)

    # Retrace back to start
    bolt.set_main_led(Color(255, 0, 0))
    for spd, hdg, secs in reversed(path):
        run_segment(bolt, spd, (hdg + 180) % 360, secs)

    bolt.set_main_led(Color(0, 0, 255))

def circle(bolt, speed=35, step_deg=6, step_time=0.05, laps=1, start_heading=0):
    """
    Approximate a circle by sweeping the heading while moving.

    speed: 0–255 (try 20–50 indoors)
    step_deg: heading increment per step (smaller = smoother, slower)
    step_time: seconds to hold each heading (smaller = smoother)
    laps: number of full 360° revolutions
    start_heading: initial heading angle
    """
    heading = int(start_heading) % 360
    bolt.set_speed(int(speed))

    steps_per_lap = max(1, int(360 / step_deg))
    total_steps = steps_per_lap * int(laps)

    for _ in range(total_steps):
        bolt.set_heading(heading)
        time.sleep(float(step_time))
        heading = (heading + int(step_deg)) % 360

    bolt.set_speed(0)

toy = scanner.find_toy()

with SpheroEduAPI(toy) as bolt:
    bolt.set_main_led(Color(0, 255, 255))  # cyan
    circle(bolt, speed=30, step_deg=5, step_time=0.06, laps=2, start_heading=0)
    bolt.set_main_led(Color(0, 0, 255))    # blue

import time

def spin_in_place(bolt, spins=2, step_deg=10, step_time=0.03):
    """
    spins: number of full 360° rotations
    step_deg: heading increment per step (smaller = smoother)
    step_time: delay per step (smaller = faster)
    """
    heading = 0
    steps = int((360 / step_deg) * spins)

    bolt.set_speed(10)  # very low speed to avoid translation

    for _ in range(steps):
        bolt.set_heading(heading)
        time.sleep(step_time)
        heading = (heading + step_deg) % 360

    bolt.set_speed(0)
