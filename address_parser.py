pip install usaddress pandas requests

# Grouped dictionaries; abbreviations
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

US_STATE_ABBREVIATIONS = {
    "alabama": "AL", "alaska": "AK", "arizona": "AZ", "arkansas": "AR", "california": "CA",
    "colorado": "CO", "connecticut": "CT", "delaware": "DE", "florida": "FL", "georgia": "GA",
    "hawaii": "HI", "idaho": "ID", "illinois": "IL", "indiana": "IN", "iowa": "IA",
    "kansas": "KS", "kentucky": "KY", "louisiana": "LA", "maine": "ME", "maryland": "MD",
    "massachusetts": "MA", "michigan": "MI", "minnesota": "MN", "mississippi": "MS",
    "missouri": "MO", "montana": "MT", "nebraska": "NE", "nevada": "NV", "new hampshire": "NH",
    "new jersey": "NJ", "new mexico": "NM", "new york": "NY", "north carolina": "NC",
    "north dakota": "ND", "ohio": "OH", "oklahoma": "OK", "oregon": "OR", "pennsylvania": "PA",
    #puerto rico
    "puerto rico": "PR",
    "rhode island": "RI", "south carolina": "SC", "south dakota": "SD", "tennessee": "TN",
    "texas": "TX", "utah": "UT", "vermont": "VT", "virginia": "VA", "washington": "WA",
    "west virginia": "WV", "wisconsin": "WI", "wyoming": "WY"
}

