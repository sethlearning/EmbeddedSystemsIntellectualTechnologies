import numpy as np
import matplotlib.pyplot as plt
import torch
from torchvision import transforms
import sys

if len(sys.argv) < 2:
    print('Specify picture file')
    exit(1)
else:
    image = plt.imread(sys.argv[1])

# class names
class_names = ['Abyssinian',
 'American Bulldog',
 'American Pit Bull Terrier',
 'Basset Hound',
 'Beagle',
 'Bengal',
 'Birman',
 'Bombay',
 'Boxer',
 'British Shorthair',
 'Chihuahua',
 'Egyptian Mau',
 'English Cocker Spaniel',
 'English Setter',
 'German Shorthaired',
 'Great Pyrenees',
 'Havanese',
 'Japanese Chin',
 'Keeshond',
 'Leonberger',
 'Maine Coon',
 'Miniature Pinscher',
 'Newfoundland',
 'Persian',
 'Pomeranian',
 'Pug',
 'Ragdoll',
 'Russian Blue',
 'Saint Bernard',
 'Samoyed',
 'Scottish Terrier',
 'Shiba Inu',
 'Siamese',
 'Sphynx',
 'Staffordshire Bull Terrier',
 'Wheaten Terrier',
 'Yorkshire Terrier']

# functions
def show_image(image, classname):
    plt.imshow(image)
    plt.axis('off')
    plt.title(classname)
    plt.show()

# transforms
resize = transforms.Resize(224, interpolation=transforms.InterpolationMode.NEAREST)
crop = transforms.CenterCrop(size=224)

# neural net
class PetsNet(torch.nn.Module):
    def __init__(self):
        super(PetsNet, self).__init__()

        # pre-normalization
        self.bn0 = torch.nn.BatchNorm2d(num_features=3)

        # layer 1: 224x224x3
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=4, kernel_size=3, padding=1)
        self.act1 = torch.nn.ReLU()
        self.bn1 = torch.nn.BatchNorm2d(num_features=4)
        self.mp1 = torch.nn.MaxPool2d(kernel_size=2, stride=2)

        # layer 2: 112x112x4
        self.conv2 = torch.nn.Conv2d(in_channels=4, out_channels=8, kernel_size=3, padding=1)
        self.act2 = torch.nn.ReLU()
        self.bn2 = torch.nn.BatchNorm2d(num_features=8)
        self.mp2 = torch.nn.MaxPool2d(kernel_size=2, stride=2)

        # layer 3: 56x56x8
        self.conv3 = torch.nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, padding=1)
        self.act3 = torch.nn.ReLU()
        self.bn3 = torch.nn.BatchNorm2d(num_features=16)
        self.mp3 = torch.nn.MaxPool2d(kernel_size=2, stride=2)

        # layer 4: 28x28x16
        self.conv4 = torch.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1)
        self.act4 = torch.nn.ReLU()
        self.bn4 = torch.nn.BatchNorm2d(num_features=32)
        self.mp4 = torch.nn.MaxPool2d(kernel_size=2, stride=2)

        # layer 5: 14x14x32
        self.conv5 = torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1)
        self.act5 = torch.nn.ReLU()
        self.bn5 = torch.nn.BatchNorm2d(num_features=64)
        self.mp5 = torch.nn.MaxPool2d(kernel_size=2, stride=2)

        # layer 6: 7x7x64
        self.fc1 = torch.nn.Linear(7*7*64, 512)
        self.act6 = torch.nn.Tanh()
        self.bn6 = torch.nn.BatchNorm1d(num_features=512)

        # layer 7: 1x512
        self.fc2 = torch.nn.Linear(512, 128)
        self.act7 = torch.nn.Tanh()
        self.bn7 = torch.nn.BatchNorm1d(num_features=128)

        # layer 8: 1x128
        self.fc3 = torch.nn.Linear(128, 37)

    def forward(self, x):
        x = self.bn0(x)

        x = self.conv1(x)
        x = self.act1(x)
        x = self.bn1(x)
        x = self.mp1(x)

        x = self.conv2(x)
        x = self.act2(x)
        x = self.bn2(x)
        x = self.mp2(x)

        x = self.conv3(x)
        x = self.act3(x)
        x = self.bn3(x)
        x = self.mp3(x)

        x = self.conv4(x)
        x = self.act4(x)
        x = self.bn4(x)
        x = self.mp4(x)

        x = self.conv5(x)
        x = self.act5(x)
        x = self.bn5(x)
        x = self.mp5(x)

        x = x.view(x.size(0), x.size(1)*x.size(2)*x.size(3))

        x = self.fc1(x)
        x = self.act6(x)
        x = self.bn6(x)

        x = self.fc2(x)
        x = self.act7(x)
        x = self.bn7(x)

        x = self.fc3(x)

        return x

# import net
net = PetsNet()
net.load_state_dict(torch.load('./model.pt', weights_only=True))
net.eval()

im = crop(resize(torch.tensor(image).permute(2,0,1).unsqueeze(0)/255.))
classname = class_names[net.forward(im).argmax(dim=1)]

show_image(image, classname)

