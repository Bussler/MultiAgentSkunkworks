import ray
import torch

print(f"Torch version: {torch.__version__}")
print(f"Torch GPU support: {torch.cuda.is_available()}")

print(f"Ray version: {ray.__version__}")