# List of U.S. states and their abbreviations
US_STATE_ABBREVIATIONS_2 = {
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
    "west virginia": "WV", "wisconsin": "WI", "wyoming": "WY",
    "puerto rico": "PR"  # Added Puerto Rico
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


import pandas as pd
import requests
from io import StringIO

# CSV of all US cities, states. 
url = "https://raw.githubusercontent.com/grammakov/USA-cities-and-states/refs/heads/master/us_cities_states_counties.csv"
response = requests.get(url)
df = pd.read_csv(StringIO(response.text), delimiter='|')

df.columns = [col.strip() for col in df.columns]
df['City'] = df['City'].str.strip()
df['State short'] = df['State short'].str.strip()

# Shoutout to NY for being difficult >:|
nyc_boroughs = [
    {"City": "Manhattan", "State short": "NY", "State full": "New York", "Country": "USA"},
    {"City": "Brooklyn", "State short": "NY", "State full": "New York", "Country": "USA"},
    {"City": "Queens", "State short": "NY", "State full": "New York", "Country": "USA"},
    {"City": "Bronx", "State short": "NY", "State full": "New York", "Country": "USA"},
    {"City": "Staten Island", "State short": "NY", "State full": "New York", "Country": "USA"}
]
df_boroughs = pd.DataFrame(nyc_boroughs)
df_city_state = pd.concat([df, df_boroughs], ignore_index=True)

# De-doop
df_city_state = df_city_state.drop_duplicates(subset=["City", "State short"]).reset_index(drop=True)

state_codes = {abbr: f"{i+1:02d}" for i, abbr in enumerate(sorted(df_city_state['State short'].unique()))}
df_city_state = df_city_state.sort_values(by=['State short', 'City']).reset_index(drop=True)
# Generate Smart Index -> state has 2-digit identifier, concat with city 4-digit id
smart_indices = []
current_state = None
counter = 0

for _, row in df_city_state.iterrows():
    state = row['State short']
    if state != current_state:
        current_state = state
        counter = 1
    else:
        counter += 1
    smart_index = f"{state_codes[state]}{counter:04d}"
    smart_indices.append(smart_index)

df_city_state['Smart Index'] = smart_indices

df_city_state = df_city_state[['City', 'State short', 'Country', 'Smart Index']]
df_city_state['Country'] = 'USA'
df_city_state = df_city_state.reset_index(drop=True)


import re
import pandas as pd
import usaddress

class AddressParser:
    def __init__(self, usps_abbreviations, state_abbreviations, city_state_index_df=None):
        self.usps_abbreviations = usps_abbreviations
        self.state_abbreviations = {k.upper(): v for k, v in state_abbreviations.items()}
        self.city_state_index_df = city_state_index_df  # your df_city_state

    # Define the fallback_city_state_lookup method
    def fallback_city_state_lookup(self, tokens):
        # Look for the last token that matches any city/state
        city, state = None, None

        # Check if any token matches city/state format from the DataFrame
        for token in reversed(tokens):
            state = token.upper() if token.upper() in self.state_abbreviations else state
            city = token.title() if token.title() in self.city_state_index_df['City'].values else city
            if state and city:
                break

        return city, state

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

    def extract_attention_marker_and_clean(self, address):
        if not isinstance(address, str):
            return address, None
        pattern = re.compile(r'(?i)\b(ATTN|Attention|C\/O|℅)\b[:\s]*')
        match = pattern.search(address)
        if match:
            marker = match.group(1).upper().replace('℅', 'C/O')
            cleaned_address = pattern.sub('', address, count=1).strip(', ')
            return cleaned_address, marker
        return address, None
    
    
    def normalize_attention_markers(self, address):
        return re.sub(r'\b(attn|attention|c/o|℅)\b[:\s]*', lambda m: m.group(0).upper().replace('.', '').replace('℅', 'C/O'), address, flags=re.IGNORECASE)

    def extract_leading_addressee(self, address):
        if ',' in address:
            first_chunk = address.split(',')[0].strip()

            # Reject if starts with known address/unit terms
            if re.search(r'^\s*(APT|UNIT|STE|SUITE|#|\d+)\b', first_chunk, re.IGNORECASE):
                return None, address

            # Reject if it contains common address words
            if re.search(r'\b(P\.?\s*O\.?\s*Box|Lot\s+\d+|Unit|Bldg|Suite|Ste|#|Street|St|Avenue|Ave|Boulevard|Blvd|Road|Rd|Place|Pl)\b', first_chunk, re.IGNORECASE):
                return None, address

            # Reject if it's very long and likely not a name
            if len(first_chunk.split()) > 6:
                return None, address

            cleaned_address = address.replace(first_chunk + ',', '', 1).strip()
            return first_chunk, cleaned_address

        return None, address

    def extract_misc_unit(self, address):
        match = re.search(r'\b(Unit|Suite|Ste|Apt|#)\s*\d+[A-Za-z]?\b', address, re.IGNORECASE)
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
            city_cleaned = False
            # First, extract addressee from the first chunk
            addressee, remaining = self.extract_leading_addressee(address)

            # Now extract attention marker from that addressee (if present)
            if addressee:
                addressee, attention_marker = self.extract_attention_marker_and_clean(addressee)
            else:
                attention_marker = None

            address = remaining
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
                "Country": "USA",
                "Attention Marker": attention_marker  # ← set it here
            }


            
            if not result["Street Name"] or not result["City"] or not result["State"]:
                result["Flag"] = "Not a valid address"
                return result

            #result["Addressee"], result["Attention Marker"] = self.extract_attention_marker(result["Addressee"])
            if result["Addressee"]:
                result["Addressee"] = result["Addressee"].title()

            if result["City"]:
                result["City"] = result["City"].title()
            if result["State"]:
                result["State"] = result["State"].upper()

            if result["Street Name"]:
                result["Street Name"] = result["Street Name"].title()

            for full, abbr in DIRECTIONAL_ABBREVIATIONS.items():
                if abbr.title() in result["Street Name"]:
                    result["Street Name"] = re.sub(rf"\b{abbr.title()}\b", abbr, result["Street Name"])

            #result["Addressee"], result["Attention Marker"] = self.extract_attention_marker(result["Addressee"])

            if not result["City"] or not result["State"]:
                tokens = re.split(r'\s+', address)
                fallback_city, fallback_state = self.fallback_city_state_lookup(tokens)

                if fallback_city and not result["City"]:
                    result["City"] = fallback_city
                if fallback_state and not result["State"]:
                    result["State"] = fallback_state

            result["Normalized Address"] = self.construct_normalized_address(result)

            # Smart Index lookup + fallback
            smart_index = None
            if self.city_state_index_df is not None:
                city = result.get("City")
                state = result.get("State")
                if city and state:
                    match = self.city_state_index_df[
                        (self.city_state_index_df['City'].str.lower() == city.lower()) &
                        (self.city_state_index_df['State short'].str.upper() == state.upper())
                    ]
                    if not match.empty:
                        smart_index = match.iloc[0]['Smart Index']

                    # Fallback: search for known city name within a messy city string
                    if not smart_index:
                        possible_cities = self.city_state_index_df[
                            self.city_state_index_df['State short'].str.upper() == state.upper()
                        ]['City'].str.lower().tolist()

                        tokens = city.lower().split()
                        for window_size in range(3, 0, -1):
                            for i in range(len(tokens) - window_size + 1):
                                candidate = " ".join(tokens[i:i+window_size])
                                if candidate in possible_cities:
                                    result["City"] = candidate.title()
                                    city_cleaned = True  # Set flag that city was cleaned
                                    match = self.city_state_index_df[
                                        (self.city_state_index_df['City'].str.lower() == candidate) &
                                        (self.city_state_index_df['State short'].str.upper() == state.upper())
                                    ]
                                    if not match.empty:
                                        smart_index = match.iloc[0]['Smart Index']
                                        break
                            if smart_index:
                                break

            result["Smart Index"] = smart_index

            flag = None

            if not result.get("City") or not result.get("State"):
                flag = "City/State missing"
            elif city_cleaned:
                flag = "City cleaned"
            elif not result.get("Smart Index"):
                flag = "City/State not recognized"

            result["Flag"] = flag

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
    

