# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:17:57 2025

@author: ellen
"""

def calculate_gcd(A,B):
    if A==0:
        return B
    elif B==0:
        return A
    else:
        #divide A by B and R is the remainder: A=B*Q+R
       R=A%B
       #recursive call of function with B now in first place 
       #(B will now be numerator as opposed to denominator in A/B)
       return calculate_gcd(B, R)
       
       
       
    
