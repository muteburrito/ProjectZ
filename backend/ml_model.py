from simple_rnn import NumberPredictor

def predict_sequence(n):
    predictor = NumberPredictor()
    predictor.train()
    return predictor.predict_next_10(n)

predict_sequence(4)