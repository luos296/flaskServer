#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests


class TestTask:

    def setup_class(self):
        self.base_url = 'http://127.0.0.1:5000/task'

    def test_post(self):
        data = {'remark': '测试数据', 'report': 'qqq'}
        r = requests.post(self.base_url, json=data)
        print(r.json())
        assert r.status_code == 200

    def test_get(self):
        r = requests.get(self.base_url, params={'id': 1})
        print(r.json())
        assert r.status_code == 200
