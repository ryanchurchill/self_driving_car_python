import torch
import torch.nn as nn
import torch.nn.functional as F

class Network(nn.Module):
	HIDDEN_LAYER_NODE_COUNT = 30

	def __init__(self, input_size: int, output_size: int):
		super(Network, self).__init__()
		self.input_size: int = input_size
		self.output_size: int = output_size
		# connections between input layer and hidden layer
		self.fc1 = nn.Linear(input_size, self.HIDDEN_LAYER_NODE_COUNT)
		# connections between hidden layer and output layer
		self.fc2 = nn.Linear(30, output_size)

	# state: input state vector
	def forward(self, state):
		tensor: Tensor = F.relu(self.fc1(state))
		q_values = self.fc2(x)
		return q_values
