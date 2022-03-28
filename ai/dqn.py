# Implementing Deep Q-Learning

from ai.network import Network
from ai.replay_memory import ReplayMemory
import torch.optim as optim
import torch
import torch.nn.functional as F
from torch.autograd import Variable

class Dqn(object):
    BATCH_SIZE = 100

    def __init__(self, input_size: int, output_size: int, gamma: float):
        self.gamma: float = gamma
        self.model: Network = Network(input_size, output_size)
        self.memory: ReplayMemory = ReplayMemory(capacity = 100000)
        self.optimizer: optim.Adam = optim.Adam(params = self.model.parameters())
        self.last_state: torch.Tensor = torch.Tensor(input_size).unsqueeze(0)
        self.last_action = 0
        self.last_reward = 0
        self.move_number = 0

    def select_action(self, state):
        probs = F.softmax(self.model.forward(Variable(state))*100)
        action = probs.multinomial(len(probs))
        return action.data[0,0]

    def learn(self, batch_states, batch_actions, batch_rewards, batch_next_states):
        print('learn!')
        batch_outputs = self.model.forward(batch_states).gather(1, batch_actions.unsqueeze(1)).squeeze(1)
        batch_next_outputs = self.model.forward(batch_next_states).detach().max(1)[0]
        batch_targets = batch_rewards + self.gamma * batch_next_outputs
        td_loss = F.smooth_l1_loss(batch_outputs, batch_targets)
        self.optimizer.zero_grad()
        td_loss.backward()
        self.optimizer.step()

    def update(self, new_state, new_reward):
        self.move_number += 1
        new_state = torch.Tensor(new_state).float().unsqueeze(0)
        self.memory.push((
            self.last_state,
            torch.LongTensor([int(self.last_action)]),
            torch.Tensor([self.last_reward]),
            new_state
        ))
        new_action = self.select_action(new_state)
        if (len(self.memory.memory) > self.BATCH_SIZE \
                and self.move_number % self.BATCH_SIZE == 0):
            batch_states, batch_actions, batch_rewards, batch_next_states = self.memory.sample(self.BATCH_SIZE)
            self.learn(batch_states, batch_actions, batch_rewards, batch_next_states)
        self.last_state = new_state
        self.last_action = new_action
        self.last_reward = new_reward
        return new_action

