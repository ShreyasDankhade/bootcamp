import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to ISO format string
        return super().default(obj)

def serialize_with_custom_encoder(obj):
    return json.dumps(obj, cls=DateTimeEncoder)

now = datetime.now()
json_data = serialize_with_custom_encoder(now)
print(json_data)
