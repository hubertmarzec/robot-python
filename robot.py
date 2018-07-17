import random

# init state
robot = {'x':1, 'y':1}

# code
def move_robot(state, maxX = 5, maxY = 5):

  prevState = {'x':state['x'],'y':state['y']}

  def new_random_position(currentValue, max):
    directions = [0]
    if  currentValue > 1 :
      directions.append(-1)

    if currentValue < max:
      directions.append(1)  

    newValue = random.choice(directions)
    return newValue   


  state['x'] += new_random_position(state['x'], maxX)
  state['y'] += new_random_position(state['y'], maxY)
  print('{0} -> {1}'.format(prevState, state))
  return state

# test

i = 0
while i < 20:
  move_robot(robot)  
  i = i +1;



