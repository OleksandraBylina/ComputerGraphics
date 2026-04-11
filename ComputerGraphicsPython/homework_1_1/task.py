import functionals
import numpy as np


def task1():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pR_1 = functionals.rotation(30, squarr1.p1)
    pR_3 = functionals.rotation(30, squarr1.p3)
    squarr2 = functionals.Square.from_diagonal(pR_1, pR_3)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_R_matrix(30))
    pT_1 = functionals.translation(2, 3, squarr2.p1)
    pT_3 = functionals.translation(2, 3, squarr2.p3)
    squarr3 = functionals.Square.from_diagonal(pT_1, pT_3)
    print("Друга трансформація:")
    squarr3.printer()
    print(functionals.get_translate_matrix(2, 3))
    functionals.square_drawer(squarr1, squarr2)


def task2():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pS_1 = functionals.scale(2, 1, squarr1.p1)
    pS_2 = functionals.scale(2, 1, squarr1.p2)
    pS_3 = functionals.scale(2, 1, squarr1.p3)
    pS_4 = functionals.scale(2, 1, squarr1.p4)
    squarr2 = functionals.Square.from_points(pS_1, pS_2, pS_3, pS_4)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_scale_matrix(2, 1))
    pR_1 = functionals.rotation(45, squarr2.p1)
    pR_2 = functionals.rotation(45, squarr2.p2)
    pR_3 = functionals.rotation(45, squarr2.p3)
    pR_4 = functionals.rotation(45, squarr2.p4)
    squarr3 = functionals.Square.from_points(pR_1, pR_2, pR_3, pR_4)
    print("Друга трансформація:")
    squarr3.printer()
    print(functionals.get_R_matrix(45))

def task3():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pR_1 = functionals.rotation(90, squarr1.p1)
    pR_3 = functionals.rotation(90, squarr1.p3)
    squarr2 = functionals.Square.from_diagonal(pR_1, pR_3)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_R_matrix(90))
    pT_1 = functionals.translation(2, 3, squarr2.p1)
    pT_3 = functionals.translation(2, 3, squarr2.p3)
    squarr3 = functionals.Square.from_diagonal(pT_1, pT_3)
    print("Друга трансформація:")
    squarr3.printer()
    print(functionals.get_translate_matrix(2, 3))

def task4():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pS_1 = functionals.scale(1, 3, squarr1.p1)
    pS_2 = functionals.scale(1, 3, squarr1.p2)
    pS_3 = functionals.scale(1, 3, squarr1.p3)
    pS_4 = functionals.scale(1, 3, squarr1.p4)
    squarr2 = functionals.Square.from_points(pS_1, pS_2, pS_3, pS_4)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_scale_matrix(1, 3))
    pR_1 = functionals.rotation(60, squarr2.p1)
    pR_2 = functionals.rotation(60, squarr2.p2)
    pR_3 = functionals.rotation(60, squarr2.p3)
    pR_4 = functionals.rotation(60, squarr2.p4)
    squarr3 = functionals.Square.from_points(pR_1, pR_2, pR_3, pR_4)
    print("Друга трансформація:")
    squarr3.printer()
    print(functionals.get_R_matrix(60))

def task5():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pT_1 = functionals.translation(1, -1, squarr1.p1)
    pT_3 = functionals.translation(1, -1, squarr1.p3)
    squarr2 = functionals.Square.from_diagonal(pT_1, pT_3)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_translate_matrix(1, -1))
    pS_1 = functionals.scale(2, 2, squarr2.p1)
    pS_3 = functionals.scale(2, 2, squarr2.p3)
    squarr3 = functionals.Square.from_diagonal(pS_1, pS_3)
    print("Друга трансформація:")
    squarr3.printer()
    print(functionals.get_scale_matrix(2, 2))

def task6_1():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pS_1 = functionals.scale(1, 3, squarr1.p1)
    pS_2 = functionals.scale(1, 3, squarr1.p2)
    pS_3 = functionals.scale(1, 3, squarr1.p3)
    pS_4 = functionals.scale(1, 3, squarr1.p4)
    squarr2 = functionals.Square.from_points(pS_1, pS_2, pS_3, pS_4)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_scale_matrix(1, 3))
    pR_1 = functionals.rotation(60, squarr2.p1)
    pR_2 = functionals.rotation(60, squarr2.p2)
    pR_3 = functionals.rotation(60, squarr2.p3)
    pR_4 = functionals.rotation(60, squarr2.p4)
    squarr3 = functionals.Square.from_points(pR_1, pR_2, pR_3, pR_4)
    print("Друга трансформація:")
    squarr3.printer()
    print(functionals.get_R_matrix(60))
    pT1 = functionals.translation(2, 3, squarr3.p1)
    pT2 = functionals.translation(2, 3, squarr3.p2)
    pT3 = functionals.translation(2, 3, squarr3.p3)
    pT4 = functionals.translation(2, 3, squarr3.p4)
    squarr4 = functionals.Square.from_points(pT1, pT2, pT3, pT4)
    print("Третя трансформація:")
    squarr4.printer()
    print(functionals.get_translate_matrix(2, 3))

