from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


def preprocess_data(df, target):
    # Separate features & target
    X = df.drop(columns=[target])
    y = df[target]

    # Drop rows where target is missing
    valid_idx = y.notna()
    X = X.loc[valid_idx]
    y = y.loc[valid_idx]

    # Column types
    num_cols = X.select_dtypes(include="number").columns.tolist()
    cat_cols = X.select_dtypes(exclude="number").columns.tolist()

    # Pipelines
    num_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ])

    cat_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("num", num_pipeline, num_cols),
        ("cat", cat_pipeline, cat_cols)
    ])

    X_processed = preprocessor.fit_transform(X)

    return train_test_split(
        X_processed, y, test_size=0.2, random_state=42
    )
