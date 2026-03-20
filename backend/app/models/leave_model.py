from app.db import db
from bson.objectid import ObjectId
import datetime

class Leave:
    collection = db.leaves

    @staticmethod
    def create_leave(employee_id, leave_type, start_date, end_date, reason):
        leave_data = {
            "employee_id": ObjectId(employee_id),
            "leave_type": leave_type,
            "start_date": start_date,
            "end_date": end_date,
            "reason": reason,
            "status": "Pending",
            "created_at": datetime.datetime.utcnow()
        }
        return Leave.collection.insert_one(leave_data)

    @staticmethod
    def get_leaves_by_employee(employee_id):
        leaves = list(Leave.collection.find({"employee_id": ObjectId(employee_id)}).sort("created_at", -1))
        # Convert ObjectId to string for JSON serialization
        for leave in leaves:
            leave['_id'] = str(leave['_id'])
            leave['employee_id'] = str(leave['employee_id'])
        return leaves

    @staticmethod
    def get_all_leaves():
        pipeline = [
            {
                "$lookup": {
                    "from": "users",
                    "localField": "employee_id",
                    "foreignField": "_id",
                    "as": "employee_details"
                }
            },
            {
                "$unwind": "$employee_details"
            },
            {
                "$project": {
                    "_id": {"$toString": "$_id"},
                    "employee_id": {"$toString": "$employee_id"},
                    "employee_name": "$employee_details.name",
                    "employee_email": "$employee_details.email",
                    "leave_type": 1,
                    "start_date": 1,
                    "end_date": 1,
                    "reason": 1,
                    "status": 1,
                    "created_at": 1
                }
            },
            {
                "$sort": {"created_at": -1}
            }
        ]
        return list(Leave.collection.aggregate(pipeline))

    @staticmethod
    def update_leave_status(leave_id, status):
        return Leave.collection.update_one(
            {"_id": ObjectId(leave_id)},
            {"$set": {"status": status}}
        )
