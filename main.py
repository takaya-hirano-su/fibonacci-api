import sys
sys.set_int_max_str_digits(10**9)

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import numpy as np


app=FastAPI()

def compute_fibonacci(n:int)->int:

    if 0<n and n<3:
        fib=1
    else:
        #フィボナッチ数列の漸化式を行列形式で解く
        fib_matrix=np.array(
            [[1,1],
             [1,0]],dtype=object)
        fib_init=np.array(
            [[1],
             [1]],dtype=object)
        fib=(np.linalg.matrix_power(fib_matrix,n-2)@fib_init)[0,0]

    return fib

@app.get("/fib")
def read_fibonacci(n:int):
    fib=compute_fibonacci(n)
    content=jsonable_encoder({"result":fib})
    return JSONResponse(content)

