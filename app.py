import streamlit as st

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

st.title("💰 APP TÍNH LÃI GỬI TIẾT KIỆM")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi và tổng số tiền nhận được.")

# =========================
# NHẬP DỮ LIỆU
# =========================

so_tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=10000000.0,
    step=100000.0,
    format="%.0f"
)

ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    value=12,
    step=1
)

lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

# =========================
# TÍNH TOÁN
# =========================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Lãi suất chuyển từ % sang số thập phân
    lai_suat_nam = lai_suat / 100

    # Tổng tiền lãi trong toàn bộ kỳ hạn
    tong_tien_lai = so_tien_gui * lai_suat_nam * ky_han / 12

    # Xác định số kỳ nhận lãi
    if hinh_thuc == "Cuối kỳ":
        so_ky = 1
        tien_lai_dinh_ky = tong_tien_lai

    elif hinh_thuc == "Hàng tháng":
        so_ky = ky_han
        tien_lai_dinh_ky = tong_tien_lai / so_ky

    else:  # Hàng quý
        so_ky = ky_han / 3

        # Nếu kỳ hạn không chia hết cho 3,
        # vẫn tính mức lãi trung bình theo quý
        tien_lai_dinh_ky = tong_tien_lai / so_ky

    tong_tien = so_tien_gui + tong_tien_lai

    # =========================
    # HIỂN THỊ KẾT QUẢ
    # =========================

    st.success("✅ Tính toán thành công!")

    st.subheader("📊 KẾT QUẢ")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "💵 Tiền lãi định kỳ",
            f"{tien_lai_dinh_ky:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "📈 Tổng tiền lãi",
            f"{tong_tien_lai:,.0f} VNĐ"
        )

    st.metric(
        "💰 Tổng tiền gốc + lãi",
        f"{tong_tien:,.0f} VNĐ"
    )

    # =========================
    # THÔNG TIN CHI TIẾT
    # =========================

    st.divider()

    st.write("### 📋 Thông tin khoản gửi")

    st.write(f"**Số tiền gửi:** {so_tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}"
