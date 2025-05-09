import pathlib
import json


def render(src: str) -> str | None:
    file: pathlib.Path = pathlib.Path(src)
    if file.is_dir():
        return None
    if file.exists:
        return file.read_text()
    else:
        return None


def change(src: str, data: dict) -> None:
    data_in_bytes: bytes = json.dumps(data).encode('utf-8')
    file: pathlib.Path = pathlib.Path(src)
    if file.is_dir():
        return None
    if file.exists():
        file.write_bytes(data_in_bytes)
    else:
        return None


json_obj: dict = {
    "is": {
        "this": "good",
        "enough": "for"
    },
    "you": "yet"
}
change("./example.json", json_obj)