# 課題1

## API構成
APIの構成は以下とした。
<!-- ![Alt text](structure.png) -->
<center>
<img src=".figs/structure.png" width=400>
</center>

### 選定理由

- python
    - 最も使い慣れた言語であり、素早くAPIを作成できると考えたため。
- Fast API
    - シンプルかつ、軽量なpythonフレームワークであり、本課題のAPIに向いていると考えたため。
- Gunicorn
    - Fast APIの起動に推奨されているため。
- Nginx
    - Gunicornの前にWebサーバーとして利用することを推奨されているため。
    - 本APIは動画や音声などの動的コンテンツはないため、Appachよりも同時接続処理が優位なNginxとした。
- AWS
    - 無料利用枠があるため。
    - シェア率が高く、ドキュメントが豊富なため。

## API概要
${n}$番目のフィボナッチ数を返すAPI。$n$番目のフィボナッチ数を$F_n$とすると、$F_n$は以下のように求められる。  
<center>

$F_n=F_{n-1}+F_{n-2}$

</center>

### 仕様
#### エンドポイント
~~~
GET http://fibonacci-api.code-labo.net/fib
~~~

#### リクエストパラメータ
~~~
n：計算するフィボナッチ数の位置を指定する自然数
   nは1以上80001以下とする
~~~

#### 使用例
##### リクエスト
~~~bash
CURL -X GET -H "Content-Type: application/json" "http://fibonacci-api.code-labo.net/fib?n=99"
~~~

##### レスポンス
~~~bash
HTTP/1.1 200 OK
{
    result:218922995834555169026
}
~~~

##### リクエスト
~~~bash
CURL -X GET -H "Content-Type: application/json" "http://fibonacci-api.code-labo.net/fib?n=abc"
~~~

##### レスポンス
~~~bash
HTTP/1.1 400 BAD REQUEST
{
    detail:"'n' is not a natural number. 
            'n' must be a natural number that is greater than 0 and less than 800001."
}
~~~

## ソースコード構成
ソースコードは以下の表の関数から構成される。
<center>

|関数名|処理内容|
:---:|:---:
read_fibonacci|httpリクエストを受け、フィボナッチ数をレスポンスとして返す
compute_fibonacci|n番目のフィボナッチ数を計算する

</center>


## ソースコード概要
### read_fibonacci(n:str)  
httpリクエストを受けて、レスポンスを返す。
リクエストパラメータ$n$によって以下のレスポンスを行う。  
<center>

|n|レスポンス|
:---:|:---:
1未満の数|BAD REQUEST 400
文字列|BAD REQUEST 400
1以上800000以下の自然数|OK 200<br>compute_fibonacciを実行し、<br>n番目のフィボナッチ数を返す
800001以上の数|BAD REQUEST 400

</center>

nの最大値を800000とした理由は、800000以上の値を入力すると、レスポンスを返すまでに1秒以上かかってしまうため。

### compute_fibonacci(n:int)
n番目のフィボナッチ数を計算する関数。  
フィボナッチ数の計算は、行列の累乗によって計算を行った。  
行列の計算を繰り返し2乗法で行うことで計算量が$O(logN)$となる。  
また、整数値のみを扱うことで誤差も生じないため、この手法を選択した。  
他の手法の特徴を以下の表に示す。  
<center>

|他の手法|特徴|
:---:|:---:
再帰的な漸化式の計算|計算量が$O(2^n)$となり、大きい数の計算時間が非現実的
一般項による計算|$√5$が一般項に含まれるため、$n$が71以上で誤差が発生する
$n=1$から動的計画法的な計算|計算量が$O(N)$となるが、$O(logN)$よりは時間が掛かる

</center>