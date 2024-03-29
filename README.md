# Particle-Ecosystem

A simulation that models a predator-prey system through "particles". Some particles are predators which chase prey particles and eat them if they get close enough. Prey particles simply run as far as they can from predator particles. This was written using Python and Pygame and is a side passion project.

![](./particle-ecosystem.gif)

### How to run

You will need Python and [Pygame](https://www.pygame.org/) (latest recommended), then simply run:

```
python main.py
```

Parameters for the simulation can be modified at the top of `main.py`. Parameters include board width height, the number of predators and prey:

```
BOARD_WIDTH
BOARD_HEIGHT
NUMBER_OF_CHASE_AGENTS
NUMBER_OF_FLEE_AGENTS
```
