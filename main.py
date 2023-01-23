import time
from datetime import datetime
import asyncio
#from shader_engine import Engine
import pygame
pygame.init()
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#engine = Engine(window)
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial",round(window.get_width()/15.4),bold=True)
size = window.get_size()

pause = False


async def main():
    image = pygame.image.load("new_image.png").convert()
    image.set_colorkey((255,0,220))
    print(image.get_at((20,0)))
    image = pygame.transform.scale(image,(round(size[0]*640/1920),round(size[0]*640/1920)))
    t = time.time()
    time_before_pause = "Temps avant la pause : "
    little_font = pygame.font.SysFont("arial",round(window.get_width()/24),bold =True)
    time_pause_text = little_font.render(time_before_pause,True,"white")
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
        secs = int(current_time[10:12])
        secs_to_go = 60 - secs
        if secs_to_go != 0:
            minutes_to_go -= 1
        time_left = str(minutes_to_go)
        if len(time_left) == 1:
            time_left = "0"+ time_left
        time_left += " : "+ str(secs_to_go)
        if len(time_left) == 6:
            time_left = time_left[:5]+"0"+time_left[5]
        if current_time[5] == "0":
            pause = True
            window.fill((100,210,86))
            time_text = font.render(current_time, True, "white")
            time_text_black = font.render(current_time, True, "black")
            window.blit(time_text_black, (((size[0] - time_text.get_width()) / 2)+5, size[1] * 0.65+5))
            window.blit(time_text, ((round((size[0] - time_text.get_width()) / 2)),round(size[1] * 0.65)))
        else:
            minutes_left_text = font.render(time_left,True,"white")
            window.blit(time_pause_text, (round(size[0]*0.08),round(size[1]*0.82)))
            window.blit(minutes_left_text,(round(size[0]*0.55),round(size[1]*0.8)))
            window.blit(time_text, (round((size[0] - time_text.get_width()) / 2), round(size[1] * 0.65)))

        window.blit(image,((size[0]-image.get_width())/2,size[1]*0.05))
        #engine()
        #engine.prog["time"] = time.time()-t
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
        await asyncio.sleep(0)

asyncio.run(main())
