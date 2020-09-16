from .array import get_array_layout
from .eventseeker import EventSeeker
from .eventsource import EventSource, event_source
from .hdf5tableio import HDF5TableReader, HDF5TableWriter
from .tableio import TableWriter, TableReader
from .datalevels import DataLevel

# import event sources to make them visible to EventSource.from_url
from .simteleventsource import SimTelEventSource

__all__ = [
    "get_array_layout",
    "HDF5TableWriter",
    "HDF5TableReader",
    "TableWriter",
    "TableReader",
    "EventSeeker",
    "EventSource",
    "event_source",
    "SimTelEventSource",
    "DataLevel",
]

# define the version of the DL1 data model written here. This should be updated
# when necessary:
# - increase the major number if there is a breaking change to the model
#   (meaning readers need to update scripts)
# - increase the minor number if new columns or datasets are added
# - increase the patch number if there is a small bugfix to the model.
DL1_DATA_MODEL_VERSION = "v2.0.0"
