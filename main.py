import pygame
pygame.init()
display = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Oreo simulator')
scoreFont = pygame.font.SysFont('arial', 30)
upgradeFont = pygame.font.SysFont('arial', 7)
upgradeIcon = pygame.image.load('Assets\\Images\\upgrade-icon.png')
upgradeIcon = pygame.transform.scale(upgradeIcon, (50, 50)).convert()
upgradeIcon.set_colorkey((255, 255, 255))


def drawOreo():
    # 62 42 26
    pygame.draw.circle(display, (6 * 16 + 2, 4 * 16 + 2, 2 * 16 + 6), (350, 350), 200)
    pygame.draw.circle(display, (0, 0, 0), (350, 350), 200, 3)
    display.blit(upgradeIcon, (600, 600))

def drawScore(score, nextClickUpgradeCost):
    text = f'Score: {score}'
    label = scoreFont.render(text, True, (0, 0, 0))
    rect = label.get_rect()
    offset = 30
    rect.topright = 700 - offset, offset
    display.blit(label, rect)
    text = f'{nextClickUpgradeCost}'
    label = scoreFont.render(text, True, (0, 0, 0))

    rect = pygame.Rect(0, 0, 0, 0)
    rect.center = 625 - label.get_width() // 2, 600 - label.get_height() - 5
    display.blit(label, rect)

def main():
    score = 0
    moneyPerClick = 1
    nextClickUpgradeCost = 10
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    distanceSquared = (pos[0] - 350) ** 2 + (pos[1] - 350) ** 2
                    if distanceSquared <= (200 ** 2):
                        score += moneyPerClick

                    upgradeRect = pygame.Rect(600, 600, 50, 50)
                    if upgradeRect.collidepoint(pos):
                        if score >= nextClickUpgradeCost:
                            score -= nextClickUpgradeCost
                            nextClickUpgradeCost *= 2
                            moneyPerClick += 1


        display.fill((255, 255, 255))
        drawOreo()
        drawScore(score, nextClickUpgradeCost)
        pygame.display.update()

if __name__ == '__main__':
    main()