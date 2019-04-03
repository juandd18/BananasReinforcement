import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc1_units=24, fc2_units=32):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): Number of nodes in first hidden layer
            fc2_units (int): Number of nodes in second hidden layer
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)
        
        #two fully connected layers
        self.fc3_adv = nn.Linear(fc2_units,64)
        self.fc4_val = nn.Linear(fc2_units,64)
        
        #advantage stream
        self.fc_advantage = nn.Linear(64,action_size)
        #value stream
        self.fc_value = nn.Linear(64,1)
        

    def forward(self, state):
        """Build a network that maps state -> action values."""
        m = nn.ELU()
        x = m(self.fc1(state))
        x = m(self.fc2(x))
        
        fc_adv = m(self.fc3_adv(x))
        fc_value = m(self.fc4_val(x))
        
        return self.fc_advantage(fc_adv) + self.fc_value(fc_value)
