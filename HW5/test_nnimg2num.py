import torch
from torchvision import datasets, transforms
import time
import matplotlib.pyplot as plt
from img2num import img2num

# Create object for NnImg2Num class
model = img2num()

# Load test data
TestLoader = torch.utils.data.DataLoader(datasets.MNIST('../data', train = False, transform = transforms.Compose([
                                                                  transforms.ToTensor(), 
                                                                  transforms.Normalize((0.1307,), (0.3801,))
                                                                  ])), 
                                           batch_size = 1, shuffle = True)

# Initiate error rate, operation time and epochs
eRate, opTime, epochs = [], [], []

# Train model using different epoch
for i in range(1, 5):
    epoch = i * 10
    startTime = time.time()
    model.epoch = epoch
    model.train()
    opTime.append(time.time() - startTime)
    correctness, total = 0, 0
    epochs.append(epoch)
    for batch_idx, (data, label) in enumerate(TestLoader):
        output = model.forward(data)
        if torch.equal(output.data, label):
            correctness += 1
        total += 1
    eRate.append((total - correctness) / total)
    print("Error Rate: ", (total - correctness) / total * 100, "%")
    

plt.figure(1)
plt.xlabel('Epoch')
plt.ylabel('Operation Time')
plt.title("Operation time for different epoch using LeNet-5")
plt.plot(epochs, opTime)

plt.figure(2)
plt.xlabel('Epoch')
plt.ylabel('Error Rate')
plt.title("Error rate for different epoch using LeNet-5")
plt.plot(epochs, eRate)

plt.show()
