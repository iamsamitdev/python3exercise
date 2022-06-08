# ไม่ต้องระบุชนิดข้อมูลของตัวแปร
a = 3
b = 4.95
c = "python programming"

print(a)
print(b)
print(c)
print(a, b, c)

# สามารถสร้างตัวแปรหลายตัวพร้อมกันในบรรทัดเดียว
x = y = z = 10
j, k = 5, 15

print(x, y, z)
print(j, k)

# Boolean
status = True
msg = False

print(status, msg)

# ตัวแปรแสดงร่วมกับข้อความ
# วิธีที่ 1 ใช้ concat string
print("ราคาสินค้าต่อชิ้น", b, "บาท มีจำนวน", a, "ชิ้น")

# วิธีที่ 2 ใช้ interpolation string
print("ราคาสินค้าต่อชิ้น %.2f บาท มีจำนวน %d ชิ้น" % (b, a))

# วิธีที่ 3 ใช้ format string
print(f"ราคาสินค้าต่อชิ้น {b} บาท มีจำนวน {a} ชิ้น")
