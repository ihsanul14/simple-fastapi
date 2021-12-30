import struct
import socket
import ctypes
import uuid
import os
from decouple import config
from .response import resp, except_response
from repository import repository


def get_data():
    result = {}
    result['data'] = []
    try:
        result['code'] = 200
        result['message'] = "success retrieve data"
        result['data'] = repository.get_data()
    except Exception as err:
        result = except_response(result, err)
    print(result)
    return result


def get_data_by_id(data):
    result = {}
    try:
        result['code'] = 200
        result['message'] = "success retrieve projects data with id = {}".format(
            data['id'])
        result['data'] = repository.get_data_by_id(data)
    except Exception as err:
        result = except_response(result, err)
    return result


def add_data(data):
    result = {}
    result['data'], err = repository.add_data(data)
    if err is "":
        result['code'] = 200
        result['message'] = "success insert data"
        result = resp(result)
    else:
        result = except_response(data, err)
    return result


def update_data(data):
    result = {}
    result['data'], err = repository.update_data(data)
    if err is "":
        result['code'] = 200
        result['message'] = "success update data with id = {}".format(
            data['project_id'])
        result = resp(result)
    else:
        result = except_response(result, err)
    return result


def delete_data(data):
    result = {}
    result['data'], err = repository.delete_data(data)
    if err is "":
        result['code'] = 200
        result['message'] = "success delete data with id = {}".format(
            data['id'])
        result = resp(result)
    else:
        result = except_response(result, err)
    return result
