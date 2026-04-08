from circleshape import *
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
        self.has_shield = False
        self.invulnerable_timer = 0
        self.is_warping = False
        self.warp_distance = PLAYER_RADIUS * 10
        self.warp_cooldown = 0
        self.WARP_COOLDOWN_MAX = 8

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        ship_color = "white"
        if self.warp_cooldown > 0:
            ship_color = (100, 100, 100)
        if self.invulnerable_timer > 0:
            if int(self.invulnerable_timer * 10) % 2 == 0:
                return
        pygame.draw.polygon(screen, ship_color, self.triangle(), LINE_WIDTH)
        if self.has_shield:
            pygame.draw.circle(screen, (0,255,0), self.position,
                                self.radius + 5, 2)
        if self.is_warping:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            warp_vector = forward * (self.radius *10)

            ghost_points = []
            for p in self.triangle():
                new_p = p + warp_vector
                new_p.x %= SCREEN_WIDTH
                new_p.y %= SCREEN_HEIGHT
                ghost_points.append(new_p)
            pygame.draw.polygon(screen, (0,255,255), ghost_points, 1)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        if self.invulnerable_timer > 0:
            self.invulnerable_timer -= dt
        self.shot_cooldown_timer -= dt
        if self.warp_cooldown > 0:
            self.warp_cooldown -= dt
        
        #screen wrapping logic
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*-1)
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown_timer > 0:
                pass
            else:
                self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shoot()
        if keys[pygame.K_f] and self.warp_cooldown <= 0:
            self.is_warping = True
        else:
            if self.is_warping:
                self.execute_warp()
                self.is_warping = False
                self.warp_cooldown = self.WARP_COOLDOWN_MAX

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED 

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def execute_warp(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * (self.radius * 10)
        #wrapping logic
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT

    
        