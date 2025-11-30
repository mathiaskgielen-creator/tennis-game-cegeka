# To run the tennis game, a python installation is required
# I used Python version 3.13.7

# Install packages
python -m pip install --user -r requirements.txt

# Run tests
python -m pytest game_test.py -q

# Run game
python game.py

# Player 1 controls with < and > keys
# Player 2 controls with q and d keys