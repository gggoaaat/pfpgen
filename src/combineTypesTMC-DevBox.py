import threading
import glob
import os
import random
import shutil
import json
import asyncio
from sticher import stitch

mintDescription = "The Monster Community"
mintExternal_url = "https://www.theMonsterCommunity.com"
mintImagePrefix = "https://tmc-suits.s3.us-west-1.amazonaws.com/assets/images/"
outputDirectory = 'src/output/TMC/arraylist.json'


async def runCopy(output_dir, filename1):

    # x = threading.Thread(target=copyFile, args=(output_dir,filename1,))
    # x.start()
    copyFile(output_dir, filename1)
    #saveFile(output_dir, filename, img_args, x, y)
    return True


def copyFile(output_dir1, filename1):
    shutil.copy(output_dir1, filename1)


async def combineTypes(FileLocations):
    result = []
    FullArray = []
    currentID = 0
    for genType in FileLocations:
        thisGlob = sorted(glob.glob(genType["search"]), key=len)

        for currentItem in thisGlob:
            currentID = currentID + 1
            FullArray.append(
                {"id": currentID, "type": genType["type"], "path": currentItem, "image": genType["image"]})

    with open(outputDirectory, 'w') as output_file:
        json.dump(FullArray, output_file)

    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)

    newID = 0

    for currentFile in FullArray:
        newID = newID + 1
        strNewID = str(newID)

        with open(currentFile["path"], 'r') as infile:
            thisJson = json.load(infile)

            #external_url = thisJson['external_url']
            theID = (currentFile["path"].rsplit('/', 1))[1]
            theID = (theID.rsplit('\\', 1))[1]
            theID = (theID.rsplit('.', 1))[0]

            thisJson["attributes"][0]["value"] = "Monster"
            thisJson["description"] = mintDescription
            thisJson["name"] = "#" + strNewID
            thisJson["external_url"] = mintExternal_url
            thisJson["image"] = mintImagePrefix + \
                strNewID + ".png"
            # del thisJson['combination']
            # del thisJson["attributes"][0]
            finalJSON = json.dumps(thisJson, indent=4)

            print(currentFile["path"])

            with open('src/output/TMC-Rename/json/' + strNewID + '.json', 'w') as output_file:
                output_file.write(finalJSON)

    # newID = 0

    # for currentFile in FullArray:
    #     newID = newID + 1
    #     theID = 0

    #     theID = (currentFile["path"].rsplit('/', 1))[1]
    #     theID = (theID.rsplit('\\', 1))[1]
    #     theID = (theID.rsplit('.', 1))[0]

    #     # with open(currentFile["path"], 'r') as infile:
    #     #     thisJson = json.load(infile)
    #     #     external_url = thisJson['external_url']
    #     #     theID = (external_url.rsplit('/', 1))[1]
    #     await runCopy(currentFile["image"] + "/" + str(theID) + ".png", "src/output/TMC-Rename/images" + "/" + str(newID) + ".png")

#allthefiles = glob.glob("src/output/xMartiansMale.20211111005517/json/*.json")

FileLocations = [
    {
        "type": "Monster",
        "image": "src/output/TMC-Rename/images",
        "search": "src/output/TMC-Rename/json rename/*.json"
    }]

asyncio.run(combineTypes(FileLocations))
