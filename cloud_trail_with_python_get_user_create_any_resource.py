# import boto3

# def print_users_who_created_services():
#     # Initialize the CloudTrail client
#     cloudtrail_client = boto3.client('cloudtrail', region_name='us-east-1')

#     # Get the events for service creation
#     response = cloudtrail_client.lookup_events(
#         LookupAttributes=[
#             {'AttributeKey': 'EventName', 'AttributeValue': 'CreateService'}
#         ]
#     )

#     # Create a set to store unique usernames
#     user_set = set('krishna')

#     # Process the events and extract the username
#     for event in response['Events']:
#         event_username = event['Username']
#         user_set.add(event_username)

#     # Print the usernames
#     if user_set:
#         print("Users who created services:")
#         for username in user_set:
#             print(username)
#     else:
#         print("No service creation events found.")

# # Call the function to print the users who created services
# print_users_who_created_services()
import boto3
import datetime,json
client=boto3.client('cloudtrail',region_name='us-east-1')
start_time = datetime.datetime(2023, 7, 12, 0, 0, 0)
end_time = datetime.datetime(2023, 7, 12, 23, 0, 0)
response = client.lookup_events(
    StartTime=start_time,
    EndTime=end_time
)
for i in response['Events']:
    # print("cloud trail event: ",i['CloudTrailEvent'],end='')
    # print()
    # for j in i['CloudTrailEvent']:
    #     print(j['eventVersion'])
    # events = i.get('CloudTrailEvent', [])
    if 'Username' in i:
        print("UserName=",i['Username'])
        json_data=json.dumps(i['CloudTrailEvent'])
        data = json.loads(json_data)
        # data1=str(data)
        # print(data1)
        s1=f''' {data}'''
        data1 = json.loads(s1)

# Print each key-value pair
        print('UserARN: ',data1['userIdentity']['arn'],"|","eventSource: ", data1['eventSource'])
        print("eventName: ", data1['eventName'],'|',"eventTime: ",data1['eventTime'])
        # for key, value in data1.items():
        #     print(f"{key}: {value}")
        print("========================================")
# print(response)
# events = response.get('Events', [])
# for event in events:
#     event_dict = event.get('CloudTrailEvent', {})
#     print(event_dict.get('eventVersion'))
####Second Program
import boto3

def print_created_services():
    # Initialize the CloudTrail client
    cloudtrail_client = boto3.client('cloudtrail', region_name='us-east-1')

    # Get the events for service creation
    response = cloudtrail_client.lookup_events(
        LookupAttributes=[{'AttributeKey': 'EventName', 'AttributeValue': 'CreateService'}]
    )

    # Process the events and print the created services and users
    for event in response['Events']:
        event_username = event['Username']
        resources = event['Resources']
        for resource in resources:
            service_name = resource['ResourceName']
            print(f"User {event_username} created the {service_name} service")

# Call the function to print the created services and users
print_created_services()
