#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="kivycalendar",
    version="0.1.3",

    author="Oleg Kozlov (xxblx)",
    author_email="xxblx.oleg@yandex.com",

    url="https://github.com/yumoqing/kivycalendar",
    description="Calendar & Date picker widgets for Kivy",

    packages=find_packages(),
    install_requires="kivy",

    license="MIT License",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="kivy widgets calendar datepicker",
)
