import sys
import requests
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient

class UserData:
    def __init__(self, phone, cities):
        self.phone = phone
        self.cities = cities

users = [ UserData("+15197814487", [ 106, 107, 548 ]) ]
cities = { 508: "Abbotsford", 81: "Ajax", 335: "Alliston", 336: "Ancaster", 91: "Aurora", 243: "Barrie", 323: "Belleville", 559: "Blainville", 94: "Bolton", 562: "Boucherville", 77: "Bowmanville", 401: "Bracebridge - Huntsville", 536: "Bradford", 346: "Brampton", 512: "Brandon", 135: "Brantford", 325: "Brockville", 555: "Brossard", 103: "Burlington", 566: "Burnaby", 342: "Caledon", 119: "Calgary", 105: "Cambridge", 506: "Campbell River", 533: "Carleton Place", 573: "Charlottetown", 339: "Chatham", 504: "Chilliwack", 570: "Clarenville", 74: "Cobourg", 88: "Collingwood", 572: "Conception Bay South", 577: "Coquitlam", 525: "Corner Brook", 338: "Cornwall", 505: "Courtenay", 78: "Courtice", 513: "Dauphin", 576: "Delta", 490: "Drummondville", 488: "Dryden", 120: "Edmonton", 486: "Elliot Lake", 111: "Etobicoke", 541: "Exeter", 539: "Fergus", 327: "Fort McMurray", 499: "Fredericton", 494: "Gananoque", 523: "Gander", 518: "Gatineau", 531: "Gloucester", 398: "Goderich", 491: "Granby", 501: "Grande Prairie", 400: "Gravenhurst", 553: "Grimsby", 104: "Guelph", 496: "Halifax", 115: "Hamilton", 569: "Hope", 548: "Ingersoll", 121: "Kamloops", 87: "Kanata", 489: "Kapuskasing", 122: "Kelowna", 517: "Kemptville", 487: "Kenora", 334: "Keswick", 544: "Kincardine", 324: "Kingston", 550: "Kirkland Lake", 106: "Kitchener", 575: "Langley", 561: "Lasalle", 556: "Laval", 337: "Leamington", 502: "Lethbridge", 333: "Lindsay", 546: "Listowel", 509: "Lloydminster", 116: "London", 557: "Longueuil", 579: "Maple Ridge", 134: "Markham", 542: "Meaford", 480: "Medicine Hat", 484: "Midland", 483: "Milton", 101: "Mississauga", 497: "Moncton", 244: "Montreal", 510: "Moose Jaw", 507: "Nanaimo", 493: "Napanee", 530: "Nepean", 520: "New Glasgow", 549: "New Liskeard", 332: "Newcastle", 344: "Newmarket", 302: "Niagara Falls", 431: "North Bay", 567: "North Vancouver", 102: "Oakville", 96: "Orangeville", 89: "Orillia", 532: "Orleans", 79: "Oshawa", 86: "Ottawa", 399: "Owen Sound", 404: "Parry Sound", 485: "Pembroke", 515: "Perth", 85: "Peterborough", 82: "Pickering", 554: "Picton", 552: "Port Colborne", 545: "Port Elgin", 75: "Port Hope", 568: "Port Moody", 84: "Port Perry", 516: "Prescott", 511: "Prince Albert", 500: "Prince George BC", 482: "Quebec City", 503: "Red Deer", 326: "Regina", 558: "Repentigny", 564: "Richmond", 92: "Richmond Hill", 498: "Saint John NB", 563: "Salaberry de valleyfield", 305: "Sarnia", 118: "Saskatoon", 306: "Sault Ste Marie", 519: "Shawinigan", 537: "Shelburne", 492: "Sherbrooke", 397: "Simcoe", 534: "Smiths Falls", 341: "St Thomas", 114: "St. Catharines", 524: "St. John's", 514: "Steinbach", 529: "Stittsville", 109: "Stoney Creek", 535: "Stouffville", 303: "Stratford", 540: "Strathroy", 307: "Sudbury", 574: "Summerside", 578: "Surrey", 522: "Sydney", 99: "Thunder Bay", 547: "Tillsonburg", 402: "Timmins", 133: "Toronto", 538: "Tottenham", 322: "Trenton", 83: "Uxbridge", 123: "Vancouver", 560: "Vaudreuil Dorion", 343: "Vaughan", 481: "Victoria", 107: "Waterloo", 551: "Welland", 80: "Whitby", 565: "White Rock", 304: "Windsor", 117: "Winnipeg", 340: "Woodstock", 521: "Yarmouth", 571: "Yellowknife" }

no_change = "no-change-sm.gif"
up_arrow = "gas_arrow_up.gif"
down_arrow = "gas_arrow_down.gif"

twilio_account_sid = "AC56f76406464bdf0381ab5b11e9f0e45a"
twilio_auth_token = "ab5fa7999704722f4d4ab585c39f4cc5"
twilio_from = "+15198005665"

def send_sms(to, body):
    client = TwilioRestClient(twilio_account_sid, twilio_auth_token)
    message = client.sms.messages.create(body=body, to=to, from_=twilio_from)

def get_content(url):
    session = requests.session()
    req = session.get(url)
    return req.content

def get_price(document):
    current_element = document.find(id="gas-info-span")
    current_element_text = current_element.get_text().strip()
    arrow_element = document.find(id="gas-info-arrow")
    image_element = arrow_element.img
    image_element_src = image_element.get('src')
    
    if image_element_src.endswith(no_change):
        return current_element_text + " no change"
    
    if image_element_src.endswith(up_arrow):
        arrow_direction = "up"
    elif image_element_src.endswith(down_arrow):
        arrow_direction = "down"
    else:
        return current_element_text + " unknown"
    
    difference_element = document.find(id="gas-info-span1")
    difference_element_text = difference_element.get_text().strip()
    
    return current_element_text + " " + arrow_direction + " " + difference_element_text

def main():
    for user in users:
        prices = []
        for city in user.cities:
            content = get_content('http://tomorrowsgaspricetoday.com/gas-prices/?city=' + str(city))
            doc = BeautifulSoup(content)
            prices.append(cities[city] + ': ' + get_price(doc))
        
        send_sms(user.phone, "; ".join(prices))

if __name__ == "__main__":
    main()
