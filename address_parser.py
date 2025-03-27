# Grouped dictionaries for better organization
STREET_ABBREVIATIONS = {
    "alley": "Aly", "annex": "Anx", " arcade": "Arc", "avenue": "Ave", "bayou": "Byu",
    "beach": "Bch", "bend": "Bnd", "bluff": "Blf", "boulevard": "Blvd", "branch": "Br",
    "bridge": "Brg", "brook": "Brk", "burg": "Bg", "bypass": "Byp", "camp": "Cp",
    "canyon": "Cyn", "cape": "Cpe", "causeway": "Cswy", "center": "Ctr", "circle": "Cir",
    "cliff": "Clf", "club": "Clb", "corner": "Cor", "course": "Crs", "court": "Ct",
    "cove": "Cv", "creek": "Crk", "crescent": "Cres", "crossing": "Xing", "dale": "Dl",
    "dam": "Dm", "divide": "Dv", "drive": "Dr", "estate": "Est", "expressway": "Expy",
    "extension": "Ext", "fall": "Fall", "ferry": "Fry", "field": "Fld", "flat": "Flt",
    "ford": "Frd", "forest": "Frst", "forge": "Frg", "fork": "Frk", "fort": "Ft",
    "freeway": "Fwy", "garden": "Gdn", "gateway": "Gtwy", "glen": "Gln", "green": "Grn",
    "grove": "Grv", "harbor": "Hbr", "haven": "Hvn", "heights": "Hts", "highway": "Hwy",
    "hill": "Hl", "hollow": "Holw", "inlet": "Inlt", "island": "Is", "junction": "Jct",
    "key": "Ky", "knoll": "Knl", "lake": "Lk", "landing": "Lndg", "lane": "Ln",
    "light": "Lgt", "loaf": "Lf", "lock": "Lck", "lodge": "Ldg", "manor": "Mnr",
    "meadow": "Mdw", "mill": "Ml", "mission": "Msn", "mount": "Mt", "mountain": "Mtn",
    "neck": "Nck", "orchard": "Orch", "park": "Prk", "parkway": "Pkwy", "pass": "Pass",
    "place": "Pl", "plain": "Pln", "plaza": "Plz", "point": "Pt", "port": "Prt",
    "prairie": "Pr", "radial": "Radl", "ranch": "Rnch", "rapids": "Rpds", "rest": "Rst",
    "ridge": "Rdg", "river": "Riv", "road": "Rd", "route": "Rte", "row": "Row",
    "run": "Run", "shoal": "Shl", "shore": "Shr", "spring": "Spg", "square": "Sq",
    "station": "Sta", "stravenue": "Stra", "stream": "Strm", "street": "St",
    "summit": "Smt", "terrace": "Ter", "trace": "Trce", "track": "Trak", "trail": "Trl",
    "tunnel": "Tunl", "turnpike": "Tpke", "union": "Un", "valley": "Vly", "viaduct": "Via",
    "view": "Vw", "village": "Vlg", "ville": "Vl", "vista": "Vis", "walk": "Walk",
    "way": "Way", "wells": "Wls"
}

UNIT_ABBREVIATIONS = {
    "apartment": "Apt", "building": "Bldg", "department": "Dept", "floor": "Fl",
    "front": "Frnt", "hanger": "Hngr", "lobby": "Lbby", "lot": "Lot", "lower": "Lowr",
    "office": "Ofc", "penthouse": "Ph", "pier": "Pier", "rear": "Rr", "room": "Rm",
    "side": "Side", "slip": "Slip", "space": "Spc", "stop": "Stop", "suite": "Ste",
    "trailer": "Trlr", "unit": "Unit", "upper": "Uppr",
    
    "PO BOX": "PO Box",
    "P.O. BOX": "PO Box",
    "P O BOX": "PO Box",
    "PO. Box": "PO Box"
}

DIRECTIONAL_ABBREVIATIONS = {
    "north": "N", "south": "S", "east": "E", "west": "W",
    "northeast": "NE", "northwest": "NW", "southeast": "SE", "southwest": "SW"
}

