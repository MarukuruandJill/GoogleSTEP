# homework1:  hash_table.py
### 実装した関数
- delete  
- calculate_hash_with_prime_number
- calculate_hash_with_middle_4_digits
- rehash

### delete関数について
- bucketsにkeyに対応するitemがあるとき: itemを削除し、item_countを1減らしてTrueを返す
- bucketsにkeyに対応するitemがないとき: 何もせずFalseを返す
- item_countの数がbucket_sizeの3割未満になったら、再ハッシュする

### calculate_hash_with_prime_number について
- 素数のリストprime_numbers = [2, 3, 5, 7, .....]を用意する
- keyの、最初からindex番目の文字iについて、ord(i)*prime_numbers[index]したものを足していく

### calculate_hash_with_middle_4_digits について
- keyに含まれるそれぞれの文字iについて、ord(i)を求め、全て掛け算する
- 全て掛け算したものを2乗する
- 出てきた数字の中央4桁を取り出す

### rehash について
- 要素数がテーブルサイズの 70%を上回ったら、テーブルサイズを 2倍 + 1 に拡張 
- 要素数がテーブルサイズの 30%を下回ったら、テーブルサイズを 1/2 + 1 に縮小
- +1しているのはテーブルサイズを奇数にするため


# homework4: cache.py
### 実装したもの
- urlを要素とするNode
- Nodeを要素とした、先頭と最後尾のノードへのポインタを持つ双方向連結リスト
- access_page関数
- get_pages関数

### access_page関数
- アクセスしたいURLが双方向連結リストに格納されているか確認
- もしあったら、そのURLが格納されたノードを先頭に移動させ、Webページにアクセスする
- もしなかったら、ハッシュテーブルに<URL, Webページ>を追加し、cache_sizeを1増やす
    - もしcache_sizeがmax_cache_sizeを超えていたら、双方向連結リストの最後尾のノードと、このノードに格納されたURLに対応するハッシュテーブルの要素を削除する

### get_pages関数
- 双方向連結リストの先頭の要素から辿っていき、格納されたURLをリストurlsに順番に格納する