# เรียนรู้และลงมือผ่าน notebook

Notebook มีคำถามนำทางและพื้นที่ให้ทำเอง ไม่มี split, preprocessing, การฝึก หรือข้อสรุปที่เลือกแทนสมาชิก

| ลำดับ | งานของสมาชิก | ทำก่อนรับข้อมูลได้หรือไม่ |
| --- | --- | --- |
| [00 orientation](00_orientation.ipynb) | เรียนรู้ cell, ตาราง, target และค่าเฉลี่ยจากตัวเลขสมมติ | ได้ |
| [01 understand dataset](01_understand_dataset.ipynb) | ยืนยันข้อมูลและเติม data dictionary/config | อ่านคำถามก่อนได้ การวิเคราะห์รอไฟล์ |
| [02 explore quality](02_explore_quality.ipynb) | ตรวจคุณภาพ สร้างกราฟและอธิบายสิ่งที่พบ | งานจริงรอไฟล์ |
| [03 split and preprocess](03_split_and_preprocess.ipynb) | เลือกและเขียนวิธี split/preprocessing | เตรียมแนวคิดได้ แต่ยังไม่ล็อกวิธี |
| [04 models and evaluation](04_models_and_evaluation.ipynb) | ทำ baseline และ 2 อัลกอริทึม เปรียบเทียบ/เลือกจากหลักฐาน | รอ 01–03 |
| [05 app testing monitoring](05_app_testing_monitoring.ipynb) | โหลด artifact ต่อแอป ตรวจผล deploy และ monitoring | อ่านแผนก่อนได้ งานจริงรอ artifact |

เปิดผ่าน JupyterLab ตาม START_HERE หรือ [เลือก notebook จาก GitHub ใน Colab](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/)

หลังติดตั้ง environment ครั้งแรก ใน JupyterLab เลือก kernel ของ `.venv` ที่ใช้ หากเครื่องมีหลาย Python ตรวจ `sys.executable` ใน cell ก่อนลงไลบรารีเพิ่ม

แต่ละ notebook ต้องรันจากต้นได้โดยไม่พึ่งตัวแปรที่ค้างจากไฟล์อื่น เมื่อนำโค้ดที่ทำแล้วมาใช้ต่อ ให้เลือกคัดลอกเป็นขั้นตอนครบหรือแยกเป็นฟังก์ชันร่วม พร้อมตรวจว่าเปลี่ยนแล้วส่วนอื่นยังทำงาน

โครงเริ่มต้นรันได้ในสถานะยังไม่มีข้อมูล แต่การรันผ่านข้อความ “รอ dataset” ไม่ใช่การทำแบบฝึก ML เสร็จ เก็บกราฟ/ผลที่ทำจริงเป็นหลักฐานแยกตามสิทธิ์ แล้วล้าง outputs และ execution counts ก่อน commit
