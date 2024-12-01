import boto3

ec2 = boto3.client('ec2')

def get_ec2_ips():
    response = ec2.describe_instances()
    ip_addresses = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            private_ip = instance.get('PrivateIpAddress', 'No private IP')
            public_ip = instance.get('PublicIpAddress', 'No public IP')

            ip_addresses.append({
                'InstanceId': instance['InstanceId'],
                'PrivateIp': private_ip,
                'PublicIp': public_ip
            })

    return ip_addresses

ips = get_ec2_ips()

for ip in ips:
    print(f"Instance ID: {ip['InstanceId']}, Private IP: {ip['PrivateIp']}, Public IP: {ip['PublicIp']}")
