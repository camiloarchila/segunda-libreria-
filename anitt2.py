"""
Created on Sat Aug 22 17:19:37 2020

@author: Camilo
"""
import unittest
import libreria_2
#import math


class unit_calculadora(unittest.TestCase):

    def test_adicion_vec(self):
        self.assertEqual(libreria_2.adicion_vec([-6, 10], [15, -5]), [9, 5])

    def test_inverso_aditivo(self):
        self.assertEqual(libreria_2.inverso_aditivo([-6, 10]), [6,-10])

    def test_mult_esc_vec(self):
        self.assertEqual(libreria_2.mult_esc_vec(10, [15, -5]), [150, -50])

    def test_adicion_matriz(self):
        self.assertEqual(libreria_2.adicion_matriz([[-6, 10], [15, -5]],[[1,2],[3,4]]), [[-5,12],[18,-1]])

    def test_inversa_adi_matriz(self):
        self.assertEqual(libreria_2.inversa_adi_matriz([[-3, 4],[1,2]]), [[3,-4],[-1,-2]])
        
    def test_mult_esc_matrizcomp(self):
        self.assertEqual(libreria_2.mult_esc_matrizcomp(3,[[2j,1+1j],[1-1j,2j]]), [[6j,(3+3j)],[(3-3j),6j]])

    def test_transpuesta(self):
        self.assertEqual(libreria_2.transpuesta([[1,2,3],[4,5,6]]), [[1,4],[2,5],[3,6]])

    def test_conjugada(self):
        self.assertEqual(libreria_2.conjugada([[2j,1+1j],[1-1j,2j]]), [[-2j, (1-1j)], [(1+1j), -2j]])
        
    def test_adjunta(self):
        self.assertEqual(libreria_2.adjunta([[2j,1+1j],[1-1j,2j]]), [[-2j, (1+1j)], [(1-1j), -2j]])
        
    def test_producto_matrices(self):
        self.assertEqual(libreria_2.producto_metrices([[1,2,3],[4,5,6]],[[1,2],[3,4],[5,6]]), [[22,28],[49,64]])
    
    def test_accion_mat_vec(self):
        self.assertEqual(libreria_2.accion_mat_vec([[1,2,3]],[[1,2],[4,5],[7,8]]), [[30,36]])
    
    def test_producto_inter_vect(self):
        self.assertEqual(libreria_2.producto_inter_vect([1,2,3],[4,5,6]), 32)
    
    def test_norma_vect(self):
        self.assertEqual(libreria_2.norma_vect([3,-6,2]), 7.0)
    
    def test_distancia_vect(self):
        self.assertEqual(libreria_2.distancia_vect([3,1,2],[2,2,-1]), 3.3166247903554)
    
    def test_mat_unitaria(self):
        self.assertEqual(libreria_2.adjunta(),)
    
    def test_mat_hermitiana(self):
        self.assertEqual(libreria_2.adjunta([[7,6+5j],[6-5j,-3]]), 'es hermitiana')
    
    def test_producto_tensor(self):
        self.assertEqual(libreria_2.adjunta([[1,2],[3,4]],[[5,6],[7,8]]), [[[5, 6, 7, 8], [10, 12, 14, 16]], [[15, 18, 21, 24], [20, 24, 28, 32]]])
   
unittest.main()