from fastapi import APIRouter, Depends
from api.dependencies import get_db_helper
from backend.core.db_helper import DBHelper


root_router = APIRouter(prefix='/root', tags=['Root'])

@root_router.get('/drop_db')
def drop_db(db_helper: DBHelper = Depends(get_db_helper)):
    db_helper.drop_tables()
    return {'status': '200'}

@root_router.get('/count_tables')
def get_count_tables(db_helper: DBHelper = Depends(get_db_helper)):
    count_tables = db_helper.get_tables_count()
    return {
        'status': '200',
        'count_tables': f'{count_tables}',
    }

@root_router.get('/create_tables/')
def create_db(db_helper: DBHelper = Depends(get_db_helper)):
    db_helper.create_tables()
    return get_count_tables(db_helper)