### CNN_MODEL.py
import torch
import torch.nn as nn
import torch.nn.functional as F

class OCR_CNN(nn.Module):
    def __init__(self, num_classes=36): 			 # 26 letters + 10 digits
        super(OCR_CNN, self).__init__()
        
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)                      
		self.conv2 = nn.Conv2d(32, 64), kernel_size=3, stride=1, padding=1)                     ##conv network, which increases in complexity detection as channels increase
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        
        self.pool = nn.MaxPool2d(2, 2)             ## pooling is to look at the whole context instead of focusing on tiny details, like the big picture of the text
        
        self.fc1 = nn.Linear(128 * 8 * 8, 512)
        self.fc2 = nn.Linear(512, num_classes)
        
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        
        x = x.view(-1, 128 * 8 * 8)  
        x = F.relu(self.fc1(x))                           ## flattened the data through the first fully connected layer (FC)
        x = self.fc2(x)
        
        return x

### CNN_train.py

import torch
import torch.optim as optim									
import torch.nn as nn                          ## torch.nn is the main building block of neural network 
from torchvision import datasets, transforms
from torch.utils.data import DataLoader 			## a system for handling large datasets  , can process many words at once
from cnn_model import OCR_CNN

																						## Torchvision:image toolbox, helps with loading, resizing and augmenting images
# define transformations
transform = transforms.Compose([                    # this defines the input image so the model can laern more efficiently
     transforms.Grayscale(),                        # ensures all images have the same format before training (size, grayscale, normalization)
     transforms.Resize((32, 32)),
     transforms.ToTensor(),
     transforms.Normalize((0.5,), (0.5,))
])

# Load dataset
train_dataset = datasets.ImageFolder(root="training-data", transform=transform)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# Initialize model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = OCR_CNN(num_classes=36).to(device)

# Loss function & optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
epochs = 10
for epoch in range(epochs):
     for images, labels in train_loader:
          images, labels = images.to(device), labels.to(device)

          optimizer.zero_grad()
          outputs = model(images)
          loss = criterion(outputs, labels)
          loss.backward()
          optimizer.step()

    print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")


# Save Model
torch.save(model.state_dicht(), "ocr_cnn.pth")
print("Model saved!")



# self.dropout = nn.Dropout(0.5)  # Drops 50% of neurons randomly