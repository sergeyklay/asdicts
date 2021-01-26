# This file is part of the asdicts.
#
# Copyright (c) 2021 Serghei Iakovlev
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Provide utilities for working with dictionaries."""

from functools import reduce


def intersect_keys(obj: dict, keys, invert=False) -> dict:
    """Select the provided keys out of an ``obj`` object.

    Selects the provided keys (or everything except the provided keys
    for ``invert=True``) out of an ``obj`` object.

    >>> o = {'include': 'fields', 'foo': 'bar', 'baz': 42}
    >>> k = {'include', 'limit'}
    >>> intersect_keys(o, k)
    {'include': 'fields'}
    >>> intersect_keys(o, k, True)
    {'foo': 'bar', 'baz': 42}
    """
    result = {}
    for key in obj:
        if (invert and key not in keys) or (not invert and key in keys):
            result[key] = obj[key]

    return result


def merge(*objects) -> dict:
    """Merge one or more objects into a new object.

    >>> merge({'a': 42}, {'foo': 'bar'})
    {'a': 42, 'foo': 'bar'}
    >>> merge({'a': 42}, {'foo': 'bar', 'a': 17})
    {'a': 17, 'foo': 'bar'}
    >>>  merge({'a': 17, 'foo': 'bar'})
    {'a': 17, 'foo': 'bar'}
    >>> merge({'a': 1}, {'b': 2}, {'c': 3}, {'a': 4})
    {'a': 4, 'b': 2, 'c': 3}
    """
    result = {}
    for obj in objects:
        result.update(obj)

    return result


def path(data: dict, item, default=None):
    """Steps through an item chain to get the ultimate value.

    If ultimate value or path to value does not exist, does not raise
    an exception and instead returns ``default``.

    >>> d = {'rel': {'org': {'data': {'id': 42}}}}
    >>> path(d, 'rel.org.data.id')
    42
    >>> path(d, 'foo.bar.baz.buz', 42)
    42
    >>> path(d, 'foo.bar.baz.buz')
    >>>
    """
    def getitem(obj, name: str):
        if obj is None:
            return default

        try:
            return obj[name]
        except (KeyError, TypeError):
            return default

    return reduce(getitem, item.split('.'), data)