ORDINAL_ABBREVIATIONS = {
    "first": "1st", "second": "2nd", "third": "3rd", "fourth": "4th",
    "fifth": "5th", "sixth": "6th", "seventh": "7th", "eighth": "8th", "ninth": "9th"
}

# U.S. State Abbreviations
US_STATE_ABBREVIATIONS = {
    "alabama": "AL", "alaska": "AK", "arizona": "AZ", "arkansas": "AR", "california": "CA",
    "colorado": "CO", "connecticut": "CT", "delaware": "DE", "florida": "FL", "georgia": "GA",
    "hawaii": "HI", "idaho": "ID", "illinois": "IL", "indiana": "IN", "iowa": "IA",
    "kansas": "KS", "kentucky": "KY", "louisiana": "LA", "maine": "ME", "maryland": "MD",
    "massachusetts": "MA", "michigan": "MI", "minnesota": "MN", "mississippi": "MS",
    "missouri": "MO", "montana": "MT", "nebraska": "NE", "nevada": "NV", "new hampshire": "NH",
    "new jersey": "NJ", "new mexico": "NM", "new york": "NY", "north carolina": "NC",
    "north dakota": "ND", "ohio": "OH", "oklahoma": "OK", "oregon": "OR", "pennsylvania": "PA",
    "rhode island": "RI", "south carolina": "SC", "south dakota": "SD", "tennessee": "TN",
    "texas": "TX", "utah": "UT", "vermont": "VT", "virginia": "VA", "washington": "WA",
    "west virginia": "WV", "wisconsin": "WI", "wyoming": "WY"
}

CANADIAN_PROVINCE_ABBREVIATIONS = {
    # Alberta
    "alberta": "AB", "alta.": "AB", "alb.": "AB",
    # British Columbia
    "british columbia": "BC", "b.c.": "BC", "c.-b.": "BC", "colombie-britannique": "BC",
    # Manitoba
    "manitoba": "MB", "man.": "MB",
    # New Brunswick
    "new brunswick": "NB", "n.b.": "NB", "n.-b.": "NB", "nouveau-brunswick": "NB",
    # Newfoundland and Labrador
    "newfoundland and labrador": "NL", "n.l.": "NL", "nfld.": "NL", "lab.": "NL", "t.-n.-l.": "NL",
    # Northwest Territories
    "northwest territories": "NT", "n.w.t.": "NT", "t.n.-o.": "NT", "territoires du nord-ouest": "NT",
    # Nova Scotia
    "nova scotia": "NS", "n.s.": "NS", "n.-é.": "NS", "nouvelle-écosse": "NS",
    # Nunavut
    "nunavut": "NU", "nvt.": "NU", "nt": "NU",  # 'nt' could also be NWT; be careful with ambiguity
    # Ontario
    "ontario": "ON", "ont.": "ON", "ont": "ON",
    # Prince Edward Island
    "prince edward island": "PE", "p.e.i.": "PE", "î.-p.-é.": "PE", "île du prince-édouard": "PE",
    # Quebec
    "quebec": "QC", "que.": "QC", "qc": "QC", "p.q.": "QC", "province de québec": "QC",
    # Saskatchewan
    "saskatchewan": "SK", "sask.": "SK",
    # Yukon
    "yukon": "YT", "yuk.": "YT", "yn": "YT", "yk": "YT"
}


#USPS_ABBREVIATIONS = {**STREET_ABBREVIATIONS, **UNIT_ABBREVIATIONS, **DIRECTIONAL_ABBREVIATIONS, **ORDINAL_ABBREVIATIONS}


def uppercase_keys(d):
    return {k.upper(): v for k, v in d.items()}

STREET_ABBREVIATIONS = uppercase_keys(STREET_ABBREVIATIONS)
UNIT_ABBREVIATIONS = uppercase_keys(UNIT_ABBREVIATIONS)
DIRECTIONAL_ABBREVIATIONS = uppercase_keys(DIRECTIONAL_ABBREVIATIONS)
ORDINAL_ABBREVIATIONS = uppercase_keys(ORDINAL_ABBREVIATIONS)
US_STATE_ABBREVIATIONS = uppercase_keys(US_STATE_ABBREVIATIONS)
CANADIAN_PROVINCE_ABBREVIATIONS = uppercase_keys(CANADIAN_PROVINCE_ABBREVIATIONS)

