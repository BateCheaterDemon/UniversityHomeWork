import pygame
import sys

# 确保正确加载图像路径
brickImage = r"..\image\brick.png"
ironImage = r"..\image\iron.png"

# 定义砖块类
class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(brickImage)
        self.rect = self.image.get_rect()

# 定义铁块类
class Iron(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(ironImage)
        self.rect = self.image.get_rect()

# 定义地图类
class Map():
    def __init__(self):
        self.brickGroup = pygame.sprite.Group()
        self.ironGroup = pygame.sprite.Group()
        
        # # 数字代表地图中的位置，画砖块
        # X1379 = [2, 3, 6, 7, 18, 19, 22, 23]
        # Y1379 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]
        # X28 = [10, 11, 14, 15]
        # Y28 = [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]
        # X46 = [4, 5, 6, 7, 18, 19, 20, 21]
        # Y46 = [13, 14]
        # X5 = [12, 13]
        # Y5 = [16, 17]
        # X0Y0 = [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]

        X1379 = []
        Y1379 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]
        X28 = [10, 11, 14, 15]
        Y28 = [2, 3, 4, 5, 16, 17, 18, 19, 20]
        X46 = [4, 5, 6, 7, 18, 19, 20, 21]
        Y46 = [13, 14]
        X5 = [12, 13]
        Y5 = [16, 17]
        X0Y0 = [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]
        
        # 添加砖块
        for x in X1379:
            for y in Y1379:
                brick = Brick()
                brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(brick)

        for x in X28:
            for y in Y28:
                brick = Brick()
                brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(brick)

        for x in X46:
            for y in Y46:
                brick = Brick()
                brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(brick)

        for x in X5:
            for y in Y5:
                brick = Brick()
                brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(brick)

        for x, y in X0Y0:
            brick = Brick()
            brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
            self.brickGroup.add(brick)

        # 添加铁块
        for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
            iron = Iron()
            iron.rect.left, iron.rect.top = 3 + x * 24, 3 + y * 24
            self.ironGroup.add(iron)

# 主函数
def main():
    pygame.init()
    
    # 设置窗口
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Map Display")

    # 创建地图
    game_map = Map()

    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 清屏
        screen.fill((255, 255, 255))  # 填充白色背景
        
        # 绘制砖块
        game_map.brickGroup.draw(screen)
        
        # 绘制铁块
        game_map.ironGroup.draw(screen)
        
        # 刷新屏幕
        pygame.display.flip()

if __name__ == "__main__":
    main()
