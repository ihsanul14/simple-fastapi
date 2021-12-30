import struct
import socket
import ctypes
import uuid
import os
from decouple import config
from database.database import connect_pg

table = "project"
conn = connect_pg()


def get_data():
    cur = conn.cursor()
    try:
        cur.execute("""SELECT * from {}""".format(table))
        result = cur.fetchall()
    except Exception as err:
        cur.execute("ROLLBACK")
    return result


def get_data_by_id(data):
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * from {} where project_id = '{}'".format(table, data['id']))
        result = cur.fetchall()
    except Exception as err:
        cur.execute("ROLLBACK")
    return result


def add_data(data):
    cur = conn.cursor()
    err = ""
    try:
        cur.execute(
            "INSERT INTO {} (project_id, project_name) VALUES ('{}', '{}')".format(table, data['project_id'], data['project_name']))
        conn.commit()
    except Exception as e:
        err = e
        cur.execute("ROLLBACK")
    return data, err


def update_data(data):
    cur = conn.cursor()
    err = ""
    try:
        cur.execute("UPDATE {} SET project_name = '{}' where project_id = '{}'".format(
            table, data['project_name'], data['project_id']))
        conn.commit()
    except Exception as e:
        err = e
        cur.execute("ROLLBACK")
    return data, err


def delete_data(data):
    cur = conn.cursor()
    err = ""
    try:
        cur.execute(
            """DELETE from {} WHERE project_id = '{}'""".format(table, data['id']))
        conn.commit()
    except Exception as e:
        err = ""
        cur.execute("ROLLBACK")
    return data, err
