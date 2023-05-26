# Background_Remover
This repository contains a Python script for removing the background from images. The script utilizes computer vision techniques and machine learning algorithms to automatically segment the foreground object from the background.

## Table of Contents
- Background Remover
- Table of Contents
- Introduction
- Installation

### Introduction
Removing the background from images can be a useful task in various applications, such as object recognition, image editing, and computer graphics. This repository provides a Python script that leverages the power of computer vision and machine learning to automatically extract the foreground object from an image.

The script uses the popular OpenCV library for image processing tasks, along with pre-trained deep learning models to perform semantic segmentation. The pre-trained model employed by the script is capable of accurately identifying the foreground object in most cases.

### Installation
To use the background removal script, follow these steps:
1. Clone this repository to your local machine:
  ```bash
  git clone https://github.com/Priyanshu-84/Background_Remover.git 
  ```
2. Install the required dependencies. It is recommended to use a virtual environment to keep the project dependencies isolated. Navigate to the cloned repository's directory and run the following command:
```bash
pip install -r requirements.txt
```
This will install all the necessary packages, including OpenCV and other dependencies.
3. The script relies on a pre-trained deep learning model for semantic segmentation. Download the model weights by running the provided `download_model_weights.sh script`:
```bash
sh download_model_weights.sh
```
This will download the model weights file and save it in the appropriate location.

Once the installation is complete, you are ready to use the background removal script.
