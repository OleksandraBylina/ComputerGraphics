from dataclasses import dataclass
import numpy as np
import math

from GraphicEngine2d.src.engine.scene.Scene import Scene
from GraphicEngine2d.src.engine.model.Polygon import Polygon
from GraphicEngine2d.src.engine.model.Point import SimplePoint
from GraphicEngine2d.src.engine.model.LineModel import LineModel, SampleScene


class Square:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    @classmethod
    def from_diagonal(cls, p1, p3):
        cx = (p1[0] + p3[0]) / 2
        cy = (p1[1] + p3[1]) / 2
        vx = (p1[0] - p3[0]) / 2
        vy = (p1[1] - p3[1]) / 2

        p2 = np.array([cx - vy, cy + vx, 1])
        p4 = np.array([cx + vy, cy - vx, 1])

        return cls(p1, p2, p3, p4)

    @classmethod
    def from_points(cls, p1, p2, p3, p4):
        return cls(p1, p2, p3, p4)

    def points(self):
        return [self.p1, self.p2, self.p3, self.p4]

    def printer(self):
        print(
            f"Координати точок:\n"
            f"перша: ({self.p1[0]}, {self.p1[1]})\n"
            f"друга: ({self.p2[0]}, {self.p2[1]})\n"
            f"третя: ({self.p3[0]}, {self.p3[1]})\n"
            f"четверта: ({self.p4[0]}, {self.p4[1]})"
        )

def get_R_matrix(phi):
    phi = math.radians(phi)
    return np.array([[math.cos(phi), -math.sin(phi), 0], [math.sin(phi), math.cos(phi), 0], [0, 0, 1]])

def get_translate_matrix(t_x, t_y):
    return np.array([[1, 0, t_x], [0, 1, t_y], [0, 0, 1]])

def get_inv_translate_matrix(t_x, t_y):
    return np.array([[1, 0, -t_x], [0, 1, -t_y], [0, 0, 1]])

def get_scale_matrix(s_x, s_y):
    return np.array([[s_x, 0, 0], [0, s_y, 0], [0, 0, 1]])

def rotation(phi, vector):
    return get_R_matrix(phi) @ vector

def translation(t_x, t_y, vector):
    return get_translate_matrix(t_x, t_y) @ vector

def inv_translation(t_x, t_y, vector):
    return get_inv_translate_matrix(t_x, t_y) @ vector

def scale(s_x, s_y, vector):
    return get_scale_matrix(s_x, s_y) @ vector

def get_rotation_with_another_point_matrix(phi, Ot_x, Ot_y):
    m1 = get_R_matrix(phi)
    m2 = get_inv_translate_matrix(Ot_x, Ot_y)
    m3 = get_translate_matrix(Ot_x, Ot_y)
    return m3 @ m1 @ m2

def get_scale_with_another_point_matrix(s_x, s_y, Ot_x, Ot_y):
    m1 = get_scale_matrix(s_x, s_y)
    m2 = get_inv_translate_matrix(Ot_x, Ot_y)
    m3 = get_translate_matrix(Ot_x, Ot_y)
    return m3 @ m1 @ m2

def rotation_with_another_point(phi, Ot_x, Ot_y, vector):
    m1 = inv_translation(Ot_x, Ot_y, vector)
    m2 = rotation(phi, m1)
    m3 = translation(Ot_x, Ot_y, m2)
    return m3

def scale_with_another_point(s_x, s_y, Ot_x, Ot_y, vector):
    m1 = inv_translation(Ot_x, Ot_y, vector)
    m2 = scale(s_x, s_y, m1)
    m3 = translation(Ot_x, Ot_y, m2)
    return m3

def get_scale_rotation_and_translation_with_another_point_matrix(phi, s_x, s_y, t_x, t_y, Ot_x, Ot_y):
    m1 = get_inv_translate_matrix(Ot_x, Ot_y)
    m2 = get_scale_matrix(s_x, s_y)
    m3 = get_R_matrix(phi)
    m4 = get_translate_matrix(Ot_x, Ot_y)
    m5 = get_translate_matrix(t_x, t_y)
    return m5 @ m4 @ m3 @ m2 @ m1

def get_translation_scale_and_rotation_matrix_with_another_point(phi, t_x, t_y, s_x, s_y, Ot_x, Ot_y):
    m1 = get_translate_matrix(t_x, t_y)
    m2 = get_inv_translate_matrix(Ot_x, Ot_y)
    m3 = get_scale_matrix(s_x, s_y)
    m4 = get_R_matrix(phi)
    m5 = get_translate_matrix(Ot_x, Ot_y)
    return m5 @ m4 @ m3 @ m2 @ m1

