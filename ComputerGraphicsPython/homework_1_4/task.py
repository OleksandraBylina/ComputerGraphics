import math
import numpy as np
import functionals

def clean_number(x):
    x = float(x)

    if abs(x) < 1e-10:
        x = 0.0

    return round(x, 6)

def clean_vector(v):
    return [clean_number(x) for x in v]

def clean_matrix(M):
    return np.array([[clean_number(M[i][j]) for j in range(M.shape[1])] for i in range(M.shape[0])])

def task_0():
    print("Завдання 0")
    vector = np.array([1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3)])
    theta = math.radians(60)
    q = functionals.quaternion(vector, theta)
    n = functionals.norm_quaternion(q)
    R = functionals.get_R_matrix_quaternion(q)

    print("Кватерніон:")
    print(clean_vector(q))
    print("Норма кватерніона:")
    print(clean_number(n))
    print("Матриця повороту:")
    print(clean_matrix(R))

def task_1():
    print("Завдання 1")
    p = np.array([1, 0, 0])
    theta = math.radians(90)
    q = functionals.quaternion(np.array([0, 0, 1]), theta)
    v = functionals.vector_to_quaternion(p)
    v_rotated = functionals.make_quaternion_rotation(p, q)
    p_rotated = functionals.quaternion_to_vector(v_rotated)
    R = functionals.get_rodrigues_matrix(np.array([0, 0, 1]), theta)
    p_matrix = R @ p

    print("Кватерніон точки:")
    print(clean_vector(v))
    print("Кватерніон повороту:")
    print(clean_vector(q))
    print("Повернута точка через кватерніони:")
    print(clean_vector(p_rotated))
    print("Повернута точка через матрицю:")
    print(clean_vector(p_matrix))

def task_2():
    print("Завдання 2")

    tetrahedron = functionals.Tetrahedron.from_points(
        np.array([0, 0, 0]),
        np.array([1, 0, 0]),
        np.array([0, 1, 0]),
        np.array([0, 0, 1])
    )
    theta1 = math.radians(45)
    theta2 = math.radians(30)
    q1 = functionals.quaternion(np.array([1, 0, 0]), theta1)
    q2 = functionals.quaternion(np.array([0, 1, 0]), theta2)
    q_total = functionals.mul_quaternion(q2, q1)
    q_total = functionals.normalize_quaternion(q_total)
    angle = functionals.find_angle_from_quaternion(q_total)
    axis = functionals.find_axis_from_quaternion(q_total)

    print("q1:")
    print(clean_vector(q1))
    print("q2:")
    print(clean_vector(q2))
    print("q_total = q2 * q1:")
    print(clean_vector(q_total))
    print("Вісь сумарного повороту:")
    print(clean_vector(axis))
    print("Кут сумарного повороту в градусах:")
    print(clean_number(math.degrees(angle)))
    print("Нові координати вершин тетраедра:")
    points = tetrahedron.points()
    for i in range(len(points)):
        point = points[i]
        vector = np.array([point[0], point[1], point[2]])
        rotated_quaternion = functionals.make_quaternion_rotation(vector, q_total)
        rotated_vector = functionals.quaternion_to_vector(rotated_quaternion)
        print(f"p{i + 1}' = {clean_vector(rotated_vector)}")

def task_3():
    print("Завдання 3")
    alpha = math.radians(20)
    beta = math.radians(90)
    gamma = math.radians(50)
    qz = functionals.quaternion(np.array([0, 0, 1]), alpha)
    qy = functionals.quaternion(np.array([0, 1, 0]), beta)
    qx = functionals.quaternion(np.array([1, 0, 0]), gamma)
    q = functionals.mul_quaternion(qz, qy)
    q = functionals.mul_quaternion(q, qx)
    q = functionals.normalize_quaternion(q)

    print("qz:")
    print(clean_vector(qz))
    print("qy:")
    print(clean_vector(qy))
    print("qx:")
    print(clean_vector(qx))
    print("Фінальний кватерніон:")
    print(clean_vector(q))
    print("Норма фінального кватерніона:")
    print(clean_number(functionals.norm_quaternion(q)))
    print("При beta = 90 градусів у кутах Ойлера виникає гімбал-лок.")
    print("Але кватерніон усе одно має коректні компоненти і норму 1.")
    print("Тобто орієнтація зберігається як один одиничний кватерніон.")

def task_4():
    print("Завдання 4")
    R = np.array([
        [0, -1, 0],
        [1, 0, 0],
        [0, 0, 1]
    ], dtype=float)
    q = functionals.R_matrix_to_quaternion(R)
    print("Матриця R:")
    print(clean_matrix(R))
    print("Кватерніон:")
    print(clean_vector(q))

def task_5():
    print("Завдання 5")
    M = np.array([
        [0, 1, 0, 10],
        [-2, 0, 0, -5],
        [0, 0, 1.5, 3],
        [0, 0, 0, 1]
    ], dtype=float)
    print("Матриця M:")
    print(clean_matrix(M))
    q = functionals.decomposition(M)
    print("Отриманий кватерніон:")
    print(clean_vector(q))

def main():
    task_0()
    print()
    task_1()
    print()
    task_2()
    print()
    task_3()
    print()
    task_4()
    print()
    task_5()

if __name__ == "__main__":
    main()