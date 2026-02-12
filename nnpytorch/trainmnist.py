import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# 1. Define the Neural Network architecture
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28*28, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# 2. Setup Data, Model, Loss, and Optimizer
transform = transforms.Compose([transforms.ToTensor()])
train_loader = torch.utils.data.DataLoader(
    datasets.MNIST('./data', train=True, download=True, transform=transform), batch_size=64)

model = SimpleNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 3. Training Loop
for epoch in range(3): # Just 1 epoch for the "Hello World"
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()   # Reset gradients
        output = model(data)    # Forward pass
        loss = criterion(output, target) # Calculate loss
        loss.backward()         # Backward pass (backprop)
        optimizer.step()        # Update weights
        
        if batch_idx % 100 == 0:
            print(f"Batch {batch_idx}, Loss: {loss.item():.4f}")
    print("\n")

# Add function 
torch.save({
    'epoch': epoch,
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': loss,
}, 'mnist_model.pth')   