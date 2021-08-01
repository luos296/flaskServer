#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask_restful import Resource
from flask import request
from models.testcase import TestCase
from server import app, db


class TestCaseServer(Resource):
    def get(self):
        case_id = request.args.get("id")
        if case_id:
            case_data = TestCase.query.filter_by(id=case_id).first()
            app.logger.info(case_data)
            data = [case_data.as_dict()]
        else:
            case_data = TestCase.query.all()
            data = [i.as_dict() for i in case_data]
        app.logger.info(data)
        return {"error": 0, "msg": "get success", "data": data}

    def post(self):
        case_data = request.json
        app.logger.info(case_data)
        testcase = TestCase(**case_data)
        db.session.add(testcase)
        db.session.commit()
        return {"error": 0, "msg": "post success"}

    def put(self):
        case_id = request.json.get('id')
        case_data = TestCase.query.filter_by(id=case_id).update(request.json)
        app.logger.info(case_data)
        db.session.commit()
        return {"error": 0, "msg": "put success", 'data': request.json}

    def delete(self):
        case_id = request.args.get('id')
        if not case_id:
            return {"error": 40001, "msg": "id can't be null"}
        else:
            case_data = TestCase.query.filter_by(id=case_id).delete()
            db.session.commit()
            return {"error": 0, "msg": "delete success", "data": case_data}
