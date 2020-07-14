# AVIF

![Travis](https://travis-ci.org/link-u/ansible-roles_avif.svg?branch=master)

## 概要
cavif と davif をインストールする ansible role

## 動作確認バージョン

* Ubuntu: 18.04, 20.04
* ansible: 2.8, 2.9

## 使い方 (ansible)

### Role variables

```yaml
## 基本設定
avif_install_flag: True ## インストールフラグ
avif_packages:
  - "cavif"
  - "davif"

# ※ 特に group_vars で修正するような項目はない
```

### Example playbook

```yaml
- hosts:
    - servers
  become: True
  roles:
    - { role: avif, tags: ["avif"] }
```

## License
MIT
