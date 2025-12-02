# 🛠 Hybrid Cloud Auto-Recovery Web Application

## 📌 개요

이 프로젝트는 AWS EC2와 온프레미스 VMware를 Active-Standby 구조로 구성한 **하이브리드 클라우드 장애 복구 시스템**입니다.  
EC2 서버가 다운되면 자동으로 VMware에서 복원 서버가 활성화되며, Slack을 통해 알림을 받고, DB 백업과 복원, 모니터링을 자동화합니다.  
웹 앱은 오픈소스를 사용했으며  Amazon SES(Simple Email Service)를 활용한 메일 발송 기능을 추가해주었습니다.

---

## 🧱 아키텍처 구성


<img width="1624" height="1170" alt="image" src="https://github.com/user-attachments/assets/b628a09f-a66f-4106-9a19-f2c39721a40f" />




- **EC2 (Ubuntu)**  
  - Flask 기반 웹 애플리케이션  
  - SQLite 데이터베이스  
  - Amazon SES를 통한 메일 발송  
  - S3에 DB 주기적 백업 자동화 (Shell + cron )
  
- **VMware (온프레미스)**  
  - Flask 서버 대기 (수동/자동 기동 가능)  
  - Lambda 요청 시 S3로부터 DB 복원

- **AWS 서비스**
  - **Route53**: 헬스체크 및 DNS 장애 조치 (Failover)
  - **S3**: DB 백업 저장소
  - **SNS**: 장애 알림 → Lambda 트리거
  - **Lambda**: 복원 트리거 + Slack 알림 + S3 백업 스크립트 실행
  - **CloudWatch**: EC2 상태 모니터링 및 알람
  - **IAM**: Lambda 권한 부여
  - **SES**: 이메일 발송 서비스

- **모니터링**
  - **CloudWatch Agent + Grafana**: EC2/VMware 리소스 시각화

---

## 🔁 장애 복구 흐름

1. EC2에서 **SQLite → S3 주기적 백업** (`cron`)
2. **Route53 헬스체크**로 EC2 상태 모니터링
3. 장애 발생 시:
   - CloudWatch Alarm → SNS → Lambda 실행
   - Lambda:
     - VMware에 Webhook POST (`/webhook/restore`) 요청
     - `restore.sh` 실행 → S3에서 최신 DB 다운로드
     - Slack Webhook으로 복원 알림 전송
     - EC2 백업 스크립트도 재실행 (Failover 대비)

## Overview
- **AWS**: VPC(2AZ), ALB(ACM), EC2(Private, Flask 5000), NAT GW, Bastion, S3 Gateway Endpoint
- **DNS**: Route53 Failover — Primary: ALB(Active), Secondary: VMware WAN IP (Standby)
- **Backup**: Private EC2 → S3 (Gateway Endpoint) via cron + AWS CLI

## Architecture (High-level)
Client → Route53 → ALB (HTTPS/ACM) → Target Group (HTTP:5000) → EC2 (Private, Flask/SQLite)
- Failover: Route53 Health Check 실패 시 → VMware WAN IP로 전환
- Backup: EC2 → S3 (VPC Endpoint), Versioning/Encryption 권장

## Prerequisites
- Domain: `cloudmailsvc.com` (Route53 퍼블릭 호스팅 영역으로 네임서버 위임 완료)
- ACM cert for `cloudmailsvc.com`, `www.cloudmailsvc.com`
- IAM Role for EC2 (S3 최소 권한)
- S3 bucket: `cloudmail-backup` (Versioning + Encryption 권장)

## AWS Setup (Console)
1. **VPC & Subnets**
   - 2 AZ, 각 AZ에 Public/Private Subnet 1개씩
   - IGW 연결, NAT GW는 AZ1 Public Subnet에 생성
2. **Route Tables**
   - Public: `0.0.0.0/0 → IGW`
   - Private: `0.0.0.0/0 → NAT GW` (+ S3 Gateway Endpoint route 자동 추가)
3. **Security Groups**
   - ALB SG: In 80/443(0.0.0.0/0), Out ALL
   - EC2 SG: In 5000 from ALB SG, Out ALL
   - Bastion SG: In 22 from 관리IP, Out to EC2:22
4. **ALB**
   - Subnets: Public(AZ1, AZ2)
   - Listeners: 80→Redirect to 443, 443(ACM)→Forward to TG
   - Target Group: HTTP:5000, Health check `/`
5. **EC2 (Private)**
   - Flask/Gunicorn on `0.0.0.0:5000`
   - IAM Role attach
6. **S3 Gateway Endpoint**
   - Service: `com.amazonaws.ap-northeast-2.s3`
   - Attach to Private Subnet Route Tables
   - (Optional) Endpoint Policy: bucket 제한
7. **S3 Bucket**
   - Name: `cloudmail-backup`
   - Block Public Access: ON
   - Versioning/Default Encryption: ON
   - (Optional) Bucket Policy: SourceVpce & SecureTransport 제한
8. **Route53**
   - A(Primary): Alias → ALB, Failover=Primary, Health Check attached
   - A(Secondary): Value → VMware WAN IP, Failover=Secondary

## Backup Script
- File: `backup-to-s3.sh`
- Make executable: `chmod +x backup-to-s3.sh`
- Run: `./backup-to-s3.sh`
- Cron: `crontab -e` → `0 3 * * * /home/ubuntu/backup-to-s3.sh`

## Health / Failover Test
- Stop Flask or block 5000 on EC2 SG → ALB Target Unhealthy
- Route53 Health Check failure → DNS answers VMware IP
- Restore: Start Flask, health green → switch back (DNS TTL 고려)

## Known Limitations
- SQLite: 동시성 제한, 장애 복구 시 **RPO** 존재
- 단일 EC2 타겟: ALB 레벨 5xx 가능 (짧은 구간)
- NAT GW/AZ 구성 비용 고려

## Observability (Recommended)
- ALB access logs → S3 (+Athena)
- CloudWatch metrics/alarms: 5xx, UnHealthyHostCount
- VPC Flow Logs


## 📬 기술 스택

- AWS: EC2, S3, Lambda, CloudWatch, Route53, SNS, IAM, SES
- Flask, SQLite
- VMware + Bridge + 포트포워딩
- Terraform
- Slack Webhook
- Docker
---

## 📬 연락

- 작성자: hanseshin
- 이메일: hansesin143@gmail.com
