# python 2.7.3
import sys
import math

def init():
    results = [0]
    results.append(1)
    results.append(1)
    results.append(2) 
    # 1, 2, 3$
    # 1, 3, 2$
    abd = 1    
    abp = 0
    apbd = 0
    apbp = 0
    bad = 1
    bap = 0
    bpad = 0
    bpap = 0    
    # ab$  -> atb$, abt$  
    # ab.+  -> atb.+
    # a.+b$  -> a.+bt$
    # a.+b.+  -> FAIL
    # ba$  -> bta$, bat$
    # ba.+  -> bta.+
    # b.+a$  -> b.+at$
    # b.+a.+  -> FAIL
    
    for i in range(60):        
        abd_new = 0   
        abp_new = 0
        apbd_new = 0
        apbp_new = 0
        bad_new = 0
        bap_new = 0
        bpad_new = 0
        bpap_new = 0
        # (1)
        bap_new += abd # 1, 3, 4, 2$
        bpad_new += abd 

        # (2)
        bap_new += abp

        # (3)
        bpad_new += apbd

        # (5)
        abd_new += bad # 1, 2, 4, 3$
        bad_new += bad # 1, 2, 3, 4$

        # (6)
        abp_new += bap

        # (7)
        bad_new += bpad
        
        abd, abp, apbd, apbp = abd_new, abp_new, apbd_new, apbp_new
        bad, bap, bpad, bpap = bad_new, bap_new, bpad_new, bpap_new
        temp = sum([abd_new, abp_new, apbd_new, apbp_new])
        temp += sum([bad_new, bap_new, bpad_new, bpap_new])
        
        results.append(temp)
    return results

results = init()
n = input()
print results[n]

    
