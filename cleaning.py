import main
import pandas as pd

"""author = []

for key,value in main.tiktok.items():
    author.append(key.id)

data = pd.DataFrame({'id' : author})"""

id = []
desc = []
createTime = []
video = []
author = []
music = []
challenges = []
stats = []
duetInfo = []
originalItem = []
officalItem = []
textExtra = []
secret = []
forFriend = []
digged = []
itemCommentStatus = []
showNotPass = []
vl1 = []
itemMute = []
authorStats = []
privateItem = []
duetEnabled = []
stitchEnabled = []
shareEnabled = []
stickersOnItem = []
isAd = []
duetDisplay = []
stitchDisplay = []
username = []
hastag = []

for tiktok in tiktoks:
    id.append(tiktok.get('id'))
    desc.append(tiktok.get('desc'))
    createTime.append(tiktok.get('createTime'))
    video.append(tiktok.get('video'))
    author.append(tiktok.get('author'))
    music.append(tiktok.get('music'))
    challenges.append(tiktok.get('challenges'))
    stats.append(tiktok.get('stats'))
    duetInfo.append(tiktok.get('duetInfo'))
    originalItem.append(tiktok.get('originalItem'))
    officalItem.append(tiktok.get('officalItem'))
    textExtra.append(tiktok.get('textExtra'))
    secret.append(tiktok.get('secret'))
    forFriend.append(tiktok.get('forFriend'))
    digged.append(tiktok.get('digged'))
    itemCommentStatus.append(tiktok.get('itemCommentStatus'))
    showNotPass.append(tiktok.get('showNotPass'))
    vl1.append(tiktok.get('vl1'))
    itemMute.append(tiktok.get('itemMute'))
    authorStats.append(tiktok.get('authorStats'))
    privateItem.append(tiktok.get('privateItem'))
    duetEnabled.append(tiktok.get('duetEnabled'))
    stitchEnabled.append(tiktok.get('stitchEnabled'))
    shareEnabled.append(tiktok.get('shareEnabled'))
    stickersOnItem.append(tiktok.get('stickersOnItem'))
    isAd.append(tiktok.get('isAd'))
    duetDisplay.append(tiktok.get('duetDisplay'))
    stitchDisplay.append(tiktok.get('stitchDisplay'))

test = df["author"]

for key in test:
    test =username.append(key.get('nickname'))



df = pd.DataFrame({'id' : id,
                    'desc': desc,
                    'createTime':createTime,
                    'video':video,
                    'author':author,
                    'music':music,
                    'challenges':challenges,
                    'stats':stats,
                    'duetInfo':duetInfo,
                    'originalItem':originalItem,
                    'officalItem' :officalItem,
                    'textExtra':textExtra,
                    'secret':secret,
                    'forFriend':forFriend,
                    'digged':digged,
                    'itemCommentStatus':itemCommentStatus,
                    'showNotPass':showNotPass,
                    'vl1':vl1,
                    'itemMute':itemMute,
                    'authorStats':authorStats,
                    'privateItem':privateItem,
                    'duetEnabled' :duetEnabled,
                    'stitchEnabled':stitchEnabled,
                    'shareEnabled':shareEnabled,
                    'stickersOnItem':stickersOnItem,
                    'isAd':isAd,
                    'duetDisplay':duetDisplay,
                    'stitchDisplay':stitchDisplay,
                   'username':username})


new_data = df.to_excel("output.xlsx")
