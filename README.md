# 🛠 Hybrid Cloud Auto-Recovery Web Application

## 📌 개요

이 프로젝트는 AWS EC2와 온프레미스 VMware를 Active-Standby 구조로 구성한 **하이브리드 클라우드 장애 복구 시스템**입니다.  
EC2 서버가 다운되면 자동으로 VMware에서 복원 서버가 활성화되며, Slack을 통해 알림을 받고, DB 백업과 복원, 모니터링을 자동화합니다.  
웹 앱은 오픈소스를 사용했으며  **Amazon SES(Simple Email Service)**를 활용한 메일 발송 기능을 추가해주었습니다.

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
