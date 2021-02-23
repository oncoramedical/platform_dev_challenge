import logging
import os
from distutils.util import strtobool

logger = logging.getLogger(__name__)


def setup_debugger():
    debugger_enabled = _get_debugger_enabled()

    if debugger_enabled:
        import multiprocessing

        if multiprocessing.current_process().pid > 1:
            import debugpy

            debug_port = int(os.environ["DEBUG_PORT"])

            debugpy.listen(("0.0.0.0", debug_port))
            logger.debug(
                "Remote debugger listening for client to attach", extra={"debug_port": debug_port}
            )


def _get_debugger_enabled():
    debugger_val = os.getenv("DEBUGGER")

    try:
        return bool(strtobool(os.getenv("DEBUGGER")))
    except AttributeError:
        # env var DEBUGGER is not set
        return False
    except ValueError:
        # env var DEBUGGER is an unrecognized value
        logger.debug(
            "Unexpected value for DEBUGGER. Debugging will be disabled",
            extra={"raw_value": debugger_val},
        )
        return False
