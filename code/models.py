import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F




device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class EncoderRNN(nn.Module):
    def __init__(self, input_sizes, hidden_size):
        super(EncoderRNN, self).__init__()
        self.hidden_size = hidden_size
        self.input_sizes = input_sizes
        self.embedding = nn.Embedding(input_sizes, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size)
        
        
    def forward(self, input, hidden):
        embedded = self.embedding(input).view(1, 1, -1)
        output = embedded
        print ("output shape", output.size())
        print ("hidden shape", hidden.size())

        output, hidden = self.gru(output, hidden)
        return output, hidden
    
    def initHidden(self):
        return torch.zeros(1, 1, self.hidden_size, device=device)
    

        
       
class DecoderRNN(nn.Module):
    def __init__(self, input_sizes, hidden_size, output_size):
        super(DecoderRNN, self).__init__()
        self.hidden_size = hidden_size
        self.input_sizes = input_sizes
        self.embedding = nn.Embedding(input_sizes, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size)
        self.out = nn.Linear(hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

        
        
    def forward(self, input, hidden):
        embedded = self.embedding(input).view(1, 1, -1)
        output = embedded
        
        output, hidden = self.gru(output, hidden)
        output = self.softmax(self.out(output[0]))
 
        return output, hidden
    
    def initHidden(self):
        return torch.zeros(1, 1, self.hidden_size, device=device)        
    
    
class DecoderAttentionRNN(nn.Module):
    def __init__(self, input_sizes, hidden_size, output_size):
        super(DecoderAttentionRNN, self).__init__()
        self.hidden_size = hidden_size
        self.input_sizes = input_sizes
        self.embedding = nn.Embedding(input_sizes, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size)
        self.out = nn.Linear(hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

        
        
    def forward(self, input, hidden, attention_input):
        embedded = self.embedding(input).view(1, 1, -1)
        output = embedded
        
        output, hidden = self.gru(output, hidden)
        output = self.softmax(self.out(output[0]))
 
        return output, hidden
    
    def initHidden(self):
        return torch.zeros(1, 1, self.hidden_size, device=device)            