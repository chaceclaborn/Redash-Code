# data_organizer.py
import redash_api

def organize_query_data(query_id):
    """Organizes data from a Redash query into columns."""
    data = redash_api.fetch_query_results(query_id)
    if data is None:
        return

    columns = {}
    if data:
        for key in data[0].keys():
            columns[key] = []
        for row in data:
            for key in row:
                columns[key].append(row[key])

    return columns
