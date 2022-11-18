#Load required libraries
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
import numpy as np
import pandas as pd
pandas2ri.activate()

def process_tpROC(df, sensitivity_bound, specificity_bound):
    """
    -----------------------------------------------------------------------------------------
    
    Processing two way partical AUC r script
    
    Args:
        df: Pandas dataframe with predicted prob (probability) and ground truth (label)
    
    Return:
        A numpy array with two way partical AUC score
    
    -----------------------------------------------------------------------------------------
    """
    r = robjects.r
    r['source']('src/two_way_partial_AUC.R')
    
    # Loading the function we have defined in R.
    filter_proc_function_r = robjects.globalenv['pROCBasedTwoWayPartialAUC']
    pdf_2_r = robjects.conversion.py2rpy(df)
    
    df_r = filter_proc_function_r(pdf_2_r, sensitivity_bound, specificity_bound)
    return np.array(df_r)

def get_tproc_score(df, sensitivity_bound, specificity_bound):
    """
    -----------------------------------------------------------------------------------------
    
    Computing two way partical AUC score
    
    Args:
        df: Pandas dataframe with predicted prob (probability) and ground truth (label)
    
    Return:
        A pandas dataframe with two way partical AUC score
    
    -----------------------------------------------------------------------------------------
    """
    tp_roc = process_tpROC(df, sensitivity_bound, specificity_bound)
    score = [{'tpAUC': tp_roc[0][0], 'pAucSe': tp_roc[1][0], 'pAucSp': tp_roc[2][0]}]
    
    df_score = pd.DataFrame(score)
    return df_score

if __name__ == "__main__":
    
    #Expected columns
    #probability: the probability that the example is a positive case
    #label: Ground truth labels 
    df = pd.read_csv('path_to_predicted_labels.csv')
    
    sensitivity_bound = 0.8 #default sensivity threshold
    specificity_bound = 0.6 #default specificity threshold
    
    #Compute two way partical AUC score
    tp_score = get_tproc_score(df, sensitivity_bound, specificity_bound)
