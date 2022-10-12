import pickle


def Star_prediction1(features):
    pickled_model = pickle.load(open('StarRestaurant_prediction1.pkl', 'rb'))
    star_rate = str(round(list(pickled_model.predict([features]))[0]))

    return str("Rating may be " + star_rate)
test_features=[4093, 88, 1766, 200, 4, 0, 0, 2]
Star_prediction1(test_features)
