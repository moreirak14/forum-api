class HttpReturnError(Exception):  # 500 or...
    message: str


class PageNotLoaded(HttpReturnError):
    message = "Erro ao buscar dados, verifique a conexão da API!"