def standardize_state_names_to_abbr_preserve_case(addresses, abbrev_map):
    standardized = []
    for address in addresses:
        new_address = address
        for full, abbr in abbrev_map.items():
            # Match full state name as a word (case-insensitive)
            pattern = re.compile(rf'\b{re.escape(full)}\b', flags=re.IGNORECASE)
            new_address = pattern.sub(abbr, new_address)
        standardized.append(new_address)
    return standardized

def insert_comma_before_state_preserve_case(addresses, abbrev_values):
    updated_addresses = []
    for address in addresses:
        modified = False
        for abbr in abbrev_values:
            pattern = re.compile(rf'\b{abbr}\b', flags=re.IGNORECASE)
            match = pattern.search(address)
            if match:
                start = match.start()
                if start > 0 and address[start - 1] != ',':
                    address = address[:start].rstrip() + ", " + address[start:]
                break
        updated_addresses.append(address)
    return updated_addresses

parser = AddressParser(
    usps_abbreviations=USPS_ABBREVIATIONS,
    state_abbreviations=US_STATE_ABBREVIATIONS,
    city_state_index_df=df_city_state
)

addresses = [
    "ATTN: Acme Inc 500 Broadway Floor 3 Rear Manhattan NY 10012",
    "John Doe 789 Elm St Apt 12C Chicago IL 60614",
    "111 West Avenue, Detroit Michigan",
    "jane smith 88 maple avenue suite 7a brooklyn ny",
    "200 Market Street 3B San Francisco CA",
    "1500 E South St SE Washington DC",
    "999 Mystery Lane Ste 1 Atlantis FL",
    "1234 Jasmine drive, Indianapolis Indiana", 
    "I want Pizza for dinner"
]

addresses_challenging = [
    "ATTN: John Smith 4567 W Maple St Apt 3B Santa Monica CA 90401",
    "PO Box 8675 12th Ave NW Seattle WA 98117",
    " Brandy Johnson 124 West Avenue Detroit michigan",
    "123 Elm St, Ste 45, Building 2 Northville MI, Attn: Susan M",
    "1234 Unit 5B Old Oak Rd, Richmond, VA 23220",
    "C/O Mr. Alan Brown, 5558 West 3rd St. Apt. 204, Los Angeles, CA 90036",
    "APT 306 78 Spring Lane Westfield NJ 07090",
    "John Doe, 1500 Park Blvd, Ste 1, San Juan,  Puerto Rico 78701",
    "1532 Maple Ln #205, Suite 47, Woodlands TX, 77380"

]

