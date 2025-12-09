import unittest

def area(a, b):
    #функция принимает длины смежных сторон прямоугольника (a, b) и возвращает его площадь
    return a * b

def perimeter(a, b):
    #функция принимает  длины смежных сторон прямоугольника (a, b) и возвращает его периметр
    return (a + b) * 2

class RectangleTestCase(unittest.TestCase):
    
    #тесты для площади прямоугольника


    #тест площади, когда одна из сторон имеет нулевую длину
    def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   #тест площади, когда стороны прямоугольника равны
    def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

   #тест площади, когда одна из сторон имеет отрицательную длину
    def test_negative_on_positive_mul(self):
       res = area(10, -20)
       self.assertEqual(res, -200)

   #тест площади, когда обе стороны имеют отрицательную длину
    def test_negative_on_negative_mul(self):
       res = area(-10, -20)
       self.assertEqual(res, 200)

   #тест площади, когда длина сторон это число с плавающей точкой
    def test_double_mul(self):
       res = area(1.5, 1.5)
       self.assertEqual(res, 2.25)


    #тесты для периметра прямоугольника


    #тест периметра, когда одна из сторон имеет нулевую длину
    def test_zero_perimeter(self):
       res = perimeter(10, 0)
       self.assertEqual(res, 20)
       
    #тест периметра, когда стороны прямоугольнка равны
    def test_square_perimeter(self):
       res = perimeter(10, 10)
       self.assertEqual(res, 40)

    #тест периметра, когда одна из сторон имеет отрицательную длину
    def test_negative_on_positive_perimeter(self):
       res = perimeter(10, -10)
       self.assertEqual(res, 0)

    #тест периметра, когда обе стороны имеют отрицательную длину
    def test_negative_on_negative_perimeter(self):
       res = perimeter(-10, -10)
       self.assertEqual(res, -40)

    #тест периметра, когда длина сторон это число с плавающей точкой
    def test_float_perimeter(self):
       res = perimeter(1.5, 1.5)
       self.assertEqual(res, 6)