def get_scale_translation_and_rotation_matrix_with_another_point(phi, t_x, t_y, s_x, s_y, Ot_x, Ot_y):
    m1 = get_inv_translate_matrix(Ot_x, Ot_y)
    m2 = get_scale_matrix(s_x, s_y)
    m3 = get_translate_matrix(Ot_x, Ot_y)
    m4 = get_translate_matrix(t_x, t_y)
    m5 = get_inv_translate_matrix(Ot_x, Ot_y)
    m6 = get_R_matrix(phi)
    m7 = get_translate_matrix(Ot_x, Ot_y)
    return m7 @ m6 @ m5 @ m4 @ m3 @ m2 @ m1

def scale_rotation_and_translation_with_another_point(phi, s_x, s_y, t_x, t_y, Ot_x, Ot_y, vector):
    return get_scale_rotation_and_translation_with_another_point_matrix(phi, t_x, t_y, s_x, s_y, Ot_x, Ot_y) @ vector

def translation_scale_and_rotation_with_another_point(phi, s_x, s_y, t_x, t_y, Ot_x, Ot_y, vector):
    return get_translation_scale_and_rotation_matrix_with_another_point(phi, t_x, t_y, s_x, s_y, Ot_x, Ot_y) @ vector

def scale_translation_and_rotation_with_another_point(phi, s_x, s_y, t_x, t_y, Ot_x, Ot_y, vector):
    return get_scale_translation_and_rotation_matrix_with_another_point(phi, t_x, t_y, s_x, s_y, Ot_x, Ot_y) @ vector

def TRS_partition(TRS_matrix):
    t_x = TRS_matrix[0, 2]
    t_y = TRS_matrix[1, 2]
    s_x = (TRS_matrix[0, 0] ** 2 + TRS_matrix[1, 0] ** 2) ** 0.5
    s_y = (TRS_matrix[0, 1] ** 2 + TRS_matrix[1, 1] ** 2) ** 0.5
    phi = math.atan2(TRS_matrix[1, 0], TRS_matrix[0, 0])
    return phi, s_x, s_y, t_x, t_y

def make_inv_TRS_matrix(TRS_matrix):
    phi, s_x, s_y, t_x, t_y = TRS_partition(TRS_matrix)
    T_matrix = get_translate_matrix(-t_x, -t_y)
    R_matrix = get_R_matrix(-math.degrees(phi))
    S_matrix = get_scale_matrix(1/s_x, 1/s_y)
    return S_matrix @ R_matrix @ T_matrix

def TRS_matrix_tester(TRS_matrix):
    eps = 1e-9
    if (TRS_matrix[2, 0] != 0 or TRS_matrix[2, 1] != 0 or TRS_matrix[2, 2] != 1):
        print("Неправильний формат матриці")
        return False
    phi, s_x, s_y, t_x, t_y = TRS_partition(TRS_matrix)
    if (s_x == 0 or s_y == 0):
        print("Вироджений масштаб")
        return False
    dot = TRS_matrix[0, 0] * TRS_matrix[0, 1] + TRS_matrix[1, 0] * TRS_matrix[1, 1]
    if abs(dot) > eps:
        print("Стовпці не перпендикулярні, є зсув")
        return False
    det = TRS_matrix[0, 0] * TRS_matrix[1, 1] - TRS_matrix[0, 1] * TRS_matrix[1, 0]
    if det < 0:
        print("Є відзеркалення")
        return False
    return True

def TRS_partition_with_another_point(TRS_matrix, Ot_x, Ot_y):
    s_x = (TRS_matrix[0, 0] ** 2 + TRS_matrix[1, 0] ** 2) ** 0.5
    s_y = (TRS_matrix[0, 1] ** 2 + TRS_matrix[1, 1] ** 2) ** 0.5
    phi = math.atan2(TRS_matrix[1, 0], TRS_matrix[0, 0])
    A = np.array([[TRS_matrix[0, 0], TRS_matrix[0, 1]], [TRS_matrix[1, 0], TRS_matrix[1, 1]]])
    p = np.array([[Ot_x], [Ot_y]])
    t_x = TRS_matrix[0, 2] - Ot_x + (A @ p)[0, 0]
    t_y = TRS_matrix[1, 2] - Ot_y + (A @ p)[1, 0]
    return phi, s_x, s_y, t_x, t_y

def square_drawer(square_1, square_2):
    square1 = np.array([square_1.p1, square_1.p2, square_1.p3, square_1.p4])
    square2 = np.array([square_2.p1, square_2.p2, square_2.p3, square_2.p4])
    scene = SampleScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, 6, 6),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    )
    square_before = Polygon(square1, color="light green", line_style="--", vertices_show=True, vertex_color="grey", vertex_size=50)
    square_after = Polygon(square2, color="green", line_style="solid", vertices_show=True, vertex_color="grey", vertex_size=50)
    scene["rect"] = square_before
    scene["rect"] = square_after
    scene.show()




















