DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

DYNAMO_CLIENT.scan(
    FilterExpression= username + " = :u AND password = :p", # username is user-controlled
    ExpressionAttributeValues={
        ":u": { 'S': username },
        ":p": { 'S': password }
     },
    ProjectionExpression="username, password",
    TableName="users"
) # Noncompliant