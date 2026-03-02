from src.extractor import fetch_radio_passes
from src.transformer import transform_pass_data
from src.database import insert_passes

def run_pipeline():
    # 1. Configurações Iniciais (Amazonia-1 e Estação SJC)
    NORAD_ID = 47699
    LAT, LNG, ALT = -23.1615, -45.7953, 600
    GROUND_STATION_ID = 1

    print("--- INICIANDO MONITORAMENTO ORBITAL AMAZONIA-1 ---")

    # 2. Extração
    raw_data = fetch_radio_passes(NORAD_ID, LAT, LNG, ALT)

    if not raw_data:
        print("[ABORTAR] Falha na extração dos dados.")
        return

    # 3. Transformação
    clean_data = transform_pass_data(raw_data, NORAD_ID, GROUND_STATION_ID)

    # 4. Carga no Banco de Dados
    insert_passes(clean_data)

    print("--- PROCESSO CONCLUÍDO COM SUCESSO ---")

if __name__ == "__main__":
    run_pipeline()