Flask-ZS demo
===============

demo

users
-------

User List http://localhost:5000/users/

Add User

    .. code-block:: sh

        curl -X POST \
        http://localhost:5000/users/ \
        -H 'content-type: application/json' \
        -d '{
            "name": "Five",
            "phone": "13800138000"
        }'