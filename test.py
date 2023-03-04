import tensorflow
import torch

print(torch.cuda.is_available())
print(tensorflow.config.list_physical_devices('GPU'))
