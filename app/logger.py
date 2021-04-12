from structlog import PrintLogger, wrap_logger
from structlog.processors import JSONRenderer


wrapped_logger = PrintLogger()
logger = wrap_logger(wrapped_logger, processors=[JSONRenderer()])
log = logger.new()
