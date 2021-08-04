#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime
from server import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # autoincrement=True
    remark = db.Column(db.String(120))
    report = db.Column(db.String(120))
    create_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def as_dict(self):
        return {
            "id": self.id,
            "remark": self.remark,
            "report": self.report,
            "create_at": str(self.create_at)
        }


if __name__ == '__main__':
    db.create_all()
