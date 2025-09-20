import xml.etree.ElementTree as ET
import pandas as pd

# helper function to safely get text and strip whitespace
def safe_text(elem, tag):
    child = elem.find(tag)
    if child is not None and child.text is not None:
        text = child.text.strip()
        return text if text != '' else ''
    return ''

cols = ["modelName", "txdName", "gameName", "vehicleMakeName", "audioNameHash"]
rows = []

xmlparse = ET.parse('vehicles.meta')  # replace with your actual file name/path
root = xmlparse.getroot()

for item in root.findall('.//InitDatas/Item'):
    modelName = safe_text(item, "modelName")
    txdName = safe_text(item, "txdName")
    gameName = safe_text(item, "gameName")
    vehicleMakeName = safe_text(item, "vehicleMakeName")
    audioNameHash = safe_text(item, "audioNameHash")

    rows.append({
        "modelName": modelName,
        "txdName": txdName,
        "gameName": gameName,
        "vehicleMakeName": vehicleMakeName,
        "audioNameHash": audioNameHash            
    })

df = pd.DataFrame(rows, columns=cols)

# remove any remaining leading/trailing whitespace
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

df.to_csv('output.csv', index=False, encoding='utf-8')

print("Extraction Complete")
