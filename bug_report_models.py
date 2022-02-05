from dataclasses import dataclass, field
from typing import Dict
from datetime import datetime
import uuid


@dataclass
class BugReport:
    pc_name: str
    datetime: datetime
    title: str
    content: str
    is_done: bool

    def update(self, **kwargs):
        for attribute in kwargs:
            if not hasattr(self, attribute):
                raise AttributeError(
                    "Not expected attribute:{} [class: {}]".format(
                        attribute, self.__class__
                    )
                )

        for attribute, value in kwargs.items():
            setattr(self, attribute, value)


@dataclass
class BugReports:
    __reports: Dict[any, BugReport] = field(default_factory=dict)

    def add(self, report: BugReport):
        id = uuid.uuid4()
        counter = 0
        while id in self.__reports:
            id = uuid.uuid4()
            counter += 1
            if counter == 1000:
                raise ValueError("Can't create UUID")

        self.__reports.update({id: report})

    def get_all(self):
        return self.__reports.values()
