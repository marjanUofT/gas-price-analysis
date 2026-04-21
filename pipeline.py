import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    df = df.dropna()
    return df

def main():
    df = load_data("data.csv")  # adjust path if needed
    df = clean_data(df)
    print(df.head())

if __name__ == "__main__":
    main()
