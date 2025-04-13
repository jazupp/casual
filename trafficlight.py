import time
from colorama import init, Fore, Style

class TrafficLightLamp:
    def __init__(self):
        # Initialize all lamp states to False (off)
        self.Red = False
        self.Yellow = False
        self.Green = False
        self.LeftTurnRed = False
        self.LeftTurnYellow = False
        self.LeftTurnGreen = False
        self.RightTurnRed = False
        self.RightTurnYellow = False
        self.RightTurnGreen = False

    def set_state(self, red, yellow, green, left_turn_red=False, left_turn_yellow=False, left_turn_green=False, right_turn_red=False, right_turn_yellow=False, right_turn_green=False):
        # Set the state of the traffic light lamps
        self.Red = red
        self.Yellow = yellow
        self.Green = green
        self.LeftTurnRed = left_turn_red
        self.LeftTurnYellow = left_turn_yellow
        self.LeftTurnGreen = left_turn_green
        self.RightTurnRed = right_turn_red
        self.RightTurnYellow = right_turn_yellow
        self.RightTurnGreen = right_turn_green

    def display(self):
        # Generate a string representation of the traffic light state
        state = ""

        # Left Turn Arrow
        if self.LeftTurnRed and self.LeftTurnYellow:
            state += f"{Fore.RED}←{Style.RESET_ALL}{Fore.YELLOW}←{Style.RESET_ALL}"
        elif self.LeftTurnRed:
            state += f"{Fore.RED}←{Style.RESET_ALL}"
        elif self.LeftTurnYellow:
            state += f"{Fore.YELLOW}←{Style.RESET_ALL}"
        elif self.LeftTurnGreen:
            state += f"{Fore.GREEN}←{Style.RESET_ALL}"
        else:
            state += "  "  # Space for alignment

        # Circle (Main Light)
        if self.Red and self.Yellow:
            state += f" {Fore.RED}●{Style.RESET_ALL}{Fore.YELLOW}●{Style.RESET_ALL} "
        elif self.Red:
            state += f" {Fore.RED}●{Style.RESET_ALL} "
        elif self.Yellow:
            state += f" {Fore.YELLOW}●{Style.RESET_ALL} "
        elif self.Green:
            state += f" {Fore.GREEN}●{Style.RESET_ALL} "
        else:
            state += "   "  # Space for alignment

        # Right Turn Arrow
        if self.RightTurnRed and self.RightTurnYellow:
            state += f"{Fore.RED}→{Style.RESET_ALL}{Fore.YELLOW}→{Style.RESET_ALL}"
        elif self.RightTurnRed:
            state += f"{Fore.RED}→{Style.RESET_ALL}"
        elif self.RightTurnYellow:
            state += f"{Fore.YELLOW}→{Style.RESET_ALL}"
        elif self.RightTurnGreen:
            state += f"{Fore.GREEN}→{Style.RESET_ALL}"
        else:
            state += "  "  # Space for alignment

        return state

class Direction:
    def __init__(self, name):
        # Initialize a direction with a name and a traffic light lamp
        self.name = name
        self.Lamp = TrafficLightLamp()

    def set_sequence(self, red, yellow, green, left_turn_red=False, left_turn_yellow=False, left_turn_green=False, right_turn_red=False, right_turn_yellow=False, right_turn_green=False):
        # Set the sequence of the traffic light for this direction
        self.Lamp.set_state(red, yellow, green, left_turn_red, left_turn_yellow, left_turn_green, right_turn_red, right_turn_yellow, right_turn_green)

    def display(self):
        # Display the traffic light state for this direction
        return self.Lamp.display()

