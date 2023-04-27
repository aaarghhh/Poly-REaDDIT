# Poly-REaDDIT
## A tool for gathering information, Polygon address and NFT details about any Reddit users.
Since last year Reddit introduced a way to costumize your profile with NFTs. This tool is a way to gather information, its NFTs and the Polygon address of any Reddit user.

<div align="center">
     <img alt="Avatar" src="img/img.png">
</div>

When you purchase or mint a Reddit NFT, Reddit client will create a Polygon wallet/address for you. This address is linked to your Reddit account and can be used to send and receive NFTs.
The wallet is related to the Poligon network, so you can use it to send and receive NFTs from other Polygon wallets or sell it. Poligon is a Layer 2 scaling solution for Ethereum.

The NFT will bring the ability to create a new revenue stream for Reddit and its users, and also customize the aspect of the profile. The related NFTs are listed on OpenSea and PolygonScan.



## Installation and usage
```
$ git clone
$ cd Poly-REaDDIT
$ pip install -r requirements.txt
```
Or directly install the requirements with pip:
```
$ pip install poly-readdit
```
Then you can run the tool with:
```
$ python ./poly-readdit/poly-readdit.py -username xxxxxx
```
Or if you installed via pip directly with:
```
$ poly-readdit -username xxxxxx
```
## Example
```
./poly-readdit/poly-readdit.py -username xxxxxxx

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


 [+] REDDIT USER INFO
  |
  ├ Username: xxxx
  ├ Created UTC: 2013-10-31 09:43:58
  ├ User ID: t2_xxx
  ├ Is mod: False
  ├ Is NSFW: False
  ├ Is Gold: False
  ├ Is Employee: False
  ├ Is Suspended: False
  ├ Hide from robots: True
  ├ Profile ID: t5_xxx
  ├ User name: u/axxxxx
  ├ User karma: 3 (0: Awards received, 0: Awards given, 1: Comments, 2: Posts)
  ├ Polygon Address: 0x5exxxxxxx
  └ ------------------------------------

 [+] NFT INFO
  |
  ├ Name: Hog-nosed Bats #71xxxxx
  ├ ID: nft_eip155:137_f33ad86bb54a2xxxx
  ├ Serial Number: 71xxxx
  ├ Title: Hog-nosed Bats #71xxxx
  ├ External Urls: https://polygonscan.com/token/0xf33ad86bb54xxxxx
  └ ------------------------------------

  ├ Name: The Big Bucks #1148
  ├ ID: nft_eip155:137_4bexxxxxx
  ├ Serial Number: 1xxx
  ├ Title: XXXXXXXXX #1xxxx
  ├ External Urls: https://polygonscan.com/token/0x4be1e0xxxxxxx
  └ ------------------------------------
```
