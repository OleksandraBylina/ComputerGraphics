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
    length = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)

    ux = vector[0] / length
    uy = vector[1] / length
    uz = vector[2] / length

    q = [0, 0, 0, 0]
    q[0] = math.cos(theta/2)
    q[1] = ux * math.sin(theta / 2)
    q[2] = uy * math.sin(theta / 2)
    q[3] = uz * math.sin(theta / 2)
    return q

def norm_quaternion(q):
    return math.sqrt(q[0] * q[0] + q[1] * q[1] + q[2] * q[2] + q[3] * q[3])

def normalize_quaternion(q):
    n = norm_quaternion(q)

    return [q[0] / n, q[1] / n, q[2] / n, q[3] / n]

def get_R_matrix_quaternion(q):
    q = normalize_quaternion(q)

    return np.array([[1 - 2 * q[2] * q[2] - 2 * q[3] * q[3], 2 * q[1] * q[2] - 2 * q[0] * q[3], 2 * q[1] * q[3] + 2 * q[0] * q[2]], [2 * q[1] * q[2] + 2 * q[0] * q[3], 1 - 2 * q[1] * q[1] - 2 * q[3] * q[3], 2 * q[2] * q[3] - 2 * q[0] * q[1]], [2 * q[1] * q[3] - 2 * q[0] * q[2], 2 * q[2] * q[3] + 2 * q[0] * q[1], 1 - 2 * q[1] * q[1] - 2 * q[2] * q[2]]])

def antiquaternion(q):
    return [q[0], -q[1], -q[2], -q[3]]

def mul_quaternion(q1, q2):
    q = [0, 0, 0, 0]
    q[0] = q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2] - q1[3] * q2[3]
    q[1] = q1[0] * q2[1] + q1[1] * q2[0] + q1[2] * q2[3] - q1[3] * q2[2]
    q[2] = q1[0] * q2[2] - q1[1] * q2[3] + q1[2] * q2[0] + q1[3] * q2[1]
    q[3] = q1[0] * q2[3] + q1[1] * q2[2] - q1[2] * q2[1] + q1[3] * q2[0]
    return q

def make_quaternion_rotation(vector, q):
    q = normalize_quaternion(q)
    aq = antiquaternion(q)
    v = vector_to_quaternion(vector)
    f1 = mul_quaternion(q, v)
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
    q = normalize_quaternion(q)
    return 2 * np.arccos(q[0])

def find_axis_from_quaternion(q):
    q = normalize_quaternion(q)
    theta = find_angle_from_quaternion(q)
    s = math.sin(theta / 2)

    if abs(s) < 1e-10:
        return [1, 0, 0]

    v = [0, 0, 0]
    v[0] = q[1] / s
    v[1] = q[2] / s
    v[2] = q[3] / s
    return v

def R_matrix_to_quaternion(R):
    trace = R[0][0] + R[1][1] + R[2][2]

    if trace > 0:
        s = np.sqrt(trace + 1.0) * 2
        w = 0.25 * s
        x = (R[2][1] - R[1][2]) / s
        y = (R[0][2] - R[2][0]) / s
        z = (R[1][0] - R[0][1]) / s

    elif R[0][0] > R[1][1] and R[0][0] > R[2][2]:
        s = np.sqrt(1.0 + R[0][0] - R[1][1] - R[2][2]) * 2
        w = (R[2][1] - R[1][2]) / s
        x = 0.25 * s
        y = (R[0][1] + R[1][0]) / s
        z = (R[0][2] + R[2][0]) / s

    elif R[1][1] > R[2][2]:
        s = np.sqrt(1.0 + R[1][1] - R[0][0] - R[2][2]) * 2
        w = (R[0][2] - R[2][0]) / s
        x = (R[0][1] + R[1][0]) / s
        y = 0.25 * s
        z = (R[1][2] + R[2][1]) / s

    else:
        s = np.sqrt(1.0 + R[2][2] - R[0][0] - R[1][1]) * 2
        w = (R[1][0] - R[0][1]) / s
        x = (R[0][2] + R[2][0]) / s
        y = (R[1][2] + R[2][1]) / s
        z = 0.25 * s

    q = [w, x, y, z]
    q = normalize_quaternion(q)
    return q

def decomposition(M):
    t =[0, 0, 0]
    t[0] = M[0][3]
    t[1] = M[1][3]
    t[2] = M[2][3]
    print("Вектор зсуву:")
    print(t)

    s =[0, 0, 0]
    s[0] = np.sqrt(M[0][0] ** 2 + M[1][0] ** 2 + M[2][0] ** 2)
    s[1] = np.sqrt(M[0][1] ** 2 + M[1][1] ** 2 + M[2][1] ** 2)
    s[2] = np.sqrt(M[0][2] ** 2 + M[1][2] ** 2 + M[2][2] ** 2)
    print("Вектор масштабу:")
    print(s)

    R = np.zeros((3, 3))
    R[0][0] = M[0][0] / s[0]
    R[1][0] = M[1][0] / s[0]
    R[2][0] = M[2][0] / s[0]
    R[0][1] = M[0][1] / s[1]
    R[1][1] = M[1][1] / s[1]
    R[2][1] = M[2][1] / s[1]
    R[0][2] = M[0][2] / s[2]
    R[1][2] = M[1][2] / s[2]
    R[2][2] = M[2][2] / s[2]
    print("Матриця повороту:")
    print(R)
    print("Перевірка ортогональності:")
    print(R.T @ R)
    q = R_matrix_to_quaternion(R)
    print("Кватерніон:")
    print(q)

    return q