import subprocess
import time
import os

# โฟลเดอร์ที่เก็บบอท
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    # ดึงไฟล์ .py ทั้งหมดในโฟลเดอร์ ยกเว้น runner.py
    scripts = sorted([
        f for f in os.listdir(BASE_DIR)
        if f.endswith(".py") and f != "runner.py"
    ])

    for script in scripts:
        print(f"\n===== กำลังรัน {script} =====")
        try:
            # run() จะรอจนกว่าสคริปต์นี้จะเสร็จ
            subprocess.run(["python", os.path.join(BASE_DIR, script)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"[Error] {script} ล้มเหลว: {e}")
        time.sleep(2)  # หน่วงเล็กน้อยระหว่างไฟล์

    print("\n===== รอบนี้เสร็จสิ้น จะเริ่มใหม่ =====\n")
    time.sleep(10)  # พักก่อนวนรอบใหม่
