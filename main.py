import time
from datetime import datetime
from shader_engine import Engine
import pygame

pygame.display.set_mode((1440,960),pygame.DOUBLEBUF|pygame.OPENGL)
window = pygame.Surface((1440,960)).convert((255, 65282, 16711681, 0))
engine = Engine(window)
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial",125,bold=True)
size = window.get_size()

pause = False

image = pygame.image.load("image.png")
image.set_colorkey((233,29,233))
t = time.time()
while True:
    pause = False
    clock.tick(60)
    window.fill("black")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time[:2]+" "+current_time[2]+" "+current_time[3:5]+" "+current_time[5]+ " "+ current_time[6:8]
    time_text = font.render(current_time, True, "white")
    minutes = int(current_time[5:7])
    minutes_to_go = 60 - minutes
    if current_time[5] == "0":
        pause = True
        window.fill((100,210,86))
        time_text = font.render(current_time, True, "white")
        time_text_black = font.render(current_time, True, "black")
        window.blit(time_text_black, (((size[0] - time_text.get_width()) / 2)+5, size[1] * 0.8+5))
        window.blit(time_text, (((size[0] - time_text.get_width()) / 2), size[1] * 0.8))
    else:
        minutes_left_text = font.render(str(minutes_to_go),True,"white")
        # window.blit(minutes_left_text,((size[0]-minutes_left_text.get_width())/2,size[1]*0.9))
        window.blit(time_text, (((size[0] - time_text.get_width()) / 2), size[1] * 0.8))

    window.blit(image,((size[0]-image.get_width())/2,size[1]*0.05))
    engine()
    engine.prog["time"] = time.time()-t
    #pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
