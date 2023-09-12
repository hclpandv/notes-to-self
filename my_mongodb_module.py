#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import pymongo
import os

def upsert_movie_data(db_name, collection_name, json_data, connection_string):
    try:
        client = pymongo.MongoClient(connection_string)
        db = client[db_name]
        collection = db[collection_name]

        query_filter = {"id": json_data["id"]}

        result = collection.update_one(query_filter, {"$set": json_data}, upsert=True)

        if result.matched_count > 0:
            return True, f"Updated document with _id {result.upserted_id}"
        else:
            return True, f"Inserted new document with _id {result.upserted_id}"

    except Exception as e:
        return False, str(e)
    finally:
        client.close()

def main():
    module = AnsibleModule(
        argument_spec=dict(
            db_name=dict(required=True, type='str'),
            collection_name=dict(required=True, type='str'),
            json_data=dict(required=True, type='dict'),
            connection_string=dict(required=True, type='str')
        )
    )

    db_name = module.params['db_name']
    collection_name = module.params['collection_name']
    json_data = module.params['json_data']
    connection_string = module.params['connection_string']

    success, msg = upsert_movie_data(db_name, collection_name, json_data, connection_string)

    if success:
        module.exit_json(changed=True, msg=msg)
    else:
        module.fail_json(msg=msg)

if __name__ == '__main__':
    main()
