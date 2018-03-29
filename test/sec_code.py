# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/29 下午1:56
"""
import base64
import uuid

A = uuid.uuid4().bytes + uuid.uuid4().bytes
print(base64.b64encode(A))
print(base64.b64encode(A))
print(A)

print(uuid.uuid4())
print(uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name='a'))
print(uuid.uuid3(namespace=uuid.NAMESPACE_OID, name=''))
print(uuid.uuid3(namespace=uuid.NAMESPACE_URL, name=''))
print(uuid.uuid3(namespace=uuid.NAMESPACE_X500, name=''))

print(uuid.UUID(bytes=uuid.uuid4().bytes))