def task6_2():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pT_1 = functionals.translation(2, 3, squarr1.p1)
    pT_3 = functionals.translation(2, 3, squarr1.p3)
    squarr2 = functionals.Square.from_diagonal(pT_1, pT_3)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_translate_matrix(2, 3))
    pS_1 = functionals.scale(1, 3, squarr2.p1)
    pS_2 = functionals.scale(1, 3, squarr2.p2)
    pS_3 = functionals.scale(1, 3, squarr2.p3)
    pS_4 = functionals.scale(1, 3, squarr2.p4)
    squarr3 = functionals.Square.from_points(pS_1, pS_2, pS_3, pS_4)
    print("Друга трансформація:")
    squarr3.printer()
    print(functionals.get_scale_matrix(1, 3))
    pR_1 = functionals.rotation(60, squarr3.p1)
    pR_2 = functionals.rotation(60, squarr3.p2)
    pR_3 = functionals.rotation(60, squarr3.p3)
    pR_4 = functionals.rotation(60, squarr3.p4)
    squarr4 = functionals.Square.from_points(pR_1, pR_2, pR_3, pR_4)
    print("Третя трансформація:")
    squarr4.printer()
    print(functionals.get_R_matrix(60))

def task_7_1():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pR_1 = functionals.rotation_with_another_point(60, 0.5, 0.5, squarr1.p1)
    pR_3 = functionals.rotation_with_another_point(60, 0.5, 0.5, squarr1.p3)
    squarr2 = functionals.Square.from_diagonal(pR_1, pR_3)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_rotation_with_another_point_matrix(60, 0.5, 0.5))

def task_7_2():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pR_1 = functionals.rotation_with_another_point(60, 0, 1, squarr1.p1)
    pR_3 = functionals.rotation_with_another_point(60, 0, 1, squarr1.p3)
    squarr2 = functionals.Square.from_diagonal(pR_1, pR_3)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_rotation_with_another_point_matrix(60, 0, 1))

def task_7_3():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pR_1 = functionals.rotation_with_another_point(60, 1, 1, squarr1.p1)
    pR_3 = functionals.rotation_with_another_point(60, 1, 1, squarr1.p3)
    squarr2 = functionals.Square.from_diagonal(pR_1, pR_3)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_rotation_with_another_point_matrix(60, 1, 1))

def task_7_4():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pR_1 = functionals.rotation_with_another_point(60, 2, 2, squarr1.p1)
    pR_3 = functionals.rotation_with_another_point(60, 2, 2, squarr1.p3)
    squarr2 = functionals.Square.from_diagonal(pR_1, pR_3)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_rotation_with_another_point_matrix(60, 2, 2))

def task_8_1():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pS_1 = functionals.scale_with_another_point(2, 3, 0.5, 0.5, squarr1.p1)
    pS_2 = functionals.scale_with_another_point(2, 3, 0.5, 0.5, squarr1.p2)
    pS_3 = functionals.scale_with_another_point(2, 3, 0.5, 0.5, squarr1.p3)
    pS_4 = functionals.scale_with_another_point(2, 3, 0.5, 0.5, squarr1.p4)
    squarr2 = functionals.Square.from_points(pS_1, pS_2, pS_3, pS_4)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_scale_with_another_point_matrix(2, 3, 0.5, 0.5))

def task_8_2():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pS_1 = functionals.scale_with_another_point(2, 3, 0, 1, squarr1.p1)
    pS_2 = functionals.scale_with_another_point(2, 3, 0, 1, squarr1.p2)
    pS_3 = functionals.scale_with_another_point(2, 3, 0, 1, squarr1.p3)
    pS_4 = functionals.scale_with_another_point(2, 3, 0, 1, squarr1.p4)
    squarr2 = functionals.Square.from_points(pS_1, pS_2, pS_3, pS_4)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_scale_with_another_point_matrix(2, 3, 0, 1))

def task_8_3():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pS_1 = functionals.scale_with_another_point(2, 3, 1, 1, squarr1.p1)
    pS_2 = functionals.scale_with_another_point(2, 3, 1, 1, squarr1.p2)
    pS_3 = functionals.scale_with_another_point(2, 3, 1, 1, squarr1.p3)
    pS_4 = functionals.scale_with_another_point(2, 3, 1, 1, squarr1.p4)
    squarr2 = functionals.Square.from_points(pS_1, pS_2, pS_3, pS_4)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_scale_with_another_point_matrix(2, 3, 1, 1))

