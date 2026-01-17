import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

# ===============================
# DYNAMIC PROJECT ROOT (FIX)
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(MODEL_DIR, "rf_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

# ===============================
# SYNTHETIC TRAINING DATA
# ===============================
n = 1000
bytes_ = np.random.randint(200, 200000, n)
packets = np.random.randint(1, 2000, n)
duration = np.random.uniform(0.001, 20.0, n)

# Labels: simple logic for demo
labels = ((bytes_ > 100000) | (packets > 1500)).astype(int)

X = pd.DataFrame({
    "bytes": bytes_,
    "packets": packets,
    "duration": duration
})
y = labels

# ===============================
# SCALER
# ===============================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ===============================
# MODEL
# ===============================
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_scaled, y)

# ===============================
# SAVE FILES
# ===============================
joblib.dump(model, MODEL_PATH)
joblib.dump(scaler, SCALER_PATH)

print("✅ Training completed successfully")
print("📁 Model saved at:", MODEL_PATH)
print("📁 Scaler saved at:", SCALER_PATH)
