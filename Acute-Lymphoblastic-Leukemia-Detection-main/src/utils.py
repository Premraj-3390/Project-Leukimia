from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def evaluate(y_true, y_pred):
    print("\n=== Model Evaluation ===")
    print(f"Accuracy: {accuracy_score(y_true, y_pred):.4f}")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))
