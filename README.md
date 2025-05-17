# SVHN Balanced Dataset

> A PyTorch‑compatible wrapper for loading a class‑balanced subset of the SVHN dataset, with seamless integration into standard `torchvision.transforms` pipelines.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
  - [Creating the Dataset](#creating-the-dataset)  
  - [Transforms and DataLoader](#transforms-and-dataloader)  
- [API Reference](#api-reference)  
- [Development & Contribution](#development--contribution)  
- [License](#license)  
- [Acknowledgments](#acknowledgments)  

---

## Overview

The **SVHN Balanced Dataset** package provides an easy way to load a **balanced** training and test split of the Street View House Numbers (SVHN) dataset. Each digit class (0–9) is represented with an equal number of samples (default: 5,000 per class for training, 1,000 per class for testing), drawn from the combined original SVHN train+test pool of 99,289 images.  

Key design goals:

- **Class‑balanced splits** (no overlap between train/test).  
- **HWC → PIL** conversion under the hood for full compatibility with `torchvision.transforms`.  
- **Optional one‑line download** of pre‑built `.npz` bundles.  
- Minimal dependencies beyond PyTorch, torchvision, NumPy, and Pillow.

---

## Features

- **Balanced sampling**: 5,000 training and 1,000 testing samples per digit by default.  
- **Seamless transforms**: Returns `PIL.Image` objects so you can apply any standard `torchvision.transforms`.  
- **Lazy download**: Automatically fetches pre‑generated `.npz` files if `download=True`.  
- **Easy packaging**: Installable via pip from GitHub or local wheel.

---

## Installation

#### 1. From GitHub (latest development)

```bash
pip install "git+https://github.com/xiaolanshu/svhn_balance_dataset.git@main#egg=svhn_balance_dataset"
```

## Acknowledgments
- Original SVHN dataset introduced by Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco, Bo Wu, and Andrew Y. Ng at Stanford University (http://ufldl.stanford.edu/housenumbers/).

- Implementation builds upon torchvision.datasets.SVHN from the PyTorch project.
