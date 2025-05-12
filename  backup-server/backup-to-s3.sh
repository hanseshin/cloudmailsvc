#!/bin/bash

# 백업 대상 SQLite DB 디렉토리
DB_DIR="/home/ubuntu/cloudmailsvc/db"

# S3 버킷 경로
S3_BUCKET="s3://cloudmail-backup"

# 현재 시간으로 백업 로그 남기기
echo "[`date`] Backing up DB from $DB_DIR to $S3_BUCKET" >> /var/log/db_backup.log

# 실제 업로드 명령
aws s3 sync "$DB_DIR" "$S3_BUCKET" --exclude "*" --include "*.db" >> /var/log/db_backup.log 2>&1
