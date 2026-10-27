# คู่มือเตรียม deploy เมื่อทำโมเดลและแอปแล้ว

ตอนนี้เปิด app.py ได้เพื่อดูโครงเริ่มต้น การเผยแพร่หน้านี้เพียงอย่างเดียวยังไม่ถือว่าส่งระบบทำนายครบตามโจทย์

## ก่อน deploy

1. ตรวจว่าได้ artifact ที่เลือกและประเมินแล้ว พร้อม preprocessing และ feature schema
2. บันทึกงานก่อนเปิด Colab runtime ใหม่ โหลดโมเดลที่สำรองไว้ และเทียบกับ notebook หลายกรณี ตรวจ app.py ด้วย AppTest ใน Colab
3. บันทึก Python และเวอร์ชัน dependencies ของ Colab ที่ฝึกจริง แล้วตั้ง environment บน Community Cloud ให้เข้ากันได้
4. จัดวิธีให้แอปเข้าถึง artifact โดยไม่ผูกกับ /content หรือ Drive mount ของ Colab และตรวจสิทธิ์ก่อนอัปโหลดผ่านเว็บ GitHub
5. เขียน README ฉบับรันจริงและทดสอบตาม normal/boundary/invalid

requirements-colab.txt เพิ่มเฉพาะ Streamlit โดยใช้ชุดไลบรารีพื้นฐานของ Colab ส่วน requirements.txt เป็นชุดเริ่มต้นสำหรับแอปบน Community Cloud ซึ่งยังอาจต่างจาก Colab จริง เมื่อฝึกโมเดลแล้วต้องอัปเดต dependencies ฝั่งแอปให้ตรงรุ่นที่จำเป็นและทดสอบโหลดซ้ำ ไม่ใช้ pip freeze ทั้ง Colab โดยไม่ทบทวน เพราะมีแพ็กเกจอื่นที่แอปไม่ได้ใช้

## บน Streamlit Community Cloud

เข้า [คู่มือทางการ](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app) เชื่อม GitHub และเลือก repository, branch และ app.py ตั้ง Python ให้สอดคล้องกับ artifact แล้ว deploy จากนั้นอ่าน logs หากติดตั้งหรือโหลดไม่สำเร็จ ชื่อเมนูให้ยึดหน้าจอปัจจุบัน

ไม่ต้องเชื่อม API อากาศเพื่อผ่านโจทย์ เว้นแต่กลุ่มเลือกขอบเขตที่จำเป็นและมีเวลา ถ้ามี secrets ใช้ระบบจัดการ secrets ไม่ commit ลง repo

## หลัง deploy

เปิดแอป Community Cloud จากอีก session ตรวจสิทธิ์ผู้ประเมิน เทียบ prediction กับ Colab notebook และเก็บ test log กับ screenshot ตามรุ่น ตรวจ logs หรือบันทึก input/prediction ที่ไม่อ่อนไหวจริง

เก็บสำเนาหลักฐานนอกพื้นที่ชั่วคราวของแอป หากยังไม่มีคำตอบจริง จะตรวจความผิดพลาดของระบบได้ แต่ยังวัดความแม่นของคำทำนายใหม่ไม่ได้

## เมื่อเปลี่ยนโมเดล

เปลี่ยน artifact, schema, preprocessing และ dependencies ให้ตรงรุ่น อัปเดตบันทึกที่มา รันการเทียบผลและ validation ซ้ำ แล้วตรวจแอปออนไลน์ ไม่ฝึกโมเดลใหม่ทุกครั้งที่ผู้ใช้กดปุ่มทำนาย
