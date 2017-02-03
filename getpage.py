import requests
import json
import os
from bs4 import BeautifulSoup
from colorama import init, Fore


# response = requests.get("http://www.basketball-reference.com\
# /leaders/pts_career.html")


def FetchData(Player, PageLink, DataList):
    response = requests.get(PageLink)
    soup = BeautifulSoup(response.text, "lxml")
    # print(soup.a)

    tables = soup.find_all("table")
    # 总共有三张表，找第2张nba排名的表
    nba = tables[1]
    Result = nba.find("a", text=Player)
    # print(Result)

    if Result is None:
        # print("Not on list")
        return

    TagLine = Result.parent.parent
    PlayerName = Result.string
    Rank = TagLine.previous_sibling.previous_sibling.string
    Data = TagLine.next_sibling.string
    DataList.insert(0, (Rank, PlayerName, Data))

    # 初始化TagLine
    TagLine = TagLine.parent.previous_sibling.previous_sibling
    # 循环找到前面几个运动员的数据，一并显示
    for i in range(1, 20):
        PlayerName = TagLine.a.string
        Rank = TagLine.contents[1].string
        Data = TagLine.contents[4].string
        DataList.insert(0, (Rank, PlayerName, Data))
        # 如果已经到了第1名，则不再往前解析
        if str(Rank) == '1.':
            # print("no more!")
            break
        TagLine = TagLine.previous_sibling.previous_sibling

    # print(DataList)


# 存储本次抓取的球员数据
def DumpHistory(Player, DataPlane):
    Info = {}
    for item in DataPlane:
        # print(item[0])
        # print(item[2])
        if len(item[2]) != 0:
            # print(item[2][-1])
            Info[item[0]] = item[2][-1]
    # print("info:")
    # print(Info)
    with open("history.text", "w") as f:
        f.write(json.dumps(Info))


def ShowData(DataPlane):
    init(autoreset=True)
    Info = {}
    if os.path.exists("history.text"):
            with open("history.text", "r") as f:
                history = f.read()
            if len(history) != 0:
                Info.update(json.loads(history))

    for item in DataPlane:
        print(Fore.LIGHTRED_EX + str(item[0]))
        for content in item[2]:
            print("%-10s %-20s %10s" % (content[0], content[1], content[2]))

        if item[0] in Info.keys():
            print("----------------Last Time-----------------")
            print("%-10s %-20s %10s" % (Info[item[0]][0], Info[item[0]][1],
                  Info[item[0]][2]))
            # print(Info[item[0]])
        print("------------------------------------------")


if __name__ == '__main__':
    prefix = "http://www.basketball-reference.com/leaders/"
    DataPlane = (
                ("Points:", prefix + "pts_career.html", []),
                ("Rebounds:", prefix + "trb_career.html", []),
                ("Blocks:", prefix + "blk_career.html", []),
                ("Assists:", prefix + "ast_career.html", []),
                ("Steals:", prefix + "stl_career.html", []),
                ("3-pt Field Goals:", prefix + "fg3_career.html", []),
                )

    for item in DataPlane:
        FetchData("Kevin Durant", item[1], item[2])
    # FetchData(DataPlane[0][1], DataPlane[0][2])
    ShowData(DataPlane)
    DumpHistory('Kevin Durant', DataPlane)
