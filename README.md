django-rest-framework-role-based-access-control
===========================

Added default function overriding for [django-rest-framework-role](https://github.com/computer-lab/django-rest-framework-roles)

Why would I use this?
---------------------

You have more than one type of user in your data model and you have
business logic that diverges depending on the type of user. You do not
want to organize your API by role because that is not very RESTful. You
do not want to manually type out a lot of conditional branching around
user roles.

You can have a **default** implementation other than specified user roles.

Modeling Requirements
---------------------

-  You must have one **Group** for each role
-  A **User** cannot belong to more than one of the **Groups**
   corresponding to each role

Installation
------------

    $ pip install drf-rbac

Configuration
-------------

-  In ``settings.py`` Register a tuple of DRF methods to override based on user roles.
   Defaults to:

```python
     VIEWSET_METHOD_REGISTRY = (
         "get_queryset",
         "get_serializer_class",
         "perform_create",
         "perform_update",
         "perform_destroy",
         ...
     )
```

-  Also in ``settings.py`` list a tuple of Group names that correspond 1-to-1 with
   user roles. Defaults to:

```python
     ROLE_GROUPS = (
         "role1",
         "role2",
         ...
     )
```

Usage
-----

Add the mixin to any ViewSet:

``` python

    from drf_rbac.mixins import RoleViewSetMixin

    class MyViewSet(RoleViewSetMixin, ModelViewSet):
```

For each of the methods specified in ``VIEWSET_METHOD_REGISTRY`` a
role-scoped method will be generated on your ViewSet.

Parameterizing
--------------

For example, let’s say you have three groups named ``Takers``, ``Leavers`` &
``Gods``. Let’s also say you included ``"list"`` in the ``settings.py``.

```python
     VIEWSET_METHOD_REGISTRY = (
         "list"
     )
     ROLE_GROUPS = (
         "takers",
         "leavers",
         "gods"
     )
```
And you put your list api logic as in your viewset class as below:

```python
     class MyViewSet(RoleViewSetMixin, ModelViewSet):
     
         ...
     
         def list_for_takers(self, request):
             return Response('Hi Takers!')
         
         def list_default(self, request):
             return Response('Hello World!')
```

When a ``Taker`` user hits an endpont on the ViewSet, the call to
``list`` will be rerouted to a call to
``list_for_takers`` and return ``"Hi Takers!"``

When a ``Leavers`` user or ``Gods`` hits an endpont on the ViewSet, the call to
``list`` will be rerouted to a call to
``list_default`` and return ``"Hello World!"``

You can implement each of these methods on your ViewSet to return a
different list function for each type of user. And default method will work for all other roles not specified.

Warning
---------

If you implement ``list`` for the same viewset, all role based access will
be overrided, so it's recommended to use ``list_default`` instead.



Reference
---------------
- [django-rest-framework-role](https://github.com/computer-lab/django-rest-framework-roles)
- [Role-Based Access Control with Django Rest Framework](https://en.wikipedia.org/wiki/Role-based_access_control)
