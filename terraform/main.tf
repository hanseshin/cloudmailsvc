provider "aws" {
  region = "ap-northeast-2"
}

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
      WEBHOOK_URL    = "https://hooks.slack.com/services/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"
      VMWARE_API     = "http://125.179.40.152:5000/webhook/restore"
      EC2_BACKUP_API = "http://3.37.80.69:5000/webhook/backup"
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

resource "aws_cloudwatch_metric_alarm" "ec2_cpu_high" {
  provider            = aws.useast1
  alarm_name          = "EC2HighCPU"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = 60
  statistic           = "Average"
  threshold           = 70
  alarm_description   = "EC2 인스턴스 CPU 사용률 70% 초과"
  alarm_actions       = [aws_sns_topic.alarm_topic_useast.arn]

  dimensions = {
    InstanceId = "<EC2_INSTANCE_ID>" # 실제 인스턴스 ID로 변경
  }
}

# CloudWatch Alarm (us-east-1)
resource "aws_cloudwatch_metric_alarm" "route53_alarm" {
  provider            = aws.useast1
  alarm_name          = "Route53HealthCheckFail"
  comparison_operator = "LessThanThreshold"
  evaluation_periods  = 1
  metric_name         = "HealthCheckStatus"
  namespace           = "AWS/Route53"
  period              = 60
  statistic           = "Minimum"
  threshold           = 1
  alarm_description   = "Route53 헬스체크 실패 시 알람 발생"
  alarm_actions       = [aws_sns_topic.alarm_topic_useast.arn]

  dimensions = {
    HealthCheckId = "2fa3b506-4146-4b78-8bd4-4a5421aa8db9"
  }
}

# Log Group (us-east-1)
resource "aws_cloudwatch_log_group" "lambda_log_group" {
  provider          = aws.useast1
  name              = "/aws/lambda/${aws_lambda_function.alert_handler.function_name}"
  retention_in_days = 14
}
