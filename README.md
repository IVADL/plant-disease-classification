# plant-disease-classification

The repository is a classifier project that allows you to easily categorize disease of plant photos using notebook env. Currently, plant disease type can be classified, and the model can be trained using a new dataset according to code commands.

- [O] Plant Disease Classification
- [O] Learning a new model
- [O] Assessing existing and new models

> We have organized data sets and codes with the goal of matching the disease type of plant, and we have achieved the goal by learning about them. These simple projects can easily be applied to new research and ideas in the future.

## Table of Contents

- [Environment](#Environment)
- [Dataset](#Dataset)
- [Model](#Model)
- [TEST](#TEST)
- [TO-DO](#TO-DO)
- [Contributing](#contributing)
- [License](#License)

## Environment

### Dependencies

plant-disease-classification was developed using the following library version:

- [Python3] - 3.8.5
- [Tensorflow] - 2.3.0
- [CUDA] - 10.1
- [Cudnn] - 7.6.5

and GPU enable Environment (Slow, but also in a CPU environment.)

### Env Setting

1. Clone food-image-classifier Repository

   ```sh
   $ git clone https://github.com/IVADL/plant-disease-classification.git
   $ cd food-image-classifier
   ```

2. Configure virtual environment

   ```sh
   $ python -m venv .venv
   $ (windows) .venv\Scripts\activate
   $ (Linux) source .venv/bin/activate
   ```

3. Install the dependencies.

   ```sh
   $ pip install -r requirements.txt
   ```

## Dataset

- [O] [Plant Village Dataset](https://data.mendeley.com/datasets/tywbtsjrjv/1)

  > n this data-set, 39 different classes of plant leaf and background images are available. The data-set containing 61,486 images. We used six different augmentation techniques for increasing the data-set size. The techniques are image flipping, Gamma correction, noise injection, PCA color augmentation, rotation, and Scaling.

- [x] [Ai-Hub Facility horticultural crop pest image Dataset](https://www.aihub.or.kr/aidata/129)
  > To be updated

## Model

O: Available
X: Currently unavailable (To be tested later)

- [O] Inception V3
  > pretrained: https://drive.google.com/file/d/1UhXIbqKp6xC2ARxMTsS2rv1Ym1O8NQIe/view?usp=sharing
  > loss: 0.3095 - accuracy: 0.9792 - val_loss: 0.2536 - val_accuracy: 0.9906
- [x] mobilenet

## TEST

You can train and test through the main.ipynb notebook file.

## TODO

- Testing of new models
- Test using video
- Speed ​​for real time

## Contributing

Feel free to [open an Issue](https://github.com/IVADL/plant-disease-classification/issues/new), if you think something needs to be changed. You are welcome to participate in development, instructions are available in our contribution guide (TBD).

Or, if you have any questions, you can ask them via [email](mailto:harimkang4422@gmail.com).

## License

---

To be updated
