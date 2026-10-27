# เชื่อมงานกับเกณฑ์อาจารย์

ยึด [โจทย์ฉบับอาจารย์](https://docs.google.com/document/d/1VuLwvOmVn9uPh-byMeTfYcuIYrbqskXJ1zU9ibKhWyM) เป็นหลัก ตารางนี้ช่วยหาหลักฐาน ไม่ใช่การรับรองคะแนน

| รายการ | คะแนนเต็ม | งาน/หลักฐานที่สมาชิกต้องทำ |
| --- | ---: | --- |
| ปัญหาและแนวทาง CO1 | 5 | ขอบเขต ผู้ใช้ X/y เหตุผลที่ใช้ ML |
| วิเคราะห์ข้อมูลและประสิทธิภาพ CO1 | 5 | notebook 02 และการตีความ error ใน 04 |
| ออกแบบ CO2 | 5 | notebook 03 เหตุผลเลือก feature/preprocessing/split และ data risks |
| พัฒนาโมเดล CO2 | 10 | notebook 04: baseline เพิ่มจาก 2 อัลกอริทึม พร้อม settings |
| ประเมินและเลือก CO2 | 10 | MAE/RMSE/R² เทียบ split เดียวกัน แยก test และวิเคราะห์ error |
| ข้อจำกัดและปรับปรุง CO2 | 5 | เชื่อมข้อเสนอเข้ากับผลจริงและทรัพยากร |
| Python ทำซ้ำได้ CO3 | 5 | รันจากต้นได้ dependencies/paths/seeds และ README |
| เชื่อมโมเดลกับ dashboard CO3 | 5 | โหลด preprocessing+model ถูกชุด ผลตรงกับ notebook |
| Input validation และ testing CO3 | 5 | normal/boundary/invalid และ test log ที่มีผลจริง |
| Deploy และ monitoring CO3 | 5 | แอปออนไลน์ logs/records ที่ดูจริงและ review trigger |
| สาธิตการใช้งาน CO3 | 5 | กรณีใหม่และอธิบาย output ได้ |
| สาธิตความเข้าใจ/ผลงาน CO3 | 5 | ทุกคนอธิบายโค้ดและวิธีตรวจ AI ได้ |
| สาธิต testing/troubleshooting CO3 | 5 | ลอง boundary/invalid ชี้โค้ดและไล่สาเหตุ |
| สาธิต deploy/monitoring CO3 | 5 | เปิดแอปและหลักฐาน อธิบายข้อจำกัด/วิธีอัปเดต |

รวมรายงาน 40 โค้ด 20 และสาธิต 20 เท่ากับ 80 คะแนน สูตรต่อหัวข้อคือ (ระดับ ÷ 4) × คะแนนเต็ม ไม่คูณ 80% ซ้ำ ไม่มีหลักฐานประเมินได้เป็น 0

## รายการงานส่ง

- รายงาน PDF ประมาณ 8–12 หน้า ไม่รวมปก อ้างอิง และภาคผนวก
- Notebook หรือ Python training script ที่รันได้ app.py requirements.txt โมเดลและ preprocessing และ README ที่ทำตามได้
- ข้อมูลที่อนุญาตให้แจก หรือแหล่งที่มาและวิธีเข้าถึงที่ถูกต้อง ระบุการกรอง/สุ่มที่ใช้
- ลิงก์ GitHub และแอป Streamlit ที่ผู้ประเมินเข้าถึงได้
- ผลเทียบโมเดล screenshots, test log และ monitoring observations
- สมาชิกทั้ง 5 พร้อมรหัส งานเฉพาะและหลักฐาน อย่างน้อย 5 representative prompts คนละช่วงพร้อมวิธีตรวจ/แก้

เวลาสาธิตที่เอกสารเสนอคือ 10 นาที + ถามตอบ 5 นาที กำหนดจริงและนโยบายคะแนนรายบุคคลให้ยึดประกาศอาจารย์
