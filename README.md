# Human-AI Interactions Dataset

## Overview
This repo provides access to our dataset of over 30,000 Human-AI interactions. 
We recruited crowdworkers and expert dermatologists and asked them to perform a variety of binary classification tasks. 
Participants gave two responses -- their initial impression after seeing the task, and their response after being presented with some "advice." 
This advice was presented as coming from either a human peer or an AI algorithm.
Responses were recorded on a sliding scale, allowing users to indicate both label choice and confidence.

***More details on the recruitment procedure, the tasks, and analysis of the dataset can be found in our papers:***
1. [How humans use AI advice](https://arxiv.org/abs/2107.07015)
    - Contains more details on the tasks we created and the data collection process.
2. [Improving human-AI collaboration](https://arxiv.org/abs/2202.05983)
    - Contains an application of this dataset to modify an AI algorithm to improve human-AI collaboration.



## Files included
* `haiid_dataset.csv`: the dataset of human-AI interactions
* `haiid_dataset_description.csv`: contains descriptions of each column in the dataset (reproduced below on this page)
* `haiid.py`: code for loading the dataset and simple calculations
* `tasks`
    * `art`: files for Art task
    * `census`: files for Census task
    * `cities`: files for Cities task
    * `dermatology`: files for Dermatology task
    * `sarcasm`: files for Sarcasm task


### Example of code use
```python
import haiid
# load all data
df = haiid.load_dataset()
# look at the dermatology task subset
derm_task = haiid.load_task(df, 'dermatology')
# get the activation rate for the dermatology task, averaging across each participant individually
derm_activation_rate = haiid.activation_rate(derm_task, 'participant_id')
```

## Detailed description of dataset columns

The dataset contains the following information: 

| Column Name | Column Values | Column Description |
| ----------- | ----------- | ----------- |
| task_name | {art, cities, sarcasm, census, dermatology} | The name of the task the participant completes. |
| task_instance_id | [1-32] | ID for the task instance. |
| path_to_task |  | Path to task instance data. |
| correct_label |  | The true label of the task instance. |
| incorrect_label |  | The incorrect label the participant sees for this task instance. |
| order_appearing_in_survey | [1-32] | Where this task instance appears in the survey. |
| advice_source | {human, ai} | Where the participant perceives the advice to come from. |
| advice | [-1,1] | Value of the advice recieved by the participant. >0 indicates advice selected the correct label. <0 indicates advice selected the incorrect label. |
| participant_id |  | Unique identifier for the participant. |
| response_1 | [-1,1] | Initial response from the participant (before advice). >0 indicates response selected the correct label. <0 indicates response selected the incorrect label. |
| response_2 | [-1,1] | Final response from the participant (after advice). >0 indicates response selected the correct label. <0 indicates response selected the incorrect label. |
| survey_q1_perceived_advice_accuracy | [0,100] | Survey Q1 -- perceived accuracy of advice (manipulation check 2). |
| survey_q2_helpfulness_of_advice | [0,1] | Survey Q2 -- perceived helpfulness of the advice. (0=not helpful; 1=very helpful) |
| survey_q3_trust_in_advice | [0,1] | Survey Q3 -- how much does the participant trust the advice. (0=no trust; 1=much trust) |
| survey_q4_prefers_human_or_AI | [-1,1] | Survey Q4 -- is a person or AI better at the task. (<0=person; >0=AI) |
| survey_q5_AI_in_life | [0,1] | Survey Q5 -- how much does the person use AI in their life. (0=never; 1=very often) |
| geographic_region |  | Where the participant is geographically located. |
| education | [1,8] | Highest education level achieved. |
| education_description |  | Highest education level achieved (described). |
| gender | {male, female, other/unknown} | Participant's gender. |
| age | [18-81] | Participant's age. |
| programming_experience | {True, False} | Does participant have programming experience. |
| socioeconomic_status | [1,10] | Socioeconomic status of participant. |
| years_of_experience | [0-33] | For dermatologist experts -- years of experience after medical school. |
| job_title | {attending, attending_certified, resident, trainee} | For dermatologist experts -- current job title. |
| perceived_accuracy | {65, 80, 95} | The accuracy level of the advice that is stated to the participants. (It does not necessarily reflect the true accuracy level.) |

## Citation
If you find this work useful or use this dataset in your research, please cite:
```
@inproceedings{vodrahalli2022humans,
  title={Do humans trust advice more if it comes from ai? an analysis of human-ai interactions},
  author={Vodrahalli, Kailas and Daneshjou, Roxana and Gerstenberg, Tobias and Zou, James},
  booktitle={Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society},
  pages={763--777},
  year={2022}
}
```

## Contact
If you have any questions, please feel free to email the authors.
