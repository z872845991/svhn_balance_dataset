from setuptools import setup, find_packages

setup(
    name="svhn_balance_dataset",
    version="0.1.0",
    license="MIT",
    description="Balanced SVHN dataset wrapper",
    author="Jesse Wang",
    author_email="z872845991@gmail.com",
    url="https://github.com/z872845991/svhn_balance_dataset",       # 可选：指向 Git 仓库
    packages=find_packages(),            # 会自动找到 svhn_balance_dataset 目录
    install_requires=[
        "torch",
        "torchvision",
        "numpy",
        "Pillow",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)

