import datetime
import logging
from typing import Optional, Tuple, Union

from bson.objectid import ObjectId
from pymongo.collection import Collection, Cursor
from pymongo.errors import AutoReconnect, PyMongoError

logger = logging.getLogger(__name__)

MAX_TIME_MS = 10000


no_id = {"_id": False}


def persist_doc(collection: Collection, doc: dict) -> Tuple[Optional[ObjectId], bool]:
    result_id = None
    success = False
    try:
        result = collection.insert_one(doc)

        if result.acknowledged:
            logger.info("doc saved and mongo update acknowledged")
            result_id = result.inserted_id
            success = True
        else:
            logger.warning("mongo update not acknowledged")
    except PyMongoError:
        logger.exception(f"failed saving doc to collection")

    return result_id, success


def _query_factory(
    collection: Collection, query: dict, find_one: bool, sort_params: Optional[Tuple[str, int]]
) -> Optional[Union[dict, Cursor]]:
    if find_one:
        data = collection.find_one(query, max_time_ms=MAX_TIME_MS)
    elif sort_params is not None:
        data = collection.find(query, max_time_ms=MAX_TIME_MS).sort(sort_params[0], sort_params[1])
    else:
        data = collection.find(query, max_time_ms=MAX_TIME_MS)
    return data


def retreive_doc(
    collection: Collection,
    query: dict,
    find_one: bool = True,
    sort_params: Optional[Tuple[str, int]] = None,
) -> Optional[Union[dict, Cursor]]:
    doc = None
    max_attempts = 2
    for attempt in range(max_attempts):
        try:
            doc = _query_factory(collection, query, find_one, sort_params)
        except AutoReconnect:
            if attempt < max_attempts - 1:
                logger.exception("autoreconnect error on mongo, retrying")
            else:
                logger.exception("autoreconnect error on mongo, no more retries")
                break
        else:
            logger.info("mongo query succeeded")
            break
    return doc


def add_user_metadata(doc: dict, username: Optional[str]) -> dict:
    doc["username"] = username
    doc["timestamp"] = datetime.datetime.now()
    return doc
