import csv

fileObject = open('cartoons.csv', 'r', newline='', encoding='utf-8')
readerObject = csv.DictReader(fileObject)
cartoon = []
for row in readerObject:
    cartoon.append(row)
fileObject.close()

inputCharacterName = input("What's the name of the character? ")

found = False
for characterIndex in range(1, len(cartoon)):
    if inputCharacterName.lower() in cartoon[characterIndex]['name'].lower(): 
        found = True
        responseString = cartoon[characterIndex]['name'] + ' works for ' + cartoon[characterIndex]['company'] + '.'
        if cartoon[characterIndex]['nemesis'] != '':
            responseString += ' Its enemy is ' + cartoon[characterIndex]['nemesis']
        print(responseString)
if not found:
    print("Didn't find that character")