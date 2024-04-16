import streamlit as st
import pickle

model = pickle.load(open('C:/Users/JOSH/2023_projects/car_price_prediction/random_forest_model.pkl', 'rb'))

def main():
    st.title('Car Price Prediction Solution')

    #input variable
    Year = st.text_input('Year')
    Present_Price = st.text_input('Present_Price')
    Kms_Driven = st.text_input('Kms_Driven')
    Owner = st.text_input('Owner')
    Fuel_Type_Diesel = st.text_input('Fuel_Type_Diesel')
    Fuel_Type_Petrol = st.text_input('Fuel_Type_Petrol')
    Seller_Type_Individual = st.text_input('Seller_Type_Individual')
    Transmission_Manual = st.text_input('Transmission_Manual')

    if st.button('Predict'):
        makeprediction = model.predict([[Year, Kms_Driven, Present_Price, Owner, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
        output = round(makeprediction[0], 2)
        st.success('You sell your car at {}'.format(output))

if __name__ == '__main__':
    main()
