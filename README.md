# 🛠 하이브리드 클라우드 이중화 DR 웹 앱 서비스

## 1. 개요

이 프로젝트는 AWS EC2와 온프레미스 VMware를 Active-Standby 구조로 구성한 **하이브리드 클라우드 이중화 DR 웹 앱 서비스**입니다.  
EC2 서버가 다운되면 자동으로 VMware에서 복원 서버가 활성화되며, Slack을 통해 알림을 받고, DB 백업과 복원, 모니터링을 자동화 수행합니다.  
웹 앱은 MIT 라이선스 오픈소스를 사용했으며  Amazon SES를 활용한 메일 발송 기능을 추가해주었습니다.

---



## 2. 아키텍처 구성


<img width="1624" height="1170" alt="image" src="https://github.com/user-attachments/assets/b628a09f-a66f-4106-9a19-f2c39721a40f" />


## Architecture (High-level)
Client → Route53 → ALB (HTTPS/ACM) → Target Group (HTTP:5000) → EC2 (Private, Flask/SQLite)
- Failover: Route53 Health Check 실패 시 → VMware WAN IP로 전환
- Backup: EC2 → S3 (VPC Endpoint), 

## Prerequisites
- Domain: `cloudmailsvc.com` (Route53 퍼블릭 호스팅 영역으로 네임서버 위임 완료)
- ACM cert for `cloudmailsvc.com`, `www.cloudmailsvc.com`
- IAM Role for EC2 (S3 최소 권한)
- S3 bucket: `cloudmail-backup` (Versioning + Encryption)

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

  
## 📬 연락

- 작성자: hanseshin
- 이메일: hansesin143@gmail.com
