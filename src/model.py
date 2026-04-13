from sklearn.ensemble import IsolationForest

def train_model(X):
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(X)
    return model