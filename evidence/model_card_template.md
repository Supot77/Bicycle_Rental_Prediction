# แม่แบบข้อมูลโมเดลที่จะส่งให้แอป

กรอกหลังทดลองและเลือกจริง ตัวเลขและชื่อไฟล์ยังไม่ได้กำหนดให้ แยกผล measured ออกจากข้อเสนอในอนาคต

## ที่มาและบริบท

- Artifact filename / version / checksum:
- Run ID / notebook/code reference:
- ผู้ฝึก / ผู้ตรวจ / วันที่:
- Intended user / prediction context / horizon:
- Target / หน่วย / ระดับเวลาและพื้นที่ที่ครอบคลุม:
- Dataset version และ split manifest:
- Feature/schema version และ preprocessing recipe:

## การสร้างและประเมิน

- อัลกอริทึม / hyperparameters / seed ที่ใช้จริง:
- ชุดที่ใช้ fit final preprocessing และ estimator:
- เหตุผลเลือกจาก validation และข้อแลกเปลี่ยน:
- ผล final test ของ artifact ตัวนี้: MAE / RMSE / R²:
- กลุ่มกรณีที่ error สูงและหลักฐาน:
- Python และรุ่นไลบรารีที่ฝึกจริงบน Colab:
- วิธีโหลดจาก runtime ใหม่และ dependencies ที่แอปต้องตรง:

## สัญญาใช้งานและการตรวจ

- รายการ feature / ชนิด / หน่วย / ลำดับ:
- กฎ missing / unknown category / input นอกช่วง:
- หน่วย output / clipping / rounding และกฎที่ใช้ใน metrics:
- Reference cases ที่เผยแพร่ได้ หรือที่อยู่ตามสิทธิ์ข้อมูล:
- Expected raw predictions และ tolerance ที่เลือกพร้อมเหตุผล:
- ผลตรวจ notebook ↔ app / test log reference:
- ข้อจำกัดและสถานการณ์ที่ไม่ควรอ้างผลเกินข้อมูล:
- Monitoring observations / review trigger:

M5 ตรวจ checksum และโหลด artifact ตัวนี้จริงก่อนต่อแอป ถ้าเปลี่ยน artifact หรือ schema ให้เปลี่ยนรุ่นและตรวจ parity ใหม่
