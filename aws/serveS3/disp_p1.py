import boto3
import mimetypes
from flask import Flask, Response
from botocore.exceptions import NoCredentialsError
import os 
app = Flask(__name__)
s3 = boto3.client('s3')

@app.route('/<path:path>', methods=['GET'])
def serve_from_s3(path='/index.html'):
    bucket_name = os.environ['S3_BUCKET']  # Use the Flask config here
    s3_prefix = os.environ['S3_DIR']
    print(bucket_name,s3_prefix)
    print(path)
    try:
        s3_file = s3.get_object(Bucket=bucket_name, Key=s3_prefix + path)
    except NoCredentialsError:
        return 'No AWS credentials found', 500
    except Exception as e:
        return 'Error in getting file {}: {}'.format(path, e), 500

    # Guess the mimetype of the file
    mimetype, _ = mimetypes.guess_type(path)

    return Response(
        s3_file['Body'].read(),
        mimetype=mimetype,  # use the guessed mimetype
        headers={"Content-Disposition": "inline;filename={}".format(path)}
    )

if __name__ == '__main__':
    app.run()
