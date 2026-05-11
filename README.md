# OOP - TÀI XỈU
- [Slides trình bày](https://www.canva.com/design/DAHIuCPVGoo/r6ZzTTugDx_R_Di2VVKHdA/edit)
- Dự án này sử dụng lập trình hướng đối tượng (OOP) trong C++ để mô phỏng và phân tích hiệu quả của các chiến thuật đặt cược khác nhau trong trò chơi Tài Xỉu. Dữ liệu sau khi mô phỏng sẽ được xử lý và vẽ biểu đồ bằng Python để đưa ra cái nhìn trực quan về rủi ro và lợi nhuận.
- ## 📌 Tính năng chính
- **Mô phỏng đa dạng chiến thuật:** Cố định, Gấp đôi khi thua (Martingale), Fibonacci, 1-3-2-6, và nhiều hơn nữa.
- **Phân tích xác suất:** Thống kê chi tiết tần suất xuất hiện các mặt xúc xắc, tổng điểm và xác suất thắng/thua.
- **Dữ liệu lớn:** Khả năng mô phỏng hàng triệu ván chơi với độ chính xác cao.
- **Trực quan hóa:** Chuyển đổi dữ liệu CSV thành biểu đồ đường và biểu đồ cột để so sánh biến động vốn.
- ## 🛠 Yêu cầu hệ thống
- **C++:** Trình biên dịch hỗ trợ chuẩn C++11 trở lên (GCC/G++, MSVC, hoặc Clang).
- **Python 3.x:** Cần cài đặt các thư viện sau để vẽ biểu đồ:
  
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  
  Bash  
  
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  
  <!---->
  <!---->
  
  <!---->
  
  <!---->
  
  ```
  pip install pandas matplotlib seaborn
  ```
  
  <!---->
  
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
- ## 🚀 Hướng dẫn sử dụng
  
  Để có kết quả phân tích cuối cùng, bạn cần thực hiện theo đúng trình tự 2 bước sau:  
- ### Bước 1: Chạy chương trình mô phỏng (C++)
  
  Biên dịch và thực thi file `.cpp` để thực hiện tính toán và tạo dữ liệu thô.  
  
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  
  Bash  
  
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  
  <!---->
  <!---->
  
  <!---->
  
  <!---->
  
  ```
  g++ main.cpp -o simulation
  ./simulation
  ```
  
  <!---->
  
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  
  **Kết quả:** Chương trình sẽ xuất ra 3 file dữ liệu quan trọng:  
- `xac_suat.csv`: Chứa thống kê xác suất lý thuyết và thực tế.
- `ket_qua.csv`: Chứa bảng tổng kết hiệu quả của từng chiến thuật.
- `ban_ghi.csv`: Ghi lại biến động vốn theo từng mốc thời gian (dùng để vẽ biểu đồ đường).
- ### Bước 2: Trực quan hóa dữ liệu (Python)
  
  Sau khi đã có các file `.csv`, chạy script Python để tạo các biểu đồ phân tích.  
  
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  
  Bash  
  
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  
  <!---->
  <!---->
  
  <!---->
  
  <!---->
  
  ```
  python plot_results.py
  ```
  
  <!---->
  
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  <!---->
  
  **Kết quả:** Các biểu đồ về biến động số dư và tỷ lệ lợi nhuận sẽ được hiển thị hoặc lưu dưới dạng hình ảnh.  
- ## 📁 Cấu trúc dự án
- `TaiXiu.cpp`: Mã nguồn chính thực hiện logic mô phỏng và quản lý các lớp (NhaCai, ConBac, MoPhong).
- `plot.py`: Script Python xử lý dữ liệu và vẽ biểu đồ.
- `*.csv`: Các file dữ liệu trung gian được tạo ra sau khi chạy C++.
- ## 📊 Các chiến thuật được mô phỏng
- **Cố định (Fixed Bet):** Luôn đặt một mức cược duy nhất.
- **Gấp đôi khi thua (Martingale):** Gấp đôi mức cược sau mỗi lần thua để gỡ vốn.
- **Fibonacci:** Cược theo dãy số Fibonacci để giảm áp lực tăng tiền cược quá nhanh.
- **1-3-2-6:** Hệ thống cược theo chu kỳ để tối ưu lợi nhuận khi thắng chuỗi.
- **Tăng/Giảm 1 đơn vị (D'Alembert):** Tăng cược nhẹ khi thua và giảm nhẹ khi thắng.
  
---
  
  *Dự án này được phát triển cho mục đích học tập và nghiên cứu về xác suất thống kê trong lập trình.*
