import pandas as pd
import pickle
import numpy as np

class LoyaltyScorePredictor:
    def __init__(self):
        # Load the encoder and model
        with open('models/encoder.pkl', 'rb') as f:
            self.encoder = pickle.load(f)
        with open('models/trained_model.pkl', 'rb') as f:
            self.model = pickle.load(f)

    def predict_loyalty_score(self, input_data):
        # Convert the input data to a DataFrame
        df = pd.DataFrame([input_data])

        # Encode categorical features
        encoded_features = self.encoder.transform(df[['Gender', 'Payment Method', 'Membership Status', 'Preferred Visit Time', 'Region', 'Product Category']])
        encoded_df = pd.DataFrame(encoded_features, columns=self.encoder.get_feature_names_out())
        
        # Combine numeric and encoded features
        numeric_features = df[['Age', 'Total Spent', 'Discount (%)', 'Satisfaction Score', 'Items Purchased','Warranty Extension', 'Revenue','Store Rating']]
        combined_df = pd.concat([numeric_features.reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)

        # Make predictions
        prediction = self.model.predict(combined_df)

        return prediction[0]  # Return the prediction