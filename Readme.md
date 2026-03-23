# Pong
Final project for CST8279. This is my own version of
pong leveraging pygame (https://www.pygame.org/wiki/about)

This is a two player game, with each player sharing the same keyboard. 
Player 1 uses W and S to move the paddle up and down, and Player 2 users the Up and Down keys.

The scoreboard increments after each point, and the game restarts.


### These were my requirements
Requirements:

- This should be as close as we can get to the original 1972 version of Pong.
- The keyboard should allow for two players. Player Two uses the up/down directional keys, and Player 1 uses W/S
- There should be a scoreboard visible as well.


### Design considerations
As a nostalgic note, There use to be a game played in the browser in the early 2000s called
slime volleyball, and it could be played with two players on one keyboard. I think the
playability of that game influenced me here. We can forget the fact that it was over 20
years ago and move on I suppose :)

I also decided to not use turtle, and use a different module, pygame, in this case. Somewhat as an additional challenge,
and I guess the other part as I wanted something a bit more aesthetically pleasing.

This also targets Python 3.10, which is compatible with Pygame. 3.14 didn't really work for me.