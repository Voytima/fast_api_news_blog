from .error_404 import page_not_found
from .error_403 import access_denied
from .error_500 import server_error

exception_handlers = {
    404: page_not_found,
    403: access_denied,
    500: server_error
}
