# เริ่มต้นบน Google Colab

สมาชิกใช้ hosted Google Colab เป็นช่องทางเดียวสำหรับเขียนโค้ด วิเคราะห์ข้อมูล ฝึกโมเดล และทดสอบ ส่วน GitHub เก็บไฟล์ที่ตกลงส่ง และ Streamlit Community Cloud เผยแพร่แอปตามโจทย์อาจารย์

## 1. เปิดและเก็บสำเนา notebook

เปิด [Notebook 00](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/00_orientation.ipynb) ลงชื่อเข้า Google แล้วใช้ File → Save a copy in Drive ตั้งชื่อให้ทราบว่าใครรับผิดชอบงานใด ใช้ CPU runtime เริ่มต้นได้ ไม่ต้องเลือก GPU สำหรับโครงเริ่มต้น

รันทีละ cell ด้วย Shift+Enter อ่านข้อความและลองแบบฝึก เมื่อถึง notebook ถัดไปเปิดจาก [รายการลิงก์ Colab](../notebooks/README.md) และบันทึกสำเนางานของตนเองเช่นกัน

## 2. เตรียม repository ใน runtime

Cell เตรียมงานใน notebook จะ clone repository ถ้ายังไม่มีใน runtime แล้วอ่าน config ให้ ถ้ามีโฟลเดอร์เดิมอยู่แล้วจะใช้ต่อ เพื่อไม่เขียนทับงานที่กำลังแก้ ไม่มีการ pull หรือ reset งานให้อัตโนมัติ

หากต้องการโค้ดรุ่นใหม่จากเพื่อน ให้สำรองไฟล์ตนเองก่อน แล้วเปิด runtime ใหม่และรัน cell เตรียมงาน ห้ามลบ/reset โฟลเดอร์เพื่อแก้ปัญหาโดยไม่ตรวจงานที่ยังไม่บันทึก

ใช้ไลบรารีหลักที่ Colab มีอยู่ก่อน Cell จะติดตั้งเฉพาะตัวที่ขาด Notebook 05 จะเพิ่ม Streamlit สำหรับ AppTest ผ่าน requirements-colab.txt ไม่ใช้ requirements-dev.txt และไม่บังคับเปลี่ยน pandas/NumPy/scikit-learn ของ runtime ให้เป็นรุ่นเดียวกับเครื่องอื่น

## 3. จัดการไฟล์ใน Colab

เปิดแถบ Files ด้านซ้าย แล้วเข้า `/content/Bicycle_Rental_Prediction`

- เมื่อได้รับ dataset ให้อัปโหลดต้นฉบับเข้า `data/raw/` และเก็บต้นฉบับอีกสำเนาในพื้นที่ Drive ที่กลุ่มมีสิทธิ์ใช้
- ดับเบิลคลิก `config/project.json` เพื่อแก้เส้นทางและค่าที่ได้ยืนยันแล้ว ใช้เส้นทางเช่น `data/raw/ชื่อไฟล์จริง.csv`
- แก้ `app.py` และไฟล์ข้อความอื่นจากตัวแก้ไขใน Files แล้วบันทึกไฟล์
- เก็บผลทดลอง กราฟ และหลักฐานใน results/evidence ตามแผน อย่าเผยแพร่ข้อมูลที่ยังไม่อนุญาต

ไฟล์ที่แชร์กับเพื่อนผ่าน Drive ไม่ได้ปรากฏใน runtime ของเพื่อนอัตโนมัติ ทุกคนต้องนำไฟล์รุ่นที่ตกลงมาไว้ตาม config ของตนเอง

## 4. ตรวจโครงงานจาก cell

หลังรัน cell เตรียมงานจะมีตัวแปร ROOT ใช้ Python ของ runtime เรียกตัวตรวจได้:

```python
import subprocess
import sys

subprocess.run([sys.executable, str(ROOT / 'scripts/check_setup.py')], check=True)
```

หลังเติม config และอัปโหลดข้อมูลแล้วจึงเพิ่ม `--require-data` ในรายการคำสั่ง หากยังรอข้อมูล ตัวตรวจแบบนี้จะหยุดพร้อมรายการที่ต้องเติม เป็นสถานะที่คาดหมาย

```python
subprocess.run([sys.executable, str(ROOT / 'scripts/check_setup.py'),
                '--require-data'], check=True)
```

## 5. ทดสอบแอปจาก notebook

