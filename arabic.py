import pygame

class Arabic:
    def __init__(self):
        self.note_degree = 0
        self.degrees = []
        for i in range(8):
            self.degrees.append(
                pygame.mixer.Sound(f"./sounds/{i+1}.mp3")
            )
        self.ninth_chord = pygame.mixer.Sound('./sounds/9th.mp3')

    def next_note(self):
        if self.note_degree < 7:
            self.note_degree += 1
        else:
            self.note_degree = 0

