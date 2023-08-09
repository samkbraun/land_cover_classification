# Land Cover Classification (Deep Learning Image Processing Project)

NOTE: THIS README IS FOR THE PLANNED FINAL PROJECT, CURRENTLY THIS REPO IS INCOMPLETE

This project aims to explore deep learning techniques for image processing using the DeepGlobe Land Cover Classification dataset. The goal is to train a deep neural network to classify land cover types in satellite images.

## Dataset

The dataset used for this project is the DeepGlobe Land Cover Classification dataset. This dataset contains high-resolution satellite images covering various regions and land cover classes.

Dataset Source: [DeepGlobe Land Cover Classification](https://competitions.codalab.org/competitions/18468)

## Project Structure

The project is organized as follows:

- `data/`: Directory to store and organize the dataset.
- `models/`: Directory for storing trained model checkpoints.
- `notebooks/`: Jupyter notebooks for data exploration, model development, and visualization.
- `scripts/`: Python scripts for data preprocessing, model training, and evaluation.
- `results/`: Directory to save experimental results, plots, and visualizations.

## Setup

1. Clone this repository:
git clone https://github.com/your-username/your-project.git
cd your-project

2. Install project dependencies:
pip install -r requirements.txt

## Usage

1. **Data Preparation**: Download the DeepGlobe Land Cover Classification dataset and place it in the `data/` directory.

2. **Data Preprocessing**: Use the scripts in the `scripts/` directory to preprocess the dataset, including resizing images, generating labels, and splitting into training/validation sets.

3. **Model Development**: Use Jupyter notebooks in the `notebooks/` directory to experiment with different deep learning architectures and training strategies.

4. **Training**: Use the training script in the `scripts/` directory to train your chosen model. Adjust hyperparameters as needed.

5. **Evaluation**: Evaluate your trained model using the evaluation script. Analyze accuracy, precision, recall, and other relevant metrics.

6. **Visualization**: Use the provided scripts and notebooks in the `notebooks/` directory to visualize model predictions, activations, and results.

## Credits

- DeepGlobe Land Cover Classification dataset: [DeepGlobe Competition](https://competitions.codalab.org/competitions/18468)

