import boto3


def lambda_handler(event):
    if event == " ":
        print("No data found")
    else:
        name = event['Name']
        age = event['Age']
    return add(name, age)


def add(name, age):
    dynamodb = boto3.resource('dynamodb')
    try:
        print('inside try block')
        dynamoTable = dynamodb.Table('test')
        dynamoTable.put_item(
            Item={
                'Name': name, 'Age': age
            }
        )
        return "added"
    except Exception as e:
        print("Oops!", e, "occurred.")