def task_8_4():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pS_1 = functionals.scale_with_another_point(2, 3, 2, 2, squarr1.p1)
    pS_2 = functionals.scale_with_another_point(2, 3, 2, 2, squarr1.p2)
    pS_3 = functionals.scale_with_another_point(2, 3, 2, 2, squarr1.p3)
    pS_4 = functionals.scale_with_another_point(2, 3, 2, 2, squarr1.p4)
    squarr2 = functionals.Square.from_points(pS_1, pS_2, pS_3, pS_4)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_scale_with_another_point_matrix(2, 3, 2, 2))

def task_9_1():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pS_1 = functionals.scale_with_another_point(2, 1, 1, 1, squarr1.p1)
    pS_2 = functionals.scale_with_another_point(2, 1, 1, 1, squarr1.p2)
    pS_3 = functionals.scale_with_another_point(2, 1, 1, 1, squarr1.p3)
    pS_4 = functionals.scale_with_another_point(2, 1, 1, 1, squarr1.p4)
    squarr2 = functionals.Square.from_points(pS_1, pS_2, pS_3, pS_4)
    print("Перша трансформація:")
    squarr2.printer()
    pT1 = functionals.translation(3, -2, squarr2.p1)
    pT2 = functionals.translation(3, -2, squarr2.p2)
    pT3 = functionals.translation(3, -2, squarr2.p3)
    pT4 = functionals.translation(3, -2, squarr2.p4)
    squarr3 = functionals.Square.from_points(pT1, pT2, pT3, pT4)
    print("Друга трансформація:")
    squarr3.printer()

def task_9_2():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pT_1 = functionals.translation(3, -2, squarr1.p1)
    pT_3 = functionals.translation(3, -2, squarr1.p3)
    squarr2 = functionals.Square.from_diagonal(pT_1, pT_3)
    print("Перша трансформація:")
    squarr2.printer()
    pS_1 = functionals.scale_with_another_point(2, 1, 1, 1, squarr2.p1)
    pS_2 = functionals.scale_with_another_point(2, 1, 1, 1, squarr2.p2)
    pS_3 = functionals.scale_with_another_point(2, 1, 1, 1, squarr2.p3)
    pS_4 = functionals.scale_with_another_point(2, 1, 1, 1, squarr2.p4)
    squarr3 = functionals.Square.from_points(pS_1, pS_2, pS_3, pS_4)
    print("Друга трансформація:")
    squarr3.printer()

def task_10_1():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pF_1 = functionals.scale_rotation_and_translation_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5, squarr1.p1)
    pF_2 = functionals.scale_rotation_and_translation_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5, squarr1.p2)
    pF_3 = functionals.scale_rotation_and_translation_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5, squarr1.p3)
    pF_4 = functionals.scale_rotation_and_translation_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5, squarr1.p4)
    squarr2 = functionals.Square.from_points(pF_1, pF_2, pF_3, pF_4)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_scale_rotation_and_translation_with_another_point_matrix(30, 2, 2, 1, -1, 0.5, 0.5))

def task_10_2():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pF_1 = functionals.translation_scale_and_rotation_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5, squarr1.p1)
    pF_2 = functionals.translation_scale_and_rotation_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5, squarr1.p2)
    pF_3 = functionals.translation_scale_and_rotation_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5, squarr1.p3)
    pF_4 = functionals.translation_scale_and_rotation_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5, squarr1.p4)
    squarr2 = functionals.Square.from_points(pF_1, pF_2, pF_3, pF_4)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_translation_scale_and_rotation_matrix_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5))

def task_10_3():
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    pF_1 = functionals.scale_translation_and_rotation_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5, squarr1.p1)
    pF_2 = functionals.scale_translation_and_rotation_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5, squarr1.p2)
    pF_3 = functionals.scale_translation_and_rotation_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5, squarr1.p3)
    pF_4 = functionals.scale_translation_and_rotation_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5, squarr1.p4)
    squarr2 = functionals.Square.from_points(pF_1, pF_2, pF_3, pF_4)
    print("Перша трансформація:")
    squarr2.printer()
    print(functionals.get_scale_translation_and_rotation_matrix_with_another_point(30, 2, 2, 1, -1, 0.5, 0.5))

