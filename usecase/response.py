import json


def resp(data):
    res = {}
    res['code'] = data['code']
    if data["code"] == 200:
        res["success"] = True
    else:
        data["success"] = False
    res['data'] = data['data']
    return res


def except_response(data, err):
    print(err)
    data['code'] = 500
    data['message'] = err.args[0]
    return data
