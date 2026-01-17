import json

lien_callout_custom = "Fichier test/callout.json"
lien_callout_standard = "callout_standard.json"
liste_lien = [lien_callout_custom, lien_callout_standard]

def aux_get_callouts(lien):
    with open(lien, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data["callouts"]["custom"]
    
    
    
def get_callouts():
    callouts = []
    for lien in liste_lien:
        callouts.extend(aux_get_callouts(lien))
    return callouts

def get_callout_json(callout_name):
    for lien in liste_lien:
        with open(lien, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if callout_name in data["callouts"]["custom"]:
                return data["callouts"]["settings"][callout_name]       

def get_callout_icon(callout_name):
    callout = get_callout_json(callout_name)
    if callout:
        return callout.get("icon")
    return None

def get_callout_color(callout_name):
    callout = get_callout_json(callout_name)
    if callout:
        return callout.get("color")
    return None

print(get_callouts())