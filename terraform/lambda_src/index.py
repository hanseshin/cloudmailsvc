import os
import json
import requests

def handler(event, context):
    webhook_url = os.environ['WEBHOOK_URL']
    vmware_api  = os.environ['VMWARE_API']

    results = []

    # 1. VMware → 복원 트리거
    try:
        res = requests.post(vmware_api)
        res.raise_for_status()
        results.append("✅ VMware 복원 요청 성공")
    except Exception as e:
        results.append(f"❌ VMware 복원 실패: {str(e)}")

    # 2. Slack 알림 전송
    slack_msg = {
        "text": "[⚠️ Route53 장애 감지]\n" + "\n".join(results)
    }
    try:
        requests.post(webhook_url, json=slack_msg)
    except Exception as e:
        print("Slack 알림 실패:", e)

    return {"status": "done"}
