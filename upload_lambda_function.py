import boto3
import dotenv
import os
dotenv.load_dotenv()

# AWS 자격증명
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")  # AWS Access Key
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")  # AWS Secret Key
AWS_REGION = os.getenv("AWS_REGION")       # 리전 이름 (예: ap-southeast-2)

# Lambda 함수 이름 및 ZIP 파일 경로
LAMBDA_FUNCTION_NAME = "test_function"
ZIP_FILE_PATH = "lambda_function.zip"

# boto3 클라이언트 초기화
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION,
)

# Lambda 함수 업데이트
def update_lambda_function():
    try:
        # ZIP 파일 읽기
        with open(ZIP_FILE_PATH, "rb") as zip_file:
            zip_content = zip_file.read()

        # Lambda 함수 코드 업데이트
        response = lambda_client.update_function_code(
            FunctionName=LAMBDA_FUNCTION_NAME,
            ZipFile=zip_content,
            Publish=True
        )

        print(f"Lambda 함수 업데이트 성공: {response['FunctionArn']}")
    except Exception as e:
        print(f"Lambda 함수 업데이트 중 오류 발생: {str(e)}")

# 실행
if __name__ == "__main__":
    update_lambda_function()
