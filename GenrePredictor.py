import librosa
import librosa.display
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from keras import models
from keras import layers
import pickle

class GenrePredictor:

    def __init__(self):
        # Load the ML model
        self.model = models.load_model('cmodel.62-0.6394.h5')

    def load_audio(path):
        y, sr = librosa.load(path, mono=True, duration=3)
        return y, sr

    def extract_features(y, sr):
        features = []
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        rmse = librosa.feature.rms(y=y)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        features.append([np.mean(chroma_stft), np.mean(rmse), np.mean(spec_cent), np.mean(spec_bw), np.mean(rolloff), np.mean(zcr)]+[np.mean(mfcc[i]) for i in range(len(mfcc))])
        return np.array(features)

    scaler = None

    with open('scaler.o', 'rb') as f:
        scaler = pickle.load(f)

    GENRES = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

    def predict_genre(path):
        print("Loading audio")
        audio, sr = load_audio(path)
        print("Getting features")
        features = extract_features(audio, sr)
        X = scaler.transform(np.array(features, dtype = float))
        print("Predicting...")
        predictions = model.predict(X)

        prediction_object = []
        for i, prediction in enumerate(predictions[0]):
            prediction_object.append({"genre":GENRES[i], "certainty": float(f'{prediction:.2f}')})
        return prediction_object

#genre = predict_genre("./blues_99-5.wav")