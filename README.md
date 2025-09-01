# SpectraTheFox's Virtual Assistant
My Virtual Assistant Completely Redone from Scratch! WORK IN PROGRESS. EXPECT BUGS.
***
## How it works
This is a basic Open Source virtual assistant with full support to create your own commands and modules. Designed from scratch to be as easy as possible to add and get commands working. It uses ElevenLabs for custom voice support. I plan to add a UI element using pygame at some point, but that is still being worked on. 
***
## Installation
To install The Virtual Assistant, follow these steps:
1. Clone the repository: `git clone https://github.com/SpectraTheFox/VirtualAssistant`
2. Navigate to the project directory: `cd VirtualAssistant`
3. Create a .env file with the required api keys for Eleven Labs with the variable `ELEVENLABS_API_KEY`
4. Install the required dependencies: `pip install -r requirements.txt`
***
## Making Commands
Creating your own commands is straightforward. Follow the format of `module_template.py` for any commands you wish to add. Place the file in `modules/` to ensure it works. The program automatically searches the modules directory for all `.py` files and runs the `checkactivation` until it finds the one you are using. Then it uses the `run` method on that specific command. Ensure your command includes both `checkactivation` and `run` functions and place any import statements at the top of the code.
***
## Running the Program
To run the program, use the following command in your terminal: 
`python main.py`.
The terminal will update with information such as thinking status, startup, prints its outputs as they are said, etc.
***
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
***
## Support
For support, please open an issue on the GitHub repository or contact the maintainers directly.
***
## Contributing
Sadly I will not be allowing contributions to the main branch due to this really being a solo passion project. Feel free to fork it and modify it however you please though. Any bug reports can be done through the Issues page on the Repository.