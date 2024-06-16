## Autism-Spectrum-Disorder-Prediction
This repository contains code for many machine learning models designed to predict Autism-Spectrum-Disorder-Prediction with high accuracy and compare them to findout the best model.

## How it Works
There are 7 models I have selected and compared through various parameters like Accuracy, Precision, Recall and F1-Score. These 7 models are ANN, Decision Tree, Random Forest, SVM, Logistic Regression, Naive Bayes and KNN.

## Dataset
The dataset we are using is the UCI Machine Learning Repository provided by Fadi Fayez Thabtah.<br>
The child dataset consists of 292 records, with 141 classified as ASD and 151 as non-ASD.<br>
The adolescent dataset contains 104 records, with 63 classified as ASD and 41 as non-ASD.<br>
The adult dataset comprises 704 records, with 189 classified as ASD and 515 as non-ASD.<br>
Overall, there are 21 features, including 10 questions related to behavioral information (A1-A10), 10 demographic attributes, and one class label indicating ASD prediction.
### Properties
i) A1_Score to A10_Score: Scores derived from the Autism Spectrum Quotient (AQ) 10-item screening tool.<br>
ii) age: Patient's age in years.<br>
iii) gender: Patient's gender.<br>
iv) ethnicity: Patient's ethnic background.<br>
v) jaundice: Indicates whether the patient had jaundice at birth.<br>
vi) autism: Indicates whether an immediate family member has been diagnosed with autism.<br>
vii) country_of_res: Patient's country of residence.<br>
viii) used_app_before: Indicates whether the patient has previously undergone a screening test.<br>
ix) result: Score obtained from the AQ1-10 screening test.<br>
x) age_desc: Description of the patient's age.<br>
xi) Class/ASD: Classified result represented as 0 (No) or 1 (Yes). This column serves as the target variable, and values should be submitted as 0 or 1 only during submission.<br>
These are the useful properties that we are using in our model, but it has 2 extra property id and relation.

## Installation
You can run it with the newest updates but it needs several changes, so I will suggest to follow my lead and do the following.
1. Use Anaconda
2. Make new environment to keep the selected updated libraries seperate from newest one.
3. Make matplotlib : 3.5 and python 3.9.18 in new environment.
4. For other Libraries just run the code and install accordingly.

Train dataset has been used to train the model and calculate the mentioned 4 parameters. You can use the test dataset to predict the result like the patient is autistic or not. You can change the test dataset according to your need or to predict in real world, but don't change in train dataset. Train dataset is collected directly from patients so it is absolutely correct.

## Screenshots
### Dataset
![dataset](https://github.com/UnknownCode01/Autism-Spectrum-Disorder-Prediction/blob/main/Screenshots/Picture1.jpg)
![ASD](https://github.com/UnknownCode01/Autism-Spectrum-Disorder-Prediction/blob/main/Screenshots/Picture2.jpg)
                        

### System Architecture

![system architecture](https://github.com/UnknownCode01/Autism-Spectrum-Disorder-Prediction/blob/main/Screenshots/Picture3.jpg)

### Comparison of Accuracy
![accuracy](https://github.com/UnknownCode01/Autism-Spectrum-Disorder-Prediction_Model/blob/main/Screenshots/Picture4.jpg)

### Comparison of Precision
![precision](https://github.com/UnknownCode01/Autism-Spectrum-Disorder-Prediction_Model/blob/main/Screenshots/Picture5.jpg)

### Comparison of Recall
![recall](https://github.com/UnknownCode01/Autism-Spectrum-Disorder-Prediction_Model/blob/main/Screenshots/Picture6.jpg)

### Comparison of F1-Score
![f1-score](https://github.com/UnknownCode01/Autism-Spectrum-Disorder-Prediction_Model/blob/main/Screenshots/Picture7.jpg)

### Comparison of Performance
![performance for no asd](https://github.com/UnknownCode01/Autism-Spectrum-Disorder-Prediction_Model/blob/main/Screenshots/Picture8.jpg)

![performance for asd](https://github.com/UnknownCode01/Autism-Spectrum-Disorder-Prediction_Model/blob/main/Screenshots/Picture9.jpg)



## Contributing

Contributions are always welcome!

See `README.md` for ways to get started.

Please adhere to this project's `During your interaction with the project, make sure to maintain respectful communication, collaborate positively with other contributors (if applicable), and follow any contribution guidelines provided by the project maintainers. If you encounter any issues or have questions, consider reaching out to the project maintainers for guidance.`.

## Developers interested in contributing to the project can follow these steps:

- Fork the repository.
- Clone the forked repository to your local machine.
- Create a new branch for your feature or bug fix.
- Make your changes and submit a pull request to the main repository.


## Known Issues
Accuracy: the highest accuracy from various model is 83.75%.

## Future Update
We are continuously working to improve the Autism-Spectrum-Disorder-Prediction. Future updates may include enhancements to the model architecture, optimization of training procedures, and integration of additional datasets for improved performance.

