import pygame
#активируем "pygame"
pygame.init()
#регулируеи размер окна
ekraani_pind=pygame.display.set_mode((300,300))
#заполняем окно определенным цветом
ekraani_pind.fill((0,0,200))
#даем название окну
pygame.display.set_caption("v.krivonogov 1")
#создаем цвета заранее, чтобы потом, писать цвета словами, а не числами RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
#рисуем снеговика
pygame.draw.circle(ekraani_pind, WHITE, (150, 125), 25) # голова
pygame.draw.circle(ekraani_pind, WHITE, (150, 175), 35) # тело
pygame.draw.circle(ekraani_pind, BLACK, (138, 118), 4) # левый глаз
pygame.draw.circle(ekraani_pind, BLACK, (163, 118), 4) # правый глаз
pygame.draw.polygon(ekraani_pind, ORANGE, [(150, 140), (152, 132), (148, 132)]) # нос
pygame.draw.line(ekraani_pind, WHITE, (135, 155), (115, 165), 3) # левая рука
pygame.draw.line(ekraani_pind, WHITE, (165, 155), (185, 165), 3) # правая рука
pygame.draw.circle(ekraani_pind, WHITE, (142, 182), 5) # левая нога
pygame.draw.circle(ekraani_pind, WHITE, (158, 182), 5) # правая нога
pygame.draw.circle(ekraani_pind, WHITE, (150, 225), 45) # еще один круг снизу 
#команда, чтобы вывести это на экран
pygame.display.flip()
#бесконечный цыкл, чтобы окно не закрвывалось сразу, после открытия 
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
#дает возможность закрыть окно с "крестика"
pygame.quit()