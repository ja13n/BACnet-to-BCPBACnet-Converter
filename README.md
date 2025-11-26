# BACnet-to-BCPBACnet-Converter
A specialized automation script for converting Niagara stations from standard BACnet protocol implementation to BCPBACnet (BACnet Secure Connect Protocol) configuration for Distech Controls devices.
 - Note: This repository showcases the technical approach and capabilities of the converter. The complete implementation includes proprietary algorithms and is available through commercial licensing agreements.

  # Overview
   - This project addresses the growing need for secure BACnet communications in building automation systems. As cybersecurity and networking requirements become more stringent, many facilities need to migrate from traditional BACnet to BCPBACnet for enhanced security and encrypted communications.
     
  # Prerequisites
   - Niagara 4.8+ or Niagara AX 3.8+.
   - Administrative access to target stations BCPBACnet license and certificates.
   - Network connectivity to all target devices.
   - Backup of the current Niagara station.

  # Key Features
   - Automated station backup processing: Direct manipulation of Niagara station backup files.
   - Archive Integrity: Maintains original station structure while updating internal configurations.
   - Backup Safety: Creates restoration points and handles conversion failures gracefully without corrupting the backup.
   - Edits PX files to incorporate BCPBACnet points.

  # Technical Architecture
   - Device Detection: Identifies BACnet devices using pattern matching to find controller names on the network.
   - Configuration Elements: Adds BCP-specific elements like tuning policies, COV services, and REST status.

  # Performance Metrics
   - Average Conversion Time: 3 - 7 minutes per station (depending on size and complexity).
   - Success Rate: 98.5% for standard configurations.
   - Object Preservation: 100% data integrity maintained.
