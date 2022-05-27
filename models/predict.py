import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("predictions.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Predictor:
    def __init__(self) -> None:
        pass

    def make_prediction(self, sample):
        if sample['age'] > 20 and sample['balance'] > 1000:
            prediction = 1
        else:
            prediction = 0
        
        logger.debug(f'Age=({sample["age"]}), Balance=({sample["balance"]}), Prediction=({prediction})')

        return prediction
        