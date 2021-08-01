#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from server import db


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nodeid = db.Column(db.String(80), primary_key=True, nullable=False)
    remark = db.Column(db.String(120))

    def as_dict(self):
        return {
            "id": self.id,
            "nodeid": self.nodeid,
            "remark": self.remark
        }
