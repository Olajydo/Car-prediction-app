# Car-prediction-app with Streamlit


# Introduction:

This project aims to predict the selling price of cars using RandomForest algorithm. The prediction model is built using the provided dataset which includes various features such as Car_Name, Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, and Owner. The model is deployed as a web application using Streamlit, allowing users to input car details and obtain the predicted selling price.

# Dataset:

The dataset used for this project contains the following columns:

1. Car_Name: Name of the car.
2. Year: Year of manufacturing.
3. Selling_Price: Selling price of the car (target variable).
4. Present_Price: Present price of the car when new.
5. Kms_Driven: Kilometers driven by the car.
6. Fuel_Type: Type of fuel used by the car (Petrol, Diesel, or CNG).
7. Seller_Type: Type of seller (Dealer or Individual).
8. Transmission: Transmission type (Manual or Automatic).
9. Owner: Number of previous owners.


# Methodology:

1. # Data Preprocessing:
   - Handle missing values.
   - Convert categorical variables into numerical format using one-hot encoding.
   - Split the dataset into features (X) and target variable (y).

2. # Model Building:
   - Implement RandomForestRegressor from the scikit-learn library.
   - Train the model using the training data.

3. # Model Evaluation:
   - Evaluate the model's performance using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.

4. # Deployment:
   - Develop a web application using Streamlit.
   - Create an interface to input car details.
   - Utilize the trained model to predict the selling price.
   - Display the predicted selling price to the user.



# Usage:

To run the application locally, follow these steps:

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit app using `streamlit run app.py`.
4. Input the car details in the provided fields.
5. Click on the "Predict" button to obtain the predicted selling price.



# Conclusion:

This project demonstrates the utilization of RandomForest algorithm to predict car prices based on various features. The deployment of the model as a web application using Streamlit allows users to conveniently predict the selling price of cars by providing relevant information. Further improvements can be made by incorporating additional features and exploring different machine learning algorithms for better prediction accuracy.

