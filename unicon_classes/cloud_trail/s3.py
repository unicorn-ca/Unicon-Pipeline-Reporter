from unicon_classes.cloud_trail.event_decode import BasicDecode as EventDecode
from typing import List


class S3(EventDecode):
    def __init__(self, event: dict):
        super().__init__(event)
        self.__s3_decode(self.cloud_trail_event)

    def __s3_decode(self, event: dict):
        pass