class TrafficSystem:
    def __init__(self):
        # Initialize the traffic system with four directions
        self.directions = {
            "North": Direction("North"),
            "East": Direction("East"),
            "South": Direction("South"),
            "West": Direction("West")
        }

    def display_all(self):
        # Display the traffic light states for all directions
        print("\n" * 10)  # Clear the screen
        print("   North   ")
        print(f"     {self.directions['North'].display()}     ")
        print("West     East")
        print(f"{self.directions['West'].display()}       {self.directions['East'].display()}")
        print("   South   ")
        print(f"     {self.directions['South'].display()}     ")
        print(f"\nCurrent Step: {getattr(self, 'current_step', 'Unknown')}")

    def set_sequence_by_step(self, step):
        # Set the traffic light sequence based on the current step
        if not hasattr(self, 'startbit'):
            self.startbit = 0
        self.current_step = step

        if self.startbit == 0:
            if step == 10:
                # Initialize: All lamps off
                for direction in self.directions.values():
                    direction.set_sequence(False, False, False, True, False, False, True, False, False)
            elif step == 20:
                # Initialize all to red
                for direction in self.directions.values():
                    direction.set_sequence(True, False, False, True, False, False, True, False, False)
                self.startbit = 1
        elif step == 100:
            # All directions red
            for direction in self.directions.values():
                direction.set_sequence(True, False, False, True, False, False, True, False, False)
        elif step == 110:
            # North-South Red & Yellow, East-West Red
            self.directions["North"].set_sequence(True, True, False, True, False, False, True, True, False)
            self.directions["South"].set_sequence(True, True, False, True, False, False, True, True, False)
            self.directions["East"].set_sequence(True, False, False, True, False, False, True, False, False)
            self.directions["West"].set_sequence(True, False, False, True, False, False, True, False, False)
        elif step == 120:
            # North-South Green, East-West Red
            self.directions["North"].set_sequence(False, False, True, True, False, False, False, False, True)
            self.directions["South"].set_sequence(False, False, True, True, False, False, False, False, True)
            self.directions["East"].set_sequence(True, False, False, True, False, False, True, False, False)
            self.directions["West"].set_sequence(True, False, False, True, False, False, True, False, False)
        elif step == 130:
            # North-South Yellow, East-West Red
            self.directions["North"].set_sequence(False, True, False, True, False, False, False, True, False)
            self.directions["South"].set_sequence(False, True, False, True, False, False, False, True, False)
            self.directions["East"].set_sequence(True, False, False, True, False, False, True, False, False)
            self.directions["West"].set_sequence(True, False, False, True, False, False, True, False, False)
        elif step == 200:
            # All directions red
            for direction in self.directions.values():
                direction.set_sequence(True, False, False, True, False, False, True, False, False)
        elif step == 210:
            # North-South Red, East-West Red & Yellow
            self.directions["North"].set_sequence(True, False, False, True, False, False, True, False, False)
            self.directions["South"].set_sequence(True, False, False, True, False, False, True, False, False)
            self.directions["East"].set_sequence(True, True, False, True, False, False, True, True, False)
            self.directions["West"].set_sequence(True, True, False, True, False, False, True, True, False)
        elif step == 220:
            # North-South Red, East-West Green
            self.directions["North"].set_sequence(True, False, False, True, False, False, True, False, False)
            self.directions["South"].set_sequence(True, False, False, True, False, False, True, False, False)
            self.directions["East"].set_sequence(False, False, True, True, False, False, False, False, True)
            self.directions["West"].set_sequence(False, False, True, True, False, False, False, False, True)
        elif step == 230:
            # North-South Red, East-West Yellow
            self.directions["North"].set_sequence(True, False, False, True, False, False, True, False, False)
            self.directions["South"].set_sequence(True, False, False, True, False, False, True, False, False)
            self.directions["East"].set_sequence(False, True, False, True, False, False, False, True, False)
            self.directions["West"].set_sequence(False, True, False, True, False, False, False, True, False)
        elif step == 240:
            # All directions red
            for direction in self.directions.values():
                direction.set_sequence(True, False, False, True, False, False, True, False, False)
        elif step == 300:
            # North-South Left Turn Red & Yellow, East-West Right Turn Red & Yellow
            self.directions["North"].set_sequence(True, False, False, True, True, False, True, False, False)
            self.directions["South"].set_sequence(True, False, False, True, True, False, True, False, False)
            self.directions["East"].set_sequence(True, False, False, True, False, False, True, True, False)
            self.directions["West"].set_sequence(True, False, False, True, False, False, True, True, False)
        elif step == 310:
            # North-South Left Turn Green, East-West Right Turn Green
            self.directions["North"].set_sequence(True, False, False, False, False, True, True, False, False)
            self.directions["South"].set_sequence(True, False, False, False, False, True, True, False, False)
            self.directions["East"].set_sequence(True, False, False, True, False, False, False, False, True)
            self.directions["West"].set_sequence(True, False, False, True, False, False, False, False, True)
        elif step == 320:
            # North-South Left Turn Yellow, East-West Right Turn Yellow
            self.directions["North"].set_sequence(True, False, False, False, True, False, True, False, False)
            self.directions["South"].set_sequence(True, False, False, False, True, False, True, False, False)
            self.directions["East"].set_sequence(True, False, False, True, False, False, False, True, False)
            self.directions["West"].set_sequence(True, False, False, True, False, False, False, True, False)
        elif step == 330:
            # All directions red
            for direction in self.directions.values():
                direction.set_sequence(True, False, False, True, False, False, True, False, False)
        elif step == 400:
            # North-South Right Turn Red & Yellow, East-West Left Turn Red & Yellow
            self.directions["North"].set_sequence(True, False, False, True, False, False, True, True, False)
            self.directions["South"].set_sequence(True, False, False, True, False, False, True, True, False)
            self.directions["East"].set_sequence(True, False, False, True, True, False, True, False, False)
            self.directions["West"].set_sequence(True, False, False, True, True, False, True, False, False)
        elif step == 410:
            # North-South Right Turn Green, East-West Left Turn Green
            self.directions["North"].set_sequence(True, False, False, True, False, False, False, False, True)
            self.directions["South"].set_sequence(True, False, False, True, False, False, False, False, True)
            self.directions["East"].set_sequence(True, False, False, False, False, True, True, False, False)
            self.directions["West"].set_sequence(True, False, False, False, False, True, True, False, False)
        elif step == 420:
            # North-South Right Turn Yellow, East-West Left Turn Yellow
            self.directions["North"].set_sequence(True, False, False, True, False, False, False, True, False)
            self.directions["South"].set_sequence(True, False, False, True, False, False, False, True, False)
            self.directions["East"].set_sequence(True, False, False, False, True, False, True, False, False)
            self.directions["West"].set_sequence(True, False, False, False, True, False, True, False, False)

    def run_sequence(self):
        # Run the traffic light sequence in a loop
        step = 10
        sequence_steps = [10, 20, 100, 110, 120, 130, 200, 210, 220, 230, 240, 300, 310, 320, 330, 400, 410, 420, 100]
        initial_steps = [10, 20]
        while True:
            if step in initial_steps:
                self.set_sequence_by_step(step)
                self.display_all()
                time.sleep(2)
                step = initial_steps.pop(0) if initial_steps else sequence_steps[2]
            else:
                self.set_sequence_by_step(step)
                self.display_all()
            # Stay in the step for 10 seconds if it involves a green light, otherwise 2 or 3 seconds
            if step in [120, 220, 310, 410]:  # Steps with green lights
                time.sleep(10)
            else:
                time.sleep(3 if step in [120, 210] else 2)
            step = sequence_steps[(sequence_steps.index(step) + 1) % len(sequence_steps)]

# Example usage
init()  # Initialize colorama
traffic_system = TrafficSystem()
traffic_system.run_sequence()
