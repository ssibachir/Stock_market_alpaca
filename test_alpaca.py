from lumibot.strategies.examples import Momentum


BASE_URL = "https://paper-api.alpaca.markets"
class AlpacaConfig:
    API_KEY = "PKMCM1ME8L1FC0AMCWVI"
    API_SECRET = "frSl1ePObqoWoX2LdLUQu6mpEObSpeJzkYSOtRot"
ALPACA_CREDS = {
    "API_KEY": AlpacaConfig.API_KEY,
    "API_SECRET": AlpacaConfig.API_SECRET,
    "PAPER": True
}

print('Hello')
