def calculate_emi(principal, annual_rate, months):
    # Chuyển lãi suất năm thành lãi suất tháng
    r = annual_rate / 12 / 100

    # Trường hợp lãi suất bằng 0
    if r == 0:
        emi = principal / months
    else:
        emi = principal * (
            r * (1 + r) ** months
        ) / ((1 + r) ** months - 1)

    # Tính tổng tiền lãi
    total_interest = emi * months - principal

    # Trả về 2 giá trị dưới dạng tuple
    return emi, total_interest


# Ví dụ kiểm tra
emi, total_interest = calculate_emi(
    1000000000, 12, 12
)

print(f"Tiền trả mỗi tháng: {emi:,.0f} VND")
print(f"Tổng tiền lãi: {total_interest:,.0f} VND")
