import requests
import json
import sys
import os
import time
from bs4 import BeautifulSoup
from colorama import init, Fore


# response = requests.get("http://www.basketball-reference.com\
# /leaders/pts_career.html")


def FetchData(Player, PageLink, DataList):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    print("Retrieving data from: " + PageLink + "...")
    response = requests.get(PageLink, headers=headers)
    print(response)
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

    # print("Result Parent: ", str(Result.parent.name))
    # 现役球员会用strong标签标出，因此需要做特殊处理
    if Result.parent.name == "strong":
        TagLine = Result.parent.parent
    else:
        TagLine = Result.parent

    # print("TagLine: ", str(TagLine))
    PlayerName = Result.string
    Rank = TagLine.previous_sibling.previous_sibling.string
    Data = TagLine.next_sibling.string
    DataList.insert(0, (Rank, PlayerName, Data))

    # 初始化TagLine
    TagLine = TagLine.parent.previous_sibling.previous_sibling
    if str(Rank) == '1.':
        # print("no more!")
        return

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


# 存储本次抓取的球员数据
def DumpHistory(Player, DataPlane):
    Info = {}
    Data = {}
    if os.path.exists("history.txt"):
        with open("history.txt", "r") as f:
            history = f.read()
            if len(history) != 0:
                Info.update(json.loads(history))

    for item in DataPlane:
        # print(item[0])
        if len(item[2]) != 0:
            # print(item[2][-1])
            Data[item[0]] = item[2][-1]
    Info[Player] = Data
    # print("info:")
    # print(Info)
    with open("history.txt", "w") as f:
        f.write(json.dumps(Info))


def ShowData(Player, DataPlane):
    init(autoreset=True)
    Info = {}
    if os.path.exists("history.txt"):
            with open("history.txt", "r") as f:
                history = f.read()
            if len(history) != 0:
                Info.update(json.loads(history))

    for item in DataPlane:
        print(Fore.LIGHTRED_EX + str(item[0]))
        for content in item[2]:
            # content[0].replace(u'\xa0', u' ')解决windows窗口不能打印unicode字符\xa0的问题
            print("%-10s %-22s %10s" % (content[0].replace(u'\xa0', u' '),
                  content[1], content[2]))

        if Player in Info.keys() and item[0] in Info[Player].keys():
            print("-----------------Last Time------------------")
            print("%-10s %-22s %10s" % (Info[Player][item[0]][0].
                  replace(u'\xa0', u' '),
                  Info[Player][item[0]][1],
                  Info[Player][item[0]][2]))
            # print(Info[Player][item[0]])
        print("--------------------------------------------")


if __name__ == '__main__':
    requests.adapters.DEFAULT_RETRIES = 10
    if len(sys.argv) == 1:
        Player = "Kevin Durant"
    elif len(sys.argv) == 2:
        Player = sys.argv[1]
    else:
        print("Too many parameters, please pass one parameter as player name!")
        sys.exit()
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
        FetchData(Player, item[1], item[2])
        time.sleep(3)
    # FetchData(DataPlane[0][1], DataPlane[0][2])
    ShowData(Player, DataPlane)
    DumpHistory(Player, DataPlane)
