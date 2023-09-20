class Ball:
    color = 'red'
    radius = 5
    weight = 19

    def info():
        print('Просто хорощий класс')

ball = Ball()

print(ball.color)
#print(ball.info())
print(Ball.radius)
Ball.info()

Ball.color = 'black'
print(Ball.color)

new_ball = Ball()

print(Ball.color)
print(new_ball.color)
