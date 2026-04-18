import pygame
import datetime

class MickeyClock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (200, 200)

        # Load image
        self.hand_img = pygame.image.load("images/mickey_hand.png").convert_alpha()

        # Scale if needed
        self.hand_img = pygame.transform.scale(self.hand_img, (100, 20))

    def get_time(self):
        now = datetime.datetime.now()
        return now.minute, now.second

    def calculate_angles(self, minute, second):
        # 360 degrees / 60 units
        minute_angle = -(minute * 6)   # clockwise
        second_angle = -(second * 6)

        return minute_angle, second_angle

    def draw_hand(self, image, angle):
        rotated = pygame.transform.rotate(image, angle)
        rect = rotated.get_rect(center=self.center)
        self.screen.blit(rotated, rect)

    def update(self):
        self.minute, self.second = self.get_time()
        self.minute_angle, self.second_angle = self.calculate_angles(self.minute, self.second)

    def draw(self):
        # Draw clock center
        pygame.draw.circle(self.screen, (0, 0, 0), self.center, 5)

        # Draw hands
        self.draw_hand(self.hand_img, self.minute_angle)  # right hand
        self.draw_hand(self.hand_img, self.second_angle)  # left hand