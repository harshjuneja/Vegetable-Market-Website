import joblib


def predict_cost(item_id, temperature, month, fresh, disasters):
    model = joblib.load('train_model.pkl')
    cost = model.predict([[item_id, temperature, month, fresh, disasters]])
    print("Prediction Result:", cost)
    return cost
