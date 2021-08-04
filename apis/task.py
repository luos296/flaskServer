#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask_restful import Resource
from flask import request
from models.task import Task
from server import app, db
from utils.jenkins_tool import ExecuteTools


class TaskServer(Resource):
    def post(self):
        nodeids = [i["nodeid"] for i in request.json["nodeids"]]
        remark = ' '.join(nodeids)
        report = ExecuteTools.invoke(remark)
        task = Task(remark=remark, report=report)
        db.session.add(task)
        db.session.commit()
        db.session.close()
        return {"error": 0, "msg": "post success", "data": {"remark": remark, "report": report}}

    def get(self):
        task_data = Task.query.all()
        data = [i.as_dict() for i in task_data]
        app.logger.info(data)
        db.session.close()
        return {"error": 0, "msg": "post success", "data": data}

