import pickle

class Model:
    @staticmethod

    def load_binary(filename='models/binary_rf.pkl'):
        with open(filename,"rb")as f:
            binary_model=pickle.load(f)
        return binary_model
    @staticmethod
    def load_multi(filename='models/multi_xgb.pkl'):
        with open(filename,"rb")as f:
            multi_model=pickle.load(f)
        return multi_model
