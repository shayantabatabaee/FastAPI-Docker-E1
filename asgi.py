import os

import uvicorn

from app.app import create_app, init_logger_format

if __name__ == '__main__':
    init_logger_format()
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("DEFAULT_PORT")) if os.getenv("DEFAULT_PORT") else 8080)
