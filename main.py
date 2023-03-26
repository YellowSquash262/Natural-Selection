import pygame
import random
import math
import time

numThings = 25
numFood = 200
screenSize = 400

energy = 50 #energy
energySev = 5 #energy sevarity, the higher the less intense
eatEn = 5 # energy repleneshed when eat

things = []
food = []
#thingsGen = [] #things genetics

screenSize = 400
  
dx = 0
dy = 0

e = False #end loop
ac = 0 #alive creatures
loop = 0

if (numThings % 2) != 0: #makes shit even
  numThings += 1 

def maxNum(x, y):
  if x > y:
    x = y
  return x
  
  #class for things
class Thing:
    def __init__(self, x, y, s, p, a, k, f, e, r):
      self.x = x
      self.y = y
      self.s = s # size
      self.p = p # pixels per frame
      self.a = a # alive
      self.k = k # kills
      self.f = f #food eaten
      self.e = e # energy
      self.r = r # ranking
  
  #class for food
class Food:
    def __init__(self, x, y, s):
      self.x = x
      self.y = y
      self.s = s

for i in range(numThings):
    things.append(Thing(round(random.randint(0, screenSize)), round(random.randint(0, screenSize)),round(random.randint(1, 30), 2) , round(random.randint(1, 10), 2) , True, 0, 0, 0, 0))

# Initialize pygame
pygame.init()
# Create a window
window = pygame.display.set_mode((screenSize, screenSize))
# Set window title
pygame.display.set_caption('Neural network')

def run():

  global loop
  loop += 1

  for i in range(numFood):
      food.append(Food(random.randint(0, screenSize), random.randint(0, screenSize), 2))

  if loop > 1:
    j = 0
    while j < len(things):
          #print(str(len(things)) + ", " + str(j) + ", " + str(numThings/2))
          if things[j].r < round(numThings/2):
            del things[j]
          j+=1

  if loop > 1:
    for i in range(len(things)):
      things.append(things[i])
      if things[i].r == numThings:
        print("Size: " + str(things[i].s) + ", Speed" + str(things[i].p))

  

  for i in range(len(things)):
        things[i].x = round(random.randint(0, screenSize))
        things[i].y = round(random.randint(0, screenSize))
        things[i].s += round(random.randint(-1, 1), 2)
        things[i].p += round(random.randint(-1, 1), 2)
        things[i].k = 0
        things[i].f = 0
        if things[i].p <= 1:
          things[i].p = 1
        if things[i].s <= 2:
          things[i].s = 2
        things[i].a = True
        things[i].e = ((energy/2)/(things[i].p/energySev)) + ((energy/2)/(things[i].s/energySev))

  ranking = 0
  
  # Create a variable to control the main loop
  running = True
  # Main loop
  while running:
      # Fill the window with white color
      window.fill((100, 100, 100))

      ac = 0
      #e = False
      for i in range(len(things)):
        if things[i].a == True:
          things[i].e -= 1
          if things[i].e <= 0:
            things[i].a = False
          ac += 1
          if things[i].s > 80:
            things[i].s = 80
          """for j in range(len(things)):
            if things[j].a == True:
              if i != j:
                if things[i].s/100*80 > things[j].s:
                  e = True

      if len(food) <= 0:
        if e == False or ac <= 1:
          run()"""

      if ac <= 1:
        run()
        for i in range(len(things)):
          if things[i].a == True:
            things[i].r = ranking
  
      #draw enviorment
      for i in range(len(things)):
        if things[i].a == True:
            pygame.draw.rect(window, (maxNum(things[i].k*15, 255), 10, maxNum(things[i].f*15, 255)), (things[i].x - things[i].s/2, things[i].y - things[i].s/2, things[i].s, things[i].s))
  
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
                    things[j].a = False
                    things[j].r = ranking
                    ranking += 1
                    things[i].e += eatEn*2
                    things[i].k += 1
                    ac -= 1
                  
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
              things[i].e += eatEn
              things[i].f += 1
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

      #if len(food) > 0:
      #  time.sleep(0.2)
    
      # Event loop
      for event in pygame.event.get():
          # Check for closing window
          if event.type == pygame.QUIT:
              running = False
  
run()
