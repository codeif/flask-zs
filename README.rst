Helpers for Flask.
====================

Helpers for Flask. 使用示例 `codeif/flask-zs-template  <https://github.com/codeif/flask-zs-template>`_

依赖:

- flask
- requests


安装
----

.. code-block:: sh

    pip install flask-zs

额外安装 `codeif/zs-mixins <https://github.com/codeif/zs-mixins>`_

.. code-block:: sh

    pip install flask-zs[mixins]


集中models
-------------

把models集中到一个__init__.py中(zsdemo为package name)::

    PYTHONPATH=. collect-models <zsdemo> instance/__init__.py
