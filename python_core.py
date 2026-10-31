raw_devices = [
    {"device_code": "D301", "type": "laptop", "price": 18500000, "status": "in_stock"},
    {"device_code": "d101 ", "type": "phone", "price": 6900000, "status": "in_stock"},
    {"device_code": "D202", "type": "tablet", "price": 9500000, "status": "out_of_stock"},
    {"device_code": "D102", "type": "phone", "price": 4200000, "status": "discontinued"},
    {"device_code": "D302", "type": "laptop", "price": 22000000, "status": "in_stock"}
]

def clean_and_validate_devices(devices):
    valid_devices = []

    for device in devices:
        code = device["device_code"].strip().upper()
        if code[0] == "D" and code[1:].isdigit():
            device["device_code"] = code
            valid_devices.append(device)

    return valid_devices

print(clean_and_validate_devices(raw_devices))

def search_device(devices, price, status):
    find_device = []

    for device in devices:
        if status is None:
            if device["price"] <= price:
                find_device.append(device)
    return find_device

print(search_device(raw_devices, 6000000))
