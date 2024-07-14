#%% 실수의 오류
print(0.1+0.2)  #0.30000000000000004
print(0.1+0.2==0.3) #false
# 어떻게 막을까?
print("%f" %0.3)    #0.300000 6번째까지만 정확하다.

#%% 실수의 오류 해결 1
import math
print(math.isclose(0.1+0.2,0.3)) #아무리 정확한 값이 안나와도 근사값으로 비교해줌.
#%% 실수의 오류 해결 2
from decimal import Decimal
print(float(Decimal('0.1')+Decimal('0.2')))