# Log chat với AI — Thí nghiệm Mergesort CUTOFF

Ghi lại các lần dùng AI hỗ trợ trong quá trình làm thí nghiệm.

---

## 1. Kiểm tra cài đặt MergeSort và InsertionSort

Trước khi chạy thí nghiệm, nhờ AI xem qua 2 file code để chắc chắn đã cài đúng phần CUTOFF.

![kiemtracode](Ai_chat/kiemtracode.png)

---

## 2. Hỏi cách đo thời gian chạy trong Java

Không chắc nên dùng `currentTimeMillis` hay `nanoTime`, hỏi AI để chọn cái phù hợp hơn.

![Dothoigian](Ai_chat/Dothoigian.png)

---

## 3. Nhờ viết code sinh dữ liệu test

Nhờ AI viết phần sinh mảng test (random, sorted, reverse, nearly sorted) và script benchmark để tập trung vào phần cài đặt thuật toán chính.

![sinhtest](Ai_chat/sinhtest.png)

---

## 4. Nhờ viết code Python vẽ đồ thị

Sau khi có file dữ liệu thô, nhờ AI viết script vẽ line chart để trực quan hóa kết quả.

![vedothi](Ai_chat/vedothi.png)

---

## 5. Hỏi về sự khác biệt CUTOFF giữa các loại mảng

Thấy kết quả CUTOFF = 7 tốt nhất với mảng random nhưng CUTOFF = 6 lại tốt nhất với nearly sorted, hỏi AI giải thích tại sao.

![nhanxet1-1](Ai_chat/nhanxet1-1.png)

![nhanxet1-2](Ai_chat/nhanxet1-2.png)

---

## 6. Hỏi tại sao CUTOFF tối ưu thay đổi khi n lớn

Nhận thấy với n rất lớn thì CUTOFF tối ưu khác với n nhỏ, hỏi AI xem có liên quan đến cache CPU không.

![nhanxet2-1](Ai_chat/nhanxet2-1.png)

![nhanxet2-2](Ai_chat/nhanxet2-2.png)
