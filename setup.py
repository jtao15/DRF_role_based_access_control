import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='drf_rbac',  
     version='0.1',
     author="Jiapeng Tao",
     author_email="jiapengtao0@gmail.com",
     description="Django rest framework user based access control.",
     long_description="Modified from django-rest-framework-roles to allow default function overriding.",
     long_description_content_type="text/markdown",
     url="https://github.com/jtao15/drf-rbac",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
