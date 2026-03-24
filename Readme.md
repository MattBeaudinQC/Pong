# Pong
Final project for CST8279. This is my own version of
pong leveraging pygame (https://www.pygame.org/wiki/about)

<img width="300" alt="pong_1" src="https://github.com/user-attachments/assets/d5a28b06-fa37-472e-9f23-4792c13c1ebe" />

### Features

- This should be as close as we can get to the original 1972 version of Pong.
- The keyboard allows for two players. Player Two uses the up/down directional keys, and Player 1 uses W/S
- There is a scoreboard. 

### Setup notes
Pong requires `pygame`, `random` and `sys` packages, and runs on Python 3.10. You will not be able to deploy `pygame` on the latest version of python anyways, as there is an exception related to `wheel`.

### Design considerations
As a nostalgic note, There use to be a game played in the browser in the early 2000s called
slime volleyball, and it could be played with two players on one keyboard. I think the
playability of that game influenced me here. We can forget the fact that it was over 20
years ago and move on I suppose :)

I also decided to not use turtle, and use a different module, pygame, in this case. Somewhat as an additional challenge,
and I guess the other part as I wanted something a bit more aesthetically pleasing.

This also targets Python 3.10, which is compatible with Pygame. 3.14 didn't really work for me.
