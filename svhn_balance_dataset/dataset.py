import os
import numpy as np
from torchvision.datasets import VisionDataset
from PIL import Image
import requests
from tqdm import tqdm
class SVHNBalancedDataset(VisionDataset):
    train_url = "https://storage.adagopro.shop/d/Aliyun/Datasets/train_svhn_balance.npz"
    test_url = "https://storage.adagopro.shop/d/Aliyun/Datasets/test_svhn_balance.npz"
    def __init__(self, 
                 root,
                 train=True,
                 transform=None,
                 target_transform=None,
                 download=False,
        ):
        super().__init__(root, transform=transform, target_transform=target_transform)
        self.transform = transform
        self.target_transform = target_transform
        self.train = train
        if download:
            self.download()
        if self.train:
            self.total_data = np.load(os.path.join(self.root, 'train_svhn_balance.npz'))
            self.data = self.total_data['data']
            self.targets = self.total_data['targets']
        else:
            self.total_data = np.load(os.path.join(self.root, 'test_svhn_balance.npz'))
            self.data = self.total_data['data']
            self.targets = self.total_data['targets']
        self.classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.class_to_idx = {name: i for i, name in enumerate(self.classes)}
        self.idx_to_class = {i: name for i, name in enumerate(self.classes)}

    def __len__(self):
        return len(self.targets)

    def __getitem__(self, index):
        img, target = self.data[index], self.targets[index]
        img = Image.fromarray(img)
        if self.transform is not None:
            img = self.transform(img)
        target = int(target)
        if self.target_transform is not None:
            target = self.target_transform(target)
        return img, target

    def download(self):
        os.makedirs(self.root, exist_ok=True)
        if self.train:
            url = self.train_url
            filename = 'train_svhn_balance.npz'
        else:
            url = self.test_url
            filename = 'test_svhn_balance.npz'
        filepath = os.path.join(self.root, filename)
        if os.path.exists(filepath):
            print(f"[SKIP] {filename} already exists.")
            return

        print(f"Downloading {url} → {filepath}")
        response = requests.get(url, stream=True)
        total = int(response.headers.get('Content-Length', 0))
        chunk_size = 1024 * 1024

        with open(filepath, 'wb') as f, tqdm(
            total=total, unit='B', unit_scale=True, desc=filename
        ) as pbar:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if not chunk:
                    break
                f.write(chunk)
                pbar.update(len(chunk))
