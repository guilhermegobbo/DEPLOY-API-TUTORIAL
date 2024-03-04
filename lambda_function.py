import pandas as pd
import json

def get_results(name, age):
    
    results = pd.read_csv('./INFORMATIONS.csv')
    results = results[(results['Name'] == name) & (results['Age'] == age)]

    return results
        
    
def lambda_handler(event, context):
    try:
        path_parameters = event['pathParameters']['proxy'].split('/')
        
        name = path_parameters[0] if len(path_parameters) > 0 else 0
        age = int(path_parameters[1]) if len(path_parameters) > 1 else 0

        results = get_results(name, age)

        json_data_combined = {
            'Name': results['Name'].tolist(),
            'Age': results['Age'].tolist(),
            'Sex': results['Sex'].tolist(),
            'City': results['City'].tolist(),
            'Income Per Year (USD)': results['Income Per Year (USD)'].tolist()
        }

        response = {
            'statusCode': 200,
            'body': json.dumps(json_data_combined),
            'headers': {
                'Content-Type': 'application/json',
            }
        }

    except Exception as e:
        response = {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
            }
        }

    return response

