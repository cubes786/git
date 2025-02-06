from fastapi import FastAPI
from typing import Dict
from decimal import Decimal
from VarCalculator import VarCalculator
from Weights import Weights

app = FastAPI()

server = VarCalculator()

@app.get("/GetInstrumentList")
def get_instrument_list():
    return server.GetInstrumentList()

@app.post("/CalculatePortfolioYield")
def calculate_portfolio_yield(weights: Weights):
    return server.CalculatePortfolioYield(weights.weights)

@app.post("/CalculateVar_HistoricalSimulation/{confidence_level}")
def calculate_var_historical_simulation(confidence_level: float, weights: Weights):
    return server.CalculateVar_HistoricalSimulation(weights.weights, confidence_level)

@app.post("/CalculateVar_Parametric/{confidence_level}")
def calculate_var_parametric(confidence_level: float, weights: Weights):
    return server.CalculateVar_Parametric(weights.weights, confidence_level)

@app.get("/CalculateDV01")
def calculate_dv01():
    return server.CalculateDV01()


