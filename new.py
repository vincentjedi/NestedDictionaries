import psycopg2
from psycopg2 import sql
import uuid
from datetime import datetime

def flatten_events(data):
    flat_data = {}

    if isinstance(data, list):  # Handle lists
        for idx, item in enumerate(data):
            if isinstance(item, dict):  # Dictionary in a list
                flat_value = flatten_events(item)
                for subkey, subvalue in flat_value.items():
                    flat_data[f"[{idx}].{subkey}"] = subvalue
            else:  # Non-dictionary item in a list
                flat_data[f"[{idx}]"] = item

    elif isinstance(data, dict):  # Handle dictionaries
        for key, value in data.items():  # Iterate over key-value pairs
            if isinstance(value, dict):  # Nested dictionary
                flat_value = flatten_events(value)
                for subkey, subvalue in flat_value.items():
                    flat_data[f"{key}.{subkey}"] = subvalue

            elif isinstance(value, list):  # List as a value
                for idx, item in enumerate(value):
                    if isinstance(item, dict):  # Dictionary in a list
                        flat_value = flatten_events(item)
                        for subkey, subvalue in flat_value.items():
                            flat_data[f"{key}[{idx}].{subkey}"] = subvalue
                    else:  # Non-dictionary item in a list
                        flat_data[f"{key}[{idx}]"] = item

            else:  # Base case: value is neither dict nor list
                flat_data[key] = value

    return flat_data


def map_and_insert(flattened_data, table_name, db_connection, table_columns):
    """
    Maps flattened JSON keys to database columns and inserts the data.

    Args:
        flattened_data (dict): The flattened JSON data.
        table_name (str): The name of the database table.
        db_connection: Active database connection.
        table_columns (dict): Mapping of flattened JSON keys to table column names.
    """
    # Map keys to their corresponding database column names
    mapped_data = {table_columns[key]: value for key, value in flattened_data.items() if key in table_columns}

    # Extract columns and values
    columns = ', '.join([f'"{col}"' for col in mapped_data.keys()])
    placeholders = ', '.join(['%s'] * len(mapped_data))
    values = tuple(mapped_data.values())

    # SQL Insert statement
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql, values)
        db_connection.commit()
        print(f"Data inserted into {table_name} successfully")
    except Exception as e:
        print(f"Error inserting data into {table_name}: {e}")
        db_connection.rollback()

# Example usage
def main():
    # Example flattened JSON data for events
    flattened_event_data = {
        "id": str(uuid.uuid4()),
        "type": "alert",
        "name": "High CPU Usage",
        "severity": "critical",
        "when": datetime.utcnow(),
        "created_at": datetime.utcnow(),
        "source_info.ip": "192.168.1.1",
        "customer_id": str(uuid.uuid4()),
        "endpoint_id": str(uuid.uuid4()),
        "endpoint_type": "server",
        "user_id": "user123",
        "source": "monitoring_system",
        "location": "datacenter1",
        "group": "system_health"
    }

    # Example flattened JSON data for alerts
    flattened_alert_data = [{
        "id": str(uuid.uuid4()),
        "javaUUID": str(uuid.uuid4()),
        "actionable": True,
        "customer_id": str(uuid.uuid4()),
        "severity": "high",
        "when": datetime.utcnow(),
        "created_at": datetime.utcnow(),
        "description": "Memory usage exceeded threshold",
        "event_service_event_id": str(uuid.uuid4()),
        "location": "region-1",
        "data.created_at": 1672531200,
        "data.endpoint_id": str(uuid.uuid4()),
        "data.endpoint_java_id": str(uuid.uuid4()),
        "data.endpoint_platform": "Linux",
        "data.endpoint_type": "server",
        "data.event_service_id.type": 1,
        "data.event_service_id.data": "event_data",
        "data.inserted_at": 1672531300
    }]

    # Column mappings for `events` table
    events_columns = {
        "id": "event_id",
        "type": "event_type",
        "name": "event_name",
        "severity": "severity",
        "when": "when",
        "created_at": "created_at",
        "source_info.ip": "source_info_ip",
        "customer_id": "customer_id",
        "endpoint_id": "endpoint_id",
        "endpoint_type": "endpoint_type",
        "user_id": "user_id",
        "source": "source",
        "location": "location",
        "group": "event_group"
    }

    # Column mappings for `alerts` table
    alerts_columns = {
        "id": "alert_id",
        "javaUUID": "java_uuid",
        "actionable": "actionable",
        "customer_id": "customer_id",
        "severity": "severity",
        "when": "when",
        "created_at": "created_at",
        "description": "description",
        "event_service_event_id": "event_service_event_id",
        "location": "location",
        "data.created_at": "data_created_at",
        "data.endpoint_id": "data_endpoint_id",
        "data.endpoint_java_id": "data_endpoint_java_id",
        "data.endpoint_platform": "data_endpoint_platform",
        "data.endpoint_type": "data_endpoint_type",
        "data.event_service_id.type": "data_event_service_id_type",
        "data.event_service_id.data": "data_event_service_id_data",
        "data.inserted_at": "data_inserted_at"
    }

    # Database connection
    db_connection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="vince123",
        database="testDb"
    )

    try:
        # Insert data into events table
        map_and_insert(flattened_event_data, "events", db_connection, events_columns)

        # Insert data into alerts table
        map_and_insert(flattened_alert_data, "alerts", db_connection, alerts_columns)
    
    finally:
        db_connection.close()

if __name__ == "__main__":
    main()

