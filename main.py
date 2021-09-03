import random
import curses


screen = curses.initscr()
curses.curs_set(0)

screenHight, screenWidth = screen.getmaxyx()
window = curses.newwin(screenHight, screenWidth, 0, 0)
window.keypad(1)
window.timeout(100)

snakeX = screenWidth // 4
snakeY = screenHight // 2

snake = [
    [snakeY, snakeX],
    [snakeY, snakeX - 1],
    [snakeY, snakeX - 2]
]

food = [screenHight // 2, screenWidth // 2]

window.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if snake[0] in snake[1: ]:
        curses.endwin()
        quit()

    
        

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    snake.insert(0, new_head)

    
    

      
    if snake[0][0] == screenHight:
        snake[0][0] = 1

    if snake[0][1] == screenWidth:
        snake[0][1] = 1

    if snake[0][0] == 0:
        snake[0][0] = screenHight
    if snake[0][1] == 0:
        snake[0][1] = screenWidth

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, screenHight - 1),
                random.randint(1, screenWidth - 1)
            ]

            food = new_food if new_food not in snake else None

        window.addch(food[0], food[1], curses.ACS_PI)

    else:
        tail = snake.pop()
        try:
            window.addch(tail[0], tail[1], ' ')
        except:
            tail = []

    try:
        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
    except:
        
        if snake[0][0] == 0:
            snake[0][0] = screenHight
        elif snake[0][1] == 0:
            snake[0][1] = screenWidth

