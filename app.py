from embedchain import Pipeline as App
from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify
import requests
import os
load_dotenv()
app = Flask(__name__)

os.environ['OPENAI_API_KEY'] = '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'

config = {
    'app': {
        'config': {
            'id': 'kahayfaqeerai'
        }
    }
}
 
kahayfaqeerai = App.from_config(config=config)
urls_to_add= [
"https://kahayfaqeer.ai/book1Data/book1Data/page/24",
"https://kahayfaqeer.ai/book1Data/book1Data/page/25",
"https://kahayfaqeer.ai/book1Data/book1Data/page/26",
"https://kahayfaqeer.ai/book1Data/book1Data/page/27",
"https://kahayfaqeer.ai/book1Data/book1Data/page/28",
"https://kahayfaqeer.ai/book1Data/book1Data/page/29",
"https://kahayfaqeer.ai/book1Data/book1Data/page/30",
"https://kahayfaqeer.ai/book1Data/book1Data/page/31",
"https://kahayfaqeer.ai/book1Data/book1Data/page/32",
"https://kahayfaqeer.ai/book1Data/book1Data/page/33",
"https://kahayfaqeer.ai/book1Data/book1Data/page/34",
"https://kahayfaqeer.ai/book1Data/book1Data/page/35",
"https://kahayfaqeer.ai/book1Data/book1Data/page/36",
"https://kahayfaqeer.ai/book1Data/book1Data/page/37",
"https://kahayfaqeer.ai/book1Data/book1Data/page/38",
"https://kahayfaqeer.ai/book1Data/book1Data/page/39",
"https://kahayfaqeer.ai/book1Data/book1Data/page/40",
"https://kahayfaqeer.ai/book1Data/book1Data/page/41",
"https://kahayfaqeer.ai/book1Data/book1Data/page/42",
"https://kahayfaqeer.ai/book1Data/book1Data/page/43",
"https://kahayfaqeer.ai/book1Data/book1Data/page/44",
"https://kahayfaqeer.ai/book1Data/book1Data/page/45",
"https://kahayfaqeer.ai/book1Data/book1Data/page/46",
"https://kahayfaqeer.ai/book1Data/book1Data/page/47",
"https://kahayfaqeer.ai/book1Data/book1Data/page/48",
"https://kahayfaqeer.ai/book1Data/book1Data/page/49",
"https://kahayfaqeer.ai/book1Data/book1Data/page/50",
"https://kahayfaqeer.ai/book1Data/book1Data/page/51",
"https://kahayfaqeer.ai/book1Data/book1Data/page/52",
"https://kahayfaqeer.ai/book1Data/book1Data/page/53",
"https://kahayfaqeer.ai/book1Data/book1Data/page/54",
"https://kahayfaqeer.ai/book1Data/book1Data/page/55",
"https://kahayfaqeer.ai/book1Data/book1Data/page/56",
"https://kahayfaqeer.ai/book1Data/book1Data/page/57",
"https://kahayfaqeer.ai/book1Data/book1Data/page/58",
"https://kahayfaqeer.ai/book1Data/book1Data/page/59",
"https://kahayfaqeer.ai/book1Data/book1Data/page/60",
"https://kahayfaqeer.ai/book1Data/book1Data/page/61",
"https://kahayfaqeer.ai/book1Data/book1Data/page/62",
"https://kahayfaqeer.ai/book1Data/book1Data/page/63",
"https://kahayfaqeer.ai/book1Data/book1Data/page/64",
"https://kahayfaqeer.ai/book1Data/book1Data/page/65",
"https://kahayfaqeer.ai/book1Data/book1Data/page/66",
"https://kahayfaqeer.ai/book1Data/book1Data/page/67",
"https://kahayfaqeer.ai/book1Data/book1Data/page/68",
"https://kahayfaqeer.ai/book1Data/book1Data/page/69",
"https://kahayfaqeer.ai/book1Data/book1Data/page/70",
"https://kahayfaqeer.ai/book1Data/book1Data/page/71",
"https://kahayfaqeer.ai/book1Data/book1Data/page/72",
"https://kahayfaqeer.ai/book1Data/book1Data/page/73",
"https://kahayfaqeer.ai/book1Data/book1Data/page/74",
"https://kahayfaqeer.ai/book1Data/book1Data/page/75",
"https://kahayfaqeer.ai/book1Data/book1Data/page/76",
"https://kahayfaqeer.ai/book1Data/book1Data/page/77",
"https://kahayfaqeer.ai/book1Data/book1Data/page/78",
"https://kahayfaqeer.ai/book1Data/book1Data/page/79",
"https://kahayfaqeer.ai/book1Data/book1Data/page/80",
"https://kahayfaqeer.ai/book1Data/book1Data/page/81",
"https://kahayfaqeer.ai/book1Data/book1Data/page/82",
"https://kahayfaqeer.ai/book1Data/book1Data/page/83",
"https://kahayfaqeer.ai/book1Data/book1Data/page/84",
"https://kahayfaqeer.ai/book1Data/book1Data/page/85",
"https://kahayfaqeer.ai/book1Data/book1Data/page/86",
"https://kahayfaqeer.ai/book1Data/book1Data/page/87",
"https://kahayfaqeer.ai/book1Data/book1Data/page/88",
"https://kahayfaqeer.ai/book1Data/book1Data/page/89",
"https://kahayfaqeer.ai/book1Data/book1Data/page/90",
"https://kahayfaqeer.ai/book1Data/book1Data/page/91",
"https://kahayfaqeer.ai/book1Data/book1Data/page/92",
"https://kahayfaqeer.ai/book1Data/book1Data/page/93",
"https://kahayfaqeer.ai/book1Data/book1Data/page/94",
"https://kahayfaqeer.ai/book1Data/book1Data/page/95",
"https://kahayfaqeer.ai/book1Data/book1Data/page/96",
"https://kahayfaqeer.ai/book1Data/book1Data/page/97",
"https://kahayfaqeer.ai/book1Data/book1Data/page/98",
"https://kahayfaqeer.ai/book1Data/book1Data/page/99",
"https://kahayfaqeer.ai/book1Data/book1Data/page/100",
"https://kahayfaqeer.ai/book1Data/book1Data/page/101",
"https://kahayfaqeer.ai/book1Data/book1Data/page/102",
"https://kahayfaqeer.ai/book1Data/book1Data/page/103",
"https://kahayfaqeer.ai/book1Data/book1Data/page/104",
"https://kahayfaqeer.ai/book1Data/book1Data/page/105",
"https://kahayfaqeer.ai/book1Data/book1Data/page/106",
"https://kahayfaqeer.ai/book1Data/book1Data/page/107",
"https://kahayfaqeer.ai/book1Data/book1Data/page/108",
"https://kahayfaqeer.ai/book1Data/book1Data/page/109",
"https://kahayfaqeer.ai/book1Data/book1Data/page/110",
"https://kahayfaqeer.ai/book1Data/book1Data/page/111",
"https://kahayfaqeer.ai/book1Data/book1Data/page/112",
"https://kahayfaqeer.ai/book1Data/book1Data/page/113",
"https://kahayfaqeer.ai/book1Data/book1Data/page/114",
"https://kahayfaqeer.ai/book1Data/book1Data/page/115",
"https://kahayfaqeer.ai/book1Data/book1Data/page/116",
"https://kahayfaqeer.ai/book1Data/book1Data/page/117",
"https://kahayfaqeer.ai/book1Data/book1Data/page/118",
"https://kahayfaqeer.ai/book1Data/book1Data/page/119",
"https://kahayfaqeer.ai/book1Data/book1Data/page/120",
"https://kahayfaqeer.ai/book1Data/book1Data/page/121",
"https://kahayfaqeer.ai/book1Data/book1Data/page/122",
"https://kahayfaqeer.ai/book1Data/book1Data/page/123",
"https://kahayfaqeer.ai/book1Data/book1Data/page/124",
"https://kahayfaqeer.ai/book1Data/book1Data/page/125",
"https://kahayfaqeer.ai/book1Data/book1Data/page/126",
"https://kahayfaqeer.ai/book1Data/book1Data/page/127",
"https://kahayfaqeer.ai/book1Data/book1Data/page/128",
"https://kahayfaqeer.ai/book1Data/book1Data/page/129",
"https://kahayfaqeer.ai/book1Data/book1Data/page/130",
"https://kahayfaqeer.ai/book1Data/book1Data/page/131",
"https://kahayfaqeer.ai/book1Data/book1Data/page/132",
"https://kahayfaqeer.ai/book1Data/book1Data/page/133",
"https://kahayfaqeer.ai/book1Data/book1Data/page/134",
"https://kahayfaqeer.ai/book1Data/book1Data/page/135",
"https://kahayfaqeer.ai/book1Data/book1Data/page/136",
"https://kahayfaqeer.ai/book1Data/book1Data/page/137",
"https://kahayfaqeer.ai/book1Data/book1Data/page/138",
"https://kahayfaqeer.ai/book1Data/book1Data/page/139",
"https://kahayfaqeer.ai/book1Data/book1Data/page/140",
"https://kahayfaqeer.ai/book1Data/book1Data/page/141",
"https://kahayfaqeer.ai/book1Data/book1Data/page/142",
"https://kahayfaqeer.ai/book1Data/book1Data/page/143",
"https://kahayfaqeer.ai/book1Data/book1Data/page/144",
"https://kahayfaqeer.ai/book1Data/book1Data/page/145",
"https://kahayfaqeer.ai/book1Data/book1Data/page/146",
"https://kahayfaqeer.ai/book1Data/book1Data/page/147",
"https://kahayfaqeer.ai/book1Data/book1Data/page/148",
"https://kahayfaqeer.ai/book1Data/book1Data/page/149",
"https://kahayfaqeer.ai/book1Data/book1Data/page/150",
"https://kahayfaqeer.ai/book1Data/book1Data/page/151",
"https://kahayfaqeer.ai/book1Data/book1Data/page/152",
"https://kahayfaqeer.ai/book1Data/book1Data/page/153",
"https://kahayfaqeer.ai/book1Data/book1Data/page/154",
"https://kahayfaqeer.ai/book1Data/book1Data/page/155",
"https://kahayfaqeer.ai/book1Data/book1Data/page/156",
"https://kahayfaqeer.ai/book1Data/book1Data/page/157",
"https://kahayfaqeer.ai/book1Data/book1Data/page/158",
"https://kahayfaqeer.ai/book1Data/book1Data/page/159",
"https://kahayfaqeer.ai/book1Data/book1Data/page/160",
"https://kahayfaqeer.ai/book1Data/book1Data/page/161",
"https://kahayfaqeer.ai/book1Data/book1Data/page/162",
"https://kahayfaqeer.ai/book1Data/book1Data/page/163",
"https://kahayfaqeer.ai/book1Data/book1Data/page/164",
"https://kahayfaqeer.ai/book1Data/book1Data/page/165",
"https://kahayfaqeer.ai/book1Data/book1Data/page/166",
"https://kahayfaqeer.ai/book1Data/book1Data/page/167",
"https://kahayfaqeer.ai/book1Data/book1Data/page/168",
"https://kahayfaqeer.ai/book1Data/book1Data/page/169",
"https://kahayfaqeer.ai/book1Data/book1Data/page/170",
"https://kahayfaqeer.ai/book1Data/book1Data/page/171",
"https://kahayfaqeer.ai/book1Data/book1Data/page/172",
"https://kahayfaqeer.ai/book1Data/book1Data/page/173",
"https://kahayfaqeer.ai/book1Data/book1Data/page/174",
"https://kahayfaqeer.ai/book1Data/book1Data/page/175",
"https://kahayfaqeer.ai/book1Data/book1Data/page/176",
"https://kahayfaqeer.ai/book1Data/book1Data/page/177",
"https://kahayfaqeer.ai/book1Data/book1Data/page/178",
"https://kahayfaqeer.ai/book1Data/book1Data/page/179",
"https://kahayfaqeer.ai/book1Data/book1Data/page/180",
"https://kahayfaqeer.ai/book1Data/book1Data/page/181",
"https://kahayfaqeer.ai/book1Data/book1Data/page/182",
"https://kahayfaqeer.ai/book1Data/book1Data/page/183",
"https://kahayfaqeer.ai/book1Data/book1Data/page/184",
"https://kahayfaqeer.ai/book1Data/book1Data/page/185",
"https://kahayfaqeer.ai/book1Data/book1Data/page/186",
"https://kahayfaqeer.ai/book1Data/book1Data/page/187",
"https://kahayfaqeer.ai/book1Data/book1Data/page/188",
"https://kahayfaqeer.ai/book1Data/book1Data/page/189",
"https://kahayfaqeer.ai/book1Data/book1Data/page/190",
"https://kahayfaqeer.ai/book1Data/book1Data/page/191",
"https://kahayfaqeer.ai/book1Data/book1Data/page/192",
"https://kahayfaqeer.ai/book1Data/book1Data/page/193",
"https://kahayfaqeer.ai/book1Data/book1Data/page/194",
"https://kahayfaqeer.ai/book1Data/book1Data/page/195",
"https://kahayfaqeer.ai/book1Data/book1Data/page/196",
"https://kahayfaqeer.ai/book1Data/book1Data/page/197",
"https://kahayfaqeer.ai/book1Data/book1Data/page/198",
"https://kahayfaqeer.ai/book1Data/book1Data/page/199",
"https://kahayfaqeer.ai/book1Data/book1Data/page/200",
"https://kahayfaqeer.ai/book1Data/book1Data/page/201",
"https://kahayfaqeer.ai/book1Data/book1Data/page/202",
"https://kahayfaqeer.ai/book1Data/book1Data/page/203",
"https://kahayfaqeer.ai/book1Data/book1Data/page/204",
"https://kahayfaqeer.ai/book1Data/book1Data/page/205",
"https://kahayfaqeer.ai/book1Data/book1Data/page/206",
"https://kahayfaqeer.ai/book1Data/book1Data/page/207",
"https://kahayfaqeer.ai/book1Data/book1Data/page/208",
"https://kahayfaqeer.ai/book1Data/book1Data/page/209",
"https://kahayfaqeer.ai/book1Data/book1Data/page/210",
"https://kahayfaqeer.ai/book1Data/book1Data/page/211",
"https://kahayfaqeer.ai/book1Data/book1Data/page/212",
"https://kahayfaqeer.ai/book1Data/book1Data/page/213",
"https://kahayfaqeer.ai/book1Data/book1Data/page/214",
"https://kahayfaqeer.ai/book1Data/book1Data/page/215",
"https://kahayfaqeer.ai/book1Data/book1Data/page/216",
"https://kahayfaqeer.ai/book1Data/book1Data/page/217",
"https://kahayfaqeer.ai/book1Data/book1Data/page/218",
"https://kahayfaqeer.ai/book1Data/book1Data/page/219",
"https://kahayfaqeer.ai/book1Data/book1Data/page/220",
"https://kahayfaqeer.ai/book1Data/book1Data/page/221",
"https://kahayfaqeer.ai/book1Data/book1Data/page/222",
"https://kahayfaqeer.ai/book1Data/book1Data/page/223",
"https://kahayfaqeer.ai/book1Data/book1Data/page/224",
"https://kahayfaqeer.ai/book1Data/book1Data/page/225",
"https://kahayfaqeer.ai/book1Data/book1Data/page/226",
"https://kahayfaqeer.ai/book1Data/book1Data/page/227",
"https://kahayfaqeer.ai/book1Data/book1Data/page/228",
"https://kahayfaqeer.ai/book1Data/book1Data/page/229",
"https://kahayfaqeer.ai/book1Data/book1Data/page/230",
"https://kahayfaqeer.ai/book1Data/book1Data/page/231",
"https://kahayfaqeer.ai/book1Data/book1Data/page/232",
"https://kahayfaqeer.ai/book1Data/book1Data/page/233",
"https://kahayfaqeer.ai/book1Data/book1Data/page/234",
"https://kahayfaqeer.ai/book1Data/book1Data/page/235",
"https://kahayfaqeer.ai/book1Data/book1Data/page/236",
"https://kahayfaqeer.ai/book1Data/book1Data/page/237",
"https://kahayfaqeer.ai/book1Data/book1Data/page/238",
"https://kahayfaqeer.ai/book1Data/book1Data/page/239",
"https://kahayfaqeer.ai/book1Data/book1Data/page/240",
"https://kahayfaqeer.ai/book1Data/book1Data/page/241",
"https://kahayfaqeer.ai/book1Data/book1Data/page/242",
"https://kahayfaqeer.ai/book1Data/book1Data/page/243",
"https://kahayfaqeer.ai/book1Data/book1Data/page/244",
"https://kahayfaqeer.ai/book1Data/book1Data/page/245",
"https://kahayfaqeer.ai/book1Data/book1Data/page/246",
"https://kahayfaqeer.ai/book1Data/book1Data/page/247",
"https://kahayfaqeer.ai/book1Data/book1Data/page/248",
"https://kahayfaqeer.ai/book1Data/book1Data/page/249",
]


# Function to check if a URL exists
def url_exists(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

# Add URLs to the pipeline only if they exist
for url in urls_to_add:
    if url_exists(url):
        kahayfaqeerai.add(url)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/conversations')
def conversation():
    return render_template('index.html')

@app.route('/chat/api/query', methods=['POST'])
def api_query():
    data = request.get_json()
    question = data.get('question', '')

    if question:
        answer, sources = kahayfaqeerai.query(f'You are an Urdu AI assistant and you will talk in urdu only, and your task is to answer our users\' questions, which is "{question}" according to our provided knowledge base', citations=True)

        return jsonify({'answer': answer, 'sources': sources[0][1]})
    else:
        return jsonify({'error': 'Invalid question'})

if __name__ == '__main__':
    app.run(debug=True)