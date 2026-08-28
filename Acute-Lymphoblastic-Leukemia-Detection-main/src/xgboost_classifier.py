import xgboost as xgb

def train_xgboost(X_train, y_train, X_val, y_val):
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dval = xgb.DMatrix(X_val, label=y_val)

    params = {
        "objective": "binary:logistic",
        "eval_metric": "logloss",
        "max_depth": 4,
        "learning_rate": 0.05,
        "tree_method": "hist",
        "device": "cuda"
    }

    evals_result = {}

    model = xgb.train(
        params=params,
        dtrain=dtrain,
        num_boost_round=1000,
        evals=[(dval, "validation")],
        early_stopping_rounds=50,
        evals_result=evals_result
    )

    return model, evals_result

def predict_xgboost(model, X_test):
    dtest = xgb.DMatrix(X_test)
    preds = model.predict(dtest)
    return (preds > 0.5).astype(int)
