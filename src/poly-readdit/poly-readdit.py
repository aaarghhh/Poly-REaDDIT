import argparse
import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime


class PolyReaddit:

    start_headers = {
        "Accept-Language": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
    }
    session = None
    session_api = None

    username = ""
    created_str = ""
    nfts = []
    user_id = ""
    is_mod = ""
    is_NSFW = ""
    is_Gold = ""
    is_Employee = ""
    is_Suspended = ""
    hide_from_robots = ""
    profile_id = "N/A"
    user_name = ""
    user_karma = ""
    reddit_access_token = ""
    polygon_address = "N/A"

    def print_banner(self):
        print(
            """
⠀⠀⠀⢠⣾⣿⣿⣿⣿⣶⣤⣤⣾⠛⠻⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡏⠉⠉⠙⠛⠿⠿⣷⣀⣀⣿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀
⠀⠀⣀⣤⣀⠀⢀⣠⣤⣶⣶⣿⣿⣿⣿⣿⣿⣶⣶⣤⣄⡀⠀⣀⣤⣀⠀⠀
⢰⡿⠋⢉⣹⣿⣿⣿⠿⠟⠛⠋⠉⠉⠉⠉⠙⠛⠻⠿⣿⣿⣿⣏⡉⠙⢿⡆
⢸⣇⣠⣾⣿⡿⠋⠀⠀⣠⣤⣀⠀⠀⠀⠀⣀⣤⣄⠀⠀⠙⢿⣿⣷⣄⣸⡗
⠈⢻⣿⣿⠋⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠙⣿⣿⡟⠁
⠀⢸⣿⣿⠀⠀⠀⠀⠀⠉⠋⠁⠀⠀⠀⠀⠈⠙⠉⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⠀⣿⣿⣧⡀⠀⠀⠀⢤⣀⡀⠀⠀⠀⠀⢀⣀⡤⠀⠀⠀⢀⣼⣿⣿⠀⠀
⠀⠀⠈⠿⣿⣷⣦⣀⠀⠀⠉⠻⠿⠿⠿⠿⠟⠉⠀⠀⣀⣴⣾⣿⠿⠁⠀⠀
⠀⠀⠀⠀⠉⠻⢿⣿⣿⣷⣶⣤⣤⣤⣤⣤⣤⣶⣾⣿⣿⡿⠟⠉⠀   Poly-REaDDIT: ⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠻⠿⠿⠿⠿⠟⠛⠛⠉⠁⠀⠀⠀⠀   a Reddit user info collector⠀⠀⠀
"""
        )

    def __init__(self, username):
        self.print_banner()
        self.reddit_session = requests.Session()
        self.reddit_session.headers = self.start_headers
        self.username = username
        self.get_reddit_user_info()
        self.get_NFT()

    def get_reddit_user_info(self):
        try:
            url = "https://www.reddit.com/user/" + self.username
            r = self.reddit_session.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            data = soup.find("script", {"id": "data"}).text
            body_data = json.loads(data.split(" = ")[1][:-1])
            created = datetime.utcfromtimestamp(
                body_data["users"]["models"][self.username.lower()]["createdUtc"]
            )
            self.created_str = created.strftime("%Y-%m-%d %H:%M:%S")
            self.user_id = body_data["users"]["models"][self.username.lower()]["id"]
            self.is_mod = body_data["users"]["models"][self.username.lower()]["isMod"]
            self.is_NSFW = body_data["users"]["models"][self.username.lower()]["isNSFW"]
            self.is_Gold = body_data["users"]["models"][self.username.lower()]["isGold"]
            self.is_Employee = body_data["users"]["models"][self.username.lower()][
                "isEmployee"
            ]
            self.is_Suspended = body_data["users"]["models"][self.username.lower()][
                "isSuspended"
            ]
            self.hide_from_robots = body_data["users"]["models"][self.username.lower()][
                "hideFromRobots"
            ]
            self.user_name = body_data["users"]["models"][self.username.lower()][
                "displayNamePrefixed"
            ]
            if body_data["users"]["models"][self.username.lower()]["hasUserProfile"]:
                self.profile_id = body_data["users"]["models"][self.username.lower()][
                    "profileId"
                ]
            self.user_karma = body_data["users"]["models"][self.username.lower()][
                "karma"
            ]["total"]
            self.user_karma_award_rec = body_data["users"]["models"][
                self.username.lower()
            ]["karma"]["fromAwardsReceived"]
            self.user_karma_award_given = body_data["users"]["models"][
                self.username.lower()
            ]["karma"]["fromAwardsGiven"]
            self.user_karma_comments = body_data["users"]["models"][
                self.username.lower()
            ]["karma"]["fromComments"]
            self.user_karma_post = body_data["users"]["models"][self.username.lower()][
                "karma"
            ]["fromPosts"]
            self.reddit_access_token = body_data["user"]["session"]["accessToken"]

        except:
            print(" [-] Error getting user info")
            return False

    def get_NFT(self):
        try:
            url = "https://gql.reddit.com/"
            self.session_api = requests.Session()
            _head = self.start_headers
            _head["Authorization"] = "Bearer " + self.reddit_access_token.replace(
                "'", ""
            )
            _head["Referer"] = "https://www.reddit.com/"
            _head["Origin"] = "https://www.reddit.com"
            _head["Content-Type"] = "application/json"
            self.session_api.headers = _head
            _payload = {
                "variables": {"id": self.user_id, "isLoggedInUserProfile": False},
                "id": "985a7e8ad0b9",
            }
            r = self.session_api.post(url, json=_payload)
            json_data = json.loads(r.text)
            for i in json_data["data"]["redditorInfoById"]["displayedCollectibleItems"][
                "edges"
            ]:
                nft = {}
                nft["name"] = i["node"]["item"]["name"]
                nft["id"] = i["node"]["item"]["id"]
                nft["serialNumber"] = i["node"]["item"]["serialNumber"]
                nft["title"] = i["node"]["item"]["nft"]["title"]
                nft["externalUrls"] = i["node"]["item"]["nft"]["externalUrls"][0]
                self.nfts.append(nft)
                if self.polygon_address == "N/A" and len(self.nfts) > 0:
                    self.get_token_owner(i["node"]["item"]["nft"]["externalUrls"][0])
        except:
            print(" [-] Error getting NFT")

    def print_data(self):
        print("")
        print(" [+] REDDIT USER INFO")
        print("  |")
        print("  ├ Username: {}".format(self.username))
        print("  ├ Created UTC: {}".format(self.created_str))
        print("  ├ User ID: {}".format(self.user_id))
        print("  ├ Is mod: {}".format(self.is_mod))
        print("  ├ Is NSFW: {}".format(self.is_NSFW))
        print("  ├ Is Gold: {}".format(self.is_Gold))
        print("  ├ Is Employee: {}".format(self.is_Employee))
        print("  ├ Is Suspended: {}".format(self.is_Suspended))
        print("  ├ Hide from robots: {}".format(self.hide_from_robots))
        print("  ├ Profile ID: {}".format(self.profile_id))
        print("  ├ User name: {}".format(self.user_name))
        print(
            "  ├ User karma: {} ({}: Awards received, {}: Awards given, {}: Comments, {}: Posts)".format(
                self.user_karma,
                self.user_karma_award_rec,
                self.user_karma_award_given,
                self.user_karma_comments,
                self.user_karma_post,
            )
        )
        print("  ├ Polygon Address: {}".format(self.polygon_address))
        print("  └ ------------------------------------")
        print("")

        if self.polygon_address != "N/A":
            print(" [+] NFT INFO")
            print("  |")
            for i in self.nfts:
                print("  ├ Name: {}".format(i["name"]))
                print("  ├ ID: {}".format(i["id"]))
                print("  ├ Serial Number: {}".format(i["serialNumber"]))
                print("  ├ Title: {}".format(i["title"]))
                print("  ├ External Urls: {}".format(i["externalUrls"]))
                print("  └ ------------------------------------")
                print("")
        else:
            print(" [-] No NFT INFO")
            print("")



    def get_token_owner(self, url):
        try:
            _query = url.split("token/")[1].split("?a=")
            _token = _query[0]
            _id = _query[1]
            text = requests.get(
                "https://opensea.io/assets/matic/{}/{}".format(_token, _id),
                headers=self.start_headers,
            ).text
            soup = BeautifulSoup(text, "html.parser")
            link = soup.find(
                "div", {"data-testid": "ItemOwnerAccountLink"}
            ).findChildren("a")
            self.polygon_address = link[0].attrs["href"].replace("/", "")
        except:
            print(" [-] Error getting token owner")

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-username", help="reddit username")
    args = parser.parse_args()
    poly = PolyReaddit(args.username)
    poly.print_data()

if __name__ == "__main__":
    run()
