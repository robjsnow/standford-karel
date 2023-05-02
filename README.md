## Usage

To use Karel, you need to install the `stanfordkarel` Python package. You can install it using pip:
`pip install stanfordkarel`


To make a new Karel program, you can use the following template:

```python
from stanfordkarel import *


def main():
    """Karel code goes here!"""
    turn_left()
    move()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
```    
    
Creating and/or editing new worlds:

```python
from stanfordkarel.world_editor import run_world_editor

if __name__ == '__main__':
    run_world_editor()
```


## Karel Commands

| Command                  | Description                                  |
|--------------------------|--------------------------------------------|
| `move()`                 | Move Karel one step forward.                |
| `right_is_clear()`       | Check if Karel's right is clear of walls.   |
| `facing_east()`          | Check if Karel is facing East.              |
| `turn_left()`            | Turn Karel to the left.                     |
| `right_is_blocked()`     | Check if Karel's right is blocked by a wall.|
| `not_facing_east()`      | Check if Karel is not facing East.          |
| `put_beeper()`           | Put a beeper down in the current location.  |
| `beepers_present()`      | Check if there is a beeper present.         |
| `facing_west()`          | Check if Karel is facing West.              |
| `pick_beeper()`          | Pick up a beeper from the current location. |
| `no_beepers_present()`   | Check if there are no beepers present.      |
| `not_facing_west()`      | Check if Karel is not facing West.          |
| `front_is_clear()`       | Check if Karel's front is clear of walls.   |
| `beepers_in_bag()`       | Check how many beepers Karel has in their bag.|
| `facing_south()`         | Check if Karel is facing South.             |
| `front_is_blocked()`     | Check if Karel's front is blocked by a wall.|
| `no_beepers_in_bag()`    | Check if Karel has no beepers in their bag. |
| `not_facing_south()`     | Check if Karel is not facing South.         |
| `left_is_clear()`        | Check if Karel's left is clear of walls.    |
| `facing_north()`         | Check if Karel is facing North.             |
| `paint_corner(color)`    | Paint the current corner with the given color.|
| `left_is_blocked()`      | Check if Karel's left is blocked by a wall. |
| `not_facing_north()`     | Check if Karel is not facing North.         |
| `corner_color_is(color)` | Check if the color of the current corner is the given color. |
