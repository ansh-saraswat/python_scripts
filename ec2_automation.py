import boto3
import datetime

ec2 = boto3.client('ec2')

def start_instances(instances):
    if instances:
        print(f"Starting instances: {instances}")
        ec2.start_instances(InstanceIds=instances)
    else:
        print("No instances to start.")

def stop_instances(instances):
    if instances:
        print(f"Stopping instances: {instances}")
        ec2.stop_instances(InstanceIds=instances)
    else:
        print("No instances to stop.")

def lambda_handler(event, context):
    # Define the time you want to start and stop instances (for example, 8 AM for start, 8 PM for stop)
    current_time = datetime.datetime.now().strftime("%H:%M")
    
    # Example times (you can modify this to suit your needs)
    start_time = "08:00"
    stop_time = "20:00"
    
    # List of EC2 instance IDs to manage
    instances = [
        'i-1234567890abcdef0',  # Replace with your EC2 instance IDs
        'i-0987654321fedcba0'
    ]
    
    if current_time == start_time:
        # Start instances
        start_instances(instances)
    
    elif current_time == stop_time:
        # Stop instances
        stop_instances(instances)
    
    return {
        'statusCode': 200,
        'body': 'Lambda function executed successfully.'
    }