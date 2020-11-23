Helpers for Flask.
====================

Helpers for Flask. 使用示例 `codeif/flask-zs-template  <https://github.com/codeif/flask-zs-template>`_

包含:

- flask
- sqlalchemy
- requests
- pydantic


安装
----

.. code-block:: sh

    pip install flask-zs

集中models
-------------

把models集中到models/__init__.py文件中(zsdemo为package name)::

    PYTHONPATH=. collect-models [zsdemo]
