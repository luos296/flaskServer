#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests


class TestCase:

    def setup_class(self):
        self.base_url = 'http://127.0.0.1:5000/testcase'

    def test_get(self):
        r = requests.get(self.base_url)
        print(r.json())
        assert r.status_code == 200

    def test_get1(self):
        r = requests.get(self.base_url, params={'id': 1})
        print(r.json())
        assert r.status_code == 200

    def test_post(self):
        data = {'id': 1, 'nodeid': 'nodeid111', 'remark': '备注1'}
        data2 = {'id': 2, 'nodeid': 'nodeid222', 'remark': '备注2'}
        data3 = {'id': 33, 'nodeid': 'nodeid333', 'remark': '备注3'}
        r = requests.post(self.base_url, json=data3)
        print(r.json())
        assert r.status_code == 200

    def test_put(self):
        data2 = {'id': 2, 'nodeid': 'nodeid222', 'remark': '修改备注2'}
        r = requests.put(self.base_url, json=data2)
        print(r.json())
        assert r.status_code == 200

    def test_delete(self):
        r = requests.delete(self.base_url)
        assert r.status_code == 200
        assert r.json()["error"] == 40001
        r = requests.delete(self.base_url, params={'id': 3})
        print(r.json())
        assert r.status_code == 200