USPS_ABBREVIATIONS = {
    **STREET_ABBREVIATIONS,
    **UNIT_ABBREVIATIONS,
    **DIRECTIONAL_ABBREVIATIONS,
    **ORDINAL_ABBREVIATIONS
}

CANADIAN_ABBREVIATIONS = {
    **STREET_ABBREVIATIONS,
    **UNIT_ABBREVIATIONS,
    **DIRECTIONAL_ABBREVIATIONS,
    **ORDINAL_ABBREVIATIONS
}



import re
import pandas as pd
import usaddress

class AddressParser:
    def __init__(self, usps_abbreviations, state_abbreviations):
        self.usps_abbreviations = usps_abbreviations
        self.state_abbreviations = {k.upper(): v for k, v in state_abbreviations.items()}

    def extract_po_box(self, address):
        match = re.search(r'\bP\.?\s*O\.?\s*Box\s*\d+\b', address, re.IGNORECASE)
        if match:
            po_box = match.group(0).strip()
            cleaned_address = address.replace(po_box, '').strip(', ')
            return po_box, cleaned_address
        return None, address

    def extract_lot_block(self, address):
        match = re.search(r'(Lot\s+\d+\s+Block\s+\d+)', address, re.IGNORECASE)
        if match:
            lot_block = match.group(1).strip()
            cleaned_address = address.replace(match.group(1), '').strip(', ')
            return lot_block, cleaned_address
        return None, address

    def extract_post_directional(self, address):
        match = re.search(
            r'\b(?:Street|St|Avenue|Ave|Boulevard|Blvd|Road|Rd|Place|Pl|Drive|Dr|Court|Ct|Lane|Ln)\s+'
            r'(Northwest|Northeast|Southwest|Southeast|North|South|East|West|NW|NE|SW|SE|N|S|E|W)\b',
            address,
            re.IGNORECASE
        )
        if match:
            return match.group(1).strip().upper()
        return None

    def standardize_state_name(self, state, country="USA"):
        if not isinstance(state, str):
            return state
        state_clean = state.strip().upper()
        if country.upper() == "USA":
            if "COLUMBIA" in state_clean:
                return "DC"
            return self.state_abbreviations.get(state_clean, state)
        return state

    def extract_attention_marker(self, addressee_text):
        if not isinstance(addressee_text, str):
            return None, None
        marker_match = re.match(r'(?i)\b(ATTN|Attention|C\/O|\u2105)\b[:\s]*', addressee_text)
        if marker_match:
            marker = marker_match.group(1).upper()
            cleaned_name = re.sub(r'(?i)\b(ATTN|Attention|C\/O|\u2105)\b[:\s]*', '', addressee_text).strip()
            return cleaned_name, marker
        return addressee_text.strip(), None

    def extract_leading_addressee(self, address):
        if ',' in address:
            first_chunk = address.split(',')[0].strip()
            if re.match(r'^\d', first_chunk) or len(first_chunk.split()) > 6:
                return None, address
            if re.search(r'\b(P\.?\s*O\.?\s*Box|Lot\s+\d+|Unit|Bldg|Suite|Ste|#|Street|St|Avenue|Ave|Boulevard|Blvd|Road|Rd|Place|Pl)\b', first_chunk, re.IGNORECASE):
                return None, address
            cleaned_address = address.replace(first_chunk + ',', '', 1).strip()
            return first_chunk, cleaned_address
        return None, address

    def extract_misc_unit(self, address):
        match = re.search(r'\b(Basement|Rear|Lower Level|Garage|Floor\s*\d+[A-Z]?)\b', address, re.IGNORECASE)
        if match:
            misc_unit = match.group(0).strip()
            cleaned_address = address.replace(misc_unit, '').strip(', ')
            return misc_unit, cleaned_address
        return None, address

    def apply_usps_abbreviations(self, text):
        if not isinstance(text, str):
            return text
        words = re.split(r'(\W+)', text)
        standardized_words = []
        for word in words:
            cleaned = word.strip().upper()
            if cleaned in self.usps_abbreviations:
                standardized_words.append(self.usps_abbreviations[cleaned])
            else:
                standardized_words.append(word)
        return ''.join(standardized_words)

    def construct_normalized_address(self, result):
        lines = []

        # First line: attention/addressee
        name_parts = []
        if result.get("Attention Marker"):
            name_parts.append(result["Attention Marker"])
        if result.get("Addressee"):
            name_parts.append(result["Addressee"])
        if name_parts:
            lines.append(' '.join(name_parts))

        # Second line: street + unit
        street_line = []
        if result.get("Street Number"):
            street_line.append(result["Street Number"])
        if result.get("Street Name"):
            street_line.append(result["Street Name"])
        if street_line:
            street_line_str = ' '.join(street_line)
            if result.get("Unit"):
                street_line_str += f", {result['Unit']}"
            lines.append(street_line_str)

        # Third line: city, state + zip
        location_line = []
        if result.get("City"):
            location_line.append(result["City"])
        if result.get("State"):
            location_line.append(result["State"])
        if result.get("Zip Code"):
            location_line.append(result["Zip Code"])
        if location_line:
            lines.append(', '.join(location_line))

        # Final line: country
        if result.get("Country"):
            lines.append(result["Country"])

        return ', '.join(lines)

    def parse_single_address(self, address):
        try:
            addressee, address = self.extract_leading_addressee(address)
            po_box, address = self.extract_po_box(address)
            lot_block, address = self.extract_lot_block(address)
            misc_unit, address = self.extract_misc_unit(address)

            tagged, _ = usaddress.tag(address)

            unit = po_box or lot_block or " ".join(filter(None, [
                tagged.get("OccupancyType", ""),
                tagged.get("OccupancyIdentifier", ""),
                misc_unit
            ])).strip() or None

            directional = tagged.get("StreetNamePostDirectional", None)
            if not directional:
                extracted_dir = self.extract_post_directional(address)
                if extracted_dir:
                    directional = DIRECTIONAL_ABBREVIATIONS.get(extracted_dir.upper(), extracted_dir.upper())

            street_name = " ".join(filter(None, [
                tagged.get("StreetNamePreDirectional", ""),
                tagged.get("StreetName", ""),
                directional,
                tagged.get("StreetNamePostType", "")
            ])).strip() or None

            result = {
                "Addressee": addressee or tagged.get("Recipient"),
                "Street Number": tagged.get("AddressNumber"),
                "Street Name": self.apply_usps_abbreviations(street_name),
                "Unit": self.apply_usps_abbreviations(unit),
                "City": tagged.get("PlaceName"),
                "State": self.standardize_state_name(tagged.get("StateName")),
                "Zip Code": tagged.get("ZipCode"),
                "Country": "USA"
            }

            result["Addressee"], result["Attention Marker"] = self.extract_attention_marker(result["Addressee"])

            result["Normalized Address"] = self.construct_normalized_address(result)
            return result

        except usaddress.RepeatedLabelError:
            return {
                "Addressee": None,
                "Street Number": None,
                "Street Name": None,
                "Unit": None,
                "City": None,
                "State": None,
                "Zip Code": None,
                "Country": "USA",
                "Attention Marker": None,
                "Normalized Address": None
            }

    def parse_addresses(self, address_list):
        parsed_data = [self.parse_single_address(addr) for addr in address_list]
        df_parsed = pd.DataFrame(parsed_data)
        df_parsed.insert(0, "Original Address", address_list)
        return df_parsed






