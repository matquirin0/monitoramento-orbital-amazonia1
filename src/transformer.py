from datetime import datetime, timezone

def transform_pass_data(raw_passes, norad_id, ground_station_id):
    transformed_list = []

    for p in raw_passes:
        start_dt = datetime.fromtimestamp(p['startUTC'], tz=timezone.utc)
        end_dt = datetime.fromtimestamp(p['endUTC'], tz=timezone.utc)

        duration = (end_dt - start_dt).total_seconds()

        data_clean = {
            "id_norad": norad_id,
            "id_gs": ground_station_id,
            "start_utc": start_dt.isoformat(),
            "end_utc": end_dt.isoformat(),
            "max_elevation": p['maxEl'],
            "duration_seconds": int(duration)
        }

        transformed_list.append(data_clean)

    return transformed_list

if __name__ == "__main__":
    mock_raw = [{"startUTC": 1772370860, "endUTC": 1772371730, "maxEl": 66.74}]
    result = transform_pass_data(mock_raw, 47699, 1)
    print(f"Dados prontos para o SQL: {result[0]}")