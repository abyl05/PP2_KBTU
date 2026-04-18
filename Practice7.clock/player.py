import pygame
import os

class MusicPlayer:
    def __init__(self, screen):
        self.screen = screen

        # Load playlist
        self.music_folder = "music"
        self.playlist = [f for f in os.listdir(self.music_folder) if f.endswith(".wav")]

        self.current_track = 0
        self.is_playing = False

        self.font = pygame.font.SysFont(None, 32)

    def load_track(self):
        track_path = os.path.join(self.music_folder, self.playlist[self.current_track])
        pygame.mixer.music.load(track_path)

    def play(self):
        self.load_track()
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.play()

    def handle_input(self, key):
        if key == pygame.K_p:
            self.play()
        elif key == pygame.K_s:
            self.stop()
        elif key == pygame.K_n:
            self.next_track()
        elif key == pygame.K_b:
            self.prev_track()
        elif key == pygame.K_q:
            pygame.quit()
            exit()

    def update(self):
        # Optional: auto-play next when track ends
        if not pygame.mixer.music.get_busy() and self.is_playing:
            self.next_track()

    def draw(self):
        if not self.playlist:
            text = self.font.render("No tracks found", True, (255, 255, 255))
            self.screen.blit(text, (50, 100))
            return

        track_name = self.playlist[self.current_track]

        status = "Playing" if self.is_playing else "Stopped"

        text1 = self.font.render(f"Track: {track_name}", True, (255, 255, 255))
        text2 = self.font.render(f"Status: {status}", True, (200, 200, 200))

        self.screen.blit(text1, (50, 100))
        self.screen.blit(text2, (50, 150))