df_results = parser.parse_addresses(addresses_challenging)
df_results


parser = AddressParser(
    usps_abbreviations=USPS_ABBREVIATIONS,
    state_abbreviations=US_STATE_ABBREVIATIONS,
    city_state_index_df=df_city_state
)


addresses_challenging = [
    "ATTN: John Smith 4567 W Maple St Apt 3B Santa Monica CA 90401",
    "PO Box 8675 12th Ave NW Seattle WA 98117",
    " Brandy Johnson 124 West Avenue Detroit michigan",
    "123 Elm St, Ste 45, Building 2 Northville MI",
    "1234 Unit 5B Old Oak Rd, Richmand, VA 23220",
    "C/O Mr. Alan Brown, 5558 West 3rd St. Apt. 204, Los Angeles, CA 90036",
    "APT 306 78 Spring Lane Westfield NJ 07090",
    "John Doe, 1500 Park Blvd, Ste 1, San Juan,  Puerto Rico 78701",
    "1532 Maple Ln #205, Suite 47, Woodlands TX, 77380"

]

addresses_abbreviated = standardize_state_names_to_abbr_preserve_case(addresses_challenging, US_STATE_ABBREVIATIONS_2)
addresses_ready_for_parse = insert_comma_before_state_preserve_case(addresses_abbreviated, US_STATE_ABBREVIATIONS_2.values())
df_results2 = parser.parse_addresses(addresses_ready_for_parse)
df_results2


addresses_challenging = [
    "ATTN: John Smith 4567 W Maple St Apt 3B Santa Monica CA 90401",
    "PO Box 8675 12th Ave NW Seattle WA 98117",
    "Brandy Johnson 124 West Avenue Detroit Michigan",
    "123 Elm St, Ste 45, Building 2 Northville MI",
    "1234 Unit 5B Old Oak Rd, Richmond VA 23220",
    "C/O Mr. Alan Brown, 5558 West 3rd St. Apt. 204, Los Angeles CA 90036",
    "APT 306 78 Spring Lane Westfield NJ 07090",
    "John Doe, 1500 Park Blvd, Ste 1, San Juan Puerto Rico 78701",
    "1532 Maple Ln #205, Suite 47, Woodlands TX 77380",
    "ATTN: Finance Dept 89 Corporate Center Dr, Philadelphia PA 17011",
    "C/O Sarah Green, 123 Innovation Way, Suite 400, Boston MA 02134",
    "PO Box 32001 65 Industrial Park Way Newark NJ 07105",
    "Robert Bell 78 Eighth Ave Apt 9C New York NY 10011",
    "789 Lakeside Dr., Bldg 3, Lot 7, Orlando FL 32801",
    "Ms. Angela Lee 900 Mission Blvd Apt 12A San Francisco California 94110",
    "C/O Procurement Team, 2222 Harbor Blvd Ste 1100 Costa Mesa CA 92627",
    "ATTN: Billing 555 Market St Ste 1000 San Francisco CA 94105",
    "Delivery Dept 321 Country Club Dr Bldg 4R Arlington Texas 76010",
    "P.O. Box 90909 123 Legal Lane Jackson MS 39201",
    "Jonathan King, 425 Digital Ave, Ste 300, Miami, FL 33130, USA"
]


addresses_abbreviated = standardize_state_names_to_abbr_preserve_case(addresses_challenging, US_STATE_ABBREVIATIONS_2)
addresses_ready_for_parse = insert_comma_before_state_preserve_case(addresses_abbreviated, US_STATE_ABBREVIATIONS_2.values())
df_results3 = parser.parse_addresses(addresses_ready_for_parse)


flagged = df_results3[df_results3["Flag"].notna()]
print(flagged[["Original Address", "Flag"]].to_string(index=False))

