import math
import numpy as np

class Tetrahedron:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    @classmethod
    def from_points(cls, p1, p2, p3, p4):
        p1 = np.array([p1[0], p1[1], p1[2], 1])
        p2 = np.array([p2[0], p2[1], p2[2], 1])
        p3 = np.array([p3[0], p3[1], p3[2], 1])
        p4 = np.array([p4[0], p4[1], p4[2], 1])

        return cls(p1, p2, p3, p4)

    def points(self):
        return [
            self.p1, self.p2, self.p3, self.p4
        ]

    def printer(self):
        print(
            f"Координати точок:\n"
            f"перша: ({self.p1[0]}, {self.p1[1]}, {self.p1[2]})\n"
            f"друга: ({self.p2[0]}, {self.p2[1]}, {self.p2[2]})\n"
            f"третя: ({self.p3[0]}, {self.p3[1]}, {self.p3[2]})\n"
            f"четверта: ({self.p4[0]}, {self.p4[1]}, {self.p4[2]})"
        )

def quaternion(vector, theta):
    q = []
    q[0] = math.cos(theta/2)
    q[1] = math.cos(theta/2) + vector[0] * math.sin(theta / 2)
    q[2] = math.cos(theta/2) + vector[1] * math.sin(theta / 2)
    q[3] = math.cos(theta/2) + vector[2] * math.sin(theta / 2)
    return q

def norm_quaternion(q):
    return math.sqrt(q[0] * q[0] + q[1] * q[1] + q[2] * q[2] + q[3] * q[3])

def get_R_matrix_quaternion(q):
    return np.array([[1 - 2 * q[2] * q[2] - 2 * q[3] * q[3], 2 * q[1] * q[2] - 2 * q[0] * q[3], 2 * q[1] * q[3] + 2 * q[0] * q[2]], [2 * q[1] * q[2] + 2 * q[0] * q[3], 1 - 2 * q[1] * q[1] - 2 * q[3] * q[3], 2 * q[2] * q[3] - 2 * q[0] * q[1]], [2 * q[1] * q[2] - 2 * q[0] * q[3], 2 * q[2] * q[3] + 2 * q[0] * q[1], 1 - 2 * q[1] * q[1] - 2 * q[2] * q[2]]])

def antiquaternion(q):
    return [q[0], -q[1], -q[2], -q[3]]

def mul_quaternion(q1, q2):
    q = []
    q[0] = q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2] - q1[3] * q2[3]
    q[1] = q1[0] * q2[1] - q1[1] * q2[0] - q1[2] * q2[3] - q1[3] * q2[2]
    q[2] = q1[0] * q2[2] - q1[1] * q2[3] - q1[2] * q2[0] - q1[3] * q2[1]
    q[3] = q1[0] * q2[3] - q1[1] * q2[2] - q1[2] * q2[1] - q1[3] * q2[0]
    return q

def make_quaternion_rotation(vector, q):
    aq = antiquaternion(q)
    f1 = mul_quaternion(q, vector)
    f2 = mul_quaternion(f1, aq)
    return f2

def vector_to_quaternion(vector):
    return [0, vector[0], vector[1], vector[2]]

def quaternion_to_vector(q):
    return [q[1], q[2], q[3]]

def get_rodrigues_matrix(vector, theta):
    length = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    ux = vector[0] / length
    uy = vector[1] / length
    uz = vector[2] / length
    c = np.cos(theta)
    s = np.sin(theta)
    R = np.array([[c + ux**2 * (1 - c), ux * uy * (1 - c) - uz * s, ux * uz * (1 - c) + uy * s], [uy * ux * (1 - c) + uz * s, c + uy**2 * (1 - c), uy * uz * (1 - c) - ux * s ], [uz * ux * (1 - c) - uy * s, uz * uy * (1 - c) + ux * s, c + uz**2 * (1 - c)]])
    return R

def make_rodrigues_rotation(vector, v, theta):
    R = get_rodrigues_matrix(v, theta)
    return R @ vector

def find_angle_from_quaternion(q):
    return 2 * np.arccos(q[0])

def find_axis_from_quaternion(q):
    v = []
    theta = find_angle_from_quaternion(q)
    s = math.sin(theta / 2)
    v[0] = q[1] / s
    v[1] = q[2] / s
    v[2] = q[3] / s
    return v









