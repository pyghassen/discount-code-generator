from logger import log
def create_code(user_id: int, code: str):
    log.msg(f'Creating code {code} for user {user_id}')
