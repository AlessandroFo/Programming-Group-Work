import turtle
import random

def game1():
    # Game configuration
    w = 500
    h = 500
    food_size = 10
    delay_base = 100
    delay_fast = 30

    # Snake and game variables
    snake = []
    snake_dir = ""
    food_position = ()
    delay = delay_base
    score = 0

    # Offsets for snake movement
    offsets = {
        "up": (0, 20),
        "down": (0, -20),
        "left": (-20, 0),
        "right": (20, 0)
    }

    # Initialize screen
    screen = turtle.Screen()
    screen.setup(w, h)
    screen.title("Snake")
    screen.bgcolor("green")
    screen.tracer(0)

    # Create pen for drawing snake segments
    pen = turtle.Turtle("square")
    pen.penup()

    # Create food turtle
    food = turtle.Turtle()
    food.shape("square")
    food.color("yellow")
    food.shapesize(food_size / 20)
    food.penup()

    # Create score pen
    score_pen = turtle.Turtle()
    score_pen.color("white")
    score_pen.speed(0)
    score_pen.penup()
    score_pen.goto(0, 200)

    # Reset game state
    def reset():
        nonlocal snake, snake_dir, food_position, score, delay
        snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
        snake_dir = "up"
        food_position = get_random_food_position()
        food.goto(food_position)
        score = 0
        delay = delay_base
        update_score()
        move_snake()

    # Move snake based on current direction
    def move_snake():
        nonlocal snake_dir

        new_head = snake[-1].copy()
        new_head[0] += offsets[snake_dir][0]
        new_head[1] += offsets[snake_dir][1]

        if new_head in snake[:-1]:
            game_over()
        else:
            snake.append(new_head)

            if not food_collision():
                snake.pop(0)

            handle_boundary()

            pen.clearstamps()
            for segment in snake:
                pen.goto(segment[0], segment[1])
                pen.stamp()

            screen.update()
            turtle.ontimer(move_snake, delay)

    # Check if snake collided with food
    def food_collision():
        nonlocal food_position, score
        if get_distance(snake[-1], food_position) < 20:
            food_position = get_random_food_position()
            food.goto(food_position)
            score += 1
            update_score()
            return True
        return False

    # Generate random food position
    def get_random_food_position():
        x = random.randint(-w / 2 + food_size, w / 2 - food_size)
        y = random.randint(-h / 2 + food_size, h / 2 - food_size)
        return (x, y)

    # Handle snake movement when reaching screen boundary
    def handle_boundary():
        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < -w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h

    # Calculate distance between two positions
    def get_distance(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
        return distance

    # Update score display
    def update_score():
        score_pen.clear()
        score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Game over
    def game_over():
        pen.clear()
        pen.goto(0, 0)
        pen.write("Game Over", align="center", font=("Courier", 36, "bold"))
        pen.goto(0, -50)
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        pen.goto(0, -100)
        pen.write("Press 'r' to play again or 'q' to quit", align="center", font=("Courier", 18, "normal"))
        screen.onkey(restart_game, "r")
        screen.onkey(quit_game, "q")

    # Restart game
    def restart_game():
        remove_game_over()
        reset()

    # Remove game over screen
    def remove_game_over():
        pen.clear()
        screen.onkey(None, "r")
        screen.onkey(None, "q")

    # Quit game
    def quit_game():
        screen.bye()

    # Keyboard controls
    def go_up():
        nonlocal snake_dir
        if snake_dir != "down":
            snake_dir = "up"

    def go_right():
        nonlocal snake_dir
        if snake_dir != "left":
            snake_dir = "right"

    def go_down():
        nonlocal snake_dir
        if snake_dir != "up":
            snake_dir = "down"

    def go_left():
        nonlocal snake_dir
        if snake_dir != "right":
            snake_dir = "left"

    # Map keyboard controls
    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_right, "Right")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")

    # Create buttons for difficulty selection
    base_button = turtle.Turtle()
    base_button.shape("square")
    base_button.color("white")
    base_button.shapesize(2, 2)
    base_button.penup()
    base_button.goto(-80, -230)
    base_button.write("Base", align="center", font=("Courier", 16, "normal"))

    advanced_button = turtle.Turtle()
    advanced_button.shape("square")
    advanced_button.color("white")
    advanced_button.shapesize(2, 2)
    advanced_button.penup()
    advanced_button.goto(80, -230)
    advanced_button.write("Advanced", align="center", font=("Courier", 16, "normal"))

    # Functions to handle button clicks
    def set_base_difficulty(x, y):
        nonlocal delay
        delay = delay_base
        base_button.color("green")
        advanced_button.color("white")
        remove_buttons()
        reset()

    def set_advanced_difficulty(x, y):
        nonlocal delay
        delay = delay_fast
        base_button.color("white")
        advanced_button.color("green")
        remove_buttons()
        reset()

    # Map button clicks
    turtle.onscreenclick(set_base_difficulty, btn=1)
    turtle.onscreenclick(set_advanced_difficulty, btn=3)

    # Remove buttons after selection
    def remove_buttons():
        base_button.hideturtle()
        advanced_button.hideturtle()
    turtle.done()
    print("Playing Game 1...")

