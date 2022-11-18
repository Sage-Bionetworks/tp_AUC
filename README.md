# Two-way partial AUC
A novel estimator for the two-way partial AUC

## Python Requirements

Some dependencies must be installed before using the script

```shell
conda install -c conda-forge r-proc
```

Default Parameters
```shell
    sensitivity_bound = 0.8 
    specificity_bound = 0.6 
```

Once you’ve successfully installed above dependency, you can use it from your python environment.

```python
python get_tproc.py
```

Note: Update the path_to_predicted_labels.csv with predicted attributes in get_tproc.py
