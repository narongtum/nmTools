
แยก module ที่ใช้งานออกมาเปลี่ยนชื่อเป็นมี suffix ว่า eh_  (ย่อมาจาก enhancement) เพื่อไม่ให้ทับซ้อนกับของเก่า โดย module ที่ remake ใหม่จะมีการอับเกรดคร่าวๆดังนี้
- ใช้ระบบ matrix orient scale, constraint จาก from function.rigging.constraint import matrixConstraint as mtc แทน parentConstraint ดั่งเดิม
- ปรับปรุงlogic ที่ผิดพลาด แก้ชื่อที่เขียนไม่ถูกต้อง(ถ้ามี) ลดการทำงานที่ซ้ำซ้อน หรือ refractor(ถ้าจำเปน)
- แต่ระบบต้องทำงานได้ ไม่ปรับเปลี่ยนมากเกินไป หากเกิดข้อผิดพลาดขึ้นสามารถกลับไปดู module ดั่งเดิมและทำการแก้ไขให้กลับมาได้