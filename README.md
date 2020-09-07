# mysql-csv-inserter

## About (日本語は下部に記載しています)

This program imports CSV data to MySQL server.  
The execution process is in the following order.

- Delete data that already registered in DB among CSV.
- Insert all CSV data.

This program is a simple snippet, so feel free to modify it to suit your needs.

## Prerequisites

This application is written in **_Python3_**.

## Usage

Please execute the following preparations before executing this program.

### 1. Install dependencies

Execute the following commands to install dependencies.

```
pip install --upgrade pip
sudo apt-get install -y mysql-server
sudo apt-get install \
  python3 \
  python-dev python3-dev \
  build-essential \
  libssl-dev \
  libffi-dev \
  libxml2-dev \
  libxslt1-dev \
  zlib1g-dev \
  python3-pip
pip install -r requirements.txt
```

### 2. Prepare CSV data

Store the CSV data in the following directory with the following file name.

```
Directory Name : csv
File Name : data.csv
```

### 3. Execution

Execute with the following command.

```
python3 main.py
```

---

## 概要

本プログラムは、MySQL サーバーに対して CSV データのインポートを実施します。  
以下の順序で処理を実行します。

- CSV データに記述されたデータのうち既に DB に登録されているデータを削除します
- CSV データを全て INSERT します

本プログラムは簡素に作られたスニペットですので、用途に応じて自由に改変してお使いください。

## 前提条件

本アプリケーションは **_Python3_** で記述されています。

## 使い方

本プログラムを実行するにあたり、以下の事前準備を実施してください。

### 1. 依存ライブラリのインストール

以下のコマンドを実行し、依存ライブラリのインストールを実施してください。

```
pip install --upgrade pip
sudo apt-get install -y mysql-server
sudo apt-get install \
  python3 \
  python-dev python3-dev \
  build-essential \
  libssl-dev \
  libffi-dev \
  libxml2-dev \
  libxslt1-dev \
  zlib1g-dev \
  python3-pip
pip install -r requirements.txt
```

### 2. CSV データの用意

CSV データを以下のディレクトリに以下のファイル名で格納してください。

```
ディレクトリ名 : csv
ファイル名 : data.csv
```

### 3. 実行

以下のコマンドで実行してください。

```
python3 main.py
```
