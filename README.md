# Kaggle-challenge-2024
## Overview

The goal of this competition is to develop models that can assist in detecting and classifying degenerative spine conditions using lumbar spine MRI images. Participants will create models simulating a radiologist's performance in diagnosing spine conditions.

## Competition Details
Start Date: May 16, 2024
Entry Deadline: October 1, 2024
Team Merger Deadline: October 1, 2024
Final Submission Deadline: October 8, 2024
Winners’ Requirements Deadline: October 28, 2024
Challenge Description
Low back pain, a leading cause of disability worldwide, often results from degenerative spine conditions like spondylosis. This competition, conducted by RSNA and ASNR, explores AI's potential to aid in detecting and classifying these conditions using MRI images.

Participants will focus on classifying five degenerative conditions:

* Left Neural Foraminal Narrowing
* Right Neural Foraminal Narrowing
* Left Subarticular Stenosis
* Right Subarticular Stenosis
* Spinal Canal Stenosis
Severity scores (Normal/Mild, Moderate, Severe) are provided for these conditions across intervertebral disc levels L1/L2 to L5/S1. The dataset, curated from eight sites on five continents, aims to standardize the classification of lumbar spine conditions and support the development of automated tools for accurate disease classification.

## Evaluation
Submissions are evaluated using sample weighted log losses and an any_severe_spinal prediction metric. The sample weights are:

[1] for Normal/Mild
[2] for Moderate
[4] for Severe
Predictions must be in the following format:

```
row_id,normal_mild,moderate,severe
123456_left_neural_foraminal_narrowing_l1_l2,0.333,0.333,0.333
...
```

Missing vertebrae predictions must still be made to avoid errors but won't be scored.

## Submission and Contact
Challenge winners will be recognized at the RSNA 2024 annual meeting. For more information, contact RSNA Informatics staff at informatics@rsna.org.

Note: All deadlines are at 11:59 PM UTC. The organizers reserve the right to update the contest timeline if necessary.

## Enviroment setup
```
conda env create -f environment.yml
conda activate kaggle_challenge
```

## Data download
Data should be downloaded from https://www.kaggle.com/competitions/rsna-2024-lumbar-spine-degenerative-classification/data and saved in the `data` folder in the root of this repo. The data folder is in the .gitignore to avoid uploading data to github. 