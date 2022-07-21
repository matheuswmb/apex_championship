import http.client

conn = http.client.HTTPSConnection("d14eb5sje6oeoy.cloudfront.net")

payload = ""

headers = {
    'authority': "d14eb5sje6oeoy.cloudfront.net",
    'accept': "application/json, text/plain, */*",
    'accept-language': "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    'if-none-match': "W/^\^135d7-PN9v46QjxTO6PETATjgS32shOow^^",
    'origin': "https://battlefy.com",
    'referer': "https://battlefy.com/",
    'sec-ch-ua': "^\^Chromium^^;v=^\^102^^, ^\^Opera"
    }

conn.request("GET", "/views/apex-legends/global-series-season-2/double-elim/viewer-match?structureID=62bdca906c9865391486038f&roundNumber=2&matchNumber=3&disableSnapshot=true", payload, headers)

res = conn.getresponse()
data = res.read()

with open('Apex_Championship', 'w') as file:
    file.write(data.decode("utf'8"))
