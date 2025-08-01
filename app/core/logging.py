import logging as log

def init_custom_logging(module: str) -> log.Logger:
    # log.basicConfig(
    #     level=log.INFO,
    #     format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    # )
    return log.getLogger(module)

def init_logging() -> log.Logger:
  return log.getLogger('uvicorn')
