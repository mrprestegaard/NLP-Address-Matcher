# US Address Parser

This Python project is a US address parser that helps with the extraction, standardization, and matching of U.S. addresses. It uses various techniques like abbreviation standardization and city/state lookups to ensure accurate address parsing. The parser can handle a wide variety of address formats, including those with minor errors or missing information.

## Features

- Extracts and parses various address components such as:
  - Addressee
  - Street number
  - Street name
  - Unit
  - City
  - State
  - Zip code
  - Country
- Standardizes address abbreviations like:
  - "St" → "Street"
  - "Ave" → "Avenue"
  - "Dr" → "Drive"
- Handles **city/state matching** with smart indexing for quick lookups.
- Identifies **missing city/state** information and flags addresses that need more information.
- Can handle edge cases like attention markers (`ATTN:`, `C/O`) and unit identifiers (e.g., **Apt 12**, **Ste 5**).

## Installation

### Prerequisites
Before you can use this parser, make sure you have the following libraries installed:

- `pandas` for data manipulation.
- `usaddress` for address tagging and parsing.
- `requests` for fetching city/state data from external sources (e.g., GitHub CSV).

To install the required libraries, create a virtual environment and run:

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, you can manually install the dependencies:

```bash
pip install pandas usaddress requests
```

## Usage

### Importing the Address Parser

```python
from address_parser import AddressParser
```

### Example of Parsing a Single Address

```python
# Initialize the parser with necessary dictionaries and city/state data
parser = AddressParser(
    usps_abbreviations=USPS_ABBREVIATIONS,
    state_abbreviations=US_STATE_ABBREVIATIONS,
    city_state_index_df=df_city_state
)

address = "ATTN: Mark Twain, 123 Main Street Suite 450 Manhattan NY 10012"

# Parse the address
parsed_result = parser.parse_single_address(address)

print(parsed_result)
```

### Example of Parsing Multiple Addresses

```python
addresses = [
    "ATTN: Acme Inc 500 Broadway Floor 3 Rear Manhattan NY 10012",
    "John Doe 789 Elm St Apt 12C Chicago IL 60614",
    "jane smith 88 maple avenue suite 7a brooklyn ny"
]

# Parse a list of addresses
df_results = parser.parse_addresses(addresses)

print(df_results[['Original Address', 'City', 'State', 'Smart Index', 'Normalized Address', 'Flag']])
```

## Data Source

This parser uses a city/state dataset retrieved from GitHub, which provides information about U.S. cities, states, and counties. The CSV is loaded dynamically from:

- [U.S. Cities and States Dataset](https://github.com/grammakov/USA-cities-and-states)

## How It Works

1. **Abbreviation Handling**: The parser normalizes common address abbreviations (e.g., "Ave" to "Avenue") using a dictionary of abbreviations.
2. **Address Parsing**: The script breaks the address down into components using **usaddress**, which tags different parts of the address (e.g., street name, city, state).
3. **City/State Lookup**: A lookup is performed using a **smart index** to ensure that the city and state are recognized correctly. If not, it flags the address as needing more information.
4. **Normalization**: The parser standardizes the case of components like the city name and street name (e.g., "brooklyn" to "Brooklyn").

## Contributing

Feel free to fork this repository, open issues, and submit pull requests. Improvements and additional features are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
