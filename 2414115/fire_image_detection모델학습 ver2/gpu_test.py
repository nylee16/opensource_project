import torch

print("gpu 사용 가능",   torch.cuda.is_available())
print("gpu이름:", torch.cuda.get_device_name(0))

