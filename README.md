# Spatial Diversified Proportionality and Spatial Fairness Experiments

This repository contains the code to reproduce the experiments for the paper **"Spatial Diversified proportionality (Spatial Fairness)"**.

The project implements and evaluates a novel retrieval paradigm that selects a subset of `k` places from an initial set `S` that are not only relevant but also **spatially proportional** and **diverse**. This approach is formalized under the concept of **spatial fairness**.

---

## Running the Experiments

To run the experiments, please follow these steps:

### 1. **Configuration**

The main configuration for all experiments is located in the `src/config.py` file. Before running any scripts, you should set the desired parameters in this file.

Here's an overview of the key parameters, explained using the terminology from the paper:

* **`NUM_CELLS`**: A list of integers representing the total number of cells (`|G|`) for the **Virtual Grid Based Algorithm**. This parameter controls the granularity of the grid used to approximate the spatial proportionality scores (`pSS(pi)`). A higher value results in a finer grid and can improve approximation quality at the cost of computation time.

* **`COMBO`**: A list of tuples, where each tuple `(K, k)` defines an experimental run.
    * `K`: The total number of relevant places in the initial set `S`.
    * `k`: The number of places to be selected for the final result set `R`.
    * **Example**: `COMBO = [(1000, 20), (5000, 50)]` will run experiments for an initial set of 1000 places to select 20, and for an initial set of 5000 places to select 50.

* **`GAMMAS`**: A list of float values for the weight parameter `w`. This weight is used in the spatial proportionality score, `pS(pi) = pSS(pi) - w * pSR(pi)`, to control the trade-off between favoring places in dense areas (`pSS(pi)`) and ensuring diversity among the selected places in `R` (`pSR(pi)`).

* **`DBPEDIA_DATASET_NAMES`** and **`YAGO_DATASET_NAMES`**: These lists contain the names of the specific dataset files to run the experiments on. The scripts will iterate through these lists and run the configured experiments for each specified dataset, consistent with the evaluation in the paper.

---

### 2. **Datasets**

The experiments use datasets derived from **DBpedia** and **YAGO2**, as described in the paper. The pre-processed datasets are expected to be in the `datasets/` directory.

Please ensure the `.pkl` and `.npy` dataset files are correctly named and placed in the `datasets/` directory so the `dataset_store.py` script can load them properly.

---

### 3. **Dependencies**

This project requires Python 3. You can install the necessary libraries using pip. Based on the project's scope, you will likely need the following:

```bash
pip install numpy pandas scikit-learn matplotlib
```

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
