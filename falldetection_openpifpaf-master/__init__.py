"""An open implementation of PifPaf."""

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .annotation import Annotation, AnnotationDet
from . import datasets
from . import decoder
from . import network
from . import optimize
import json

version_json = '''
{
 "date": "2020-08-19T17:37:50+0200",
 "dirty": false,
 "error": null,
 "full-revisionid": "775d01952330a9d2347c68ea137054d1cc7689cb",
 "version": "0.11.8"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