def task_11():
    TRS_matrix = np.array([[2.394, -0.416, 2.0], [0.624, 1.956, 3.4], [0, 0, 1]])
    inv_TRS_matrix = functionals.make_inv_TRS_matrix(TRS_matrix)
    p_1 = np.array([2, 3.4, 1])
    p_2 = np.array([4.9, 4, 1])
    p_3 = np.array([4.5, 6, 1])
    p_4 = np.array([1.6, 5.4, 1])
    squarr1 = functionals.Square.from_points(p_1, p_2, p_3, p_4)
    pF_1 = inv_TRS_matrix @ p_1
    pF_2 = inv_TRS_matrix @ p_2
    pF_3 = inv_TRS_matrix @ p_3
    pF_4 = inv_TRS_matrix @ p_4
    squarr2 = functionals.Square.from_points(pF_1, pF_2, pF_3, pF_4)
    print(inv_TRS_matrix)
    squarr2.printer()

def task_12():
    TRS_matrix = np.array([[0.866, 0.5, 4], [0.5, 0.866, 3], [0, 0, 1]])
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    test = functionals.TRS_matrix_tester(TRS_matrix)
    if test:
        phi, s_x, s_y, t_x, t_y = functionals.TRS_partition(TRS_matrix)
        print(f"phi: {phi}, s_X: {s_x}, s_Y: {s_y}, t_X: {t_x}, t_Y: {t_y}")
        pF_1 = TRS_matrix @ squarr1.p1
        pF_2 = TRS_matrix @ squarr1.p2
        pF_3 = TRS_matrix @ squarr1.p3
        pF_4 = TRS_matrix @ squarr1.p4
        squarr2 = functionals.Square.from_points(pF_1, pF_2, pF_3, pF_4)
        squarr2.printer()

def task_13():
    TRS_matrix = np.array([[1.414, -2.121, 1], [1.414, -2.121, 1], [0, 0, 1]])
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    phi, s_x, s_y, t_x, t_y = functionals.TRS_partition(TRS_matrix)
    print(f"phi: {phi}, s_X: {s_x}, s_Y: {s_y}, t_X: {t_x}, t_Y: {t_y}")
    pF_1 = TRS_matrix @ squarr1.p1
    pF_2 = TRS_matrix @ squarr1.p2
    pF_3 = TRS_matrix @ squarr1.p3
    pF_4 = TRS_matrix @ squarr1.p4
    squarr2 = functionals.Square.from_points(pF_1, pF_2, pF_3, pF_4)
    squarr2.printer()

def task_14():
    TRS_matrix = np.array([[1.732, -1, 5], [1, 1.732, -3], [0, 0, 1]])
    squarr1 = functionals.Square.from_diagonal(np.array([0, 0, 1]), np.array([1, 1, 1]))
    phi, s_x, s_y, t_x, t_y = functionals.TRS_partition_with_another_point(TRS_matrix, 1, 1)
    print(f"phi: {phi}, s_X: {s_x}, s_Y: {s_y}, t_X: {t_x}, t_Y: {t_y}")
    pF_1 = TRS_matrix @ squarr1.p1
    pF_2 = TRS_matrix @ squarr1.p2
    pF_3 = TRS_matrix @ squarr1.p3
    pF_4 = TRS_matrix @ squarr1.p4
    squarr2 = functionals.Square.from_points(pF_1, pF_2, pF_3, pF_4)
    squarr2.printer()



def main():
    print("===== Завдання 1 =====")
    task1()

    print("\n===== Завдання 2 =====")
    task2()

    print("\n===== Завдання 3 =====")
    task3()

    print("\n===== Завдання 4 =====")
    task4()

    print("\n===== Завдання 5 =====")
    task5()

    print("\n===== Завдання 6.1 =====")
    task6_1()

    print("\n===== Завдання 6.2 =====")
    task6_2()

    print("\n===== Завдання 7.1 =====")
    task_7_1()

    print("\n===== Завдання 7.2 =====")
    task_7_2()

    print("\n===== Завдання 7.3 =====")
    task_7_3()

    print("\n===== Завдання 7.4 =====")
    task_7_4()

    print("\n===== Завдання 8.1 =====")
    task_8_1()

    print("\n===== Завдання 8.2 =====")
    task_8_2()

    print("\n===== Завдання 8.3 =====")
    task_8_3()

    print("\n===== Завдання 8.4 =====")
    task_8_4()

    print("\n===== Завдання 9.1 =====")
    task_9_1()

    print("\n===== Завдання 9.2 =====")
    task_9_2()

    print("\n===== Завдання 10.1 =====")
    task_10_1()

    print("\n===== Завдання 10.2 =====")
    task_10_2()

    print("\n===== Завдання 10.3 =====")
    task_10_3()

    print("\n===== Завдання 11 =====")
    task_11()

    print("\n===== Завдання 12 =====")
    task_12()

    print("\n===== Завдання 13 =====")
    task_13()

    print("\n===== Завдання 14 =====")
    task_14()


if __name__ == "__main__":
    main()