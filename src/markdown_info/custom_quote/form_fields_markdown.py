"""
This file contains the markdown definition of the custom quote form.
"""

from src.agents.agent_names import PLANNER_AGENT_NAME, PRICE_QUOTE_AGENT_NAME
from src.agents.price_quote.instructions_constants import PLANNER_ASK_USER
from src.tools.hubspot.tickets.constants import TypeOfTicketEnum
from .constants import (
    UseTypeEnum,
    BusinessCategoryEnum,
    LocationEnum,
    ProductGroupEnum,
    TypeOfClingEnum,
    TypeOfDecalEnum,
    TypeOfMagnetEnum,
    TypeOfPatchEnum,
    TypeOfLabelEnum,
    TypeOfStickerEnum,
    TypeOfTattooEnum,
    TypeOfTapeEnum,
    TypeOfPackagingEnum,
    PreferredFormatEnum,
    PouchSizeEnum,
    PouchLabelMaterialEnum,
    WhatSizeOfTapeEnum,
)

CUSTOM_QUOTE_FORM_MARKDOWN_DEFINITION = f"""
**Custom Quote Form Structure & Rules:**

The following defines the fields, requirements, and conditional logic for collecting custom quote information.
- **'Required: Yes'**: This information must be provided by the user.
- **'Required: No'**: This information is optional.
- **'ask_group_id'**: An optional identifier. Fields sharing the same `ask_group_id` may be asked together by the PQA in a single conversational turn. PQA will parse the user's raw response for these grouped fields.
- **'Conditional Logic'**: Describes when a field becomes relevant or required based on previous answers.
- **'List values'**: For Dropdown fields, these are the exact, fixed options the user must choose from. The Planner Agent MUST present these options to the user.
- **'PQA Guidance Note'**: Specific instructions for the Price Quote Agent on how to guide the Planner for this field. PQA should use these notes to formulate its instructions to the Planner.

**I. Initial Contact & Use Type:**
*(PQA aims to collect these efficiently at the start)*
1.  **Display Label:** First name
    - **HubSpot Internal Name:** `firstname`
    - **Property Type:** Contact Property
    - **Field Type:** Text
    - **Required:** No
    - **ask_group_id:** `contact_basics`
    - **PQA Guidance Note:** This is the primary field for the 'contact_basics' group. PQA will instruct Planner to politely ask for the user's first name, last name, and email address in a single interaction. PQA will parse the user's raw response for these three fields.
2.  **Display Label:** Last name
    - **HubSpot Internal Name:** `lastname`
    - **Property Type:** Contact Property
    - **Field Type:** Text
    - **Required:** No
    - **ask_group_id:** `contact_basics`
3.  **Display Label:** Email
    - **HubSpot Internal Name:** `email`
    - **Property Type:** Contact Property
    - **Field Type:** Text
    - **Required:** Yes
    - **ask_group_id:** `contact_basics`
4.  **Display Label:** Phone number
    - **HubSpot Internal Name:** `phone`
    - **Property Type:** Contact Property
    - **Field Type:** Phone number
    - **Required:** Yes
    - **Limits:** Must be between 7 and 20 characters.
    - **PQA Guidance Note:** PQA will instruct Planner to ask for the phone number separately and politely, typically after the 'contact_basics' group is collected or if a support call is requested.
5.  **Display Label:** Personal or business use?
    - **HubSpot Internal Name:** `use_type`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes
    - **List values:** {', '.join(f"'{e}'" for e in UseTypeEnum.get_all_values())}
    - **Conditional Logic:** If this is '{UseTypeEnum.BUSINESS.value}', then fields in Section II become relevant.
    - **PQA Guidance Note:** PQA will instruct Planner to ask about 'Personal or business use?', presenting the available options.

**II. Business Details (Conditional on `use_type` being '{UseTypeEnum.BUSINESS.value}'):**
*(PQA guides Planner to ask these individually if Section I, field 5 is '{UseTypeEnum.BUSINESS.value}')*
6.  **Display Label:** Company name
    - **HubSpot Internal Name:** `company`
    - **Property Type:** Contact Property
    - **Field Type:** Text
    - **Required:** No (but PQA should guide Planner to ask if `use_type` is Business)
    - **PQA Guidance Note:** If 'Personal or business use?' is Business, PQA will instruct Planner to ask for the 'Company name'.
7.  **Display Label:** Business Category
    - **HubSpot Internal Name:** `business_category`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** No (but PQA should guide Planner to ask if `use_type` is Business)
    - **List values:** {', '.join(f"'{e}'" for e in BusinessCategoryEnum.get_all_values())}
    - **Conditional Logic:** If this is '{BusinessCategoryEnum.OTHER.value}', then field 8 becomes relevant.
    - **PQA Guidance Note:** If 'Personal or business use?' is Business, PQA will instruct Planner to ask about 'Business Category', presenting options. If '{BusinessCategoryEnum.OTHER.value}' is chosen, PQA will then guide asking for 'Business Category (Other)'.
8.  **Display Label:** Business Category (Other)
    - **HubSpot Internal Name:** `other_business_category`
    - **Property Type:** Ticket Property
    - **Field Type:** Text
    - **Required:** No (but PQA should guide Planner to ask if `business_category` is '{BusinessCategoryEnum.OTHER.value}')
    - **PQA Guidance Note:** If 'Business Category' is Other, PQA will instruct Planner to ask for this detail.
9.  **Display Label:** Are you a promotional product distributor?
    - **HubSpot Internal Name:** `promotional_product_distributor_`
    - **Property Type:** Ticket Property
    - **Field Type:** Single Checkbox (Boolean: Yes/No)
    - **Required:** No (but PQA should guide Planner to ask if `use_type` is Business)
    - **PQA Guidance Note:** If 'Personal or business use?' is Business, PQA will instruct Planner to ask 'Are you a promotional product distributor?'.

**III. General Product & Quote Details:**
*(PQA guides Planner after Business Details (if applicable) or Initial Details)*
10. **Display Label:** Location
    - **HubSpot Internal Name:** `location`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** No
    - **List values:** {', '.join(f"'{e}'" for e in LocationEnum.get_all_values())}
    - **PQA Guidance Note:** PQA will instruct Planner to ask about 'Location', presenting options.
11. **Display Label:** Product:
    - **HubSpot Internal Name:** `product_group`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes
    - **List values:** {', '.join(f"'{e}'" for e in ProductGroupEnum.get_all_values())}
    - **Conditional Logic:** The selection here determines which of fields in Section IV become relevant and required.
    - **PQA Guidance Note:** This is a key question. PQA will instruct Planner to ask about 'Product:', presenting options. The answer drives conditional logic for Section IV.

**IV. Product Specifics (Conditional on 'Product:' selection from Section III, field 11):**
*(PQA guides Planner to ask the relevant field(s) from this section based on the answer to 'Product:')*
12. **Display Label:** Type of Cling:
    - **HubSpot Internal Name:** `type_of_cling_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes (IF `product_group` is '{ProductGroupEnum.CLING.value}')
    - **List values:** {', '.join(f"'{e}'" for e in TypeOfClingEnum.get_all_values())}
    - **PQA Guidance Note:** If 'Product:' is Cling, PQA will instruct Planner to ask for 'Type of Cling:', presenting options.
13. **Display Label:** Type of Decal:
    - **HubSpot Internal Name:** `type_of_decal_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes (IF `product_group` is '{ProductGroupEnum.DECAL.value}')
    - **List values:** {', '.join(f"'{e}'" for e in TypeOfDecalEnum.get_all_values())}
    - **PQA Guidance Note:** If 'Product:' is Decal, PQA will instruct Planner to ask for 'Type of Decal:', presenting options.
14. **Display Label:** Type of Magnet:
    - **HubSpot Internal Name:** `type_of_magnet_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes (IF `product_group` is '{ProductGroupEnum.MAGNET.value}')
    - **List values:** {', '.join(f"'{e}'" for e in TypeOfMagnetEnum.get_all_values())}
    - **PQA Guidance Note:** If 'Product:' is Magnet, PQA will instruct Planner to ask for 'Type of Magnet:', presenting options.
15. **Display Label:** Type of Patch:
    - **HubSpot Internal Name:** `type_of_patch_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes (IF `product_group` is '{ProductGroupEnum.PATCH.value}')
    - **List values:** {', '.join(f"'{e}'" for e in TypeOfPatchEnum.get_all_values())}
    - **PQA Guidance Note:** If 'Product:' is Patch, PQA will instruct Planner to ask for 'Type of Patch:', presenting options.
16. **Display Label:** Type of Label:
    - **HubSpot Internal Name:** `type_of_label_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes (IF `product_group` is '{ProductGroupEnum.ROLL_LABEL.value}')
    - **List values:** {', '.join(f"'{e}'" for e in TypeOfLabelEnum.get_all_values())}
    - **PQA Guidance Note:** If 'Product:' is Roll Label, PQA will instruct Planner to ask for 'Type of Label:', presenting options.
17. **Display Label:** Type of Sticker:
    - **HubSpot Internal Name:** `type_of_sticker_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes (IF `product_group` is '{ProductGroupEnum.STICKER.value}')
    - **List values:** {', '.join(f"'{e}'" for e in TypeOfStickerEnum.get_all_values())}
    - **PQA Guidance Note:** If 'Product:' is Sticker, PQA will instruct Planner to ask for 'Type of Sticker:', presenting options.
18. **Display Label:** Type of Tattoo:
    - **HubSpot Internal Name:** `type_of_tattoo_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes (IF `product_group` is '{ProductGroupEnum.TATTOO.value}')
    - **List values:** {', '.join(f"'{e}'" for e in TypeOfTattooEnum.get_all_values())}
    - **PQA Guidance Note:** If 'Product:' is Tattoo, PQA will instruct Planner to ask for 'Type of Tattoo:', presenting options.
19. **Display Label:** Type of Tape:
    - **HubSpot Internal Name:** `type_of_tape_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes (IF `product_group` is '{ProductGroupEnum.PACKING_TAPE.value}')
    - **List values:** {', '.join(f"'{e}'" for e in TypeOfTapeEnum.get_all_values())}
    - **PQA Guidance Note:** If 'Product:' is Tape, PQA will instruct Planner to ask for 'Type of Tape:', presenting options.
20. **Display Label:** Preferred Format
    - **HubSpot Internal Name:** `preferred_format`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes (IF `product_group` is '{ProductGroupEnum.STICKER.value}' OR `product_group` is '{ProductGroupEnum.ROLL_LABEL.value}')
    - **List values:** {', '.join(f"'{e}'" for e in PreferredFormatEnum.get_all_values())}
    - **PQA Guidance Note:** If 'Product:' is Sticker or Roll Label, PQA will instruct Planner to ask for 'Preferred Format', presenting options.
21. **Display Label:** Type of Packaging:
    - **HubSpot Internal Name:** `type_of_packaging_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes (IF `product_group` is '{ProductGroupEnum.PACKAGING.value}')
    - **List values:** {', '.join(f"'{e}'" for e in TypeOfPackagingEnum.get_all_values())}
    - **PQA Guidance Note:** If 'Product:' is Packaging, PQA will instruct Planner to ask for 'Type of Packaging:', presenting options.
22. **Display Label:** Pouch Size:
    - **HubSpot Internal Name:** `pouch_size_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes (IF `product_group` is '{ProductGroupEnum.PACKAGING.value}')
    - **List values:** {', '.join(f"'{e}'" for e in PouchSizeEnum.get_all_values())}
    - **PQA Guidance Note:** If 'Product:' is Packaging, PQA will instruct Planner to ask for 'Pouch Size:', presenting options.
23. **Display Label:** Pouch Label Material:
    - **HubSpot Internal Name:** `pouch_label_material_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** Yes (IF `product_group` is '{ProductGroupEnum.PACKAGING.value}')
    - **List values:** {', '.join(f"'{e}'" for e in PouchLabelMaterialEnum.get_all_values())}
    - **PQA Guidance Note:** If 'Product:' is Packaging, PQA will instruct Planner to ask for 'Pouch Label Material:', presenting options.
24. **Display Label:** What size of tape?
    - **HubSpot Internal Name:** `what_size_of_tape_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** No (but PQA should guide Planner to ask IF `product_group` is '{ProductGroupEnum.PACKING_TAPE.value}')
    - **List values:** {', '.join(f"'{e}'" for e in WhatSizeOfTapeEnum.get_all_values())}
    - **PQA Guidance Note:** If 'Product:' is Tape, PQA will instruct Planner to ask 'What size of tape?', presenting options.

**V. Core Quote Specifications:**
*(PQA guides Planner after product type and specifics are established)*
25. **Display Label:** Total Quantity:
    - **HubSpot Internal Name:** `total_quantity_`
    - **Property Type:** Ticket Property
    - **Field Type:** Number
    - **Required:** Yes
    - **ask_group_id:** `quantity_dimensions`
    - **PQA Guidance Note:** This is the primary field for the 'quantity_dimensions' group. PQA will instruct Planner to politely ask for the total quantity, width, and height in a single interaction. PQA will parse the user's raw response for these three fields.
26. **Display Label:** Width in Inches:
    - **HubSpot Internal Name:** `width_in_inches_`
    - **Property Type:** Ticket Property
    - **Field Type:** Number
    - **Required:** Yes
    - **ask_group_id:** `quantity_dimensions`
27. **Display Label:** Height in Inches:
    - **HubSpot Internal Name:** `height_in_inches_`
    - **Property Type:** Ticket Property
    - **Field Type:** Number
    - **Required:** Yes
    - **ask_group_id:** `quantity_dimensions`

**VI. Final Details, Design & Consent:**
*(PQA guides Planner after core specifications are known. Order adjusted for conversational flow.)*
28. **Display Label:** Application Use:
    - **HubSpot Internal Name:** `application_use_`
    - **Property Type:** Ticket Property
    - **Field Type:** Text
    - **Required:** No
    - **ask_group_id:** `final_details`
    - **PQA Guidance Note:** This is the primary field for the 'final_details' group. PQA will instruct Planner to politely ask about the application use and any other additional instructions/details in a single interaction. PQA will parse the user's raw response for these two fields.
29. **Display Label:** Additional Instructions:
    - **HubSpot Internal Name:** `additional_instructions_`
    - **Property Type:** Ticket Property
    - **Field Type:** Textarea
    - **Required:** No
    - **ask_group_id:** `final_details`
    - **PQA Guidance Note:** This field is typically asked along with 'Application Use:'. If PQA parses that the user requests design assistance (from the 'Upload your design' interaction), PQA will internally add a note like "User requested design assistance." to this field in its `form_data`.
30. **Display Label:** Request a support call
    - **HubSpot Internal Name:** `call_requested`
    - **Property Type:** Ticket Property
    - **Field Type:** Single Checkbox (Boolean: Yes/No)
    - **Required:** No
    - **PQA Guidance Note:** PQA may instruct Planner to ask this contextually later in the conversation, especially if the user seems to need more help, if the quote is complex, or if the user expresses frustration. Typically asked before the final summary if deemed appropriate by PQA. Example prompt: 'Would you prefer to discuss the details further with one of our support team members over the phone?'
31. **Display Label:** Upload your design
    - **HubSpot Internal Name:** `upload_your_design`
    - **Property Type:** Ticket Property
    - **Field Type:** File (Conceptually for PQA; actual file handling is via chat)
    - **Required:** No
    - **PQA Guidance Note:** PQA will manage a multi-step interaction using `{PLANNER_ASK_USER}`:
        1. PQA instructs Planner to ask the user to upload their file with a friendly prompt like, "Great! Do you have a design file you'd like to use for your stickers? If so, please upload it now. We'd love to see it!"
        2. Based on the user's raw response (relayed by Planner), PQA parses it.
        3. If the user indicates they do *not* have a file (e.g., says "no," "I don't have one"), PQA's next step is to instruct Planner to ask if they need design assistance (Yes/No).
        4. If the user uploads a file, the system will detect it, and PQA can consider this step complete. PQA will internally update its `form_data` for `upload_your_design` (e.g., "File provided by user", "No file, assistance requested", "No file, no assistance needed") and potentially add a note to `additional_instructions_` if assistance is requested.
32. **Display Label:** Consent to communicate
    - **HubSpot Internal Name:** `hs_legal_communication_consent_checkbox`
    - **Property Type:** Contact Property
    - **Field Type:** Single Checkbox (Boolean: Yes/No)
    - **Required:** No (Disabled - Do not ask for now)
    - **PQA Guidance Note:** This field is currently disabled. PQA should NOT instruct Planner to ask for this. For now, consent can be assumed if the user proceeds, or handled by other business processes. If this needs to be re-enabled, this note and the 'Required' status should be updated.

33. **Display Label:** Have you ordered with us before?
    - **HubSpot Internal Name:** `have_you_ordered_with_us_before_`
    - **Property Type:** Ticket Property
    - **Field Type:** Single Checkbox (Boolean: Yes/No)
    - **Required:** No (Disabled - Do not ask for now)
    - **List values:** 'Yes', 'No'
    - **PQA Guidance Note:** This field is defined in HubSpot but is not currently part of the active conversational flow. Do not ask the user for this information.
34. **Display Label:** How did you find us?
    - **HubSpot Internal Name:** `how_did_you_find_us_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** No (Disabled - Do not ask for now)
    - **List values:** 'Google Search', 'Social Media', 'Email', 'PPAI/ASI', 'Tradeshow', 'StickerYou Store', 'Existing customer', 'Banner Ads', 'Referral from Another Customer', 'Catalog', 'Live Chat', 'General Inquiry Form'
    - **PQA Guidance Note:** This field is defined in HubSpot but is not currently part of the active conversational flow. Do not ask the user for this information.
35. **Display Label:** Number of colours in design:
    - **HubSpot Internal Name:** `number_of_colours_in_design_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** No (Disabled - Do not ask for now)
    - **List values:** '1', '2', '3'
    - **PQA Guidance Note:** This field is defined in HubSpot but is not currently part of the active conversational flow. Do not ask the user for this information.
36. **Display Label:** Preferred Format Stickers
    - **HubSpot Internal Name:** `preferred_format_stickers`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** No (Disabled - Do not ask for now)
    - **List values:** 'Pages', 'Kiss-Cut Singles', 'Die-Cut Singles'
    - **PQA Guidance Note:** This field is defined in HubSpot but is not currently part of the active conversational flow. Do not ask the user for this information. This might be a duplicate or more specific version of 'Preferred Format'.
37. **Display Label:** Upload your vector artwork
    - **HubSpot Internal Name:** `upload_your_vector_artwork`
    - **Property Type:** Ticket Property
    - **Field Type:** File (Conceptual for PQA; actual file handling is via chat)
    - **Required:** No (Disabled - Do not ask for now)
    - **PQA Guidance Note:** This field is defined in HubSpot but is not currently part of the active conversational flow. Do not ask the user for this information.
38. **Display Label:** What kind of content would you like to hear about?
    - **HubSpot Internal Name:** `what_kind_of_content_would_you_like_to_hear_about_`
    - **Property Type:** Ticket Property
    - **Field Type:** Dropdown
    - **Required:** No (Disabled - Do not ask for now)
    - **List values:** 'Business Products and News', 'Consumer Products and News', 'Products and Sweet Deals for Parents', 'Not sure yet - send me everything!'
    - **PQA Guidance Note:** This field is defined in HubSpot but is not currently part of the active conversational flow. Do not ask the user for this information.

    **VII. System Generated Fields (For AI agents internal use only - DO NOT ask user for these):**
    1.  **Label:** Subject
        *   **HubSpot Internal Name:** `subject`
        *   **Property Type:** Ticket Property
        *   **Field Type:** Text
        *   **Required:** Yes (Agent Generated Based On Context - Do not ask user)
        *   **Planner Guidance Note:** The Planner Agent is responsible for generating the ticket subject. It should be concise and informative, based on key collected information. This field should not be directly asked to the user.

    2.  **Label:** Content
        *   **HubSpot Internal Name:** `content`
        *   **Property Type:** Ticket Property
        *   **Field Type:** Text (HubSpot may render this as Rich Text)
        *   **Required:** Yes (Agent Generated Based On Context - Do not ask user)
        *   **Planner Guidance Note:** With most data now in specific ticket properties, the Planner Agent should generate a brief, human-readable summary for this field.

    3.  **Label:** Type of Ticket
        *   **HubSpot Internal Name:** `type_of_ticket`
        *   **Property Type:** Ticket Property
        *   **Field Type:** Dropdown (Single choice among the following values: {', '.join(f"'{e}'" for e in TypeOfTicketEnum.get_all_values())})
        *   **Required:** Yes (Agent Generated Based On Context - Do not ask user)
        *   **List values:** {', '.join(f"'{e}'" for e in TypeOfTicketEnum.get_all_values())}
        *   **PQA Guidance Note:** This field is determined and set by the `{PLANNER_AGENT_NAME}` based on its internal logic and the overall context of the request (User issues vs. Custom Quote).
            For custom quotes processed through this form, the PQA will typically set this to "{TypeOfTicketEnum.QUOTE.value}". This field should not be directly asked to the user.
"""
