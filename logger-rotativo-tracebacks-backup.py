#!/usr/bin/python3
# -*- coding: utf-8 -*-

# - - - - - - - - - - - - - - [ Bloco de Importar Bibliotecas (libs) ] - - - - - - - - - - - - - - #

try:
    import traceback

    import logging
    from logging.handlers import RotatingFileHandler
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.ERROR)
    handler = RotatingFileHandler("./log.txt", maxBytes=10000, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

except Exception as E:
    print('Erro ao Importar Bibliotecas: ' + str(E))


try:
    PRINT(A)  # para causar erro proposital

except Exception as E:
    logger.error(traceback.format_exc())