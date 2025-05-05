# test_transaction.py

from transaction import Transaction

# Tạo giao dịch mẫu
tx1 = Transaction("Alice", "Bob", 100.5)

# In thông tin giao dịch ra màn hình
print("Người gửi:", tx1.sender)
print("Người nhận:", tx1.receiver)
print("Số tiền:", tx1.amount)
print("Thời gian:", tx1.timestamp)
