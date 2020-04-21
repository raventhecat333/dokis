import threading

def setInteractions():
    global interactions
    interactions = []
    return interactions

def addInteraction(channelID, interactionID):
    item = {
        "channelID": channelID,
        "interactionID": interactionID
    }
    def removeIt():
        interactions.remove(item)
        return
    t = threading.Timer(10, removeIt)
    item['timer'] = t
    interactions.append(item)
    item['timer'].start()
    