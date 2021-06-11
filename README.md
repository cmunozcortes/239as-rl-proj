# UCLA ECE 239AS Reinforcement Learning Final Project

This repository contains the source code for the implementations we used to
evaluate three deep Q-learning algorithms:
1. Deep Q-learning (DQN)
2. Double Deep Q-learning (Double DQN or DDQN)
3. Dueling DQN

Additionally, the repository hosts the LaTeX source for the various reports we
had to produce, and the poster we created to present a summary of our work.

For the algorithm implementations, we leveraged example code from the
[Tensorpack repository](https://github.com/tensorpack/tensorpack), with minimal
modifications to fit our goals and limited compute resources.
## Team members
* Ryan Chau
* My-Quan Hong
* Nathan Kang
* Chris Munoz
## Getting started
To clone the repository, run the following command:
```
git clone https://github.com/cmunozcortes/239as-rl-proj.git project
```

## Requirements/Dependencies
Instructions for installing dependencies and required packages can be found
[here](https://github.com/tensorpack/tensorpack/tree/master/examples/DeepQNetwork).

## Training
To train a model to play breakout, run the following commands:
```
cd src
python DQN.py --env breakout.bin --algo <algorithm>
```
where `<algorithm>` can be `DQN`, `Double`, `Dueling`.

## Evaluation
To evaluate a trained model for 100 episodes, run the following command:
```
python DQN.py --env breakout.bin --task eval --load <trained_model> --algo <algorithm>
```