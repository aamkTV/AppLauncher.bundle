import subprocess

VIDEO_PREFIX = "/video/applauncher"
NAME = "App Launcher"
ART = "art-default.jpg"
ICON = "icon-default.png"

def Start():
    Plugin.AddPrefixHandler(VIDEO_PREFIX, MainMenu, NAME, ICON, ART)
    Plugin.AddViewGroup("List", viewMode = "List", mediaType = "items")

    MediaContainer.art = R(ART)
    MediaContainer.title1 = NAME
    MediaContainer.viewGroup = "List"
    DirectoryItem.thumb = R(ICON)

def MainMenu():
    oc = ObjectContainer()
    items = JSON.ObjectFromString(Resource.Load('Apps.json'))
    for item in items:
        oc.add(DirectoryObject(key = Callback(RunApp, path = item["path"]), title = item["title"]))
    return oc

def RunApp(path):
    p = subprocess.Popen(path, stdout=subprocess.PIPE)
    out, err = p.communicate()