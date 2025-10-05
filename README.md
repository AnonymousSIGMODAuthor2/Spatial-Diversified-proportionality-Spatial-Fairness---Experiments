# Spatial Diversified Proportionality and Spatial Fairness Experiments

This repository contains the code and experiments for the paper "Spatial diversified proportionality and spatial fairness".

---

## Running the Experiments

To run the experiments, follow these steps:

### 1. **Configuration**

The main configuration for the experiments is in the `src/config.py` file. Before running any experiment, you need to set the desired parameters in this file.

Here's an overview of the parameters you can configure:

* **`NUM_CELLS`**: This is a list of integers representing the different grid sizes you want to use for the experiments. The grid is divided into `G x G` cells, where `G` is the square root of a value in this list.
    * **Example**: `NUM_CELLS = [256, 1024]` will run experiments on a 16x16 and 32x32 grid.

* **`COMBO`**: A list of tuples, where each tuple `(n, k)` defines a combination of the number of points `n` and the number of desired results `k`.
    * **Example**: `COMBO = [(1000, 20), (5000, 50)]` will run experiments for 1000 points with k=20 and 5000 points with k=50.

* **`GAMMAS`**: A list of float values for the `gamma` parameter, which is likely used in your fairness or diversity metric.
    * **Example**: `GAMMAS = [0.5, 1.0, 1.5]`

* **`DBPEDIA_DATASET_NAMES`** and **`YAGO_DATASET_NAMES`**: These lists contain the names of the datasets you want to run the experiments on. The experiment scripts will iterate through these lists and run the configured experiments for each dataset.

---

### 2. **Datasets**

The experiments use datasets from DBPedia and YAGO2. The datasets are expected to be in the `datasets/` directory. Based on the file names, it seems you are using `.pkl` and `.npy` files.

Make sure the dataset files are correctly named and placed in the `datasets/` directory so the `dataset_store.py` script can load them.

---

### 3. **Dependencies**

This project requires Python 3 and several libraries. You can install them using pip. While a `requirements.txt` file is not provided, based on the file types and common usage in scientific experiments, you will likely need the following libraries:

```bash
pip install numpy pandas scikit-learn matplotlib
```

---

### 4. **Running the Experiments**

The experiment scripts are located in the `src/exp/` directory. To run an experiment, you can execute the desired Python script from the `src/` directory.

For example, to run the `hardcore_exp.py` experiment, you would run the following command from the root of the project:

```bash
python src/exp/hardcore_exp.py
```

This will run the experiment with the parameters you have defined in `src/config.py`. The script will likely iterate through all the configured datasets, grid sizes, and other parameters, running the necessary algorithms and saving the results.

---

### 5. **Results**

The output of the experiments, such as logs, plots, or raw data, will be saved to a directory (e.g., `results/` or `output/`). You may need to create this directory if the scripts don't do it automatically.
