import pygame
import random
import sys

class FlappyBlock:

    def __init__(self):
        self.screen = pygame.display.set_mode((400, 711))
        pygame.display.set_caption('Flappy Block')
        self.bird = pygame.Rect(65, 50, 50, 50)
        self.birdYPos = 350
        self.jump = 0
        self.jumpSpeed = 10
        self.gravity = 1
        self.resetValues()

    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("Helvetica", 50)
        
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead:
                    self.jump = 17
                    self.gravity = 2
                    self.jumpSpeed = 10

            self.screen.fill((255, 255, 255))
			
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(self.wallx, 500 - self.offset, 100, 500))
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(self.wallx, -140 - self.offset, 100, 500))

            pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(65, self.birdYPos, 50, 50))
            self.screen.blit(font.render(str(self.score), -1, (0, 0, 0)), (200, 50))
			
            self.updateWalls()
            self.updateBird()
            pygame.display.update()

    def updateBird(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdYPos -= self.jumpSpeed
            self.jump -= 1
        else:
            self.birdYPos += self.gravity
            self.gravity += 0.2
		
        self.bird[1] = self.birdYPos
        upRect = pygame.Rect(self.wallx, 500 - self.offset, 90, 500)
        downRect = pygame.Rect(self.wallx, -140 - self.offset, 90, 500)
		
        if upRect.colliderect(self.bird) or downRect.colliderect(self.bird):
            self.dead = True
		
        if not 0 < self.bird[1] < 720:
            self.bird[1] = 50
            self.birdYPos = 50
            self.gravity = 5
            self.resetValues()
	
    def updateWalls(self):
        self.wallx -= 2
		
        if self.wallx < -80:
            self.wallx = 400
            self.score += 1
            self.offset = random.randint(-100, 100)
	
    def resetValues(self):
        self.score = 0
        self.wallx = 400
        self.offset = random.randint(-100, 100)
        self.dead = False

if __name__ == "__main__":
    FlappyBlock().run()
