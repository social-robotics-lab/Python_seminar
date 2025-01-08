# Python勉強会について

## 概要

この勉強会はPython初学者向けのものです。
3年生からジョイントリサーチが始まりますが、いきなりPythonでロボットを開発しろと言われても難しいと思うので、この勉強会である程度Pythonに慣れてもらってから進級してもらえると嬉しい限りです。

## 使用ツール

* VSCode
* Python (3.12.2)
* Git + GitHub

## カリキュラム

この勉強会のカリキュラムはこんな感じで考えてます。  
進め方としては、初回で各自GitHubに上がっている資料をダウンロードしてもらって、各回の演習ファイルをどこかに出してもらおうかなという感じで考えてます。（仮）  
2月の内容はみなさんと相談しながら決めようかな。

|    | 日程 | 内容 |
| ---- | ---- | ---- |
| 第1回 | 1/9 21時〜 | Python (繰り返しまで) |
| 第2回 | 1/ | Python (関数・クラス) |
| 第3回 | 1/ | Python (復習) |
| 第4回 | 1/ | Git・コマンドラインの使い方 |
| 第5回 | 2/ | TBD |
| 第6回 | 2/ | TBD |
| 第7回 | 2/ | TBD |
| 第8回 | 2/ | TBD |

## 準備物

準備するものやその方法を書いてます。

### Windows

#### 0. WinGetのインストール (Windows 10の人のみ)

1. Microsoft Storeで「アプリインストーラー」と検索
2. `インストール` ボタンを押し、画面の指示に従ってインストール

#### 1. WinGetの確認

1. 管理者として「ターミナル」アプリを開く

    ①「スタート」ボタンを右クリック  
    ②「ターミナル (管理者)」をクリック

    ![管理者としてターミナルを開く方法](img/スクリーンショット%202025-01-06%20182530.png)

2. 「このアプリがデバイスに変更を加えることを許可しますか？」というメッセージが表示された場合は「はい」を選択
3. 開かれたターミナルのウィンドウで `winget -v` と入力し、Enterキーを押して実行
4. `v1.2.10691` のように表示されればOK

#### 2. VSCodeのインストール

1. ターミナルに以下を入力して実行

    ```powershell
    winget install Microsoft.VisualStudioCode
    ```

2. 契約条件への同意

    ```plaintext
    すべてのソース契約条件に同意しますか？
    [Y] はい  [N] いいえ:
    ```

    と表示されたら `y` と入力し、Enter

    `インストールが完了しました` と表示されればOK

#### 3. Pythonのインストール

