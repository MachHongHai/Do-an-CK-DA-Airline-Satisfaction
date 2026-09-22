# Đồ án cuối kỳ môn Lập trình Phân tích dữ liệu UEH – Phân tích mức độ hài lòng của hành khách hàng không

Đồ án phân tích bộ dữ liệu **Airline Passenger Satisfaction** nhằm tìm hiểu mức độ hài lòng của hành khách theo hạng vé, mục đích chuyến đi, loại khách hàng, thời gian trễ và các tiêu chí dịch vụ.

## Dữ liệu

Nguồn:  
https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction

Dataset gốc gồm `train.csv` và `test.csv`. Hai file được gộp thành `airline.csv` để phục vụ phân tích.

## Phương pháp

- Thống kê mô tả
- Trực quan hóa dữ liệu
- Chi-square test
- Cramér's V
- Mann–Whitney U test

## Công cụ

Python, Pandas, Matplotlib, SciPy và Visual Studio Code.

## Cấu trúc

```text
data/
├── raw/
│   ├── train.csv
│   └── test.csv
├── airline.csv
└── airline_clean.csv

00_gop_du_lieu.py
01_doc_du_lieu.py
02_kiem_tra_du_lieu.py
03_tien_xu_ly.py
04_thong_ke_mo_ta.py
05_phan_tich_nhom_hanh_khach.py
06_phan_tich_delay.py
07_phan_tich_dich_vu.py
08_phan_tich_tuoi_khoang_cach.py
09_kiem_dinh.py
```

## Cách chạy

Cài thư viện:

```bash
pip install -r requirements.txt
```

Sau đó chạy lần lượt:

```bash
python 00_gop_du_lieu.py
python 01_doc_du_lieu.py
python 02_kiem_tra_du_lieu.py
python 03_tien_xu_ly.py
```

Các file từ `04` đến `09` dùng để thực hiện thống kê mô tả, trực quan hóa và kiểm định.
