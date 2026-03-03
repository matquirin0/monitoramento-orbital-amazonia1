import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from src.database import get_engine

def generate_elevation_chart():
    """
    Busca dados do banco e gera um relatório gráfico na pasta 'reports/'.
    """
    try:

        engine = get_engine()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(current_dir)
        folder_name = os.path.join(root_dir, 'docs', 'assets', 'reports')
        os.makedirs(folder_name, exist_ok=True)

        query = """
            SELECT DISTINCT ON (start_utc) start_utc, max_elevation
            FROM pass_predictions
            WHERE start_utc >= NOW()
            ORDER BY start_utc ASC
            LIMIT 7;
        """
        df = pd.read_sql(query, engine)

        if df.empty:
            print("[VISUALIZER] Nenhum dado encontrado no banco para gerar o gráfico.")
            return

        agora = datetime.now()
        timestamp_titulo = agora.strftime('%d/%m/%Y %H:%M:%S')
        timestamp_arquivo = agora.strftime('%Y%m%d_%H%M')

        total_records = len(df)

        df['label'] = df['start_utc'].dt.strftime('%d/%m\n%H:%M')

        plt.figure(figsize=(12, 7))
        bars = plt.bar(df['label'], df['max_elevation'], color='#1f77b4', alpha=0.8)

        plt.title(f'Monitoramento Amazonia-1: Lote de {total_records} Passagens\nRelatório gerado em: {timestamp_titulo}',
                  fontsize=12, pad=20)

        plt.ylabel('Elevação Máxima (Graus)')
        plt.xlabel('Janelas de Passagem (SJC)')
        plt.ylim(0, 100)
        plt.grid(axis='y', linestyle='--', alpha=0.6)

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval}°",
                     ha='center', va='bottom', fontsize=9, fontweight='bold')

        plt.tight_layout()

        filename = f'{folder_name}/monitoramento_{timestamp_arquivo}.png'
        plt.savefig(filename)
        print(f"[VISUALIZER] Sucesso! Relatório gerado em: {filename}")


    except Exception as e:
        print(f"[VISUALIZER ERROR] Falha ao processar visualização: {e}")

if __name__ == "__main__":
    generate_elevation_chart()