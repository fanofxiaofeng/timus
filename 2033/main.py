# python 2.7.3
import sys
import math

m_cnt = {}
m_price = {}

for i in range(6):
    name = raw_input()
    device = raw_input()
    price = input()
    if device in m_cnt:
        m_cnt[device] += 1
        if price < m_price[device]:
            m_price[device] = price
    else:
        m_cnt[device] = 1
        m_price[device] = price

opt_device, opt_cnt = m_cnt.popitem()
opt_price = m_price[opt_device]
while m_cnt:
    temp_device, temp_cnt = m_cnt.popitem()
    temp_price = m_price[temp_device]
    if temp_cnt > opt_cnt or (temp_cnt == opt_cnt and temp_price < opt_price):
        opt_device = temp_device
        opt_price = temp_price
        opt_cnt = temp_cnt
print opt_device
    
    


    
