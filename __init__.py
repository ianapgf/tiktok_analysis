# tiktok_analysis/__init__.py

# Importações de módulos do pacote
from .data_processing import DataProcessor
from .model_training import ModelTrainer
from .campaign import Campaign

# Lista de módulos a serem exportados
__all__ = ['DataProcessor', 'ModelTrainer', 'Campaign']

print("Pacote 'tiktok_analysis' inicializado.")
