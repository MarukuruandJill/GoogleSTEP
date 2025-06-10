# homework1: 「*」、「/」に対応しよう
## 実装した関数
- read_multiply function
- read_divide function
- evaluate_multiply_and_divide function
- evaluate_plus_and_minus function
- evaluate function

### read_multiply functionについて
- '*' を読み込んだら、token = {'type': 'MULTIPLY'}としてtokensに加える
- tokensとindex+1を返す

### read_divide functionについて
- '/' を読みこんだら、 token = {'type': 'DIVIDE'}としてtokensに加える
- tokensとindex+1を返す

### evaluate_multiply_and_divide functionについて
- 掛け算と割り算を先に計算するための関数
- 計算したら、計算した箇所に計算結果を置き換える
- 連続した掛け算、割り算に対応(ex. 5*4/2)
- tokensに含まれる全ての掛け算、割り算を計算し、数字と足し算、引き算だけが残ったtokensを返す

### evaluate_plus_and_minus functionについて
- 足し算と引き算だけを行う
- evaluate_multiply_and_divide functionに通した後のtokensに対して処理を行う
- 最終的な式の答えを返す

### evaluate functionについて
- まずevaluate_multiply_and_divide functionを呼び出し、tokensを数字と足し算、引き算だけにしたものをtmp_tokensに代入する
- tmp_tokensを引数としてevaluate_plus_and_minus functionを呼び出し、最終結果answerを算出する
- answerを返す


# homework2: テストケースを追加しよう
## 追加したテストケース
- 2-1
- 2.3*5.4
- 2/4
- 3.0+4*2-1/5
- 4/2/2+5+6*3/2
- 3+6/3*2-4
- 5.6*3.2*5+46-67+56/4/4


# homework3: 括弧に対応しよう
## 実装した関数
- read_opening_parentheses function
- read_closing_parentheses function
- evaluate_parentheses function
- evaluate function

### read_opening_parentheses functionについて
- '(' を読み込んだら、token = {'type': 'OPENING_PARENTHESES'}としてtokensに加える
- tokensとindex+1を返す

### read_closing_parentheses functionについて
- ')' を読み込んだら、token = {'type': 'CLOSING_PARENTHESES'}としてtokensに加える
- tokensとindex+1を返す

### evaluate_parentheses functionについて
- ()内の式を先に計算するための関数
  
1. index = 0とし、tokensを左から順に見ていく
2. 'OPENING_PARENTHESES'が見つかったら、その位置をstart_indexesに追加する
3. 'CLOSING_PARENTHESES' または次の 'OPENING_PARENTHESES' が出てくるまで、tokenをinside_parentheses に追加する
4. 'CLOSING_PARENTHESES'が見つかったら、inside_parenthesesの内容をevaluate functionで計算し、その部分を'NUMBER'型で値をinside_parenthesesの計算結果とするtokenで置き換える。
5. 'OPENING_PARENTHESES'が見つかったら、inside_parentheses = []にして、3に戻る
6. 全ての()について計算したら、tokensを返す

### evaluate functionについて
- homework2で作ったevaluate functionの最初に、evaluate_parentheses functionを追加するだけ


# homework4: abs(), int(), round()に対応しよう
## 実装した関数
- read_abs function
- read_int function
- read_round function
- evaluate_abs_int_round function
- evaluate function

### read_abs functionについて
- 'abs' を読み込んだら、token = {'type': 'ABS'}としてtokensに加える
- tokensとindex+3を返す

### read_int functionについて
- 'int' を読み込んだら、token = {'type': 'INT'}としてtokensに加える
- tokensとindex+3を返す

### read_round functionについて
- 'round' を読み込んだら、token = {'type': 'ROUND'}としてtokensに加える
- tokensとindex+5を返す

### evaluate_abs_int_round functionについて
- abs(),int(),round()の中身を計算する関数
- ()の部分はevaluate_parentheses functionで計算されたものとする
  
1. tokensを左から順に見ていく、
2. 'ABS', 'INT', 'ROUND'があったら、その隣のtoken('NUMBER'型になっているはず)のnumberについてabs, int, 又はroundした値を計算し、resultに格納
3. 計算した部分を'NUMBER'型で値をresultとするtokenで置き換える
4. tokensを返す

### evaluate function
- homework3 で追加したevaluate_parentheses functionの次にevaluate_abs_int_round functionを追加する