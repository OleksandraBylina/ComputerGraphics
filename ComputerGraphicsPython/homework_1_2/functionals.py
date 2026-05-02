import numpy as np
import math



class Box:
    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7
        self.p8 = p8

    @classmethod
    def from_diagonal(cls, p1, p7):
        x1, y1, z1 = p1[0], p1[1], p1[2]
        x2, y2, z2 = p7[0], p7[1], p7[2]

        p1 = np.array([x1, y1, z1, 1])
        p2 = np.array([x2, y1, z1, 1])
        p3 = np.array([x2, y2, z1, 1])
        p4 = np.array([x1, y2, z1, 1])

        p5 = np.array([x1, y1, z2, 1])
        p6 = np.array([x2, y1, z2, 1])
        p7 = np.array([x2, y2, z2, 1])
        p8 = np.array([x1, y2, z2, 1])

        return cls(p1, p2, p3, p4, p5, p6, p7, p8)

    @classmethod
    def from_points(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        return cls(p1, p2, p3, p4, p5, p6, p7, p8)

    def points(self):
        return [
            self.p1, self.p2, self.p3, self.p4,
            self.p5, self.p6, self.p7, self.p8
        ]

    def printer(self):
        print(
            f"Координати точок:\n"
            f"перша: ({self.p1[0]}, {self.p1[1]}, {self.p1[2]})\n"
            f"друга: ({self.p2[0]}, {self.p2[1]}, {self.p2[2]})\n"
            f"третя: ({self.p3[0]}, {self.p3[1]}, {self.p3[2]})\n"
            f"четверта: ({self.p4[0]}, {self.p4[1]}, {self.p4[2]})\n"
            f"п'ята: ({self.p5[0]}, {self.p5[1]}, {self.p5[2]})\n"
            f"шоста: ({self.p6[0]}, {self.p6[1]}, {self.p6[2]})\n"
            f"сьома: ({self.p7[0]}, {self.p7[1]}, {self.p7[2]})\n"
            f"восьма: ({self.p8[0]}, {self.p8[1]}, {self.p8[2]})"
        )

class Tetrahedron:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    @classmethod
    def default(cls):
        p1 = np.array([0, 0, 0, 1])
        p2 = np.array([1, 0, 0, 1])
        p3 = np.array([0, 1, 0, 1])
        p4 = np.array([0, 0, 1, 1])

        return cls(p1, p2, p3, p4)

    @classmethod
    def from_points(cls, p1, p2, p3, p4):
        return cls(p1, p2, p3, p4)

    def points(self):
        return [self.p1, self.p2, self.p3, self.p4]

    def faces(self):
        return [
            [self.p1, self.p2, self.p3],
            [self.p1, self.p2, self.p4],
            [self.p1, self.p3, self.p4],
            [self.p2, self.p3, self.p4]
        ]

    def printer(self):
        print(
            f"Координати точок:\n"
            f"перша: ({self.p1[0]}, {self.p1[1]}, {self.p1[2]})\n"
            f"друга: ({self.p2[0]}, {self.p2[1]}, {self.p2[2]})\n"
            f"третя: ({self.p3[0]}, {self.p3[1]}, {self.p3[2]})\n"
            f"четверта: ({self.p4[0]}, {self.p4[1]}, {self.p4[2]})"
        )

class Triangle3D:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    @classmethod
    def default(cls):
        p1 = np.array([1, 2, 3, 1])
        p2 = np.array([4, 5, 6, 1])
        p3 = np.array([7, 8, 9, 1])

        return cls(p1, p2, p3)

    @classmethod
    def from_points(cls, p1, p2, p3):
        return cls(p1, p2, p3)

    def points(self):
        return [self.p1, self.p2, self.p3]

    def printer(self):
        print(
            f"Координати точок:\n"
            f"перша: ({self.p1[0]}, {self.p1[1]}, {self.p1[2]})\n"
            f"друга: ({self.p2[0]}, {self.p2[1]}, {self.p2[2]})\n"
            f"третя: ({self.p3[0]}, {self.p3[1]}, {self.p3[2]})"
        )

class Rectangle3D:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    @classmethod
    def from_points(cls, p1, p2, p3, p4):
        return cls(p1, p2, p3, p4)

    @classmethod
    def default(cls):
        p1 = np.array([0, 0, 0, 1])
        p2 = np.array([2, 0, 0, 1])
        p3 = np.array([2, 1, 0, 1])
        p4 = np.array([0, 1, 0, 1])
        return cls(p1, p2, p3, p4)

    def points(self):
        return [self.p1, self.p2, self.p3, self.p4]

    def printer(self):
        print(
            f"Координати точок:\n"
            f"перша: ({self.p1[0]}, {self.p1[1]}, {self.p1[2]})\n"
            f"друга: ({self.p2[0]}, {self.p2[1]}, {self.p2[2]})\n"
            f"третя: ({self.p3[0]}, {self.p3[1]}, {self.p3[2]})\n"
            f"четверта: ({self.p4[0]}, {self.p4[1]}, {self.p4[2]})"
        )

def get_R_x_matrix(phi):
    return np.array([[1, 0, 0, 0], [0, math.cos(phi), -math.sin(phi), 0], [0, math.sin(phi), math.cos(phi), 0], [0, 0, 0, 1]])

def get_R_y_matrix(phi):
    return np.array([[math.cos(phi), 0, math.sin(phi), 0], [0, 1, 0, 0], [-math.sin(phi), 0, math.cos(phi), 0], [0, 0, 0, 1]])

def get_R_z_matrix(phi):
    return np.array([[math.cos(phi), -math.sin(phi), 0, 0], [math.sin(phi), math.cos(phi), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

def get_R_matrix_for_rotate_around_vector(vector, alpha):
    alpha = math.radians(alpha)

    phi = math.atan2(vector[0], vector[2])
    vec_len = math.sqrt(vector[0] * vector[0] + vector[2] * vector[2])
    theta = math.atan2(vector[1], vec_len)

    R_y_phi = get_R_y_matrix(phi)
    R_x_theta = get_R_x_matrix(theta)
    R_z_alpha = get_R_z_matrix(alpha)
    R_x_untheta = get_R_x_matrix(-theta)
    R_y_unphi = get_R_y_matrix(-phi)

    R = R_y_phi @ R_x_theta @ R_z_alpha @ R_x_untheta @ R_y_unphi
    return R

def get_R_euler_matrix_xyz(phi, theta, psi):
    phi = math.radians(phi)
    theta = math.radians(theta)
    psi = math.radians(psi)
    R_x_phi = get_R_x_matrix(phi)
    R_y_theta = get_R_y_matrix(theta)
    R_z_psi = get_R_z_matrix(psi)
    R = R_z_psi @ R_y_theta @ R_x_phi
    return R

def get_R_euler_matrix_zyx(phi, theta, psi):
    phi = math.radians(phi)
    theta = math.radians(theta)
    psi = math.radians(psi)
    R_z_phi = get_R_z_matrix(phi)
    R_y_theta = get_R_y_matrix(theta)
    R_x_psi = get_R_x_matrix(psi)
    R = R_x_psi @ R_y_theta @ R_z_phi
    return R

def get_translate_matrix(t_x, t_y, t_z):
    return np.array([[1, 0, 0, t_x], [0, 1, 0, t_y], [0, 0, 1, t_z], [0, 0, 0, 1]])

def get_scale_matrix(s_x, s_y, s_z):
    return np.array([[s_x, 0, 0, 0], [0, s_y, 0, 0], [0, 0, s_z, 0], [0, 0, 0, 1]])

def make_rotation_around_vector(vector, vector_rotate, alpha):
    R = get_R_matrix_for_rotate_around_vector(vector_rotate, alpha)
    return R @ vector

def make_rotation_euler_xyz(vector, phi, theta, psi):
    R = get_R_euler_matrix_xyz(phi, theta, psi)
    return R @ vector

def make_rotation_euler_zyx(vector, phi, theta, psi):
    R = get_R_euler_matrix_zyx(phi, theta, psi)
    return R @ vector

def make_translation(vector, t_x, t_y, t_z):
    R = get_translate_matrix(t_x, t_y, t_z)
    return R @ vector

def make_scale(vector, s_x, s_y, s_z):
    R = get_scale_matrix(s_x, s_y, s_z)
    return R @ vector






























