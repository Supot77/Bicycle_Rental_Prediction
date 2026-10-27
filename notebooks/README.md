# Notebook สำหรับ Google Colab เท่านั้น

เปิดลิงก์ด้านล่างแล้วบันทึกสำเนาใน Drive สมาชิกเป็นผู้ลงมือเขียน split/preprocessing ฝึกโมเดลและสรุปผลเอง

อ่าน [Workflow สำหรับสมาชิก 5 คน](../docs/WORKFLOW_5_MEMBERS_TH.md) ก่อนรับงาน: M1 ดู 01–02, M2 ดู 03 และ final pipeline, M3/M4 แยกสำเนา 04 สำหรับอัลกอริทึม A/B แล้วรวมผลร่วมกัน ส่วน M5 ดู 05 และ app.py ทุกคนทำ 00 และตรวจรับงานของเพื่อน

| ลำดับ | เปิดใน Colab | งานของสมาชิก |
| --- | --- | --- |
| 00 | [เปิด notebook 00](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/00_orientation.ipynb) | ฝึก Python พื้นฐานด้วยตัวเลขสมมติ ทำได้ก่อนรับข้อมูล |
| 01 | [เปิด notebook 01](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/01_understand_dataset.ipynb) | ยืนยัน schema หน่วยและ data dictionary |
| 02 | [เปิด notebook 02](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/02_explore_quality.ipynb) | ตรวจคุณภาพและสร้างกราฟ |
| 03 | [เปิด notebook 03](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/03_split_and_preprocess.ipynb) | ออกแบบ split และ preprocessing |
| 04 | [เปิด notebook 04](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/04_models_and_evaluation.ipynb) | ทดลอง baseline และ 2 อัลกอริทึม |
| 05 | [เปิด notebook 05](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/05_app_testing_monitoring.ipynb) | ต่อแอป AppTest, testing และ monitoring |

Cell เตรียมงานจะ clone repository เมื่อ runtime ยังไม่มี แต่จะไม่เขียนทับ/pull งานเดิม ดูวิธีจัดการไฟล์และสำรองใน [คู่มือเริ่มต้น](../docs/START_HERE_TH.md)

ทุก notebook ต้องรันจากต้นได้โดยไม่พึ่งตัวแปรที่ค้างในอีกไฟล์ Notebook ที่เปิดจากหน้าเว็บกับไฟล์ .ipynb ในโฟลเดอร์ที่ clone เป็นคนละสำเนา ต้องบันทึกฉบับที่แก้จริงจากหน้า notebook เมื่อส่งงาน

โครงเริ่มต้นรันได้ในสถานะรอ dataset แต่ข้อความรอข้อมูลไม่ใช่การทำแบบฝึก ML เสร็จ เก็บผลจริงตามสิทธิ์ก่อนล้าง outputs และ execution counts แล้วส่งผ่านเว็บ GitHub

## Notebook แยกตามสมาชิก 5 คน

ไฟล์ Colab ของ M1–M5 ถูกบันทึกไว้ในโฟลเดอร์ Drive ของแต่ละบทบาทแล้ว เปิดไฟล์ของตัวเองจาก Drive เพื่อทำงานและบันทึกได้เลย หากเปิดแม่แบบจาก GitHub ให้เลือก **File → Save a copy in Drive** แล้วเก็บสำเนาไว้ในโฟลเดอร์ `notebooks` ของตัวเอง แต่ละบัญชีมี Colab runtime แยกกัน ช่องโค้ดวิเคราะห์/เทรนเว้นไว้ให้สมาชิกเขียนเอง มีเพียงโค้ดเชื่อม Drive สร้างโฟลเดอร์ และคัดลอกไฟล์ผลลัพธ์ให้พร้อมใช้

| สมาชิกตัวอย่าง | งานนำ | เปิดใน Colab |
| --- | --- | --- |
| M1 | ความหมายข้อมูลและ EDA | [M1 · Data / EDA](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/team/M1_data_eda.ipynb) |
| M2 | split และ preprocessing | [M2 · Split / Preprocessing](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/team/M2_split_preprocess.ipynb) |
| M3 | baseline และโมเดล A | [M3 · Baseline / Model A](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/team/M3_baseline_model_a.ipynb) |
| M4 | โมเดล B และประเมินผล | [M4 · Model B / Evaluation](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/team/M4_model_b_evaluation.ipynb) |
| M5 | แอปและเตรียม deploy | [M5 · App / Deploy](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/team/M5_app_deploy.ipynb) |

โฟลเดอร์ Drive สำหรับเก็บสำเนา notebook, outputs และ handoff แยกตาม M1–M5 แชร์ให้สมาชิกที่ได้รับเชิญแล้ว ลิงก์โฟลเดอร์ส่งให้กลุ่มแยกจาก repository
