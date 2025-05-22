#!/bin/bash

# 환경 변수 설정
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# 복원할 S3 버킷
S3_BUCKET="s3://cloudmail-backup"

# SQLite DB 파일을 복원할 로컬 경로
LOCAL_DB_DIR="/home/hans/cloudmailsvc/flaskBlog/db"

# 로그 파일
LOG_FILE="/home/hans/db_restore.log"

echo "[$(date)] === 복원 시작 ===" >> "$LOG_FILE"

# 로컬 디렉토리가 없으면 생성
mkdir -p "$LOCAL_DB_DIR"

# DB 파일 복원 (S3 → local)
aws s3 sync "$S3_BUCKET" "$LOCAL_DB_DIR" --exclude "*" --include "*.db" >> "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
  echo "[$(date)] ✅  복원 성공" >> "$LOG_FILE"
else
  echo "[$(date)] ❌  복원 실패" >> "$LOG_FILE"
fi

echo "[$(date)] === 복원 종료 ===" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
