import unittest 
import math 
import triangle, circle, rectangle, square
class RectangleTestCase(unittest.TestCase):
    
    #тесты для площади прямоугольника


    #тест площади, когда одна из сторон имеет нулевую длину
    def test_zero_mul(self):
       res = rectangle.area(10, 0)
       self.assertEqual(res, 0)
       
   #тест площади, когда стороны прямоугольника равны
    def test_square_mul(self):
       res = rectangle.area(10, 10)
       self.assertEqual(res, 100)

   #тест площади, когда одна из сторон имеет отрицательную длину
    def test_negative_on_positive_mul(self):
       res = rectangle.area(10, -20)
       self.assertEqual(res, -200)

   #тест площади, когда обе стороны имеют отрицательную длину
    def test_negative_on_negative_mul(self):
       res = rectangle.area(-10, -20)
       self.assertEqual(res, 200)

   #тест площади, когда длина сторон это число с плавающей точкой
    def test_double_mul(self):
       res = rectangle.area(1.5, 1.5)
       self.assertEqual(res, 2.25)


    #тесты для периметра прямоугольника


    #тест периметра, когда одна из сторон имеет нулевую длину
    def test_zero_perimeter(self):
       res = rectangle.perimeter(10, 0)
       self.assertEqual(res, 20)
       
    #тест периметра, когда стороны прямоугольнка равны
    def test_square_perimeter(self):
       res = rectangle.perimeter(10, 10)
       self.assertEqual(res, 40)

    #тест периметра, когда одна из сторон имеет отрицательную длину
    def test_negative_on_positive_perimeter(self):
       res = rectangle.perimeter(10, -10)
       self.assertEqual(res, 0)

    #тест периметра, когда обе стороны имеют отрицательную длину
    def test_negative_on_negative_perimeter(self):
       res = rectangle.perimeter(-10, -10)
       self.assertEqual(res, -40)

    #тест периметра, когда длина сторон это число с плавающей точкой
    def test_float_perimeter(self):
       res = rectangle.perimeter(1.5, 1.5)
       self.assertEqual(res, 6)

class CircleTestCase(unittest.TestCase):
    
    #тесты для площади круга


    #тест площади, когда радиус имеет нулевую длину
    def test_zero_mul(self):
       res = circle.area(0)
       self.assertEqual(res, 0)
       
    #тест площади, когда длина радиусу положителена
    def test_square_mul(self):
       res = circle.area(10) / math.pi
       self.assertEqual(res, 100)

    #тест площади, когда длина радиусу отрицательна
    def test_negative_on_positive_mul(self):
       res = circle.area(-10) / math.pi
       self.assertEqual(res, 100)

   #тест площади, когда длина радиуса это число с плавающей точкой
    def test_double_mul(self):
       res = circle.area(1.5) / math.pi
       self.assertEqual(res, 2.25)


    #тесты для периметра круга


    #тест периметра, когда радиус имеет нулевую длину
    def test_zero_perimeter(self):
       res = circle.perimeter(0)
       self.assertEqual(res, 0)
       
    #тест периметра, когда длина радиусу положителена
    def test_square_perimeter(self):
       res = circle.perimeter(10) / math.pi
       self.assertEqual(res, 20)

    #тест периметра, когда длина радиусу отрицательна
    def test_negative_on_positive_perimeter(self):
       res = circle.perimeter(-10) / math.pi
       self.assertEqual(res, -20)

   #тест периметра, когда длина радиуса это число с плавающей точкой
    def test_double_perimeter(self):
       res = circle.perimeter(1.5) / math.pi
       self.assertEqual(res, 3)

class SquareTestCase(unittest.TestCase):
    
    #тесты для площади квадрата


    #тест площади, стороны имеют нулевую длину
    def test_zero_mul(self):
       res = square.area(0)
       self.assertEqual(res, 0)

   #тест площади, когда  стороны имеют отрицательную длину
    def test_negative_on_negative_mul(self):
       res = square.area(-10)
       self.assertEqual(res, 100)

   #тест площади, когда длина сторон это число с плавающей точкой
    def test_double_mul(self):
       res = square.area(1.5)
       self.assertEqual(res, 2.25)


    #тесты для периметра квадрата


    #тест периметра, когда стороны имеют нулевую длину
    def test_zero_perimeter(self):
       res = square.perimeter(0)
       self.assertEqual(res, 0)
       

     #тест периметра, когда  стороны имеют отрицательную длину
    def test_negative_on_negative_perimeter(self):
       res = square.perimeter(-10)
       self.assertEqual(res, -40)

    #тест периметра, когда длина сторон это число с плавающей точкой
    def test_float_perimeter(self):
       res = square.perimeter(1.5)
       self.assertEqual(res, 6)

class TriangleTestCase(unittest.TestCase):
    
    #тесты для площади треугольника


    #тест площади, когда высота проведенная к стороне, имеет нулевую длину
    def test_zero_mul(self):
       res = triangle.area(10, 0)
       self.assertEqual(res, 0)

   #тест площади, высота проведенная к стороне, имеет отрицательную длину
    def test_negative_on_positive_mul(self):
       res = triangle.area(10, -20)
       self.assertEqual(res, -100)

   #тест площади, когда сторона и высота проведенная к ней, имеют отрицательную длину
    def test_negative_on_negative_mul(self):
       res = triangle.area(-10, -20)
       self.assertEqual(res, 100)

   #тест площади, когда сторона и высота проведенная к ней, имеют длинной, число с плавающей точкой
    def test_double_mul(self):
       res = triangle.area(1.5, 1.5)
       self.assertEqual(res, 1.125)


    #тесты для периметра треугольника


    #тест периметра, когда одна из сторон имеет нулевую длину
    def test_zero_perimeter(self):
       res = triangle.perimeter(10, 0, 10)
       self.assertEqual(res, 20)
       
    #тест периметра, когда стороны треугольник равны
    def test_square_perimeter(self):
       res = triangle.perimeter(10, 10, 10)
       self.assertEqual(res, 30)

    #тест периметра, когда одна из сторон имеет отрицательную длину
    def test_negative_on_positive_perimeter(self):
       res = triangle.perimeter(10, -10, 10)
       self.assertEqual(res, 10)

    #тест периметра, когда все стороны имеют отрицательную длину
    def test_negative_on_negative_perimeter(self):
       res = triangle.perimeter(-10, -10, -10)
       self.assertEqual(res, -30)

    #тест периметра, когда длина сторон это число с плавающей точкой
    def test_float_perimeter(self):
       res = triangle.perimeter(1.5, 1.5, 1.5)
       self.assertEqual(res, 4.5)