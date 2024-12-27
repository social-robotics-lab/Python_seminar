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
進め方としては、初回で各自githubに上がっている資料をダウンロードしてもらって、各回の演習ファイルをどこかに出してもらおうかなという感じで考えてます。（仮）  
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
   1. Chocolateyのインストール
      1. [こちら](https://chocolatey.org/install)のサイトにアクセス
      2. Individual（個人）を選択
      3. 「2.Install with powershell.exe」内にある「Now run the following command:」の下に書いてあるコマンドをコピー
      4. PowerShellを開いて、右クリックし「管理者として実行」を選択
      5. コピーしたコマンドを貼り付けてエンターキーを押す
         * ログ中に `Chocolatey (choco.exe) is now ready.` と出ていればインストール完了
      6. `choco -v`コマンドを実行し、バージョンが表示されればOK
   2. pyenvのインストール
      1. PowerShellに以下のコマンドを入力

         ```powershell
         choco install pyenv-win
         ```

      2. バージョンの確認
         PowerShellに以下のコマンドを入力

         ```powershell
         pyenv --version
         ```

   3. pythonのインストール
      terminalで以下のコマンドを入力

      ```powershell
      pyenv install 3.12.2
      ```

   4. 使用するpythonのversionを指定
      terminalで以下のコマンドを入力

      ```powershell
      pyenv versions
      ```

      ここで、3.12.2が確認されたら、次に下のコマンドを入力

      ```powershell
      pyenv global 3.12.2
      pyenv local 3.12.2
      ```

   5. pythonのversionを確認
      terminalで以下のコマンドを入力

      ```powershell
      python --version
      ```

      ちゃんとインストールしたバージョンが出てきたら成功です！

#### Mac

1. Mac App Store から Xcode をインストール
   * Xcodeはインストールに20～30分かかる。ひたすら待つ

2. Homebrewのインストール
   * terminal.app を起動
   * 以下のコマンドを入力

    ``` zsh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

3. Pythonのインストール
   1. pyenvのインストール  
      terminalで以下のコマンドを入力

      ``` zsh
      brew install pyenv
      ```

   2. 使用しているShellの確認  
      terminalで以下のコマンドを入力

      ``` zsh
      echo $SHELL
      ```

      スラッシュの最後が`zsh`か`bash`か覚えといてください

   3. 環境変数の設定
      terminalで以下のコマンドをコピー&ペースト
      * `zsh`の人の場合

         ```zsh
         echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
         echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
         echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
         echo 'eval "$(pyenv init -)"' >> ~/.zshrc
         cat ~/.zshrc
         ```

      * `bash`の人の場合

         ```zsh
         echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
         echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
         echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile
         echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
         cat ~/.bash_profile
         ```

      最後に`echo`の中身が出力されているか確認してください。

   4. pythonのインストール
      terminalで以下のコマンドを入力

      ```zsh
      pyenv install 3.12.2
      ```

   5. 使用するpythonのversionを指定
      terminalで以下のコマンドを入力

      ```zsh
      pyenv versions
      ```

      ここで、3.12.2が確認されたら、次に下のコマンドを入力

      ```zsh
      pyenv global 3.12.2
      pyenv local 3.12.2
      ```

   6. pythonのversionを確認
      terminalで以下のコマンドを入力

      ```zsh
      python --version
      ```

      ちゃんとインストールしたバージョンが出てきたら成功です！

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
