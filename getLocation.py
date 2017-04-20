import requests

string = "서울 종로구 율곡로 99, 창덕궁 (와룡동)"
string = string.split(',')[0]
string_result = string.replace(" ","+")

req = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+string_result+"&components=country:KR&key=AIzaSyDGRr4l2jPpRuMztpopST44-ZzNUV_jVOw")
jsonData=req.json()
print(req.text)
print(jsonData["results"][0]["geometry"]["location"]["lng"],jsonData["results"][0]["geometry"]["location"]["lat"])

