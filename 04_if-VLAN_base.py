# Create a simple IF function that compares nativeVLAN and dataVLAN values and prints result.
def vlans(native_vlan, data_vlan):
    if native_vlan == data_vlan:
        result = "Match"
    else:
        result = "No Match"
    print(f"Comparison result: {result}")
    print(f"Native VLAN: {native_vlan}, Data VLAN: {data_vlan}")
native_vlan = 10
data_vlan = 30
vlans(native_vlan, data_vlan)