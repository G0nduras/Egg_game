import random
from typing import List
from PyQt6.QtCore import QTimer, Qt, QPointF, pyqtSignal
from PyQt6.QtWidgets import QGraphicsScene
from egg import Egg
from handler import Handler
from output_widget import create_output_widget
from database import DataBase


class Scene(QGraphicsScene):
    EPS = 1e-5
    create_output_widget_signal = pyqtSignal(str)

    def __init__(
            self,
            widget: "Widget",
    ):
        super().__init__()
        self.all_timer = QTimer()
        self.all_timer.timeout.connect(self.on_timer_tick)
        self.all_timer.start(round(1000 / 60))

        self.timer_spawn_egg = QTimer()
        self.timer_spawn_egg.timeout.connect(self.spawn_egg_on_tick)
        self.timer_spawn_egg.start(1000)

        self._score = 0
        self._HP = 3
        self.spawns_egg: List[Egg] = []
        self._egg = Egg(
            x=random.randint(20, 1000),
            y=20,
            egg_color="beige",
            radius=20,
            speed=4,
        )
        self._platform = Handler(
            x=500,
            y=600,
            width=100,
            height=10,
            speed=20,
            platform_color="dark"
        )
        self._widget = widget
        self._shift: QPointF = QPointF(self._platform._speed, 0)
        self._drop: QPointF = QPointF(0, self._egg._speed)

        self._platform.add_platform_to_scene(self)
        self._database = DataBase(path="database_scores.db")

    def key_press_event(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self._widget.close()

        if event.key() == Qt.Key.Key_Right:
            new_pos = self._platform.pos() + self._shift
            self._platform.setPos(new_pos)
        if event.key() == Qt.Key.Key_Left:
            new_pos = self._platform.pos() - self._shift
            self._platform.setPos(new_pos)

    def egg_intersect_platform(self, scene: QGraphicsScene):
        for spawn_egg in self.spawns_egg:
            lower_bound_egg = spawn_egg.pos().y() + (spawn_egg._radius)
            if abs(self._platform.pos().y() - lower_bound_egg) < Scene.EPS:
                if spawn_egg.pos().x() > self._platform.pos().x():
                    if spawn_egg.pos().x() < (self._platform.pos().x() + self._platform.rect().width()):
                        scene.removeItem(spawn_egg)
                        self._score += 1
                    else:
                        self._game_over()

                else:
                    self._game_over()

    def _game_over(self):
        self._HP -= 1
        if self._HP == 0:
            print("GAME_OVER!" * 10)
            self._database.write(login=self._widget._output_widget, score=self._score)
            create_output_widget(self._widget, login=self._widget._output_widget, database=self._database)
            self._widget.hide()
            self.timer_spawn_egg.stop()

    def on_timer_tick(self):
        for spawn_egg in self.spawns_egg:
            drop_spawns_egg = spawn_egg.pos() + self._drop
            spawn_egg.setPos(drop_spawns_egg)
        self.egg_intersect_platform(scene=self)

    def spawn_egg_on_tick(self):
        egg = Egg(
            x=random.randint(100, 700),
            y=20,
            egg_color="beige",
            radius=20,
            speed=4,
        )
        self.spawns_egg.append(egg)
        egg.add_egg_to_scene(self)


def linear_int_sort(values: List[int]) -> List[int]:
    counter = {}
    for value in values:
        if value not in counter:
            counter[value] = 0
        counter[value] += 1
    max_value = max(values)
    min_value = min(values)
    result = []
    for value in range(min_value, max_value + 1):
        if value in counter:
            result += [value] * counter[value]
    return result
