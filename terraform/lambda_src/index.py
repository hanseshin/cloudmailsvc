import os
import requests
import json

def handler(event, context):
    webhook_url = os.environ['WEBHOOK_URL']
    vmware_api  = os.environ['VMWARE_API']

    results = []

    # VMware 복원 요청
    try:
        res = requests.post(vmware_api)
        res.raise_for_status()
        results.append(" VMware 복원 요청 성공")
    except Exception as e:
        results.append(f" VMware 복원 실패: {str(e)}")
        print(f"VMware API 요청 실패: {e}")

    # Slack 알림
    slack_msg = {
        "text": "[Route53 장애 감지]\n" + "\n".join(results)
    }
    try:
        slack_res = requests.post(webhook_url, json=slack_msg)
        slack_res.raise_for_status()
    except Exception as e:
        print("Slack 알림 실패:", e)

    print("결과:", results)
    return {"status": "done"}
