import datetime
import googleapiclient.discovery
from google.cloud import storage


def get_archive():
    archive = dict()
    storage_client = storage.Client()
    bucket = storage_client.get_bucket("website-posts")
    blobs = bucket.list_blobs()
    for blob in blobs:
        meta = bucket.get_blob(blob.name)
        archive[meta.generation] = blob.name
    return archive

def get_file_text(filename):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket("website-posts")
    blob = bucket.blob(filename)
    return blob.download_as_string().decode("utf-8")
