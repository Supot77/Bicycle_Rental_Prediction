# โมเดลที่กลุ่มสร้างภายหลัง

ยังไม่มีโมเดลในโครงเริ่มต้น สมาชิกต้องทดลองและเลือกจากหลักฐานเอง

เมื่อทำถึงช่วงบันทึกโมเดล ให้เก็บ pipeline รวม preprocessing หรือไฟล์ที่มีรุ่นสอดคล้องกัน พร้อมรายการ feature หน่วย รุ่น Python/ไลบรารี ช่วงข้อมูลฝึก และผลประเมินของ artifact ตัวที่จะใช้จริง

ค่าเริ่มต้น Git ไม่ติดตาม model binaries เพื่อป้องกันการใส่ไฟล์ทดลองที่ไม่ทราบที่มา หลังตรวจและตัดสินใจเผยแพร่แล้ว ให้เลือกวิธีเก็บ artifact หรือดาวน์โหลดระหว่างติดตั้ง พร้อมวิธีตรวจรุ่น/ความครบถ้วนใน README และทดสอบ deploy ใหม่

โหลดเฉพาะไฟล์ joblib/pickle ที่กลุ่มสร้างหรือเชื่อถือที่มา ไม่โหลดไฟล์ที่คนอื่นส่งมาโดยไม่ตรวจ
# Current application model

The user authorized promotion of personal run `20261028T153400574248Z`. `final_pipeline.joblib` is the tuned Random Forest pipeline with time features. Keep it with `input_schema.json`, `model_metadata.json`, and the repository-root `personal_features.py` module. The app checks the model and feature-module hashes before predicting.

See [release evidence and limitations](../docs/PERSONAL_MODEL_RELEASE_2026-10-28.md). The older scaffold guidance below is retained for reference.
