# Bicycle Rental Demand Prediction

พื้นที่ทำงานกลุ่ม IFJC4002 สำหรับพัฒนาระบบทำนายจำนวนครั้งที่เช่าจักรยาน

**Current status (28 October 2026): corrected Drive sources and the trained application are ready for Streamlit Community Cloud. The app passed 16 validation/parity checks in hosted Colab. Deployment is pending.**

## Deploy the current application

Use this repository, branch `main`, entry point `app.py`, and Python 3.12 in Streamlit Community Cloud. Keep `models/final_pipeline.joblib`, `models/input_schema.json`, and `models/model_metadata.json` together. `requirements.txt` pins the tested Colab library versions. No dataset or credentials are needed by the application.

The model uses seven inputs and excludes `record_id`, `timestamp`, and the target. Validation compared a mean baseline, Linear Regression, and Random Forest; Random Forest was selected. Repeated test evaluation after implementation repair: MAE 13.931, RMSE 18.701039, R² 0.798475. The test partition had already been inspected, and these results do not establish real-world accuracy.

See [Drive sync and validation record](docs/DRIVE_SYNC_2026-10-28.md). Corrected member notebooks are in `notebooks/team/`; they use hosted Colab and the existing shared Drive. The remaining starter guides below are retained as learning material and describe the original scaffold.


## เริ่มอ่านตรงไหน

1. เปิด [Notebook 00 ใน Google Colab](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/00_orientation.ipynb) แล้วบันทึกสำเนาใน Drive
2. อ่าน [คู่มือเริ่มต้นบน Colab](docs/START_HERE_TH.md) สมาชิกใช้ Colab สำหรับเขียนโค้ด ฝึกโมเดล และทดสอบทั้งหมด
3. คุยและใส่ชื่อใน [Workflow สำหรับสมาชิก 5 คน](docs/WORKFLOW_5_MEMBERS_TH.md) แล้วรับงานย่อยใน [แผนลงมือ](docs/WORKBOOK_TH.md)
4. เรียนรู้ผ่าน [notebooks](notebooks/README.md) ตามลำดับ 00–05 แล้วบันทึกหลักฐานให้เพื่อนตรวจ

อ่านไกด์ภาพรวมและข้อดีข้อเสียได้ที่ [ไกด์ฉบับเต็ม](docs/PROJECT_GUIDE_TH.md)

## เว็บกลางของกลุ่ม

มีหน้าเว็บ **Bicycle Lab** บน Google Apps Script สำหรับอ่าน workflow เลือกดูงาน M1–M5 เปิด Colab และอัปเดตสถานะ/หลักฐานร่วมกัน รับลิงก์จากเจ้าของกลุ่มและดู [วิธีใช้เว็บ](apps-script/README.md) หน้าเว็บนี้ใช้ประสานงาน ส่วนการฝึกโมเดลยังทำใน Colab

## สิ่งที่เตรียมไว้ให้

- คู่มือภาษาไทย ลำดับการเรียนรู้ จุดตรวจ และแนวทางทำงานร่วมกัน
- Notebook ที่มีคำอธิบาย ตัวช่วยอ่านข้อมูล และพื้นที่ลงมือทำ
- แบบตั้งค่าข้อมูลที่ยังไม่ผูกชื่อคอลัมน์กับ dataset ใด
- หน้า Streamlit ที่เปิดได้และแจ้งสถานะตามจริง
- แบบฟอร์มวางแผน เก็บผลทดลอง ทดสอบ monitoring และ contribution
- ตัวตรวจโครงเริ่มต้นและการตั้งค่า รวมถึงการตรวจอัตโนมัติบน GitHub

สมาชิกยังต้องกำหนดคำถาม ตรวจข้อมูล เลือก feature และ split เขียน preprocessing ทดลอง baseline กับอย่างน้อย 2 อัลกอริทึม วิเคราะห์ผล เชื่อมโมเดล ทดสอบ และเขียนข้อสรุปด้วยตนเอง มีคำถามนำทางให้ในแต่ละช่วง

## ใช้ Google Colab เท่านั้นสำหรับพัฒนา

เปิด notebook จากลิงก์ Colab ในตาราง [notebooks](notebooks/README.md) แล้วรัน cell เตรียมงาน ระบบจะ clone repository เข้า runtime เมื่อยังไม่มี และใช้ไลบรารีพื้นฐานที่ Colab มีอยู่ก่อน

สมาชิกไม่ต้องติดตั้ง Python, Git หรือ Jupyter ในเครื่อง แก้ config/app.py จาก Files ใน Colab ได้ Notebook 05 มีตัวอย่างตรวจ Streamlit ด้วย AppTest ภายใน notebook ส่วนแอปที่เปิดผ่านลิงก์จริงเผยแพร่บน Streamlit Community Cloud ตามโจทย์

บันทึก notebook ที่แก้ใน Drive และสำรองไฟล์จาก runtime ก่อนเลิกงาน การบันทึก notebook ไม่ได้สำรอง dataset โมเดล หรือ app.py ที่อยู่ใน runtime ดูวิธีส่งงานผ่านเว็บ GitHub ใน CONTRIBUTING

## เมื่อได้รับ dataset

1. อ่าน [ข้อตกลงข้อมูล](docs/DATA_CONTRACT_TH.md) และเก็บไฟล์ใน `data/raw/`
2. ยืนยันความหมายคอลัมน์ หน่วย แหล่งที่มา และสิทธิ์เผยแพร่กับอาจารย์
3. แก้ `config/project.json` ตามข้อมูลจริง
4. รันตัวตรวจผ่าน cell ใน Colab ตามคู่มือ หรือ notebook 01
5. เริ่ม notebook 01 แล้วทำตามแผน ไม่ข้ามไปเลือกโมเดลก่อนเข้าใจข้อมูล

ตัวตรวจนี้ตรวจการตั้งค่าและหัวตาราง CSV เท่านั้น ไม่รับรองคุณภาพข้อมูล ความถูกต้องของ split หรือประสิทธิภาพโมเดล

## แผนที่โฟลเดอร์

| ตำแหน่ง | หน้าที่ |
| --- | --- |
| `config/project.json` | ตั้งชื่อคอลัมน์และบริบทหลังได้รับข้อมูล |
| `notebooks/` | แบบฝึกและงานวิเคราะห์ที่สมาชิกลงมือทำ |
| `app.py` | โครงหน้าจอ Streamlit ให้สมาชิกต่อยอด |
| `starter_support.py` | ตัวช่วยอ่าน config และตรวจหัวตาราง ไม่มีโค้ดฝึกโมเดล |
| `data/` | คำอธิบายและพื้นที่ข้อมูลใน Colab runtime ไฟล์ข้อมูลไม่ถูกติดตามด้วย Git โดยค่าเริ่มต้น |
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
