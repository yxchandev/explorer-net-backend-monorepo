from pathlib import Path

import uvicorn
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


def main() -> None:
    uvicorn.run(
        "apps.consumer.src.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
