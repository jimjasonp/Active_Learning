from model_training import saved_model,X_test
import pickle

# Load the pickled model 
model_from_pickle = pickle.loads(saved_model) 
  
# Use the loaded pickled model to make predictions 
model_from_pickle.predict(X_test) 

