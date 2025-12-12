import os
import program

def main():
    try:
        size = int(
            input(
                "Maze size (maze is displayed if size between 2 to 150) (if maze size is more than 150, maze will not be displayed but statistics will be shown): "
            )
        )
    except ValueError:
        print("Please enter a valid integer")
        os._exit(3)

    if size < 2:
        print("invalid maze size")
        os._exit(2)

    try:
        wallBreakPercent = float(
            input("Percantage of walls to remove (between 0 and 100): ")
        )
    except ValueError:
        print("Please enter a valid float")
        os._exit(4)

    if wallBreakPercent < 0 or wallBreakPercent > 100:
        print("invalid percentage")
        os._exit(1)

    program.program(size, wallBreakPercent)


main()
