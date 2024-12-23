# Python勉強会

## Python勉強会について

### 概要

この勉強会はPython初学者向けのものです。
3年生からジョイントリサーチが始まりますが、いきなりPythonでロボットを開発しろと言われても難しいと思うので、この勉強会である程度Pythonに慣れてもらってから進級してもらえると嬉しい限りです。

### 使用ツール

* VSCode
* Python
* Git

### カリキュラム

この勉強会のカリキュラムはこんな感じで考えてます。
進め方としては、初回で各自githubに上がっている資料をcloneしてもらって、自分でしたものを勉強会ごとに各自のbranchにpushしてもらう感じで考えてます。（仮）
2月の内容はみなさんと相談しながら決めようかな。

|    | 日程 | 内容 |
|----| ---- | ---- |
|第1回| 1/ | Python (繰り返しまで) |
|第2回| 1/ | Python (関数・クラス) |
|第3回| 1/ | Python　(復習) |
|第4回| 1/ | Git・コマンドラインの使い方 |
|第5回| 2/ | TBD |
|第6回| 2/ | TBD |
|第7回| 2/ | TBD |
|第8回| 2/ | TBD |

### 準備物

準備するものやその方法を書いてます。

#### Windows

1. wgetのインストール(Windows 10の人のみ)
   * Microsoft Storeのアプリインストーラーにアクセス
   * `インストール`ボタンを押し、画面の指示に従ってインストール
2. VSCodeのインストール
   * コマンドプロンプトを開く
   * コマンドプロンプトに以下を入力

    ``` bash
    winget install Microsoft.VisualStudioCode
    ```

3. Pythonのインストール
   * コマンドプロンプトに以下を入力

    ``` bash
    winget install python.python.3.12
    ```

#### Mac

1. Mac App Store から Xcode をインストール
   * Xcodeはインストールに20～30分かかる。ひたすら待つ
2. brewのインストール
   * terminal.app を起動
   * 以下のコマンドを入力

    ``` zsh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

3. Pythonのインストール
   * terminalで以下のコマンドを入力

    ``` zsh
    brew install python@3.12
    ```

4. VSCodeのインストール
    * [こちら](https://code.visualstudio.com/docs?dv=osx)をクリックして、VSCodeのzipファイルをインストール
    * 解凍してアプリケーションに移す

<!-- #### 両方

1. githubのアカウント登録
   * [こちら](https://github.co.jp/)にアクセスしてサインアップする
2. 登録したメールアドレスを勉強会のグループチャットに送る
3. VSCodeにてcodeコマンドをインポート
   1. コントロール＋シフト＋p（Macはコマンド＋シフト＋p）を押す
        * 上にテキストボックスが出てきます
   2. そこに`shell`と打ち込むと、`Shell Command: Install 'code' command in PATH`が出てくるのでそれを選択
   3. パスワードを要求されたら打ち込む
   4. `successfully imported`的な文章が出てきたらOK -->
