# =====================================================
# ĐỒ ÁN: ỨNG DỤNG QUẢN LÝ BẢO HÀNH SẢN PHẨM
# PHẦN NGƯỜI 4 - TUẦN 3 ĐẾN TUẦN 5
# =====================================================


# =====================================================
# 1. CLASS TÀI KHOẢN
# =====================================================

class TaiKhoan:
    def __init__(self, ten_dang_nhap, mat_khau, vai_tro):
        self.ten_dang_nhap = ten_dang_nhap
        self.mat_khau = mat_khau
        self.vai_tro = vai_tro

    def dang_nhap(self, mat_khau):
        return self.mat_khau == mat_khau

    def hien_thi(self):
        print("Tên đăng nhập:", self.ten_dang_nhap)
        print("Vai trò:", self.vai_tro)


# =====================================================
# 2. CLASS THỐNG KÊ
# =====================================================

class ThongKe:
    def __init__(self, danh_sach_phieu):
        self.danh_sach_phieu = danh_sach_phieu

    def tong_so_phieu(self):
        return len(self.danh_sach_phieu)

    def thong_ke_trang_thai(self):
        ket_qua = {}

        for phieu in self.danh_sach_phieu:
            trang_thai = phieu["trang_thai"]

            if trang_thai not in ket_qua:
                ket_qua[trang_thai] = 0

            ket_qua[trang_thai] += 1

        return ket_qua

    def thong_ke_loi(self):
        ket_qua = {}

        for phieu in self.danh_sach_phieu:
            loi = phieu["loi"]

            if loi not in ket_qua:
                ket_qua[loi] = 0

            ket_qua[loi] += 1

        return ket_qua

    def hien_thi_thong_ke(self):
        print("\n===== THỐNG KÊ BẢO HÀNH =====")

        print("Tổng số phiếu:", self.tong_so_phieu())

        print("\nTheo trạng thái:")
        for trang_thai, so_luong in self.thong_ke_trang_thai().items():
            print("-", trang_thai, ":", so_luong)

        print("\nTheo lỗi:")
        for loi, so_luong in self.thong_ke_loi().items():
            print("-", loi, ":", so_luong)


# =====================================================
# 3. DỮ LIỆU MẪU
# =====================================================

tai_khoan_admin = TaiKhoan(
    "admin",
    "123",
    "Quản trị viên"
)

tai_khoan_nhan_vien = TaiKhoan(
    "nhanvien",
    "123",
    "Nhân viên"
)


danh_sach_phieu = [
    {
        "ma_phieu": "BH001",
        "san_pham": "Laptop",
        "loi": "Lỗi pin",
        "trang_thai": "Đang sửa"
    },
    {
        "ma_phieu": "BH002",
        "san_pham": "Điện thoại",
        "loi": "Vỡ màn hình",
        "trang_thai": "Đã tiếp nhận"
    },
    {
        "ma_phieu": "BH003",
        "san_pham": "Máy in",
        "loi": "Không lên nguồn",
        "trang_thai": "Đã hoàn tất"
    },
    {
        "ma_phieu": "BH004",
        "san_pham": "Laptop",
        "loi": "Lỗi pin",
        "trang_thai": "Đang sửa"
    }
]


# =====================================================
# 4. CHƯƠNG TRÌNH CHẠY THỬ
# =====================================================

print("===================================")
print("  QUẢN LÝ BẢO HÀNH SẢN PHẨM")
print("===================================")

# Kiểm tra tài khoản
print("\n--- THÔNG TIN TÀI KHOẢN ---")

tai_khoan_admin.hien_thi()

if tai_khoan_admin.dang_nhap("123"):
    print("Đăng nhập: Thành công")
else:
    print("Đăng nhập: Thất bại")


# Thống kê
thong_ke = ThongKe(danh_sach_phieu)

thong_ke.hien_thi_thong_ke()

