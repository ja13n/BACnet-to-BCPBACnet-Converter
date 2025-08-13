# Troubleshooting Guide

## Common Issues

### "No devices found with Distech Controls"
**Cause**: Station contains no compatible Distech devices
**Solution**: Verify device models match supported patterns (ECB/ECC/ECY/S-100)

### "XML parsing failed: Root element is None"
**Cause**: Corrupted or invalid XML in config.bog
**Solution**: Use a different backup or check original station integrity

### "config.bog file not found"
**Cause**: Invalid .dist file structure
**Solution**: Verify backup was created properly from Niagara station

## Error Codes
- ERR001: Archive extraction failure
- ERR002: XML namespace conflict
- ERR003: Missing tuning policy configuration
- ERR004: Device handle mismatch

## Recovery Procedures
All conversions maintain original .dist integrity with automatic rollback capability.
