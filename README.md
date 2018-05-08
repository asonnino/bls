# BLS Signatures
[![license](https://img.shields.io/badge/license-BSD-brightgreen.svg)](https://github.com/asonnino/bls/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/asonnino/bls.svg?branch=master)](https://travis-ci.org/asonnino/bls)

A simple Python implementation of threshold BLS signatures.

A link to the full paper is available at the following address: [https://arxiv.org/abs/1802.07344](https://iacr.org/archive/asiacrypt2001/22480516.pdf)


## Pre-requisites
**Coconut** is built on top of [petlib](https://github.com/gdanezis/petlib) and [bplib](https://github.com/gdanezis/bplib), make sure to follow [these instructions](https://github.com/gdanezis/petlib#pre-requisites) to install all the pre-requisites.


## Install
If you have `pip` installed, you can install **bls** with the following command:
```
$ pip install bls-lib
```
otherwise, you can build it manually as below:
```
$ git clone https://github.com/asonnino/bls
$ cd bls
$ pip install -e .
```


## Test
Tests can be run as follows:
```
$ pytest -v --cov=bls tests/
```
or simply using tox:
```
$ tox
```

## License
[The GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.en.html)