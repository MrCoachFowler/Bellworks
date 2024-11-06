import pandas as pd

def getDataFramesFromURL(link):
    #use pandas to read data from doc
    return pd.read_html(link, encoding='utf-8')[0]

def createEmptyGrid(rowCount, colCount):
    resultGrid = []
    defaultRow = []
    for i in range(max(xCoords) + 1):
        defaultRow.append(' ')

    for i in range(max(yCoords)+ 1):
        resultGrid.append(defaultRow.copy()) #has to be a copy because of how python uses pointers for lists
    
    return resultGrid

link = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
dfs = getDataFramesFromURL(link)
#load data into three lists
xCoords = list(map(int, dfs[0].values.tolist()[1:]))
yCoords = list(map(int, dfs[2].values.tolist()[1:]))
chars = dfs[1].values.tolist()[1:]

resultGrid = createEmptyGrid(max(yCoords), max(xCoords))

#fill in the spots that need characters
for i in range(len(chars)):
    x = xCoords[i]
    y = yCoords[i]
    char = chars[i]
    resultGrid[y][x] = char

#print out image
for row in resultGrid:
    print(''.join(row))

