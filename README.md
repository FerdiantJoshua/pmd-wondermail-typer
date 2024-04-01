# Pokemon Mystery Dungeon Red Rescue Team, WonderMail Typer

A bot to automatically type WonderMail code into your Gameboy emulator.
PMD WonderMail code consists of 24 random character, which takes time to type,
as we can only type my moving the cursor along the screen keyboard.

This bot quickens the process by allowing us to copy-paste the code into the script,
then let the script to type the 24-length code for us.

Steps:

1. Start the script (refer to setup, step 4)
2. Generate code from WonderMail code generator (e.g. https://syphist.com/pmd/rt/wondermail.php)
3. Copy the generated code, and paste into the script, press ENTER
4. Re-open your Gameboy emulator, head to the typing page
5. Press ESC, and wait for the script to type the code for you.

## Setup

1. Install Python 3.8 or above

2. Setup venv

    ```sh
    python -m venv venv
    ```

3. Install dependencies

    ```sh
    pip install -r requirements.txt
    ```

4. Start app

    ```sh
    python wondercode_typer.py
    ```

## Dependencies

```text
keyboard==0.13.5
PyDirectInput==1.0.4
```

## Author

- Ferdiant Joshua Muis
