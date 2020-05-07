# 本应用的前缀是word, 主要用来解决词语方面的分析


### 结构
.
├── db.sqlite3
├── manage.py
├── mysite
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── word                                   --word app
    ├── admin.py
    ├── apps.py
    ├── dataPro.py                         --数据处理函数, 主要数据处理在里面
    ├── __init__.py
    ├── migrations
    │   ├── __init__.py
    │   └── __pycache__
    │       └── __init__.cpython-38.pyc
    ├── models.py
    ├── __pycache__
    │   ├── admin.cpython-38.pyc
    │   ├── __init__.cpython-38.pyc
    │   ├── models.cpython-38.pyc
    │   ├── urls.cpython-38.pyc
    │   └── views.cpython-38.pyc
    ├── README.md
    ├── tests.py
    ├── urls.py                            --url设置
    └── views.py                           --试图函数



