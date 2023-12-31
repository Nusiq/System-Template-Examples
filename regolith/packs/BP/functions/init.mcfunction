# The function that initializes basic scoreboards, fake players, gamerules etc.

# Commonly used scoreboards
# Temporary variables
scoreboard objectives add tmp dummy
for <i 1..11 1>:
    scoreboard objectives add tmp`eval:i` dummy

# The scoreboard for the fake players
scoreboard objectives add var dummy

# The scoreboard for temporary variables stored in the fake players
scoreboard objectives add tmp_var dummy

# The scoreboard for numbers
scoreboard objectives add const dummy
for <i -1..11 1>:
    scoreboard players set _`eval:i` const `eval:i`