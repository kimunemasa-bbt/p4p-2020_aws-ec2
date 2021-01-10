## ライブラリインポート
import os
import boto3

## 環境変数
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
REGION_NAME = os.environ.get('REGION_NAME')
BUCKET = os.environ.get('BUCKET')

## S3 client(両方リソースにしたかったけどできなかった)
s3_cli = boto3.client('s3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY ,
    region_name=REGION_NAME
)

## S3 resource
s3_res = boto3.resource('s3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)

## S3からファイル名のリストを取得
def get_filename_from_s3():
    filenames = []
    bucket = s3_res.Bucket(BUCKET)
    for obj in bucket.objects.all():
        filenames.append(obj.key)
    return filenames

## S3からファイル名に紐づくタグのリストを取得
def get_tags_from_s3(filename):
    obj = s3_cli.get_object_tagging(Bucket=BUCKET,Key=filename)
    obj_tagset = obj['TagSet']
    tags = []
    for row in obj_tagset:
        if row['Key'] == 'element':
            tags = row['Value'].split('-')
    return tags
