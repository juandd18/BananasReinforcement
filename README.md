# BananasReinforcement
Udacity Deep Reinforcement Learning First Project

[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif "Trained Agent"



### Introduction

This repo provides an implementation of an agent which learns to navigate and collect bananas in a large, square world provided by [Unity ML Agents](https://github.com/Unity-Technologies/ml-agents).

![Trained Agent][image1]

### Environment

The agent operates in a state space which has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction. Given this information, the agent learns how to best select actions.

Four discrete actions are available to agent, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of the agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The task is episodic, and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes.

### Getting Started

1. Clone this repository

```
git clone https://github.com/juandd18/BananasReinforcement.git
cd BananasReinforcement
```

2. Install python dependencies

It's **highly advisable** to create a separate `Python` [virtual environment](https://docs.python-guide.org/dev/virtualenvs/). Once your virtualenv has been activated you can proceed with installing `Python` dependencies as per [Udacity guide](https://github.com/udacity/deep-reinforcement-learning#dependencies).

**Note:** Udacity guide recommends using the [Conda](https://conda.io/) `Python` distribution which overrides the system `Python` setup. The author of this repository refuses to mess with the system `Python` and was successful with setting up the workspace without using the Conda `Python` distribution.


3. Download the environment from one of the links below. You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
    
4. Move the downloaded file to the project directory and unzip (or decompress) it.

5. Open the ProjectNavigation.ipynb in a jupyter notebook a run the cells or the last one to run a pretrained model

