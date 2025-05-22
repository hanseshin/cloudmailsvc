output "sns_topic_arn" {
  value = aws_sns_topic.alarm_topic_useast.arn
}


output "lambda_function_name" {
  value = aws_lambda_function.alert_handler.function_name
}
