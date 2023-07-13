import requests
import pytest

from main import compute_fibonacci

#fibonacci計算のテスト
@pytest.mark.parametrize(
        ("n","expected_fib"),
        [
         (0,None),
         (1,1),
         (2,1),
         (3,2),
         (99,218922995834555169026),
         ]
)
def test_compute_fibonacci(n,expected_fib):
    fib=compute_fibonacci(n)
    assert fib==expected_fib


#httpレスポンスのテスト
@pytest.mark.parametrize(
        ("n","expected_status_code"),
        [
         (-1,400),
         (0,400),
         (800000,200),
         (800001,400),
         ("1aaaa",400),
         (" ",400),
         ]
)
def test_read_fibonacci(n,expected_status_code):
    response=requests.get(f"http://fibonacci-api.code-labo.net/fib?n={n}")
    assert response.status_code==expected_status_code


