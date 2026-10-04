from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# CSV file project root mein honi chahiye
data = pd.read_csv(BASE_DIR / "house_price.csv")


X = data[[
    "bedrooms",
    "bathrooms",
    "sqft_living",
    "sqft_lot",
    "floors",
    "waterfront",
    "view",
    "condition",
    "sqft_above",
    "sqft_basement",
    "yr_built",
    "yr_renovated",
    "street",
    "city",
    "statezip",
    "country"
]]

y = data["price"]


# Categorical columns
col = [
    "street",
    "city",
    "statezip",
    "country"
]


# OneHotEncoder
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            col
        )
    ],
    remainder="passthrough"
)


# Random Forest Model
model = Pipeline([
    (
        "preprocessor",
        preprocessor
    ),

    (
        "regressor",
        RandomForestRegressor(
            n_estimators=200,
            max_depth=8,
            min_samples_leaf=2,
            random_state=42
        )
    )
])


# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


# Train
model.fit(X_train, y_train)


# Accuracy / R2
predict = model.predict(X_test)

r2 = r2_score(y_test, predict)

print("R2 Score:", round(r2, 4))


def predict_house(data):
    """
    data = dictionary containing house details
    """

    new_house = pd.DataFrame([data])

    result = model.predict(new_house)

    return result[0]