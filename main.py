import sys
sys.set_int_max_str_digits(10**9)

from fastapi import FastAPI,HTTPException,status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import numpy as np


app=FastAPI()

def compute_fibonacci(n:int)->int:

    if n<=0:
        fib=None
    elif 0<n and n<3:
        fib=1
    else:
        #フィボナッチ数列の漸化式を行列形式で解く
        fib_matrix=np.array(
            [[1,1],
             [1,0]],dtype=object)
        fib_init=np.array(
            [[1],
             [1]],dtype=object)
        fib=(np.linalg.matrix_power(fib_matrix,n-2)@fib_init)[0,0] #繰り返し2乗法で実装されているので,O(logN)

    return fib


@app.get("/fib")
def read_fibonacci(n:str):

    if not n.isdigit() or int(n)==0:
        #nが自然数でなかったとき
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="'n' is not a natural number. 'n' must be a natural number that is greater than 0 and less than 800001."
        )

    elif int(n)>800000:
        #nが大きすぎるとき
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="'n' is too large. 'n' must be a natural number that is greater than 0 and less than 800001."
        )
    
    else:
        fib=compute_fibonacci(int(n))
        content=jsonable_encoder({"result":fib})

    return JSONResponse(content)

