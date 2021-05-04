from libHBCurveCalculator import *
import matplotlib.pyplot as plt
import unittest

class TestCalculator(unittest.TestCase):
    # Testing loading and printing data
    def test_Carpenter49(self):
        H_col, B_col = getData('carpenter_49.txt')
        print()
        [print(index, H_value, B_value) for index, (H_value, B_value)
         in enumerate(zip(H_col, B_col))]

    def test_IronMalleable(self):
        H_col, B_col = getData('iron_malleable.txt')
        print()
        [print(index, H_value, B_value) for index, (H_value, B_value)
         in enumerate(zip(H_col, B_col))]

    # Testing indexes of near values
    def test_IndexCarpenter49AgreesAtBeginning(self):
        H_col, B_col = getData('carpenter_49.txt')
        indexes = nearValues(0, H_col)
        self.assertEqual(indexes, [0,1,2,3])

    def test_IndexCarpenter49AgreesAtMiddle(self):
        H_col, B_col = getData('carpenter_49.txt')
        indexes = nearValues(12.631, H_col)
        self.assertEqual(indexes, [30,31,32,33])

    def test_IndexCarpenter49AgreesAtTop(self):
        H_col, B_col = getData('carpenter_49.txt')
        indexes = nearValues(988.82, H_col)
        self.assertEqual(indexes, [65,66,67,68])

    def test_IndexIronMalleableAgreesAtBeginning(self):
        H_col, B_col = getData('iron_malleable.txt')
        indexes = nearValues(4, H_col)
        self.assertEqual(indexes, [0,1,2,3])
        
    # Testing interpolation agrees with app
    def test_InterpolCarpenter49AgreesAtBeginning(self):
        H_col, B_col = getData('carpenter_49.txt')
        
        x = 4
        y = calcB(x, H_col, B_col)
        
        self.assertAlmostEqual(round(y,3), 0.306)

    def test_InterpolIronMalleableAgreesAtBeginning(self):
        H_col, B_col = getData('iron_malleable.txt')
        
        x = 4
        y = calcB(x, H_col, B_col)
        
        self.assertAlmostEqual(round(y,3), -0.031)

    def test_InterpolIronMalleableAgreesAtMiddle(self):
        H_col, B_col = getData('iron_malleable.txt')
        
        x = 14
        y = calcB(x, H_col, B_col)
        
        self.assertAlmostEqual(round(y,3), 0.315)

    def test_InterpolIronMalleableAgreesAtMiddle(self):
        H_col, B_col = getData('iron_malleable.txt')
        
        x = 2000
        y = calcB(x, H_col, B_col)
        
        self.assertAlmostEqual(round(y,3), 1.663)
'''
x_values = np.arange(0,18,1)
y_values = np.multiply(x_values, x_values)
y2_values = calcH(x_values, x_values, y_values)

plt.plot(x_values, y_values)
plt.plot(x_values, y2_values)
    
plt.show()
'''

    
'''
x = np.array([-5, -1, 0, 2, 6, 13])
y = np.array([-2, 6, 1, 3, 9, 3])
# get the divided difference coef
a_s = divided_diff(x, y)[0, :]

# evaluate on new data points
x_new = np.arange(-5, 15, .1)
y_new = newton_poly(a_s, x, x_new)

plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo')
plt.plot(x_new, y_new)
plt.show()
'''
