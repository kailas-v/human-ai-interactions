"""
Basic functions for loading and interacting with the 
Human-AI Interactions Dataset (HAIID).

Author: Kailas Vodrahalli
Version: June 28, 2022
"""
import os
import numpy as np
import pandas as pd


# -- Loading the dataset / tasks --
def load_dataset(path="."):
    """Load the HAIID dataset."""
    dataset_path = os.path.join(path, "haiid_dataset.csv")
    return pd.read_csv(dataset_path, dtype={'job_title':str})

def load_tasks(haiid, task_name, drop_unused=True):
    """Load a subset of the HAIID tasks."""
    loaded_tasks = [load_task(haiid, task_name, drop_unused) for task_name in task_names]
    return df.concat(loaded_tasks, ignore_index=True)

def load_task(haiid, task_name, drop_unused=True):
    """Load an individual HAIID task."""
    tasks = ['art', 'cities', 'sarcasm', 'census', 'dermatology']
    task_name = task_name.lower().strip()
    if task_name not in tasks:
        print(f"Task <{task_name}> not a valid task. Please select one of"\
              f"<{tasks}>.")
        raise

    subset = haiid[haiid.task_name==task_name]

    if drop_unused:
        # drop unused columns depending on dataset
        if task_name == 'dermatology':
            drop_cols = ['gender', 'age', 'programming_experience', 
                         'socioeconomic_status']
        else:
            drop_cols = ['years_of_experience', 'job_title']
        
        return subset[[c for c in subset.columns if c not in drop_cols]]
    return subset


# -- Basic calculations --
def aggregate_output(df, fn, agg_grouping, agg_method, *fn_args, **fn_kwargs):
    if agg_method == 'mean':
        agg_fn = pd.DataFrame.mean
    else:
        agg_fn = lambda x: x

    if agg_grouping=='all':
        output = agg_fn(fn(df, *fn_args, **fn_kwargs))
    elif agg_grouping in df.columns:
        g = df.groupby(agg_grouping)
        output = g.apply(lambda x: agg_fn(fn(x, *fn_args, **fn_kwargs)))
    else:
        print(f"Grouping method <{agg_grouping}> not valid.")
        raise

    return output
def construct_agg_fn(fn, agg_grouping_default, agg_method_default):
    def calc_fn(df, 
           agg_grouping=agg_grouping_default, agg_method=agg_method_default, 
           *fn_args, **fn_kwargs):
        return aggregate_output(df, fn, agg_grouping, agg_method, 
                                *fn_args, **fn_kwargs)
    return calc_fn

def _activation_rate(df, min_to_activate=0.07):
    """min_to_activate in [0,1]"""
    r1 = df.response_1
    r2 = df.response_2
    activated = ((r2-r1).abs()>min_to_activate)
    return activated

def _accuracy(df, stage='response_1'):
    """stage in [response_1, advice, response_2]"""
    responses = df[stage]
    return responses>0

def _correct_confidence(df, stage):
    """stage in [response_1, advice, response_2]"""
    responses = df[stage]
    return responses

def _weight_of_advice(df):
    r1 = df.response_1
    r2 = df.response_2
    a = df.advice
    # to ensure nonzero denominator
    #   r1,r2,a all have 2 decimal places, so 0.001 is chosen
    epsilon = 1e-3 
    return (r2-r1)/(a-r1+epsilon)

activation_rate = construct_agg_fn(_activation_rate, "all", "mean")
accuracy = construct_agg_fn(_accuracy, "all", "mean")
correct_confidence = construct_agg_fn(_correct_confidence, "all", "mean")
weight_of_advice = construct_agg_fn(_weight_of_advice, "all", "mean")



