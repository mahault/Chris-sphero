from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
import time

toy = scanner.find_toy()

with SpheroEduAPI(toy) as bolt:
    print("Hello, world from Sphero BOLT!")

    bolt.set_main_led(Color(0, 255, 0))  # ✅ NOT a tuple

    bolt.roll(speed=50, heading=0)
    time.sleep(2)
    bolt.stop()
