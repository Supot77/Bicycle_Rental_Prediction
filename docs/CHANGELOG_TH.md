# ประวัติการเปลี่ยนแปลง

## 2026-10-27: โครงเริ่มต้นสำหรับสมาชิกลงมือทำเอง

เตรียม README, START_HERE, WORKBOOK, DATA_CONTRACT, RUBRIC_MAP, DEPLOYMENT, REPORT_OUTLINE, CONTRIBUTING และสำเนาไกด์เต็ม ให้สมาชิกเริ่มงานและส่งต่อกันได้

เพิ่ม notebook 00–05 พร้อมบทนำ คำถาม พื้นที่ทำงาน และตัวช่วยอ่านข้อมูล ส่วนการตัดสินใจ วิเคราะห์ split/preprocessing ฝึกโมเดล และสรุปผลยังเป็นงานของสมาชิก

เพิ่ม config ที่ยังไม่กำหนดคอลัมน์ app.py ที่เปิดได้โดยไม่มี prediction ปลอม และตัวช่วยตรวจ config/หัวตาราง CSV พร้อมกฎป้องกัน target ปนใน X และ path ออกนอก data/

เพิ่มแบบฟอร์มหลักฐานที่ไม่มีผลสมมติ กฎ Git สำหรับข้อมูลและ credentials, PR template และ CI สำหรับโครงเริ่มต้น

### ผลการตรวจ

- สร้าง virtual environment ใหม่ด้วย Python 3.12.14 และติดตั้ง requirements-dev สำเร็จ `pip check` ไม่พบ dependency ขัดกัน จากนั้นตรึงรุ่น dependencies หลักตามชุดที่ตรวจจริง
- `python scripts/check_setup.py` ผ่าน ตรวจรูปแบบ config, notebook และ syntax ของ code cells ในโครงเริ่มต้น
- `python -m unittest discover -s tests -v` ผ่าน 7 กรณี ทั้ง Python ในเครื่อง 3.10 และ environment ทดสอบ 3.12: target ปนใน X, feature ซ้ำ/ถูก exclude, path ออกนอก data, settings ผิดรูปแบบ, CSV header ผิด, ไม่มีไฟล์ และสถานะรอ dataset
- ตรวจ schema ด้วย nbformat และรัน notebook 00–05 ผ่านทุกไฟล์ใน kernel ใหม่ ผ่าน nbclient ในสถานะยังไม่มี dataset ไม่บันทึก output กลับลง notebook
- ใช้ Streamlit AppTest ตรวจ app.py ผ่าน 2 สถานการณ์: หน้ารอข้อมูลไม่มีการทำนายปลอม และ config อ่านไม่ได้มีข้อความแจ้งโดยแอปไม่ล่ม
- `check_setup.py --require-data` ออกด้วยสถานะ 1 ตามที่ตั้งใจ พร้อมแจ้ง path/target/unit/context/features ที่ยังไม่กำหนด ไม่มีการเติมข้อมูลแทนสมาชิกเพื่อให้ผ่าน
- ตรวจ Markdown links ภายในไม่พบปลายทางหาย แบบฟอร์ม CSV หลักฐานทั้ง 7 ไฟล์มีเพียงหัวตาราง และตรวจว่า Git ignore ครอบคลุมข้อมูล โมเดลทดลอง secrets และ .venv

ผลเหล่านี้ยืนยันความพร้อมของ scaffold ในสถานะเริ่มต้น ยังไม่มีผล ML ไม่มีการทดลองกับ dataset จากอาจารย์ และยังไม่ได้ deploy ระบบทำนายจริง