Notebook 05 มี cell ติดตั้ง Streamlit และใช้ AppTest โหลด app.py เพื่อตรวจการทำงานภายใน notebook โดยยังไม่เปิดเว็บ server AppTest ช่วยตรวจพฤติกรรมแอป แต่การดูหน้าจอและทดสอบลิงก์จริงให้ทำบน Streamlit Community Cloud ในช่วง deploy

ไม่ต้องตั้ง tunnel หรือใช้ Colab เป็นเว็บโฮสต์ถาวร การเผยแพร่แอปยังทำตาม DEPLOYMENT_TH

## 6. สำรองก่อนปิดหรือเปลี่ยน runtime

Colab มี notebook กับไฟล์ใน runtime เป็นคนละส่วน:

| สิ่งที่แก้ | วิธีเก็บ |
| --- | --- |
| ข้อความ/โค้ด cell ในหน้า notebook | บันทึกสำเนาใน Drive และดาวน์โหลด .ipynb เมื่อส่งงาน |
| app.py, config, ตารางหลักฐาน, กราฟ และโมเดลใน Files | ดาวน์โหลดไฟล์ที่เปลี่ยน หรือคัดลอกไป Drive ที่มีสิทธิ์ ก่อน runtime ถูกลบ |
| dataset | เก็บต้นฉบับในพื้นที่ที่อาจารย์/กลุ่มอนุญาต ไม่แนบขึ้น repo โดยอัตโนมัติ |

การกด Save notebook ไม่สำรองไฟล์อื่นใน runtime และไฟล์ .ipynb ในโฟลเดอร์ที่ clone ไม่ได้อัปเดตตาม cell ที่แก้ในหน้าเว็บ ต้องบันทึก/ดาวน์โหลดจากหน้า notebook ที่ทำงานอยู่แยกกัน

หากต้องการคัดลอกไฟล์ไป Drive สามารถใช้ `from google.colab import drive` และ `drive.mount('/content/drive')` ใน cell แยก แล้วเลือกโฟลเดอร์ปลายทางที่กลุ่มตกลง การ mount ต้องให้เจ้าของบัญชีอนุญาต และการแชร์ notebook ไม่ได้แชร์ Drive ทั้งหมดให้เพื่อน

## 7. ส่งงานผ่านเว็บ

ทำตาม CONTRIBUTING: บันทึก notebook ล้าง output ที่ไม่ควรเผยแพร่ ดาวน์โหลดไฟล์ที่เปลี่ยน แล้วส่งผ่านเว็บ GitHub บน branch หรือ fork ให้เพื่อนตรวจ ไม่ต้องติดตั้ง Git ในเครื่องหรือใส่ token ใน notebook

งานแรกที่ทำได้ทันทีคือ notebook 00 จากนั้นรับงานเล็กหนึ่งชิ้นใน task board และบันทึก contribution เมื่อได้ทำจริง

## ถ้ารันไม่ผ่าน

| อาการ | สิ่งที่ตรวจ |
| --- | --- |
| หา config ไม่เจอ | รัน cell เตรียมงานก่อน และตรวจโฟลเดอร์ใน Files |
| ติดตั้งแพ็กเกจแล้วมีคำขอ restart | บันทึกงานและสำรองไฟล์ก่อน แล้วทำตามคำขอของ Colab จากนั้นรัน cell ที่จำเป็นใหม่ |
| dataset หายหลังเปลี่ยน runtime | อัปโหลดไฟล์จากสำเนาที่เก็บไว้ใหม่ ตรวจชื่อและ config ให้ตรง |
| ยังไม่กำหนด target | รอยืนยันความหมาย ไม่เดาขึ้นมาเพื่อให้ตัวตรวจผ่าน |
| ภาษาใน CSV อ่านไม่ได้ | ตรวจ encoding จากไฟล์ต้นฉบับ ไม่แก้ค่าข้อมูลโดยเดา |
| ผลแอปไม่ตรง notebook | ตรวจรุ่นโมเดล preprocessing feature order และรุ่นไลบรารี |

เมื่อขอความช่วยเหลือ ให้บอกคำสั่ง error และสิ่งที่คาดหวัง โดยไม่แนบข้อมูลที่ห้ามเผยแพร่

อ้างอิง: [Colab FAQ](https://research.google.com/colaboratory/faq.html), [Streamlit AppTest](https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest)
