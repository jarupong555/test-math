import math

def find_double_squares(x):
    """
    ฟังก์ชันสำหรับหาคู่ (a, b) ที่ทำให้ a^2 + b^2 = x
    Args:
        x (int): ค่าที่ต้องการตรวจสอบ
    Returns:
        list: รายการคู่ (a, b) ที่เป็นไปได้
    """
    pairs = []  # เก็บคู่ (a, b) ที่ตรงเงื่อนไข
    limit = int(math.sqrt(x)) + 1  # จำกัดค่า a ไม่เกิน √x
    for a in range(limit):  # ลองค่าของ a ตั้งแต่ 0 ถึง √x
        b_squared = x - a**2  # คำนวณ b^2 = x - a^2
        # ตรวจสอบว่า b^2 เป็นกำลังสองสมบูรณ์หรือไม่
        if b_squared >= 0 and int(math.sqrt(b_squared))**2 == b_squared:
            b = int(math.sqrt(b_squared))  # หา b จาก √(b^2)
            # หลีกเลี่ยงการนับซ้ำ เช่น (a, b) กับ (b, a)
            if (a, b) not in pairs and (b, a) not in pairs:
                pairs.append((a, b))  # เพิ่มคู่ (a, b) ลงในรายการ
    return pairs  # คืนค่ารายการคู่ (a, b)

def process_test_case(x):
    """
    ฟังก์ชันสำหรับประมวลผลข้อมูลแต่ละเคส
    Args:
        x (int): ค่าของ X ที่ต้องการตรวจสอบ
    Returns:
        str: ผลลัพธ์ที่จัดรูปแบบพร้อมจำนวนวิธีและคู่ที่หาได้
    """
    pairs = find_double_squares(x)  # หาคู่ (a, b) สำหรับค่า x
    return f"{len(pairs)} วิธี --> {pairs}"  # คืนค่าจำนวนวิธีและคู่ที่หาได้

def main():
    """
    ฟังก์ชันหลักสำหรับจัดการ Input/Output ของโปรแกรม
    """
    # อ่านจำนวนเคส
    num_cases = int(input("ใส่จำนวนเคส: "))
    results = []  # เก็บผลลัพธ์สำหรับทุกเคส
    
    # ประมวลผลแต่ละเคส
    for case in range(1, num_cases + 1):
        x = int(input(f"ใส่ค่า X สำหรับเคส #{case}: "))  # รับค่าของ X
        result = process_test_case(x)  # ประมวลผลเคส
        results.append(f"Case #{case}: {result}")  # จัดเก็บผลลัพธ์ในรูปแบบข้อความ
    
    # แสดงผลลัพธ์ทั้งหมด
    print("\n".join(results))

# จุดเริ่มต้นของโปรแกรม
if __name__ == "__main__":
    main()
