# Homework1: find_shortest_path() 関数の実装
## 実装した関数、クラス
- ReversedLinkedList class
- find_shortest_path(self, start, goal)
- find_page_id(self, target_title)
- print_path(self, trace_list: ReversedLinkedList)

### ReversedLinkedList class
- 今通ったページと、その一つ前に通ったページの情報をもつ
- 経路が見つかった時に後ろから辿れるようにするために用意

### find_shortest_path(self, start, goal)について
- find_page_id(self, target_title)でページのタイトルに対応するidを見つけ、BFSで最短経路を探索
- 探索の過程で通ったページのidを連結リストに入れておく
- print_path(self, trace_list: ReversedLinkedList)で経路を出力

### find_page_id(self, target_title)
- ページのタイトルに対応するページのidを返す

### print_path(self, trace_list: ReversedLinkedList)
- ReversedLinkedListに入っているidを順番に取り出し、配列に入れる
- 配列の後ろから順にidを取り出し、対応するページタイトルを出力していく


# HomeWork2: find_most_popular_pages() 関数の実装
## 実装した関数
- find_most_popular_pages(self)
- init_page_rank(self)
- update_page_rank(self, page_ranks)
- random_surfer_model(self, page_ranks, old_page_ranks, distributions) 上手くいった
- old_random_surfer_model(self, page_ranks, old_page_ranks, distributions) 遅すぎた
- check_converged(self,page_ranks, old_page_ranks)
- find_top_10_pages(self, page_ranks)
- print_page_rank_sum(self, page_ranks) デバッグ用

### find_most_popular_pages(self)
1. 収束したかどうかを表すフラグisConvergedを初期値Falseにする
2. page_rankをinit_page_rank(self)で初期化して、全ノートにページランク1.0を割り当てる
3. isConvergedがFalseである間、ステップ4, 5を繰り返す
4. update_page_rank(self, page_ranks)で、random surfer modelを用いてpage_rankを更新する
5. check_converged(self,page_ranks, old_page_ranks)を用いて、収束したらisConvergedをTrueにする
6. 収束したら、find_top_10_pages(self, page_ranks)を用いて上位10ページを表示する

### init_page_rank(self)
- ページidをキー、ページランクを値とする辞書page_rankを用意し、値を全て1.0で初期化する

### update_page_rank(self, page_ranks)
1. 現在のpage_rankをold_page_rankにコピー(深いコピー)する
2. 分配されるページランクを保存しておくための辞書distributionsを用意し、値を全て0.0で初期化する
3. random_surfer_model(self, page_ranks, old_page_ranks, distributions)を用いて、distributionsを計算し、これを新たなpage_rankとする
4. check_converged(self,page_ranks, old_page_ranks)のため、old_page_rankとpage_rankを返す

### random_surfer_model(self, page_ranks, old_page_ranks, distributions)
1. page_rankの大きさNと、page_rankのkeyの配列keysを用意する
2. まず全体に分配する分をいっぺんに計算する
3. 隣接するページがないページのページランクを合計し、0.85倍してNで割る
4. 全てのページについてページランクを合計し、0.15倍してNで割る
5. 全てのページに3,4で計算した分配を足す(distributionsに入れていく)
6. 隣接するページがあるページに対して、自身のページランクの85%を隣接するページに均等に分配する
7. distributionsを返す

### old_random_surfer_model(self, page_ranks, old_page_ranks, distributions)
- page_rankの全てのページについて、一つずつみていく
- 隣接するページがなければページランクを全てのノードに分配する
- 隣接するページがあれば、ページランクの85%を隣接するページへ、15%を全ページに分配する
- 時間がかかりすぎる

### check_converged(self,page_ranks, old_page_ranks)
- page_rankが収束した確認する
- old_page_ranksとpage_ranksの差の2乗の和が0.01未満になったらisConvergedフラグをTrueにする

### find_top_10_pages(self, page_ranks)
- ページランクのキーと値のタプルのリストranksを用意する
- ranksを値の大きい順にソートする
- ranksの最初から10個を表示

### print_page_rank_sum(self, page_ranks)
- ページランクの合計値を出力する
- デバッグ時に、ページランクの分配が正しく行われているか確認するため

# Homework3: find_longest_path(self, start, goal)の実装
- 考え中です
- 最短経路からどんどん寄り道していくイメージで考えてますが、上手くいってません