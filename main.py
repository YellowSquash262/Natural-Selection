

import pygame
import random
import math
import time

# Initialize pygame
pygame.init()
# Create a window
window = pygame.display.set_mode((400, 400))
# Set window title
pygame.display.set_caption('Neural network')

numThings = 50
things = []
  
numFood = 100
food = []
  
dx = 0
dy = 0
f_closest_x = 0
f_closest_y = 0
  
  #class for things
class Thing:
    def __init__(self, x, y, s, p, a, r):
      self.x = x
      self.y = y
      self.s = s # size
      self.p = p # pixels per frame
      self.a = a # alive
      self.r = r # reward
  
  #class for food
class Food:
    def __init__(self, x, y, s):
      self.x = x
      self.y = y
      self.s = s

for i in range(numThings):
    things.append(Thing(round(random.randint(0, 400)), round(random.randint(0, 400)), round(random.randint(4, 10)) ,round(random.randint(4, 6)), True, 0))

def run():

  for i in range(numFood):
      food.append(Food(random.randint(0, 400), random.randint(0, 400), 5))

  for i in range(len(things)):
        things[i].x = round(random.randint(0, 400))
        things[i].y = round(random.randint(0, 400))
  
  # Create a variable to control the main loop
  running = True
  # Main loop
  while running:
      # Fill the window with white color
      window.fill((100, 100, 100))

      if len(food) <= 1:
        #if len(things) <= 1:
        run()
  
      #draw enviorment
      for i in range(len(things)):
        if things[i].s > 100:
          things[i].s = 100
        if things[i].a == True:
          if things[i].r*15 <= 255:
            pygame.draw.rect(window, (things[i].r*15, 0, 0), (things[i].x - things[i].s/2, things[i].y - things[i].s/2, things[i].s, things[i].s))
          else:
            pygame.draw.rect(window, (0, 255, 0), (things[i].x - things[i].s/2, things[i].y - things[i].s/2, things[i].s, things[i].s))
  
      for i in range(len(food)):
        pygame.draw.rect(window, (0, 255, 0), (food[i].x, food[i].y, food[i].s, food[i].s))
  
      # ! get nearest food and creture and creture size
      # closest creture
    
      for i in range(len(things)):
        if things[i].a == True:
          for j in range(len(things)):
            if things[j].a == True:
              if i != j:
                if things[i].s/100*80 > things[j].s:
                  if (things[i].x - things[i].s/2 < things[j].x + things[j].s/2) and (things[i].x + things[i].s/2 > things[j].x - things[j].s/2) and (things[i].y - things[i].s/2 < things[j].y + things[j].s/2) and (things[i].y + things[i].s/2 > things[j].y - things[j].s/2):
                    things[i].r += 1
                    things[i].s += 2
                    things[j].a = False
                  
      for i in range(len(things)):
        if things[i].a == True:
          c_closest_x = None
          c_closest_y = None
          min_distance = float('inf')
          c = False
        
          for j in range(len(things)):
            if things[j].a == True:
              if i != j:
                  if things[i].s/100*80 > things[j].s:
                    CDistance = ((things[i].x - things[j].x)**2 + (things[i].y - things[j].y)**2)**0.5
                    if CDistance < min_distance:
                        min_distance = CDistance
                        c_closest_x = things[j].x
                        c_closest_y = things[j].y
                        c = True
          j = 0
          while j < len(food):
            if things[i].x - things[i].s/2 < food[j].x - food[j].s/2 + food[j].s and things[i].x - things[i].s/2 + things[i].s > food[j].x - food[j].s/2 and things[i].y - things[i].s/2 < food[j].y - food[j].s/2 + food[j].s and things[i].s + things[i].y - things[i].s/2 > food[j].y- food[j].s/2 :
              del food[j]
              things[i].s += 1
            else:
              j += 1
        
          min_distance = float('inf')
          for j in range(len(food)):
                  FDistance = ((things[i].x - food[j].x)**2 + (things[i].y - food[j].y)**2)**0.5
                  if FDistance < min_distance:
                      min_distance = FDistance
                      f_closest_x = food[j].x
                      f_closest_y = food[j].y
                    
          if c == True and CDistance < FDistance:
              angle = math.atan2(c_closest_x - things[i].x, c_closest_y - things[i].y)
              dy = math.cos(angle) * things[i].p
              dx = math.sin(angle) * things[i].p
          else:
          	angle = math.atan2(f_closest_x - things[i].x, f_closest_y - things[i].y)
          	dy = math.cos(angle) * things[i].p
          	dx = math.sin(angle) * things[i].p
  
          things[i].x += dx
          things[i].y += dy
          
      # ! reward
  
      # ! rinse and repeat
    
      #Update the windo
      pygame.display.update()
  
      time.sleep(0.06)
    
      # Event loop
      for event in pygame.event.get():
          # Check for closing window
          if event.type == pygame.QUIT:
              running = False
  
run()
