#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask_restful import Resource
from flask import request
from models.task import Task
from server import app, db
from utils.jenkins_tool import ExecuteTools


class TaskServer(Resource):
    def post(self):
        nodeids = request.json
        remark = ' '.join(nodeids.get('nodeids'))
        report = ExecuteTools.invoke(remark)
        task = Task(remark=remark, report=report)
        db.session.add(task)
        db.session.commit()
        return {"error": 0, "msg": "post success", "data": {"remark": remark, "report": report}}

    def get(self):
        id = request.args.get('id')
        task_data = Task.query.filter_by(id=id).first()
        data = task_data.as_dict()
        app.logger.info(data)
        return {"error": 0, "msg": "post success", "data": data}