def game2():
    turtle.bgcolor("green")
    def drawMan(x):      
        guess = x     
        if guess == 1:
            # draw head
            turtle.goto(-74, 140)
            turtle.pendown()
            turtle.right(90)
            turtle.circle(15,None,100)
            turtle.penup()
        elif guess == 2:
            # draw torso
            turtle.goto(-74, 140)
            turtle.pendown()
            turtle.left(90)
            turtle.penup()
            turtle.forward(30)
            turtle.pendown()
            turtle.forward(40)
            turtle.right(180)
            turtle.forward(30)
            turtle.penup()
        elif guess == 3:
            # draw first arm
            turtle.goto(-74, 100)
            turtle.pendown()
            turtle.left(55)
            turtle.forward(45)
            turtle.right(180)
            turtle.forward(45)
            turtle.penup()
        elif guess == 4:
            # draw second arm
            turtle.goto(-74, 100)
            turtle.pendown()
            turtle.left(70)
            turtle.forward(45)
            turtle.right(180)
            turtle.forward(45)
            turtle.penup()
        elif guess == 5:
            # draw first leg
            turtle.goto(-74, 100)
            turtle.pendown()
            turtle.left(55)
            turtle.forward(30)
            turtle.right(30)
            turtle.forward(60)
            turtle.right(180)
            turtle.forward(60)
            turtle.penup()
        elif guess == 6:
            # draw second leg
            turtle.goto(-74, 70)
            turtle.pendown()
            turtle.right(120)
            turtle.forward(60)
            turtle.penup()

    # initialize turtle
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(2)

    wordbank = ["stgallen", "luxury", "pixel", "galaxy", "finance", "subway", "funny", "python", "professor", "rhythm", "java", "staff", "game", "loop", "implementation", "incredible", "brackets", "computer", "player"]

    bored = False
    while not bored:

        # draw gallows
        turtle.home()
        turtle.pendown()
        turtle.left(90)
        turtle.forward(175)
        turtle.left(90)
        turtle.forward(74)
        turtle.left(90)
        turtle.forward(35)
        turtle.penup()
        turtle.goto(-135,-35)
        
        word = random.choice(wordbank)

        for i in word:
            turtle.write('_ ', True, font=("Courier", 14, "normal"))

        correct = []
        wrong = 0
        terminate = False
        while wrong < 6 and not terminate:
            letter = turtle.textinput('Hangman','Guess a letter:')
            turtle.goto(-135,-35)
            if letter not in correct:
                for i in word:
                    if i == letter:
                        turtle.write(letter.upper() + ' ', True, font=("Courier", 14, "normal"))
                        correct += letter
                    else:
                        turtle.write('_ ', True, font=("Courier", 14, "normal"))  
            if letter not in word:
                wrong += 1
                drawMan(wrong)
            if wrong == 6:
                turtle.goto(-135,-35)
                for i in word:
                    if i in correct:
                        turtle.write('_ ', True, font=("Courier", 14, "normal"))
                    else:
                        turtle.write(i.upper() + ' ', True, font=("Courier", 14, "normal"))
                turtle.goto(-74, -60)
                turtle.write('Sorry, you lose!', False, align='center', font=("Courier", 14, "normal"))
            if len(correct) == len(word):
                turtle.goto(-74, -60)
                turtle.write('Congratulations!', False, align='center', font=("Courier", 14, "normal"))
                terminate = True

        # play again?
        response = turtle.textinput('Hangman','Would you like to play again? (y or n): ')
        while response != 'y' and response != 'n':
            response = turtle.textinput('Hangman','Please enter "y" or "n": ')
        if response == 'y':
            turtle.clear()
        elif response == 'n':
            turtle.clear()
            turtle.home()
            turtle.write('Thanks for playing!', False, align='center', font=("Courier", 25, "normal")) 
            bored = True

    print("Playing Game 2...")