1. Chocolateyのインストール
    1. [こちら](https://chocolatey.org/install#individual)のサイトにアクセス
        * メールアドレスは登録しなくても構いません
    2. 「2. Install with powershell.exe」内にある「Now run the following command:」の下に書いてあるコマンドをコピー

        例：

        ```powershell
        Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
        ```

    3. 先ほどコピーしたコマンドをターミナルに貼り付けてEnter
        * 以下のように表示されればインストール完了

            ```plaintext
            Chocolatey (choco.exe) is now ready.
            You can call choco from anywhere, command line or powershell by typing choco.
            Run choco /? for a list of functions.
            You may need to shut down and restart powershell and/or consoles
            first prior to using choco.
            Ensuring chocolatey commands are on the path
            Ensuring chocolatey.nupkg is in the lib folder
            ```

    4. `choco -v` コマンドを実行し、`2.4.1` のようにバージョンが表示されればOK

2. pyenvのインストール
    1. ターミナルで以下のコマンドを実行

        ```powershell
        choco install pyenv-win
        ```

        以下のようなメッセージが表示されたら `y` と入力し、Enter

        ```plaintext
        Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint):
        ```

        次のように表示されればOK

        ```plaintext
        The install of pyenv-win was successful.
            Deployed to 'C:\Users\ユーザー名\.pyenv\'
        ```

    2. 「設定」アプリを開き、「アプリ > アプリの詳細設定 > アプリ実行エイリアス」の順に選択して、「アプリ インストーラー」の「python.exe」と「python3.exe」をオフにする

        ![アプリ インストーラーのスクリーンショット](img/スクリーンショット%202025-01-06%20184530.png)

    3. PCを再起動

    4. バージョンの確認

        ターミナルで以下のコマンドを実行

        ```powershell
        pyenv --version
        ```

        `pyenv 3.1.1` のように表示されればOK

    5. pyenvのアップデート

        ターミナルで以下のコマンドを実行

        ```powershell
        pyenv update
        ```

3. Pythonのインストール

    ターミナルで以下のコマンドを実行

    ```powershell
    pyenv install 3.12.2
    ```

4. 使用するPythonのバージョンを指定

    ターミナルで以下のコマンドを実行

    ```powershell
    pyenv versions
    ```

    ここで `3.12.2` が確認されたら、以下のコマンドをそれぞれ実行

    ```powershell
    pyenv global 3.12.2
    ```

    ```powershell
    pyenv local 3.12.2
    ```
    <!-- PowerShellで `&&` 使えなかった -->

5. Pythonのバージョンを確認

    ターミナルで以下のコマンドを実行

    ```powershell
    python --version
    ```

    ちゃんとインストールしたバージョン (今回は `Python 3.12.2`) が表示されたら成功です！

### Mac

#### 1. Mac App StoreからXcodeをインストール

* Xcodeはインストールに20～30分かかる。ひたすら待つ

#### 2. Homebrewのインストール

* 「ターミナル.app (terminal.app)」を起動
* 以下のコマンドを実行

    ```zsh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

#### 3. Pythonのインストール

1. pyenvのインストール

    ターミナルで以下のコマンドを実行

    ```zsh
    brew install pyenv
    ```

2. 使用しているShellの確認

    ターミナルで以下のコマンドを実行

    ```zsh
    echo $SHELL
    ```

    スラッシュの最後が `zsh` か `bash` か覚えておいてください

3. 環境変数の設定

    ターミナルで以下のコマンドをコピー＆ペースト

    * `zsh` の人の場合

        ```zsh
        echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc \
        && echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc \
        && echo 'eval "$(pyenv init --path)"' >> ~/.zshrc \
        && echo 'eval "$(pyenv init -)"' >> ~/.zshrc \
        && cat ~/.zshrc
        ```

    * `bash` の人の場合

        ```bash
        echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile \
        && echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile \
        && echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile \
        && echo 'eval "$(pyenv init -)"' >> ~/.bash_profile \
        && cat ~/.bash_profile
        ```

    最後に`echo`の中身が出力されているか確認してください

4. Pythonのインストール

    ターミナルで以下のコマンドを実行

    ```zsh
    pyenv install 3.12.2
    ```

5. 使用するPythonのバージョンを指定

    ターミナルで以下のコマンドを実行

    ```zsh
    pyenv versions
    ```

    ここで `3.12.2` が確認されたら、以下のコマンドを実行

    ```zsh
    pyenv global 3.12.2 \
    && pyenv local 3.12.2
    ```

6. Pythonのバージョンを確認

    ターミナルで以下のコマンドを実行

    ```zsh
    python --version
    ```

    ちゃんとインストールしたバージョン (今回は `Python 3.12.2`) が表示されたら成功です！

#### 4. VSCodeのインストール

* [こちら](https://code.visualstudio.com/docs?dv=osx)をクリックして、VSCodeのzipファイルをインストール
* 解凍してアプリケーションに移す

<!--
### 両方

#### 1. GitHubのアカウント登録

* [こちら](https://github.co.jp/)にアクセスしてサインアップする

#### 2. 登録したメールアドレスを勉強会のグループチャットに送る

#### 3. VSCodeにてcodeコマンドをインポート

1. `Ctrl`+`Shift`+`P` (Macは `⌘ Cmd`+`⇧ Shift`+`P`) を押す
    * 上にテキストボックスが出てきます
2. そこに `shell` と打ち込むと、`Shell Command: Install 'code' command in PATH` が出てくるのでそれを選択
3. パスワードを要求されたら打ち込む
4. `successfully imported` 的な文章が出てきたらOK
-->
