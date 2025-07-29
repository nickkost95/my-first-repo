
from app.rps import determine_winner

def test_winner():
    assert determine_winner("rock", "rock") == "TIME GAME"
    assert determine_winner("rock", "paper") == "COMPUTER WINS"
    assert determine_winner("rock", "scissors") == "PLAYER WINS"
    assert determine_winner("paper", "rock") == "PLAYER WINS"
    assert determine_winner("paper", "paper") == "TIME GAME"
    assert determine_winner("paper", "scissors") == "COMPUTER WINS"
    assert determine_winner("scissors", "rock") == "COMPUTER WINS"
    assert determine_winner("scissors", "paper") == "PLAYER WINS"
    assert determine_winner("scissors", "scissors") == "TIME GAME"

