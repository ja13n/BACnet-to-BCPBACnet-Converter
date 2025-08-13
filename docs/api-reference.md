# API Reference

## Core Functions

### find_devices_with_vendor(root)
Identifies Distech Controllers using regex pattern matching
- **Parameters**: XML root element
- **Returns**: List of matching device elements
- **Pattern**: `^(EC[CYB]|S-100)(?:[-_\s].*)?$`

### append_new_elements_to_devices(xml_file, root, devices)
Adds BCPBACnet-specific elements to converted devices
- **Elements Added**: PollServiceOnCOV, restStatus, BcpParameters
- **Tuning Policy**: Automatic BcpPolicy injection

### clean_and_parse_xml(file_path)
Sanitizes XML content and creates parseable tree
- **Removes**: Null characters, invalid XML chars
- **Returns**: lxml ElementTree object

## Namespace Mappings
```python
replacements = {
    "bac:BacnetNetwork": "bcs3:BcpBacnetNetwork",
    "bac:BacnetPointDeviceExt": "bcs3:BcpBacnetPointDeviceExt",
    "bac:BacnetScheduleDeviceExt": "bcs3:BcpBacnetScheduleDeviceExt"
}
