import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("N2YO_API_KEY")
BASE_URL = "https://api.n2yo.com/rest/v1/satellite"

def fetch_radio_passes(norad_id, lat, lng, alt=0, days=2, min_elevation=10):
    endpoint = f"{BASE_URL}/radiopasses/{norad_id}/{lat}/{lng}/{alt}/{days}/{min_elevation}/&apiKey={API_KEY}"

    try:
        print(f"[INFO] Solicitando dados para o satélite {norad_id}...")
        response = requests.get(endpoint)
        response.raise_for_status()

        data = response.json()


        if data.get("info", {}).get("passescount", 0) > 0:
            print(f"[SUCCESS] {data['info']['passescount']} passagens encontradas!")
            return data.get("passes", [])
        else:
            print("[WARNING] Nenhuma passagem encontrada para os critérios atuais.")
            return []

    except Exception as e:
        print(f"[ERROR] Falha na extração: {e}")
        return None

if __name__ == "__main__":
    passes = fetch_radio_passes(47699, -23.1615, -45.7953, 600)
    if passes:
        print(f"Primeira passagem começa em (Unix): {passes[0]['startUTC']}")