from dataclasses import dataclass
from datetime import datetime
import uuid


@dataclass
class BugReport:
    id: uuid
    datetime: datetime
    title: str
    content: str

    def update(self, **kwargs):

        if "id" in kwargs:
            raise ValueError("Trying to change primary key")

        for attribute in kwargs:
            if not hasattr(self, attribute):
                raise AttributeError(
                    "Not expected attribute:{} [class: {}]".format(
                        attribute, self.__class__
                    )
                )

        for attribute, value in kwargs.items():
            setattr(self, attribute, value)


def create_bug_report(title, content=''):
    bug = BugReport(uuid.uuid4(), datetime.now(), title, content)
    return bug


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    title = input('Введите название бага: ')
    content = input('Введите описание бага: ')
    create_bug_report(title, content)