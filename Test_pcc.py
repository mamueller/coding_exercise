import numpy as np
import unittest 
from mod_names import func_mod_names, loop_mod_names, all_mod_names
import importlib


func_mods= [importlib.import_module(name) for name in func_mod_names]
loop_mods= [importlib.import_module(name) for name in loop_mod_names]
class Test_pcc(unittest.TestCase):
    #
    # We assume r_{X,Y} to be defined as the Pearson correlation coefficient
    # r_{X,Y} = \frac{cov(X,Y)}{sigma_X*sigma_Y}
    # as defined on a sample (where expactations are approximated by means)
    #
    # We test several implementations (unusually iterating over different modules) 
    # with the same fixtures.


    def test_my_mean(self):
        n=2
        X=np.array([i for i in range(1,n)])
        for mod in func_mods: 
            with self.subTest(mod=mod):
                self.assertEqual(
                    getattr(mod,'my_mean')(X)
                    ,n/2.0*(n-1)
                )
    
    def test_my_sample_cov(self):
        n=2
        X=np.array([i for i in range(n)])
        Y=np.array([i for i in range(n)])
        for mod in func_mods: 
            with self.subTest(mod=mod):
                self.assertEqual(
                    getattr(mod,'my_sample_cov')(X,Y)
                    ,1.0/n
                )
    
    def test_my_sample_var(self):
        n=2
        X=np.array([i for i in range(n)])
        for mod in func_mods: 
            with self.subTest(mod=mod):
                self.assertEqual(
                    getattr(mod,'my_sample_var')(X)
                    ,1.0/n
                )

    def test_my_sample_sig(self):
        n=2
        X=np.array([i for i in range(n)])
        for mod in func_mods: 
            with self.subTest(mod=mod):
                self.assertEqual(
                    getattr(mod,'my_sample_sig')(X)
                    ,np.sqrt(1.0/n)
                )

    def test_correlationCoefficient(self):
        # check corner cases of 1 and -1
        mods=func_mods+loop_mods
        for mod in func_mods: 
            with self.subTest(mod=mod):
                n=4
                X=np.array([i for i in range(n)])
                Y=np.array([i for i in range(n)])
                fun=getattr(mod,"correlationCoefficient")
                self.assertEqual( fun(X,Y) ,1)

                Y=np.array([1+3*v for v in range(n)])
                self.assertEqual(fun(X,Y),1)
        
                Y=np.array([-3*v for v in range(n)])
                self.assertEqual(fun(X,Y),-1)

unittest.main()
