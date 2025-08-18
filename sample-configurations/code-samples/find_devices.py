def find_devices_with_vendor(root):
    """
    Finds elements with t='bac:BacnetDevice' and where 'n' matches a regex pattern.
    If a match is found, replaces t='bac:BacnetDevice' with t='bcs3:BcpBacnetDevice'.
    """
    regex_pattern = re.compile(r"^(EC[CYB]|S-100)(?:[-_\s].*)?$")

    matching_devices = []
    for device in root.xpath(".//p[@t='bac:BacnetDevice' or @t='bcnt:BacnetDevice' or @t='bcs3:BcpBacnetDevice']"):
        # Search for 'modelName' attributes in descendants of the device
        for grandchild in device.xpath('.//p[@n="modelName"]'):
            model_name_value = grandchild.attrib.get("v")  # Extract the 'v' attribute
            if model_name_value and re.match(regex_pattern, model_name_value):
                # Replace `t` attribute and add the device to the list
                device.attrib['t'] = 'bcs3:BcpBacnetDevice'
                matching_devices.append(device)
            else:
                pass
    return matching_devices
