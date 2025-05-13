#!/bin/bash

# 환경 변수 설정 (cron 환경에서 필요)
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# 백업 대상 SQLite DB 디렉토리
DB_DIR="/home/ubuntu/cloudmailsvc/flaskBlog/db"

# S3 버킷 경로
S3_BUCKET="s3://cloudmail-backup"

# 로그 파일 경로 (홈 디렉토리에 작성)
LOG_FILE="/home/ubuntu/db_backup.log"

# 현재 시간 기록
echo "[$(date)] === 백업 시작 ===" >> "$LOG_FILE"

# 백업 디렉토리 확인
if [ ! -d "$DB_DIR" ]; then
  echo "[$(date)] ERROR: 백업 대상 디렉토리가 존재하지 않음: $DB_DIR" >> "$LOG_FILE"
  exit 1
fi

# S3로 백업 실행
aws s3 sync "$DB_DIR" "$S3_BUCKET" --exclude "*" --include "*.db" >> "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
  echo "[$(date)] ✅ 백업 성공" >> "$LOG_FILE"
else
  echo "[$(date)] ❌ 백업 실패" >> "$LOG_FILE"
fi

echo "[$(date)] === 백업 종료 ===" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

