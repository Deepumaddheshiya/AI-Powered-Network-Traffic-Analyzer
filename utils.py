import os
import joblib
import numpy as np
import pandas as pd

# Get current project directory dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "rf_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

def load_model():
    """Load model and scaler safely using relative paths."""
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")
    if not os.path.exists(SCALER_PATH):
        raise FileNotFoundError(f"Scaler file not found at: {SCALER_PATH}")

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return model, scaler


def align_and_scale_features(df_features, scaler):
    if not hasattr(scaler, "mean_"):
        raise ValueError("Scaler is not fitted.")

    expected_n = len(scaler.mean_)

    if isinstance(df_features, pd.DataFrame):
        X = df_features.values
    else:
        X = np.array(df_features)

    if X.ndim == 1:
        X = X.reshape(1, -1)

    if X.shape[1] > expected_n:
        X = X[:, :expected_n]
    elif X.shape[1] < expected_n:
        pad = np.zeros((X.shape[0], expected_n - X.shape[1]))
        X = np.hstack([X, pad])

    return scaler.transform(X)


def predictions_to_labels(preds):
    if preds.dtype.kind in 'iuf':
        return np.array(["attack" if int(p) == 1 else "normal" for p in preds])
    return preds.astype(str)
