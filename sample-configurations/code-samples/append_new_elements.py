def append_new_elements_to_devices(xml_file, root, devices):
    """
    Appends new elements to each matching device block using BeautifulSoup.
    """
    try:
        # Parse the file once before processing
        with open(xml_file, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "lxml-xml")

        for device in devices:
            device_element = soup.find("p", {"n": device.attrib["n"]})
            if not device_element:
                print(f"'{device.attrib['n']}' not found.")
                continue
            
            station_name = soup.find("p", {"n": "stationName"})
            station_name["m"] = "bcs3=bcsv3"
            tuning_policy = soup.find("p", {"t": "bac:BacnetTuningPolicyMap"})

            # Check if a BcpPolicy with the same structure already exists
            existing_policy = tuning_policy.find("p", {"n": "BcpPolicy", "t": "bcs3:BcpBacnetTuningPolicy"})
            if not existing_policy:
                # Only add a new policy if one doesn't exist
                new_policy = soup.new_tag("p", n="BcpPolicy", h=hex(highest_h)[2:], t="bcs3:BcpBacnetTuningPolicy")
                highest_h += 1
                new_policy.append(soup.new_tag("p", n="writeOnStart", f="r"))
                new_policy.append(soup.new_tag("p", n="writeOnUp", f="r"))
                new_policy.append(soup.new_tag("p", n="writeOnEnabled", f="r"))
                tuning_policy.append(new_policy)

            # Add PollServiceOnCOV element
            new_cov_element = soup.new_tag("p", n="PollServiceOnCOV", h=hex(highest_h)[2:], t="bcs3:BcpPollServiceOnCOV")
            highest_h += 1
            device_element.append(new_cov_element)

            # Add restStatus element
            rest_status_element = soup.new_tag("p", n="restStatus", t="bcs3:BcpEnumRestStatus", v="down")
            device_element.append(rest_status_element)

            # Add BcpSupportBacnetDevice element with child elements
            bcp_support_device_element = soup.new_tag("p", n="BcpParameters", h=hex(highest_h)[2:], t="bcs3:BcpSupportBacnetDevice")
            highest_h += 1
            bcp_support_device_element.append(soup.new_tag("p", n="proxyGeneratorFileOrd", t="b:Ord", v=f"file:^Bcp/{device.attrib['h']}/InternalPoints.xml"))
            bcp_support_device_element.append(soup.new_tag("p", n="deviceHandle", v=device.attrib["h"]))
            bcp_support_device_element.append(soup.new_tag("p", n="modelType", v=""))
            device_element.append(bcp_support_device_element)

            # Add tuningPolicyName element to deviceFacets if present
            device_points = device_element.find("p", {"n": "points"})
            for point in device_points.findChildren():
                device_facets = point.find("p", {"n": "deviceFacets"})
                if device_facets:
                    # Check if tuningPolicyName already exists in this proxyExt
                    proxy_ext = device_facets.parent
                    existing_policy = proxy_ext.find("p", {"n": "tuningPolicyName"})
                    
                    # Only add if it doesn't exist
                    if not existing_policy:
                        tuning_policy_name_element = soup.new_tag("p", n="tuningPolicyName", v="BcpPolicy")
                        device_facets.insert_after(tuning_policy_name_element)
            print(f"{device.attrib["n"]} has been converted.")

        # Write all changes to the file once after the loop
        with open(xml_file, "w", encoding="utf-8") as file:
            file.write(soup.prettify())

    except Exception as e:
        logger.info(f"{device.attrib['n']} was not converted. Program stopped.")
        print("Error while appending new elements to devices:")
        print(e)
