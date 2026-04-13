from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.model import train_model
from src.detect import detect_anomalies
from src.visualize import plot_results

data = load_data("data/dataset.csv")

clean = preprocess_data(data)

model = train_model(clean)

preds = detect_anomalies(model, clean)

plot_results(preds)

print("AI Cybersecurity Detection Completed 🚀")