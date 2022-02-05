from datetime import datetime
from bug_report_models import BugReport, BugReports
import socket


def create_bug_report():
    pc_name = socket.gethostname()
    title = input('Введите название бага: ')
    content = input('Введите описание бага: ')
    bug = BugReport(pc_name, datetime.now(), title, content, False)
    return bug


def bugreport_to_str(bug: BugReport) -> str:
    return f"Автор: {bug.pc_name}\nНазвание бага: {bug.title}\nОписание бага: {bug.content}\nИсправлен: {bug.is_done}\n"


def bugreports_to_str(bugs: BugReports) -> str:
    sum = []
    for _ in bugs.get_all():
        sum.append(bugreport_to_str(_))
    return sum

def print_all(new_bugs):
    print(*bugreports_to_str(new_bugs), sep='\n')


if __name__ == '__main__':
    new_bugs = BugReports()
    num = int(input('Введите кол-во багов: '))
    for _ in range(num):
        new_bugs.add(create_bug_report())
    print_all(new_bugs)
