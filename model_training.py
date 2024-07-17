import autokeras as ak

class ModelTrainer:
    @staticmethod
    def create_model():
        try:
            model = ak.StructuredDataRegressor(max_trials=10, overwrite=True)
            return model
        except Exception as e:
            raise RuntimeError(f"Error creating model: {e}")

    @staticmethod
    def train_model(model, X, y):
        try:
            model.fit(X, y, epochs=10)
            return model
        except Exception as e:
            raise RuntimeError(f"Error training model: {e}")

    @staticmethod
    def evaluate_model(model, X, y):
        try:
            loss, accuracy = model.evaluate(X, y)
            print(f"Loss: {loss}, Accuracy: {accuracy}")
        except Exception as e:
            raise RuntimeError(f"Error evaluating model: {e}")

    @staticmethod
    def save_model(model, path='best_model'):
        try:
            model.export_model().save(path)
        except Exception as e:
            raise RuntimeError(f"Error saving model: {e}")
