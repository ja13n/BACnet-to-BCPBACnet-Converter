# BACnet to BCPBACnet Conversion Guide

## Overview
Step-by-step guide for preparing and executing station conversions.

## Pre-Conversion Checklist
- [ ] Verify Niagara station backup (.dist file) availability
- [ ] Confirm Distech Controllers are present (ECB//ECY series)
- [ ] Ensure BCPBACnet licensing is in place
- [ ] Create additional backup of original .dist file

## Supported Device Models
- ECB Series: Environmental Control Modules
- ECY Series: Advanced Controllers
  
## Conversion Process
1. Place .dist backup in working director
2. Run conversion script and type in the name of the backup without .dist at the end.
3. Monitor conversion logs for progress
4. Validate converted configuration

## Post-Conversion Verification
- Check device connectivity
- Verify point mappings
- Test BCPBACnet communication
- Confirm tuning policy application
