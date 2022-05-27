from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import List
import logging
from models.predict import Predictor

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("dummy_ml_log.log")
file_handler.setFormatter(formatter)


stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

app = FastAPI()

predictor = Predictor()

class Sample(BaseModel):
    active: bool
    balance: float = 0.0
    email: str
    age: int
    name: str
    gender: str

# Path operation decorator
@app.get("/")
# Path operation function
async def root():
    logger.debug('Hello World was executed')
    logger.info('Hello World was executed')
    return {"message": "Hello World"}

@app.get("/validate_data")
async def validate_data():
    logger.debug('Data was validated')
    logger.info('Data was validated')
    return {"message":"Data was validated",
            "valid":"All true"}

@app.post("/predict", response_model=Sample)
async def predict(sample: Sample = Body(..., embed=True)):
    result = sample.dict()
    s = ""
    for k,v in result.items():
        s += f'--{k}:{v}--'
    logger.info(f'Sample: {s}')
    logger.debug(f'Sample: {s}')
    return result

sample_example = { "sample": {
        "active": True,
        "balance": 1564.48,
        "email": "leanne.perry@gmail.com",
        "age": 21,
        "name": "Leanne Perry",
        "gender": "female"
}
        }

@app.get("/info")
async def info():
    return {
        "message": "DummyML App, needs to send a user via POST method",
        "data_example": sample_example
        }

@app.post("/predict_result")
async def predict(sample: Sample = Body(..., embed=True)):
    result = sample.dict()
    #s = ""
    #for k,v in result.items():
    #    s += f'--{k}:{v}--'
    #logger.info(f'Sample: {s}')
    #logger.debug(f'Sample: {s}')
    prediction = predictor.make_prediction(result)
    return prediction
