# IPCGANs

## Introduction
This project is an implementation based on the [Identity-Preserved Conditional Generative Adversarial Networks](https://openaccess.thecvf.com/content_cvpr_2018/papers/Wang_Face_Aging_With_CVPR_2018_paper.pdf).

## Dataset
The datasets utilized in this project include:
- [UTKFace Dataset](https://www.kaggle.com/datasets/jangedoo/utkface-new/data): a large-scale face dataset with long age span (range from 0 to 116 years old). The dataset consists of over 20,000 face images with annotations of age, gender, and ethnicity.
- [AffectNet Training Data](https://www.kaggle.com/datasets/noamsegal/affectnet-training-data): contains approximately 30,000 facial RGB images of different expressions with size restricted to 48×48, and the main labels of it can be divided into 7 types: Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral.

## Directory Structure

### ExTraining
- **cgan4aging.ipynb**: Training a Conditional GAN (CGAN) model for face-aging tasks.
- **facealexnet-pretrain4aging.ipynb**: Pretraining the AlexNet model specifically for face-aging tasks.
- **ipcgans-train-for-aging.ipynb**: Training the IPCGAN model for face-aging tasks.
- **facealexnet-pretrain4emotion.ipynb**: Pretraining the AlexNet model for emotion trans tasks.
- **ipcgans-train-for-emo.ipynb**: Training the IPCGAN model for emotion trans tasks.

### Preprocessing
- **balance_sample.py**
- **check_size.py**
- **create_pairs.py**: Generate paired samples for training.
- **group.py**: Grouping images or labels based on specific criteria.
- **pre.py**: Handles image normalization, resizing, and augmentation.
  
## Results
Below are the example results from the trained models:
- **Face Aging:** [checkpoint/validation/epoch_19](https://www.kaggle.com/code/poongln/ipcgans-train-for-aging/output)
- **Emotion Trans:** [checkpoint/validation/epoch_29](https://www.kaggle.com/code/poongln/ipcgans-train-for-emo/output)
