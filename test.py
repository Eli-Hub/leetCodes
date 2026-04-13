import math
from typing import List

def constructRectangle(area: int) -> List[int]:
    w = int(area ** 0.5)
    while area % w != 0:
        w -= 1
    return [area // w, w]

        

    
    
    
    
a = 41
print(constructRectangle(a))
