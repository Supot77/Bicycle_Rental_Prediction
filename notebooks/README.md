# Notebook สำหรับ Google Colab เท่านั้น

เปิดลิงก์ด้านล่างแล้วบันทึกสำเนาใน Drive สมาชิกเป็นผู้ลงมือเขียน split/preprocessing ฝึกโมเดลและสรุปผลเอง

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
