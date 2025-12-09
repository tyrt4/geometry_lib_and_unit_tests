import unittest
def area(a):
    #функция принимает длину стороны квадрата (a) и возвращает его площадь
    return a * a


def perimeter(a):
    #функция принимает длину стороны квадрата (a) и возвращает его периметр
    return 4 * a


class SquareTestCase(unittest.TestCase):
    
    #тесты для площади квадрата


    #тест площади, стороны имеют нулевую длину
    def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)

   #тест площади, когда  стороны имеют отрицательную длину
    def test_negative_on_negative_mul(self):
       res = area(-10)
       self.assertEqual(res, 100)

   #тест площади, когда длина сторон это число с плавающей точкой
    def test_double_mul(self):
       res = area(1.5)
       self.assertEqual(res, 2.25)


    #тесты для периметра квадрата


    #тест периметра, когда стороны имеют нулевую длину
    def test_zero_perimeter(self):
       res = perimeter(0)
       self.assertEqual(res, 0)
       

     #тест периметра, когда  стороны имеют отрицательную длину
    def test_negative_on_negative_perimeter(self):
       res = perimeter(-10)
       self.assertEqual(res, -40)

    #тест периметра, когда длина сторон это число с плавающей точкой
    def test_float_perimeter(self):
       res = perimeter(1.5)
       self.assertEqual(res, 6)