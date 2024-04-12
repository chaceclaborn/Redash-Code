# main.py
import data_organizer


def main():
    query_id = input("Enter the query ID: ")
    organized_data = data_organizer.organize_query_data(query_id)

    if organized_data:
        for column_name, column_data in organized_data.items():
            print(f"Column: {column_name}, Data: {column_data}")


if __name__ == "__main__":
    main()
