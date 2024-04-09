**A Stroke Prediction Model**


This project, a course evaluation requirement for Machine Learning Labs with Python at Data ScienceTech Institute, creates a python machine learning model learned on a select dataset to predict a patient’s stroke status given a set of health, physical and social attributes. The data is derived from the popular stroke dataset and the model is based on scikit-learn machine learning package. 

Stroke is a medical condition caused by death of brain cells that atrophied due to poor blood flow to the brain arising from a bleeding or flow restriction. The dataset is imbalanced with respect to stroke occurence, which was in the minority class. The Synthetic Minority Over-sampling Technique (SMOTE) is used to reduce the impact of imbalance on model learning and its predictive outputs. 

The listed classifiers were evaluated to find a fit with the project's preference for a model with predictive qualities that delivers a balanced perspective in a medical use case.
* Logistic Regression (LR)
* K-Nearest Neighbors (KNN)
* Decision Tree (DT)
* Random Forest (RF)
* SVM

The metric used to select the preferred classifier was the Matthews Correlation Coefficient (MCC). A validation and test set was important in scoring model performance and to avoid quantifying a model with an overly optimistic performance. This conservative approach is further reflected in the use of imbalance- pipelines to avoid common pitfalls and anti-patterns that occur when using scikit-learn. Both the data centric approach and the pipeline management approach were central to the aim of avoiding data leakage during training to avoid degraded performance downstream when actual novel data is used during production.


**The following are available in this repository:**
* A jupyter notebook documenting reproducible steps for the project's analysis and approach 
* A report that provides a summary of the project's methodology and results
* Sourcefiles to simplify the process of building a docker image for model deployment
* Workflow actions that creates a docker image and saves it in a private AWS repository as part of an automated CI/CD process.


**Using the Model:** 

To use the model, there are several data processing steps you might want to take note of:

* Additional features were derived from from selected variables, in the initial datasets, each with categories based on binned values
* data processing steps included name change and category remapping for selected variables 
* Column Transformers were utilised to preprocess categorical variables with one hot encoding and to scale numeric variables with a standard scale

These are easily identifiable within the notebook, however, it imposes the requirement that similar preprocessing steps be applied to test data or to ensure novel data have column names and indexes that match what the model expects.

**Improvements or Found a Bug?**

We would love to have your feedback in the comments. 