import re
import pandas as pd

class CanadianAddressParser:
    def __init__(self, province_abbreviations, general_abbreviations):
        self.province_abbreviations = {k.lower(): v for k, v in province_abbreviations.items()}
        self.valid_abbreviations = set(self.province_abbreviations.values())
        self.general_abbreviations = general_abbreviations

    def extract_po_box(self, address):
        match = re.search(r'\bP\.?\s*O\.?\s*Box\s*\d+\b', address, re.IGNORECASE)
        if match:
            po_box = match.group(0).strip()
            cleaned_address = address.replace(po_box, '').strip(', ')
            return po_box, cleaned_address
        return None, address

    def extract_lot_block(self, address):
        match = re.search(r'(Lot\s+\d+\s+Block\s+\d+)', address, re.IGNORECASE)
        if match:
            lot_block = match.group(1).strip()
            cleaned_address = address.replace(match.group(1), '').strip(', ')
            return lot_block, cleaned_address
        return None, address

    def extract_misc_unit(self, address):
        match = re.search(r'\b(Basement|Rear|Lower Level|Garage|Floor\s*\d+[A-Z]?)\b', address, re.IGNORECASE)
        if match:
            misc_unit = match.group(0).strip()
            cleaned_address = address.replace(misc_unit, '').strip(', ')
            return misc_unit, cleaned_address
        return None, address

    def extract_unit(self, address):
        match = re.search(r'(Suite\s*\d+[A-Z]?|Apt\s*\d+[A-Z]?|Unit\s*\d+[A-Z]?|Box\s*\d+|RR\s*#?\s*\d+|Site\s*\d+)', address, re.IGNORECASE)
        if match:
            unit = match.group(0).strip()
            cleaned = address.replace(match.group(0), '', 1).strip(', ')
            return unit, cleaned
        return None, address

    def extract_attention_marker(self, addressee_text):
        if not isinstance(addressee_text, str):
            return None, None
        marker_match = re.match(r'(?i)\b(ATTN|Attention|C\/O|\u2105)\b[:\s]*', addressee_text)
        if marker_match:
            marker = marker_match.group(1).upper()
            cleaned_name = re.sub(r'(?i)\b(ATTN|Attention|C\/O|\u2105)\b[:\s]*', '', addressee_text).strip()
            return cleaned_name, marker
        return addressee_text.strip(), None

    def extract_leading_addressee(self, address):
        if ',' in address:
            first_chunk = address.split(',')[0].strip()
            if re.match(r'^\d', first_chunk) or len(first_chunk.split()) > 6:
                return None, address
            if re.search(r'\b(Box\s*\d+|Lot\s+\d+|Unit|Bldg|Suite|Ste|#|Street|St|Avenue|Ave|Boulevard|Blvd|Road|Rd|Place|Pl)\b', first_chunk, re.IGNORECASE):
                return None, address
            cleaned_address = address.replace(first_chunk + ',', '', 1).strip()
            return first_chunk, cleaned_address
        return None, address

    def extract_postal_code(self, address):
        match = re.search(r'[A-Z]\d[A-Z]\s?\d[A-Z]\d', address, re.IGNORECASE)
        if match:
            postal_code = match.group(0).upper()
            cleaned_address = address.replace(postal_code, '').strip(', ')
            return postal_code, cleaned_address
        return None, address

    def standardize_province(self, province):
        if not isinstance(province, str):
            return province
        prov_clean = province.strip().lower()
        return self.province_abbreviations.get(prov_clean, province.upper())

    def apply_abbreviations(self, text, abbr_dict):
        if not isinstance(text, str):
            return text
        words = re.split(r'(\W+)', text)  # Keep punctuation
        standardized_words = []
        for word in words:
            upper_clean = word.strip().upper()
            if upper_clean in abbr_dict:
                standardized_words.append(abbr_dict[upper_clean])
            else:
                standardized_words.append(word)
        return ''.join(standardized_words).strip()

    def construct_normalized_address(self, result):
        lines = []

        # First line: attention/addressee
        name_parts = []
        if result.get("Attention Marker"):
            name_parts.append(result["Attention Marker"])
        if result.get("Addressee"):
            name_parts.append(result["Addressee"])
        if name_parts:
            lines.append(' '.join(name_parts))

        # Second line: street + unit
        street_line = []
        if result.get("Street Number"):
            street_line.append(result["Street Number"])
        if result.get("Street Name"):
            street_line.append(result["Street Name"])
        if street_line:
            street_line_str = ' '.join(street_line)
            if result.get("Unit"):
                street_line_str += f", {result['Unit']}"
            lines.append(street_line_str)

        # Third line: city, province + postal
        location_line = []
        if result.get("City"):
            location_line.append(result["City"])
        if result.get("Province"):
            location_line.append(result["Province"])
        if result.get("Postal Code"):
            location_line.append(result["Postal Code"])
        if location_line:
            lines.append(', '.join(location_line))

        # Final line: country
        if result.get("Country"):
            lines.append(result["Country"])

        return ', '.join(lines)

    def parse_single_address(self, address):
        try:
            addressee, address = self.extract_leading_addressee(address)
            po_box, address = self.extract_po_box(address)
            lot_block, address = self.extract_lot_block(address)
            misc_unit, address = self.extract_misc_unit(address)
            postal_code, address = self.extract_postal_code(address)
            unit, address = self.extract_unit(address)

            parts = [p.strip() for p in address.split(',') if p.strip()]

            result = {
                "Addressee": addressee,
                "Street Number": None,
                "Street Name": None,
                "Unit": po_box or lot_block or unit or misc_unit,
                "City": None,
                "Province": None,
                "Postal Code": postal_code,
                "Country": "Canada"
            }

            # Extract street number and name
            if parts:
                street_parts = parts[0].split()
                if street_parts and re.match(r'^\d', street_parts[0]):
                    result["Street Number"] = street_parts[0]
                    result["Street Name"] = ' '.join(street_parts[1:])
                else:
                    result["Street Name"] = parts[0]

            # Find province
            for part in parts:
                words = part.split()
                for word in words:
                    lw = word.lower().strip(', ')
                    uw = word.upper().strip(', ')
                    if lw in self.province_abbreviations:
                        result["Province"] = self.province_abbreviations[lw]
                        break
                    elif uw in self.valid_abbreviations:
                        result["Province"] = uw
                        break
                if result["Province"]:
                    break

            # Find city: skip province & postal, ignore street or unit duplicates
            for part in parts:
                if result["Province"] and result["Province"] in part:
                    continue
                if postal_code and postal_code in part:
                    continue
                if result["Street Name"] and result["Street Name"] in part:
                    continue
                if result["Unit"] and result["Unit"] in part:
                    continue
                result["City"] = part
                break

            # Final cleanups: abbreviate street and unit
            if result["Street Name"]:
                result["Street Name"] = self.apply_abbreviations(result["Street Name"], self.general_abbreviations)
            if result["Unit"]:
                result["Unit"] = self.apply_abbreviations(result["Unit"], self.general_abbreviations)

            # Extract attention marker from addressee
            result["Addressee"], result["Attention Marker"] = self.extract_attention_marker(result["Addressee"])

            # Construct normalized address
            result["Normalized Address"] = self.construct_normalized_address(result)
            return result

        except Exception as e:
            print(f"Error parsing address: {address}\n{e}")
            return {
                "Addressee": None,
                "Street Number": None,
                "Street Name": None,
                "Unit": None,
                "City": None,
                "Province": None,
                "Postal Code": None,
                "Country": "Canada",
                "Attention Marker": None,
                "Normalized Address": None
            }

    def parse_addresses(self, address_list):
        parsed_data = [self.parse_single_address(addr) for addr in address_list]
        df_parsed = pd.DataFrame(parsed_data)
        df_parsed.insert(0, "Original Address", address_list)
        return df_parsed




# Exmaple Usage 3/27/25



sample_addresses = [
    "ATTN: John Doe, 123 Main St Suite 200, Toronto, Ontario, M5J 2N1",
    "Jane Smith, PO Box 456, Vancouver, BC, V6B 4N6",
    "Lot 7 Block 12, 789 Elm Street, Saskatoon, SK, S7H 5K5",
    "C/O Mike Jones, 234 Queen St Apt 3B, Ottawa ON K1P 1N2",
    "Unit 10 999 Maple Avenue, Calgary AB T2P 3N4",
    "Basement 55 Birchmount Road, Halifax, NS, B3J 2Y3"
]

#canadian_address_list = [
#    "ATTN: Samuel Samuelson, PO Box 450, 4457 Blackhawk Dr, Alberta, Canada"
#]

canadian_parser = CanadianAddressParser(CANADIAN_PROVINCE_ABBREVIATIONS, CANADIAN_ABBREVIATIONS)
df_canada = canadian_parser.parse_addresses(sample_addresses)
df_canada



