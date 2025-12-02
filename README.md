# 🛠 하이브리드 클라우드 이중화 DR 웹 앱 서비스

## 개요

이 프로젝트는 AWS EC2와 온프레미스 VMware를 Active-Standby 구조로 구성한 **하이브리드 클라우드 이중화 DR 웹 앱 서비스**입니다.  
AWS EC2가 장애로 동작 불가 상태가 되면 VMware Standby 서버가 자동 활성화되며,
DNS Failover, DB 복원, Slack 알림까지 완전 자동화된 DR 시나리오를 제공합니다.

웹 애플리케이션은 Flask 기반 오픈소스를 사용하였으며,
추가로 Amazon SES(Simple Email Service) 기반 메일 발송 기능을 구현했습니다.



## 아키텍처 구성


<img width="1624" height="1170" alt="image" src="https://github.com/user-attachments/assets/b628a09f-a66f-4106-9a19-f2c39721a40f" />

- **AWS VPC**: 2개 AZ, 퍼블릭/프라이빗 서브넷 구성
- **Active 서버**: AZ1 프라이빗 서브넷 내 EC2 (Flask + SQLite)
- **Load Balancer**: ALB (HTTPS 리스너 + ACM 인증서)
- **Route53**: Active(ALB Alias) + Standby(VMware WAN IP) Failover 정책
- **S3 Gateway Endpoint**: 프라이빗 서브넷 EC2 → S3 백업 경로
- **Bastion Host**: 퍼블릭 서브넷 EC2, SSH 중계
- **백업/복원**: EC2 주기적 SQLite → S3 백업, 장애 발생 시 VMware 복원
- **모니터링**: Route53 Health Check (ALB DNS), CloudWatch Alarm → SNS → Lambda → Slack

##  기술스택
- **Backend**: Python (Flask)
- **Database**: SQLite, AWS S3 
- **메일 시스템**: Amazon SES, SPF/DKIM/ACM 
- **웹 서버**: Nginx 
- **컨테이너화**: Docker
- **인프라**: AWS EC2 (Ubuntu 20.04), VMware ESXi 가상머신
- **도메인 관리**: AWS Route53 (Failover 라우팅, 헬스체크)
- **모니터링 및 자동화**: AWS CloudWatch, SNS, Lambda, Slack Webhook, Grafana
- **IaC**: Terraform 

## 주요 기능
- Active-Standby 하이브리드 클라우드 DR 구성
- HTTPS(ACM) 기반 보안 통신
- 주기적 SQLite DB → S3 백업 (Gateway Endpoint 사용)
- 장애 발생 시 Route53 DNS Failover
- CloudWatch Alarm → SNS → Lambda → Slack 알림 및 VMware DB 복원
- Bastion Host를 통한 안전한 SSH 접속
- Amazon SES를 이용한 메일 발송 기능

## 결과 및 성과
- **다운타임 최소화**: 장애 시 수 초 내 DNS Failover → Standby 전환
- **백업 및 복원 자동화**: RTO(Recovery Time Objective) 수 초 이내 단축
- **운영 효율성**: 단일 명령/자동화 스크립트로 백업·복원 관리
- **보안 강화**: 프라이빗 서브넷 + 보안 그룹 + ACM 기반 HTTPS


  
## 📬 연락

- 작성자: hanseshin
- 이메일: hansesin143@gmail.com
