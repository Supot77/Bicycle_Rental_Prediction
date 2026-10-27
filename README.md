# Bicycle Rental Demand Prediction

พื้นที่ทำงานกลุ่ม IFJC4002 สำหรับพัฒนาระบบทำนายจำนวนครั้งที่เช่าจักรยาน

**สถานะปัจจุบัน: โครงเริ่มต้นเพื่อเรียนรู้และแบ่งงาน รอ dataset จากอาจารย์ ยังไม่มีโมเดลหรือผลทดลองจริง**

## เริ่มอ่านตรงไหน

1. อ่าน [เริ่มต้นครั้งแรก](docs/START_HERE_TH.md) แล้วเลือกวิธีใช้เครื่องตัวเองหรือ Google Colab
2. เปิด [แผนลงมือทีละช่วง](docs/WORKBOOK_TH.md) และรับงานย่อยหนึ่งชิ้น
3. เรียนรู้ผ่าน [notebooks](notebooks/README.md) ตามลำดับ 00–05
4. บันทึกงานจริงใน [evidence](evidence/README.md) และให้เพื่อนช่วยตรวจ

อ่านไกด์ภาพรวมและข้อดีข้อเสียได้ที่ [ไกด์ฉบับเต็ม](docs/PROJECT_GUIDE_TH.md)

## สิ่งที่เตรียมไว้ให้

- คู่มือภาษาไทย ลำดับการเรียนรู้ จุดตรวจ และแนวทางทำงานร่วมกัน
- Notebook ที่มีคำอธิบาย ตัวช่วยอ่านข้อมูล และพื้นที่ลงมือทำ
- แบบตั้งค่าข้อมูลที่ยังไม่ผูกชื่อคอลัมน์กับ dataset ใด
- หน้า Streamlit ที่เปิดได้และแจ้งสถานะตามจริง
- แบบฟอร์มวางแผน เก็บผลทดลอง ทดสอบ monitoring และ contribution
- ตัวตรวจโครงเริ่มต้นและการตั้งค่า รวมถึงการตรวจอัตโนมัติบน GitHub

สมาชิกยังต้องกำหนดคำถาม ตรวจข้อมูล เลือก feature และ split เขียน preprocessing ทดลอง baseline กับอย่างน้อย 2 อัลกอริทึม วิเคราะห์ผล เชื่อมโมเดล ทดสอบ และเขียนข้อสรุปด้วยตนเอง มีคำถามนำทางให้ในแต่ละช่วง

## ทดลองเปิดโครงงานในเครื่อง

ใช้ Python 3.12 สำหรับ environment เริ่มต้นนี้ คำสั่งต่อไปนี้สำหรับ Windows PowerShell โดยไม่ต้องเปลี่ยน execution policy

```powershell
git clone https://github.com/Supot77/Bicycle_Rental_Prediction.git
cd Bicycle_Rental_Prediction
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe scripts/check_setup.py
.\.venv\Scripts\python.exe -m streamlit run app.py
```

หาก clone แล้วให้เข้าโฟลเดอร์เดิม ไม่ต้อง clone ซ้ำ ดูวิธี macOS/Linux, Colab และการแก้ปัญหาใน [คู่มือเริ่มต้น](docs/START_HERE_TH.md)

## เมื่อได้รับ dataset

1. อ่าน [ข้อตกลงข้อมูล](docs/DATA_CONTRACT_TH.md) และเก็บไฟล์ใน `data/raw/`
2. ยืนยันความหมายคอลัมน์ หน่วย แหล่งที่มา และสิทธิ์เผยแพร่กับอาจารย์
3. แก้ `config/project.json` ตามข้อมูลจริง
4. รัน `python scripts/check_setup.py --require-data` จาก environment ที่ติดตั้งแล้ว
5. เริ่ม notebook 01 แล้วทำตามแผน ไม่ข้ามไปเลือกโมเดลก่อนเข้าใจข้อมูล

ตัวตรวจนี้ตรวจการตั้งค่าและหัวตาราง CSV เท่านั้น ไม่รับรองคุณภาพข้อมูล ความถูกต้องของ split หรือประสิทธิภาพโมเดล

## แผนที่โฟลเดอร์

| ตำแหน่ง | หน้าที่ |
| --- | --- |
| `config/project.json` | ตั้งชื่อคอลัมน์และบริบทหลังได้รับข้อมูล |
| `notebooks/` | แบบฝึกและงานวิเคราะห์ที่สมาชิกลงมือทำ |
| `app.py` | โครงหน้าจอ Streamlit ให้สมาชิกต่อยอด |
| `starter_support.py` | ตัวช่วยอ่าน config และตรวจหัวตาราง ไม่มีโค้ดฝึกโมเดล |
| `data/` | คำอธิบายและพื้นที่ข้อมูลในเครื่อง ไฟล์ข้อมูลไม่ถูกติดตามด้วย Git โดยค่าเริ่มต้น |
| `models/`, `results/` | คำแนะนำการเก็บ artifact และผลทดลอง |
| `evidence/` | แบบฟอร์มหลักฐาน ยังไม่มีรายการผลจริง |
| `docs/` | คู่มือ แผนงาน และการเชื่อมกับ rubric |
| `tests/`, `scripts/` | ตรวจตัวช่วยและความสมบูรณ์ของโครงงาน |

## ข้อกำหนดที่ต้องทำให้ครบ

เปรียบเทียบ baseline เพิ่มจากอย่างน้อย 2 อัลกอริทึม รายงาน MAE, RMSE และ R² ใช้ Streamlit + GitHub + Streamlit Community Cloud ทดสอบ notebook เทียบ dashboard มี monitoring เก็บอย่างน้อย 5 prompts พร้อมวิธีตรวจ และหลักฐานสมาชิกทั้ง 5 คน ดูรายละเอียดใน [แผนเทียบเกณฑ์](docs/RUBRIC_MAP_TH.md)

เครื่องหมายตรวจผ่านบน GitHub หมายถึงโครงเริ่มต้นผ่านการตรวจที่กำหนดไว้ ยังไม่ใช่การผ่านเกณฑ์โครงงาน ML

## เอกสารอาจารย์และแผนที่ใช้ร่วมกัน

- [โจทย์และ rubric](https://docs.google.com/document/d/1VuLwvOmVn9uPh-byMeTfYcuIYrbqskXJ1zU9ibKhWyM)
- [ไกด์วางแผนภาษาไทย](https://docs.google.com/document/d/1Dy6pKGc6g3ajfUPVXpmX2B8j8_gT00fiDLyrpS25nm8)
- [ประวัติสิ่งที่เตรียมและผลตรวจ](docs/CHANGELOG_TH.md)

กำหนดส่ง ภาษาในรายงาน และรายละเอียด dataset ให้ยึดคำยืนยันของอาจารย์
