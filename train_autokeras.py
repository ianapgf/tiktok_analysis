from tiktok_analysis.data_processing import DataProcessor
from tiktok_analysis.model_training import ModelTrainer

def main():
    csv_path = 'data/tiktok_creators_fictitious.csv'
    df = DataProcessor.load_data(csv_path)
    X, y = DataProcessor.preprocess_data(df)

    model = ModelTrainer.create_model()
    model = ModelTrainer.train_model(model, X, y)

    ModelTrainer.evaluate_model(model, X, y)
    ModelTrainer.save_model(model)

if __name__ == '__main__':
    main()
