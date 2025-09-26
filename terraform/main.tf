
provider "aws" {
  alias  = "useast1"
  region = "us-east-1"
}

# SNS Topic (us-east-1)
resource "aws_sns_topic" "alarm_topic_useast" {
  provider = aws.useast1
  name     = "cloudwatch-alarm-topic-useast"
}

# IAM Role for Lambda (us-east-1)
resource "aws_iam_role" "lambda_exec" {
  provider = aws.useast1
  name     = "lambda_exec_role_useast"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# IAM Policies (us-east-1)
resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  provider   = aws.useast1
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "lambda_s3" {
  provider   = aws.useast1
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}

# Lambda Function (us-east-1)
resource "aws_lambda_function" "alert_handler" {
  provider        = aws.useast1
  function_name   = "route53_alert_handler"
  timeout         = 15 
  role            = aws_iam_role.lambda_exec.arn
  runtime         = "python3.10"
  handler         = "index.handler"
  filename        = "lambda.zip"
  source_code_hash = filebase64sha256("lambda.zip")

   environment {
    variables = {
      WEBHOOK_URL    = var.webhook_url
      VMWARE_API     = var.vmware_api
      EC2_BACKUP_API = var.ec2_backup_api
    }
  }
}

# SNS → Lambda (us-east-1)
resource "aws_sns_topic_subscription" "lambda_subscription" {
  provider = aws.useast1
  topic_arn = aws_sns_topic.alarm_topic_useast.arn
  protocol  = "lambda"
  endpoint  = aws_lambda_function.alert_handler.arn
}

resource "aws_lambda_permission" "allow_sns_invoke" {
  provider      = aws.useast1
  statement_id  = "AllowExecutionFromSNS"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.alert_handler.function_name
  principal     = "sns.amazonaws.com"
  source_arn    = aws_sns_topic.alarm_topic_useast.arn
}






# Log Group (us-east-1)
resource "aws_cloudwatch_log_group" "lambda_log_group" {
  provider          = aws.useast1
  name              = "/aws/lambda/${aws_lambda_function.alert_handler.function_name}"
  retention_in_days = 14
}