def game3():
    # Draw the board with turtle. The background color is green and the lines are white
    def draw_board():
        turtle.bgcolor("green")
        turtle.penup()
        turtle.goto(-150, 150)
        turtle.pendown()
        turtle.color("white")
        turtle.width(3)
        turtle.speed(0)
        for _ in range(2):
            turtle.forward(300)
            turtle.right(90)
            turtle.forward(300)
            turtle.right(90)

    def draw_mark(row, col, player):
        if player == "X":
            x = col * 100 - 150
            y = 160 - row * 100

            turtle.penup()
            turtle.goto(x + 50, y - 70)
            turtle.pendown()
            turtle.color("white")
            turtle.width(2)
            turtle.speed(0)
            turtle.setheading(45)
            turtle.forward(40)
            turtle.backward(80)
            turtle.forward(40)
            turtle.right(90)
            turtle.forward(40)
            turtle.backward(80)
        else:
            x = col * 100 - 170
            y = 140 - row * 100
            turtle.penup()
            turtle.goto(x + 50, y - 70)
            turtle.pendown()
            turtle.color("white")
            turtle.width(2)
            turtle.speed(0)
            turtle.circle(30)

    # The function records the moves of each player. If the player inserts an invalid input, the program gives an error message
    def get_move(player):
        while True:
            try:
                row = int(turtle.numinput("Move Input", "Enter the row (0-2):"))
                col = int(turtle.numinput("Move Input", "Enter the column (0-2):"))
                if row < 0 or row > 2 or col < 0 or col > 2:
                    turtle.textinput("Invalid Move", "Invalid move. Press OK to try again.")
                else:
                    return row, col
            except TypeError:
                pass


    # The function checks which player has won by looking at the raws, diagonals and columns of the board
    def is_winner(board, player):
        for row in board:
            if row.count(player) == 3:
                return True

        for col in range(3):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                return True

        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True

        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True

        return False

    # The function checks if the board is full
    def is_board_full(board):
        for row in board:
            if " " in row:
                return False
        return True

    # Main function to play the game
    def play_tris():
        board = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

        current_player = "X" #Player X starts the game

        turtle.setup(500, 500)
        turtle.title("Tic Tac Toe")
        draw_board()

        while True:
            row, col = get_move(current_player)
            if board[row][col] != " ":
                turtle.textinput("Invalid Move", "That cell is already occupied. Press OK to try again.")
                continue  # Skip this iteration if the cell is already occupied and gives an error message. The player can
                          # try again the move by inputting other values for rows and columns

            board[row][col] = current_player
            draw_mark(row, col, current_player) # X or O are drawn in the board in the position desired by the player

            if is_winner(board, current_player):
                turtle.textinput("Game Over", "Player {} wins! Press OK to Exit the game.".format(current_player)) #If one of the players win, the game is over and a message is displaied 
                turtle.done()
                break
            elif is_board_full(board):
                turtle.textinput("Game Over", "It's a tie!") #If the board is full and none has won, the game is tie
                turtle.done()
                break

            current_player = "O" if current_player == "X" else "X" #Swithces the playrs

        turtle.done()


    play_tris()


# Entry screen: the player has the possibility to choose which game to play: Snake, Hangman and Tic-Tac-Toe 1 vs 1. If the player inserts an invalid input he/she has the possibility to reinsert the input
def main():
    print("Welcome to the Game Selection!")
    print("1. Game 1: Snake")
    print("2. Game 2: Hangman")
    print("3. Game 3: Tic-Tac-Toe - 1 vs 1")
    choice = input("Enter the number of the game you want to play: ")

    while choice != "1" and choice != "2" and choice != "3":
        print("Invalid choice. Please try again.")
        choice = input("Enter the number of the game you want to play: ")
    pass

    if choice == '1':
        game1()
    elif choice == '2':
        game2()
    elif choice == '3':
        game3()
    


if __name__ == "__main__":
    main()





