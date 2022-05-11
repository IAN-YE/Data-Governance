import torch
from torch import nn
import torch.nn.functional as F

a = torch.randn((1,64,256))

b = torch.randn((256,256))

print(torch.matmul(a,b).shape)

