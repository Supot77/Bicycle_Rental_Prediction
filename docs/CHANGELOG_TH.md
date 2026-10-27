# ประวัติการเปลี่ยนแปลง

## 2026-10-28: เว็บกลาง Bicycle Lab บน Google Apps Script

เพิ่ม apps-script/Code.gs, Index.html, project-data.json, manifest, DESIGN และคู่มือใช้เว็บ เพื่อให้สมาชิกเห็น workflow 7 ช่วง/22 งาน กรอง M1–M5 เปิด Colab และบันทึกสถานะ บันทึกสั้น และ HTTPS evidence link ร่วมกันได้ เพิ่ม scripts/build_apps_script.py เพื่อสร้าง task definitions จากแผน CSV โดยไม่ส่งออก progress จริง

เก็บความคืบหน้าใน Script Properties หนึ่งค่าต่องาน ใช้ ScriptLock กับ expected revision ป้องกันการเขียนทับกัน ตรวจ dependency ก่อนส่งตรวจ/ปิดงาน และให้ทบทวนงานปลายทางเมื่อ upstream เปิดแก้ ไม่เก็บ dataset หรืออ้างว่าบทบาทที่เลือกเป็นตัวตนที่ยืนยันแล้ว

นำโค้ดเข้าโปรเจกต์ Apps Script ที่ผู้ใช้ระบุและเผยแพร่เว็บแอปสำเร็จ ตั้งผู้เข้าถึงเป็นผู้มีบัญชี Google ที่ได้รับลิงก์ ทุกคนที่เข้าถึงแก้สถานะได้ ยังไม่จำกัด allowlist เฉพาะสมาชิก จึงไม่ใส่ URL ที่แก้สถานะได้ใน repository สาธารณะ ส่งลิงก์ให้เจ้าของเพื่อแชร์กับกลุ่มโดยตรง

ผลตรวจ: backend tests 9 กรณีผ่าน JavaScript syntax ผ่าน ตรวจ UI บนจอคอมพิวเตอร์และ viewport 390px เปิดรายละเอียด/กรองบทบาท/บันทึก/ข้อผิดพลาด dependency/แก้ชนกันสองหน้าจอ/ใช้ข้อมูลล่าสุด/เปิดลิงก์หลักฐานในข้อมูลจำลองผ่าน เว็บจริงโหลดจาก Apps Script และอ่านสถานะเริ่มต้น 22 งานได้ โดยไม่ใส่ความคืบหน้าทดลองลงข้อมูลทีมจริง

แก้ README และเพิ่ม backend tests ใน GitHub Actions การพัฒนา/ฝึกโมเดลของสมาชิกยังเป็น Colab และ deployment แอป prediction ยังเป็น Community Cloud เว็บใหม่นี้เป็นพื้นที่ประสานงานเท่านั้น

## Workflow จาก preprocessing ถึงใช้งานสำหรับสมาชิก 5 คน

เพิ่ม WORKFLOW_5_MEMBERS_TH พร้อมภาพรวม Mermaid บทบาท M1–M5 งานรับ/ส่ง จุดตรวจ G0–G6 และลำดับตั้งแต่รับข้อมูล split/preprocessing ทดลอง baseline กับ A/B เลือกจาก validation ฝึก/ประเมิน final artifact ต่อแอป deploy และ monitoring

เพิ่ม handoff, split manifest และ model card templates ปรับ task_board ให้มีงานเสนอ 22 งาน สถานะทั้งหมด not_started และยังไม่มีชื่อจริง/กำหนดส่ง/หลักฐานสำเร็จ เชื่อม workflow จาก README, WORKBOOK, notebooks/README และเพิ่ม markdown อธิบายเจ้าของ/การส่งต่อใน notebook ทั้ง 6 โดยไม่แก้ code cells

ยังไม่เลือกอัลกอริทึม feature split หรือ preprocessing ให้สมาชิก ไม่มีการฝึกโมเดลหรือสร้างผลทดลองแทน ทุกคนใช้ Colab และเขียนรายงาน/หลักฐานจากงานจริง

ผลตรวจ: check_setup และ tests ตัวช่วย 7 กรณีผ่าน ตรวจว่างานเสนอ 22 งานอ้าง dependency ที่มีจริงและไม่มีวงจร สถานะยังไม่เริ่ม/กำหนดส่งและหลักฐานยังว่างทั้งหมด notebook ทั้ง 6 ผ่าน schema และยืนยันว่า code cells ไม่เปลี่ยนจากรุ่นก่อน ตรวจลิงก์ Markdown ภายในและ diff whitespace ผ่าน จึงไม่รันการทดลองโมเดลหรือ AppTest ซ้ำเพราะไม่มีโค้ดพฤติกรรมเปลี่ยน

## 2026-10-27: ใช้ Google Colab เป็นช่องทางพัฒนาเดียว

ปรับ README, START_HERE, CONTRIBUTING, WORKBOOK, DEPLOYMENT, PROJECT_GUIDE และรายการ notebook ให้เปิดผ่าน Colab บันทึกสำเนาใน Drive และส่งงานผ่านเว็บ GitHub เอาขั้นตอนติดตั้ง Python/venv/Jupyter ในเครื่องออกจากคู่มือสมาชิก พร้อมบันทึกข้อกำหนดใน AGENTS.md

ปรับ notebook ทั้ง 6 ให้เตรียม repository ใน runtime ได้เมื่อยังไม่มี โดยไม่ pull/reset โฟลเดอร์เดิม ใช้ scientific libraries ที่ Colab มีอยู่และติดตั้งเฉพาะตัวที่ขาด เพิ่ม requirements-colab.txt สำหรับ Streamlit และตัวอย่าง AppTest ใน notebook 05 ส่วน dependencies สำหรับผู้ดูแลตรวจงานแยกไว้ใน requirements-dev.txt

อธิบายการสำรอง notebook แยกจากไฟล์ใน runtime และการตรวจไฟล์ก่อนอัปโหลดผ่านเว็บ เพราะ .gitignore ไม่ป้องกันการเลือกอัปโหลดผ่านเว็บ อัปเดตไกด์ Google Docs เดิมเฉพาะ 8 ข้อความที่เกี่ยวข้องและตรวจอ่านกลับแล้ว โดยคงโจทย์/rubric ของอาจารย์

ผลตรวจ: check_setup ผ่าน tests ตัวช่วยเดิมผ่าน 7 กรณี notebook 00–05 ผ่านการตรวจ schema และรันใน kernel ใหม่ รวม cell AppTest ที่เพิ่มใหม่ หน้า app ผ่าน 2 สถานการณ์เดิม ตรวจลิงก์ในเอกสารและ outputs ที่ว่างแล้ว จำลอง runtime ใหม่เพื่อยืนยันว่า clone ครั้งเดียวและรันซ้ำไม่ทับ config ที่แก้ไว้

ขอบเขตการตรวจ: รันใน environment ทดสอบและจำลองเส้นทาง Colab ยังไม่ได้รันใน hosted Colab ของบัญชีผู้ใช้จริง ไม่มีการเข้าถึง Drive ของสมาชิกและไม่มี dataset จริง แอปเผยแพร่จริงยังใช้ Streamlit Community Cloud ตามโจทย์

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
