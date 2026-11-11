###############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) typedef int GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
###############################################################################

# What used to be an AttributeError on None, at the sites ty 0.0.100's
# missing-union-attribute found (#224), is now a clear error.

import asyncio
import os

import pytest
import txaio

import xbr
from xbr._buyer import SimpleBuyer
from xbr._schema import FbsSchema
from xbr._seller import KeySeries, SimpleSeller
from xbr._util import contract


@pytest.fixture
def framework():
    # the delegates make a txaio logger: keep a framework another test selected
    if not (txaio.using_twisted or txaio.using_asyncio):
        txaio.use_asyncio()


def test_contract_before_set_provider(monkeypatch):
    monkeypatch.setattr(xbr, "xbrtoken", None)
    with pytest.raises(RuntimeError, match="call xbr.setProvider"):
        contract("xbrtoken")


def test_contract_after_set_provider(monkeypatch):
    sentinel = object()
    monkeypatch.setattr(xbr, "xbrtoken", sentinel)
    assert contract("xbrtoken") is sentinel


def test_key_series_encrypt_before_start():
    ks = KeySeries(os.urandom(16), 1, interval=10)
    with pytest.raises(RuntimeError, match="call start"):
        asyncio.run(ks.encrypt({"a": 1}))


def test_seller_session_before_start(framework):
    seller = SimpleSeller(os.urandom(20), os.urandom(32))
    with pytest.raises(RuntimeError, match="not running"):
        seller._running_session()


def test_buyer_session_before_start(framework):
    buyer = SimpleBuyer(os.urandom(20), os.urandom(32), 10)
    with pytest.raises(RuntimeError, match="not running"):
        buyer._running_session()


def test_schema_load_missing_file(tmp_path):
    # a path that is not a file: open() names it, instead of str has no read()
    with pytest.raises(FileNotFoundError):
        FbsSchema.load(None, str(tmp_path / "missing.bfbs"))
