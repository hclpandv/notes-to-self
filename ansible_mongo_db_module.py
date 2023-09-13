#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import json
import pymongo

def post_data_to_mongodb(db_name, collection_name, connection_string, json_data):
    """Upsert data in MongoDB collection."""
    try:
        # Establish a connection to MongoDB
        client = pymongo.MongoClient(connection_string)
        db = client[db_name]
        collection = db[collection_name]
        # Use "id" as the query filter
        query_filter = {"id": json_data["id"]}

        # Use "$set" to update existing fields or insert a new document if not found
        result = collection.update_one(query_filter, {"$set": json_data}, upsert=True)

        return "Upserted document with _id {}".format(result.upserted_id)
    except Exception as e:
        raise Exception("Failed to upsert data into mongodb collection: {}".format(e))
    finally:
        # Close the MongoDB client connection when done
        client.close()

def main():
    '''Main def to invoke ansible module'''
    arguments = dict(
            db_name=dict(required=True),
            collection_name=dict(required=True),
            connection_string=dict(required=True),
            json_data=dict(required=True)
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=arguments,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(changed=True)

    
    result['original_message'] = post_data_to_mongodb(
        db_name=module.params['db_name'],
        collection_name=module.params['collection_name'],
        connection_string=module.params['connection_string'],
        json_data=json.loads(module.params['json_data'])
    )
    
    result['message'] = 'Upsert data into mongodb collection'

    # OUTPUT
    module.exit_json(**result)


if __name__ == '__main__':
    main()
