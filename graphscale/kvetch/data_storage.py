import pickle
import zlib
# import json
from typing import Dict, Any, cast

from uuid import UUID


def data_to_body(data: Dict[str, Any]) -> bytes:
    return zlib.compress(pickle.dumps(data))
    # this should switch to json, but I need to do some special support
    # for correct serializing and deserializing UUIDS and other types
    # return zlib.compress(json.dumps(data).encode())


def body_to_data(body: bytes) -> Dict[str, Any]:
    if body is None:
        return {}
    return cast(Dict[str, Any], pickle.loads(zlib.decompress(body)))


def row_to_obj(row: Dict[str, Any]) -> Dict[str, Any]:
    id_dict = {'obj_id': UUID(bytes=row['obj_id']), 'type_id': row['type_id']}
    body_dict = body_to_data(row['body'])
    return {**id_dict, **body_dict}
