# Predicting Churn - TopBank

In this project we perform an exploratory data analysis in the data from TopBank client's database in order to select the most important features that will help us predict the probability of a client churning.
We use an XGBoost Classifier for the prediction and we discuss 3 possible business scenarios and a baseline scenario based on a random model, always using a total available investment of $10,000. 

In these scenarios, we want to give a financial incentive to a client identified as an exiting client in the hope that it will retain him/her as a client. The first 2 scenarios and the baseline random model assume a simplified case where $100 gift cards are given with 100% effectiveness, i.e., giving a gift card will always make the client stay.

- Our baseline model randomly selects 100 clients from our database and gives the $100 gift cards, assuming the best we can do is to predict TopBank's average churn rate;
- In the first scenario, we give $100 gift cards to the 100 clients most likely to churn (highest churning probability as predicted by our AI model);
- In the second, we give $100 gift cards to the highest LTV clients classified as churning (P(churn) > threshold);


Finally, in the last (more realistic) case we rank our clients based on their churning probability as divide them into 4 groups:
- In the first, we assume they are very likely to churn, independent of any (reasonable) financial incentive;
- The second group is assumed to have a churning probability high enough that $100 gift cards will not be enough, but they would stay with a $200 incentive;
- The third group is similar to the previous scenarios, where the $100 gift card garantees the client will stay;
- And finally, in the fourth group we say that if a client is predicted to churn, a $50 gift card is enough of an incentive to keep him/her one more year.

This final case is much more challenging than the others given the freedom for choosing which clients to give the gift cards with different values.
We solve this problem using the 0-1 Knapsack algorithm. Given the $10,000 total investment constraint and the clients with different (LTV, gift card value) combinations, this fits perfectly in the description of the Knapsack problem.

# Results

Our final result shows that we are more than 4 times better in predicting churning clients compared to the baseline model, which results in a financial gain more than 22 times the baseline.

### Description of the Data Set:
**RowNumber**: corresponds to the record (row) number and has no effect on the output.  
**CustomerId**: contains random values and has no effect on customer leaving the bank.  
**Surname**: the surname of a customer has no impact on their decision to leave the bank.  
**CreditScore**: can have an effect on customer churn, since a customer with a higher credit score is less likely to leave the bank.  
**Geography**: a customer’s location can affect their decision to leave the bank.  
**Gender**: it’s interesting to explore whether gender plays a role in a customer leaving the bank.  
**Age**: this is certainly relevant, since older customers are less likely to leave their bank than younger ones.  
**Tenure**: refers to the number of years that the customer has been a client of the bank. Normally, older clients are more loyal and less likely to leave a bank.  
**Balance**: also a very good indicator of customer churn, as people with a higher balance in their accounts are less likely to leave the bank compared to those with lower balances.  
**NumOfProducts**: refers to the number of products that a customer has purchased through the bank.  
**HasCrCard**: denotes whether or not a customer has a credit card. This column is also relevant, since people with a credit card are less likely to leave the bank.  
**IsActiveMember**: active customers are less likely to leave the bank.  
**EstimatedSalary**: as with balance, people with lower salaries are more likely to leave the bank compared to those with higher salaries.  
**Exited**: whether or not the customer left the bank. (0=No,1=Yes)

Original Data Set:
https://www.kaggle.com/mervetorkan/churndataset

Descricao do projeto aqui:
https://sejaumdatascientist.com/predicao-de-churn/