pythonのウェブフレームワークであるflaskを用いてpython練習
使用言語　Python, flaks, jQuery, html, 
2021/8/04

IDE: PyCharm
まずrequirements.txt => installする

<仕様>

AさんがBさんに1ビットコインを送ることを想定する。

AさんのウォレットにBさんのブロックチェーンアドレスを貼りつける
sendボタンを押すと、Are you sure to send? と聞かれるので
okボタンを押す。

この段階でblockchain_server.pyで立ち上げた
'0.0.0.0:5000/transactions' を確認すると
length:1, 'transactions': [ 取引情報 ] とAさん、Bさんのアドレス
及び、送ったビットコイン数（今回は１ビットコイン）入っているのが
確認できる

'0.0.0.0:5000/chain' を確認すると、一番初めに作られたblock情報しか入っていない

理由はまだマイニングしていないからだ。
ブロックチェーンの取り引きの流れは
まず、transaction(取引情報　　たとえばAさんがBさんに１ビットコイン送る等)
が transaction_pool たまっていき、
そのたまった取引情報が正しいを判断されたら（その作業をマイニングと呼ぶ）
その塊（block)が連結されていく。
よってブロックチェーンとよぶ。

なので　'0.0.0.0:5000/mine' （＜＝　これはマイニングするurl)
と打ってやると、'0.0.0.0:5000/transactions' が空になっており、
'0.0.0.0:5000/chain' を確認すると、chain にblock情報が
格納されている。

おわり
