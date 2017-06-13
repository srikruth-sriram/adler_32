import pygame
import random
  
def display(codeword):
    pygame.init()

    screen=pygame.display.set_mode([700,500])
    pygame.display.set_caption("Front End")
    font = pygame.font.SysFont('Calibri',25, True, False)
    Sender = font.render("Sender",True,(0,0,0))
    Reciever = font.render("Reciever",True,(0,0,0))
    packet = font.render(codeword,True,(0,0,0))
    clock=pygame.time.Clock()
    done=False
    pos=-100
    while not done:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        

        screen.fill((255,255,255))
        screen.blit(packet, [pos, 250])

        pygame.draw.rect(screen,(255,255,255), [0,0,150,500])
        pygame.draw.rect(screen,(255,255,255), [550,0,150,500])
        
                 
        pygame.draw.line(screen,(0,0,0), [150, 0], [150, 500],2)
        pygame.draw.line(screen,(0,0,0), [550, 0], [550, 500],2)

        screen.blit(Sender, [10, 250])
        screen.blit(Reciever, [560, 250]) 

        
        pygame.display.flip()
        

        pos+=1
        if(pos>700):
            done=True
        clock.tick(60)
        
            
              
    
    pygame.quit()
    
    ans="" 
    for i in range(len(codeword)):
        if(random.randint(1,100) in (5,23,67,84)):
            ans+='X'
        else:
            ans+=codeword[i]
    return ans



