from fastapi import Request


def get_db_helper(request: Request):
    return request.app.state.db