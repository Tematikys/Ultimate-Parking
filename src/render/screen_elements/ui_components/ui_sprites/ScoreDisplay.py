import arcade
from pyglet.math import Vec2 as Vector2D

from src.render.sprites import BasicSprite
from src.utils import load_font


class ScoreDisplay:
    def __init__(
        self,
        score: int = 0,
        position: Vector2D = Vector2D(300, 300),
        font_path: str = "assets/fnt/ka1.ttf",
        font_name: str = "Karmatic Arcade",
        color: arcade.color = arcade.color.WHITE,
        size: int = 25,
        width: int = 200,
        icon: str = "assets/pic/icon/coin_2.png",
    ) -> None:
        if font_path is not None:
            load_font(font_path)
        self.current_score: int = score
        self.target_score: int = score
        self.change_speed: float = 0.03

        self.border_width: int = 5
        self.box_width: int = width
        self.box_height: int = size + self.border_width * 3
        self.half_box_width: int = self.box_width // 2

        self.sprite_list: arcade.SpriteList = arcade.SpriteList()

        self.border_box: arcade.SpriteSolidColor = arcade.SpriteSolidColor(
            self.box_width + self.border_width * 2,
            self.box_height + self.border_width * 2,
            (56, 56, 56),
        )
        self.background_box: arcade.SpriteSolidColor = arcade.SpriteSolidColor(
            self.box_width,
            self.box_height,
            (135, 135, 135),
        )

        self.sprite_list.append(self.border_box)
        self.sprite_list.append(self.background_box)

        self.text: arcade.Text = arcade.Text(
            str(score),
            0,
            0,
            color,
            size,
            width,
            "left",
            font_name=font_name,
            anchor_y="center",
            anchor_x="center",
        )
        self.icon: BasicSprite = BasicSprite(icon, scale=5.5)
        self.icon.center_x = -width / 2
        self.icon.center_y = 0
        self.sprite_list.append(self.icon)

        self.set_position(position)

    def draw(self) -> None:
        self.text.draw()

    def set_position(self, new_position: Vector2D | tuple[float, float]) -> None:
        center_x, center_y = new_position
        self.sprite_list.move(center_x, center_y)
        self.text.position = (center_x, center_y + 5)

    def update_score(self, new_score: float) -> None:
        self.target_score = new_score
        self.current_score -= (
            self.current_score - self.target_score
        ) * self.change_speed
        self.text.text = int(self.current_score)
