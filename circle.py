import math
import unittest
 #имортируем библеотеку math для работы с числом пи

def area(r):
     #функция принимает радиус круга (r) и возвращает его площадь(float)
    return math.pi * r * r
    


def perimeter(r):
    #функция принимает радиус круга (r) и возвращает его периметры(float)
    return 2 * math.pi * r



class CircleTestCase(unittest.TestCase):
    
    #тесты для площади круга


    #тест площади, когда радиус имеет нулевую длину
    def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
       
    #тест площади, когда длина радиусу положителена
    def test_square_mul(self):
       res = area(10) / math.pi
       self.assertEqual(res, 100)

    #тест площади, когда длина радиусу отрицательна
    def test_negative_on_positive_mul(self):
       res = area(-10) / math.pi
       self.assertEqual(res, 100)

   #тест площади, когда длина радиуса это число с плавающей точкой
    def test_double_mul(self):
       res = area(1.5) / math.pi
       self.assertEqual(res, 2.25)


    #тесты для периметра круга


    #тест периметра, когда радиус имеет нулевую длину
    def test_zero_perimeter(self):
       res = perimeter(0)
       self.assertEqual(res, 0)
       
    #тест периметра, когда длина радиусу положителена
    def test_square_perimeter(self):
       res = perimeter(10) / math.pi
       self.assertEqual(res, 20)

    #тест периметра, когда длина радиусу отрицательна
    def test_negative_on_positive_perimeter(self):
       res = perimeter(-10) / math.pi
       self.assertEqual(res, -20)

   #тест периметра, когда длина радиуса это число с плавающей точкой
    def test_double_perimeter(self):
       res = perimeter(1.5) / math.pi
       self.assertEqual(res, 3)