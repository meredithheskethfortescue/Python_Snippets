#!/bin/bash
# Installation of a pip package provided by PyPi in Anaconda

conda skeleton pypi PackageName
conda build packagename
conda install --use-local packagename
