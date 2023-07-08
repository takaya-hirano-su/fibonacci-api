import sys
sys.set_int_max_str_digits(10**9)

from fastapi import FastAPI
import numpy as np
import json

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
    return json.dumps({"result":compute_fibonacci(n)})


# if __name__=="__main__":
#     import uvicorn
#     uvicorn.run("main:app --host 127.0.0.1 --port 8000")