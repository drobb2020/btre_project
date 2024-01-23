# Model/DB fields

## Listings App

- id: INT
- realtor: INT (Foreign Key [realtor])
- title: STR
- address: STR
- city: STR
- state: STR
- zip: STR
- description: TEXT
- price: INT
- bedrooms: INT
- Bathrooms: INT
- Garage: INT (default (0))
- SQFT: INT
- lot_size: FLOAT
- is_published: BOOLEAN (true)
- list_date: DATE
- photo_main: STR
- photo_1: STR
- photo_2: STR
- photo_3: STR
- photo_4: STR
- photo_5: STR
- photo_6: STR

## Realtor App

- id: INT
- name: STR
- photo: STR
- description: TEXT
- email: STR
- phone: STR
- is_mvp: BOOLEAN (default (false))

## Contact App

- id: INT
- user_id: INT
- listing: INT
- listing_id: INT
- name: STR
- phone: STR
- message: TEXT
- contact_date: DATE
