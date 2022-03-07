##原生套件
import os
import requests
import itertools
from io import BytesIO
import sys

sys.path.append(r"C:/Users/TibeMe_user/Desktop/Python與LINE Bot機器人全面實戰特訓班--Flask最強應用學習資源/本書範例/ch02/packages")

##模型第三方套件
import torch
from torch.autograd import Variable
from tqdm import tqdm
from glob import glob
from torch import optim, nn
from torchvision import transforms
from torchvision import models, transforms
from PIL import Image


def switchName(num):
    if num == 0:
        return '光化性角化病和表皮內層癌(akiec)'
    if num == 1:
        return '基底細胞癌(bcc)'
    if num == 2:
        return '角化病病變(bkl)'
    if num == 3:
        return '皮膚纖維瘤(df)'
    if num == 4:
        return '黑色素細胞痣(nv)'
    if num == 5:
        return '血管受損(vasc)'
    if num == 6:
        return '黑色素瘤(mel)'
    else:
        return '無相符(None)'


# img_path = './input/HAM10000_images_part_1/SpongeBob.jpg'

def set_parameter_requires_grad(model, feature_extracting):
    if feature_extracting:
        for param in model.parameters():
            param.requires_grad = False

def initialize_model(feature_extract):
    """densenet121"""
    model_ft = models.densenet121(pretrained=True)
    set_parameter_requires_grad(model_ft, feature_extract)
    num_ftrs = model_ft.classifier.in_features
    model_ft.classifier = nn.Linear(num_ftrs, 7)
    input_size = 224
    return model_ft, input_size

# 模型方法
def predict(url):
    # url="https://i1.kknews.cc/SIG=a36m3u/1p6700040q8r58so473s.jpg"
    req = requests.get(url)
    url = BytesIO(req.content)

    feature_extract = False
    model_ft, input_size = initialize_model(feature_extract)
    device = torch.device('cpu')
    model = model_ft.to(device)
    model.load_state_dict(torch.load('./densenetSkin.pt', map_location=torch.device('cpu')))
    model.eval()

    input_size = 224
    norm_mean = [0.7630329, 0.54564583, 0.5700466]
    norm_std = [0.14092815, 0.15261224, 0.1699708]

    img_1_PIL = Image.open(url)
    val_transform = transforms.Compose([transforms.Resize((input_size,input_size)),
                                        transforms.ToTensor(),
                                        transforms.Normalize(norm_mean, norm_std)])

    img_1_X = val_transform(img_1_PIL)
    img_trainsformed = torch.unsqueeze(img_1_X, 0)

    device = torch.device('cpu')

    images = img_trainsformed
    images = Variable(images).to(device)
    outputs = model(images)
    prediction = outputs.max(1, keepdim=True)[1]
    predicts = switchName(prediction[0][0].item())

    return predicts

