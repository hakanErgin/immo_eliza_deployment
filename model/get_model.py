import pickle

def get_model():
    filename = 'model/finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model