# Receipt_Matching_DS_Challenge

# Model Development Approach 
Please refer to "Receipt_Matching_DS_Challenge_Model_Development.ipynb" for development code

## Steps:- 
1. Data loading
2. Flag creation and Event rate check (~7.12%)
3. Correlation Check
4. Multicollinearity check
5. EDA (Bivariate - woe and event rate)
6. Dropped the variables 'DifferentPredictedDate', 'DifferentPredictedTime' and'DateMappingMatch' on the basis of points 2,3 and 4. Kept only 'DateMappingMatch', 'AmountMappingMatch', 'DescriptionMatch', 'TimeMappingMatch', 'PredictedNameMatch', 'ShortNameMatch', 'PredictedAmountMatch', 'PredictedTimeCloseMatch'
7. Train-Test (30%) split
8. As it was a rare event model or data had a class imbalance I applied SMOTE/Oversampling technique on Train data
9. Build mutiple models with hyperparameter tuning (grid search CV) using different algo's - Logistic Regression, Random forest,  Gradient Boosting, SVM, KNN, SVM and ANN
10. Tested each of the models performance on "Test" (unbiased original sample)
11. Random forest outperformed all other models with best performance with ROC of 81 (Note: Please do not test your model on a sample taken out of oversampled data as it will lead to misleading results. Our models should always be tested on original/unbiased/untouched test set as this set best represents the real time data)

ROC Value:  0.8103408671683036


                      precision    recall  f1-score   support
        
                   0       0.97      0.90      0.93      3354
                   1       0.34      0.68      0.45       257
        
        
        
            accuracy                           0.88      3611
           macro avg       0.66      0.79      0.69      3611
        weighted avg       0.93      0.88      0.90      3611
        



![image](https://github.com/AmitKumar25011991/Receipt_Matching_DS_Challenge/assets/141259189/6dece655-34f7-475f-abb1-7c1d5ae01d2d)

11.Importance is plotted. Importance plot shows good linear trend i.e., our model doesn't give undue or lot of importance of 1 or 2 variables in data. It relies on mutiple variables for performance thus avoiding generalization.

![image](https://github.com/AmitKumar25011991/Receipt_Matching_DS_Challenge/assets/141259189/d815ddb8-9285-4e77-b64d-3e62e6db7728)



# Model Scoring 
I have created a file "Model_Scoring.py" which takes an "csv" input from "Input" folder, scores the transactions, sorts them basis scores or probabilities (with receipts having highest scores on top) and generates an output file "Scored.csv" which gets saved/stored in "Output" folder.

# How to run scoring file
Please run "Model_Scoring.py". On running using command "python Model_Scoring.py", it will automatically pick the file from the input folder and save the scored file "Scored.csv" in putput folder

# Observations from model results
1. ShortNameMatch (if short name matches or have higher % then most likely receipt matches) and DiscriptionMatch (Higher the values/percentage match, higher the chnace of receipt matching) turned out be most important variables as is evident from "woe" and "event rate" graphs in EDA
2. PredictedNameMatch (% match is higher may lead to higher receipt match), TimeMappingMatch and PredictedTimeCloseMatch have middling ore moderate importance indicating significant portion of the distribution has an impact on receipt matching

# Recommendations to improve results
1. If possible/available, please capture more variables like type of trasaction etc.. These are all trasaction related variables which will help us match transactions basis their values.
These discriptors regarding transactions can be extracted using 'OCR' techniques
2. Please bring more gradation in confidence scores as currently the cofidence scores are concetrated which might lead to overfitting
3. Elemenmts in the image: If no of elements present in the receipts are captured are used for matching the transactions. This can turn out be an important indicator
4. Please capture more variation of receipts, may be across departmets to help bring in variation in the data to prevent the algorithm from genralizing








