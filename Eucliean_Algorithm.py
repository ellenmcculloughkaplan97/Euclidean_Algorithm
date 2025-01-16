# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:17:57 2025

@author: ellen
"""

def calculate_gcd_recursive(A,B):
    if A==0:
        return B
    elif B==0:
        return A
    else:
        # if A is smaller than B, swap values
        if A<B:
            A,B=B,A
        #divide A by B and R is the remainder: A=B*Q+R
        R=A%B
       #recursive call of function with B now in first place 
       #(B will now be numerator as opposed to denominator in A/B)
        return calculate_gcd_recursive(B, R)
       
  
# non-recursive method 
def calculate_gcd(A,B):
    if A==0:
        return B
    if B==0:
        return A
    
    #swap values if A is smaller than B
    if A<B:
        A,B=B,A
        
    while B!=0:
        R=A%B
        #replace values 
        A=B # B moves to first place
        B=R #remainder moves to second place
        
    return A #once a remainder of 0 is found, we have found the GCD which is A
        
        
    
       
    
