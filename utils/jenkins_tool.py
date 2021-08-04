#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from jenkinsapi.jenkins import Jenkins


class ExecuteTools:
    BASE_URL = 'http://127.0.0.1:8081/'
    USERNAME = 'admin'
    PASSWORD = '111299c20f5add99e9450341bec7af56ce'
    JOB_NAME = '测试平台demo'

    @classmethod
    def get_jobs(cls):
        jenkins = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        return jenkins.keys()

    @classmethod
    def invoke(cls, task):
        """
        调用执行器执行
        task: 指定执行的用例
        :return: 报告链接
        """
        jenkins = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        job_demo = jenkins.get_job(cls.JOB_NAME)
        job_demo.invoke(build_params={"task": task})
        last_build_number = job_demo.get_last_buildnumber()
        while True:
            build_number = job_demo.get_last_buildnumber()
            if last_build_number != build_number:
                report_path = cls.BASE_URL + "job/" + cls.JOB_NAME + "/" + \
                              str(build_number) + "/allure"
                return report_path


if __name__ == '__main__':
    print(ExecuteTools.get_jobs())
    path = ExecuteTools.invoke('test_add.py')
    print(path)
