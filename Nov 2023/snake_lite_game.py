import tkinter as TK
import random

WIDTH = 400
HEIGHT = 400
GRID_SIZE = 20

#Window is the way we create a title for game when using this phrase which can also be extended to make a canvas of it's own but for more formal things with no animations or moving objects.
window = TK.Tk()
window.title = ("Snake Game 1")

#This is our score chart which is what we will be using for our score
score = 0
score_label = TK.Label(window, text=f"Score: {score}", font=("Arial", 16))
score_label.pack()

#This is how we count our score and get it to the score chart
score += 1
score_label.config(text=f"Score: {score}")

#This is canvas the window of games and animations when using tkinter in python
canvas = TK.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

#This is the base head of the snake since it hasn't ate anything yet
snake = [(100, 100)]  
snake_squares = []

#Here is the function for making increasing the snakes body per item it eats, so this can show how the snake slowly evolves ad grows
def draw_snake():
    for x, y in snake:
        square = canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="green")
        snake_squares.append(square)

#This is where we call our function so that it will actually work
draw_snake()

#This is our base layout functoin for using the grid to make and distribute the food around the grid randomly using our libraries
def place_food():
    x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
    y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
    food = canvas.create_oval(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="red")
    return (food, (x, y))

#After creating that function we now use it and print it out onto our grid or canvas
food_item, food_pos = place_food()

#this is calling x an y coordinates on our canvas
dx = GRID_SIZE
dy = 0

#This is where we have if functions for each button on our simple keyboard when we hit up it will go uplike that
def change_direction(event):
    global dx, dy
    if event.keysym == "Up" and dy == 0:
        dx, dy = 0, -GRID_SIZE
    elif event.keysym == "Down" and dy == 0:
        dx, dy = 0, GRID_SIZE
    elif event.keysym == "Left" and dx == 0:
        dx, dy = -GRID_SIZE, 0
    elif event.keysym == "Right" and dx == 0:
        dx, dy = GRID_SIZE, 0

#This is using the function to ask the code to use the keys pressed to move the snake using the buttons we hit on our keyboard
window.bind("<KeyPress>", change_direction)

#This is our function for he snake to move even when the user is not clicking a button the snake should still keep on going they can do this by moving the head a coorinate up each time while he body is connected to keep on going over and over by using a loop and if conditions also if the snake hits its own tail or the wll it will die and loose the game
def move_snake():
    global food_item, food_pos

    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

    # Wall collision
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT
    ):
        game_over()
        return

    # Self collision
    if new_head in snake:
        game_over()
        return

    # Insert new head
    snake.insert(0, new_head)

    # Check for food
    if new_head == food_pos:
        canvas.delete(food_item)
        food_item, food_pos = place_food()
    else:
        tail = snake.pop()
        canvas.delete(snake_squares.pop())

    # Draw new head segment
    square = canvas.create_rectangle(new_head[0], new_head[1], new_head[0] + GRID_SIZE, new_head[1] + GRID_SIZE, fill="green")
    snake_squares.insert(0, square)

    # Keep game loop going
    window.after(100, move_snake)

#This is calling the previous function and making it work
move_snake()

#This is the game over that will print if you hit yourself our the wall
def game_over():
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text="GAME OVER", fill="white", font=("Arial", 24))


#This is the most important part of the code which is crucial to making the code run because without this it will not run the code will not print think of it like the print function for tkinter
window.mainloop()