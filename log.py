import datetime

today = datetime.datetime.now()
today = (today.strftime("%Y%m%d"))

def logger(message):
    log = open('scanResults'+today+'.log', 'a')
    log.write('\n' + str(message))
    log.close()
    #print(message)