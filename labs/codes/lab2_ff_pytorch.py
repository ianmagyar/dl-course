import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import torch.optim as optim

from PIL import Image, ImageDraw, ImageShow
import matplotlib.pyplot as plt

# This solution works but it is not efficient in several ways
# 1. Correct and/or remove the activation functions?
# 2. Minimize number of parameters?
# 3. Find the correct function? IS RMSE the right one? Why?
# 4. Reduce the number of layers? Why is it possible or why it is not?
# 5. Optimizers parameters modification.
# 6. Introduction of minibatches? Will it help?

def get_n_params(model):
    pp=0
    for p in list(model.parameters()):
        nn=1
        for s in list(p.size()):
            nn = nn*s
        pp += nn
    return pp

def circle_in_square():
    img = Image.new("1", (10, 10))
    draw = ImageDraw.Draw(img)
    draw.ellipse([1, 1, 9, 9], 1)
    xv, yv = np.meshgrid(range(0, 10), range(0, 10), sparse=False, indexing='ij')

    circle = np.array(img)

    return np.squeeze(np.array([xv.reshape((1, 100)), yv.reshape((1, 100)), circle.reshape((1, 100))])).transpose()

#net
class CircleNet(nn.Module):
    def __init__(self):
        super(CircleNet, self).__init__()

        self.fc1 = nn.Linear(2, 256)
        self.fc2 = nn.Linear(256, 64)
        self.fc3 = nn.Linear(64, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        return x


if __name__ == '__main__':
    net = CircleNet()
    print("Networks parameters: " + str(get_n_params(net)))

    criterion = nn.MSELoss()
    optimizer = optim.SGD(net.parameters(), lr=0.01)

    train_data = circle_in_square()
    data_len = train_data.shape[0]

    for epoch in range(0, 1000):
        for batch in range(0, data_len):
            optimizer.zero_grad()
            input_tensor = torch.tensor(train_data[batch, 0:2] / 10, dtype=torch.float32)
            output = net(input_tensor)
            goal_val = torch.tensor(train_data[batch, 2], dtype=torch.float32)
            loss = criterion(output, goal_val)
            loss.backward()
            optimizer.step()
        pred_y = net(torch.tensor(train_data[:, 0:2] / 10, dtype=torch.float32))
        print("Accuracy: " + str(np.equal(torch.round(pred_y.detach()).numpy().reshape(100,),train_data[:, 2].transpose()).sum()))
        if epoch % 100 == 0:
            plt.imshow(pred_y.reshape((10, 10, 1)).squeeze().detach().numpy())
            plt.title('Epoch: ' + str(epoch))
            plt.draw()
            plt.pause(0.0001)
            plt.clf()

