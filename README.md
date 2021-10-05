# 2048
# 2048 is played on a gray 4×4 grid,
with numbered tiles that slide when a player moves them
using the four arrow keys. Every turn, a new tile will randomly appear in an empty spot on the
board with a value of either 2 or 4. Tiles slide as far as possible in the chosen direction until they
are stopped by either another tile or the edge of the grid. If two tiles of the same number collide
while moving, they will merge into a tile with the total value of the two tiles that collided. The
resulting tile cannot merge with another tile again in the same move. If a move causes three
consecutive tiles of the same value to slide together, only the two tiles farthest along the
direction of motion will combine. If all four spaces in a row or column are filled with tiles of the
same value, a move parallel to that row/column will combine the first two and last two.


steps used :
1. setup an empty board 
2. function for merging rows to left, right, up and down
3. random values to be filled on initial board
4. take the input (each move), check for validity and perform the corresponding merging. 
5. add a random value to the board after each move
6. functions for checking win or lose

screenshots: 
code 
![Annotation 2021-10-05 114406](https://user-images.githubusercontent.com/91930683/135972599-058b50c3-9b81-4740-a9d3-4d50ee603fa5.png)

output
![Annotation 2021-10-05 121754](https://user-images.githubusercontent.com/91930683/135973835-32800dc2-d3bd-4e57-ab34-7a82df1ddca6.png)
![Annotation 2021-10-05 113910](https://user-images.githubusercontent.com/91930683/135972899-3e9811df-af9a-433c-8538-9d93a1397708.png)
