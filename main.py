from datetime import datetime
from bug_report_models import BugReport, BugReports


def create_bug_report():
    id = input('Введите имя автора сообщения: ')
    title = input('Введите название бага: ')
    content = input('Введите описание бага: ')
    bug = BugReport(id, datetime.now(), title, content, False)
    return bug


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    new_bugs = BugReports()
    for _ in range(2):
        new_bugs.add(create_bug_report())
    print(new_bugs)