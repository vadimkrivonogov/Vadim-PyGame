ristkülik=pygame.Rect(30,30,30,30)
pygame.draw.rect(ekraani_pind,(255,0,0),ristkülik)

ristkülik=pygame.Rect(60,60,60,60)
pygame.draw.rect(ekraani_pind,(0,250,0),ristkülik)

ristkülik=pygame.Rect(120,120,120,120)
pygame.draw.rect(ekraani_pind,(60,250,100),ristkülik)

ristkülik=pygame.Rect(240,240,240,240)
pygame.draw.rect(ekraani_pind,(100,100,255),ristkülik)

ristkülik=pygame.Rect(200,50,200,50)
pygame.draw.rect(ekraani_pind,(130,130,200),ristkülik)

obvodka=pygame.Rect(300,150,1,100)
pygame.draw.aaline(,(255,255,0), [100,390], [430,120], 5)

pilt=pygame.image.load("red.png")
ekraani_pind.blit(pilt,(120,240))

font=pygame.font.SysFont("Calibri", 40)
sõnad="Tere Tulemast!"
värv=[0,0,0]
teksti_lisamine=font.render(sõnad,False,(värv))
ekraani_pind.blit(teksti,lisamine,(60,120)

pygame.display.flip()