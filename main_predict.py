import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Check for GPU availability
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# --- 1. Data Preparation ---
def generate_synthetic_data(start_year=1975, end_year=2025):
    """Simulate 50 years of daily temperature data for northwest India."""
    dates = pd.date_range(start=f"{start_year}-01-01", end=f"{end_year}-04-03", freq="D")
    # Synthetic temperature: seasonal pattern + noise + urban warming trend
    days = np.arange(len(dates))
    temp = 25 + 10 * np.sin(2 * np.pi * days / 365) + np.random.normal(0, 2, len(dates)) + 0.02 * (days / 365)
    return pd.DataFrame({"date": dates, "temp": temp})

def prepare_time_series(data, lookback=30):
    """Convert data into sequences for LSTM."""
    scaler = MinMaxScaler()
    temp_scaled = scaler.fit_transform(data["temp"].values.reshape(-1, 1))
    X, y = [], []
    for i in range(lookback, len(temp_scaled)):
        X.append(temp_scaled[i-lookback:i])
        y.append(temp_scaled[i])
    return np.array(X), np.array(y), scaler

# --- 2. Urbanization Analysis ---
def estimate_urbanization(dates):
    """Simulate urbanization trend (e.g., from satellite imagery)."""
    # Proxy: linear increase in urban area from 5% to 30% over 50 years
    years = np.array([d.year for d in dates])
    urban_percent = 5 + 25 * (years - 1975) / 50
    return urban_percent

# --- 3. LSTM Model ---
class WeatherLSTM(nn.Module):
    def __init__(self, input_size=1, hidden_size=64, num_layers=2):
        super(WeatherLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])  # Take the last time step
        return out

def train_model(model, X_train, y_train, epochs=50, batch_size=32):
    """Train the LSTM model on GPU."""
    model = model.to(device)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    X_train_tensor = torch.FloatTensor(X_train).to(device)
    y_train_tensor = torch.FloatTensor(y_train).to(device)

    for epoch in range(epochs):
        model.train()
        for i in range(0, len(X_train), batch_size):
            X_batch = X_train_tensor[i:i+batch_size]
            y_batch = y_train_tensor[i:i+batch_size]
            optimizer.zero_grad()
            outputs = model(X_batch)
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
    return model

# --- 4. Prediction and Evaluation ---
def predict_weather(model, X_test, scaler):
    """Make predictions and inverse transform."""
    model.eval()
    with torch.no_grad():
        X_test_tensor = torch.FloatTensor(X_test).to(device)
        predictions = model(X_test_tensor).cpu().numpy()
    return scaler.inverse_transform(predictions)

# --- Main Execution ---
# Generate synthetic data (replace with real IMD/NASA data)
data = generate_synthetic_data()
urbanization = estimate_urbanization(data["date"])

# Prepare data for LSTM
lookback = 30
X, y, scaler = prepare_time_series(data, lookback)
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Train LSTM model
model = WeatherLSTM(input_size=1, hidden_size=64, num_layers=2)
model = train_model(model, X_train, y_train, epochs=50)

# Predict and evaluate
y_pred = predict_weather(model, X_test, scaler)
y_test_actual = scaler.inverse_transform(y_test)

# Calculate precision
errors = np.abs(y_pred - y_test_actual)
mean_error = np.mean(errors)
print(f"Mean Absolute Error: {mean_error:.2f}°C")
if mean_error <= 4:
    print("Precision within ±4°C achieved!")
else:
    print("Precision exceeds ±4°C; further tuning needed.")

# --- 5. Visualization ---
plt.figure(figsize=(12, 6))
plt.plot(data["date"][train_size+lookback:], y_test_actual, label="Actual Temp")
plt.plot(data["date"][train_size+lookback:], y_pred, label="Predicted Temp")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Prediction for Northwest India")
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(data["date"], urbanization, label="Urbanization (%)")
plt.xlabel("Date")
plt.ylabel("Urbanization Percentage")
plt.title("Estimated Urbanization Trend (1975-2025)")
plt.legend()
plt.show()
