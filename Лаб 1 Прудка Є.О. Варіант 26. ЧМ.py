import numpy as np

def f(x, y):
 return np.abs(x - y) / np.abs(x)
def main():
 x1 = np.sqrt(41) 
 x2 = 6 / 7 
 x1_1 = 6.40
 x2_2 = 0.857
 rel_error_x1 = f(x1, x1_1)
 rel_error_x2 = f(x2, x2_2)
 if rel_error_x1 < rel_error_x2:
    print("Перша рівність точніше з відносною похибкою:", round(rel_error_x1, 5))
 elif rel_error_x2 < rel_error_x1:
    print("Друга рівність точніше з відносною похибкою:", round(rel_error_x2, 5))
 else:
    print("Обидві рівності мають однакову точність з відносною похибкою:", round(rel_error_x2, 5))
if __name__ == "__main__":
 main()
 