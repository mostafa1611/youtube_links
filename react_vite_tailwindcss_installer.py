import subprocess
import os
import textwrap
import re


# <div align="center" className="App flex flex-col items-center justify-center min-h-screen bg-red-300 p-4">
# <h1 >Vite + React</h1> by  <div className="  bg-linear-to-r from-red-600 to-transparent w-auto" >
 #     <h1 >Vite + React + Tailwindcss4</h1>
 #     </div>
def replace_react_fragment_content(file_path: str, new_content: str):
    """
    Replaces everything between <> and </> in a React fragment inside App.jsx (or any JSX file).

    Args:
        file_path (str): Path to the JSX file.
        new_content (str): The new code/text to insert between <> and </>.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match everything between <> and </> (non-greedy)
    updated = re.sub(r"<>\s*.*?\s*</>", f"<>\n{new_content}\n</>", content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated)

    print(f"✅ Updated content inside React fragment in: {file_path}") 

def run_npm_dev_windows():
    """
    Runs 'npm run dev' in a new Windows cmd window and returns immediately.
    """

    try:
        # Works reliably on Windows (no wait)
        subprocess.Popen(
            ["cmd", "/c", "start", "cmd", "/k", "npm run dev"],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        print("🚀 'npm run dev' started in a new Command Prompt window (non-blocking).")

    except Exception as e:
        print(f"⚠️ Error: {e}")
def add_tailwind_import_to_css(file_path="src/index.css"):
    """
    Adds '@import "tailwindcss";' at the top of index.css if not already present.
    """

    tailwind_import = '@import "tailwindcss";\n'

    # Check if file exists
    if not os.path.isfile(file_path):
        print(f"❌ Error: {file_path} not found.")
        return

    # Read current content
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if import already exists
    if tailwind_import.strip() in content:
        print(f"✅ Tailwind import already exists in {file_path}.")
        return

    # Add import to the top
    updated_content = tailwind_import + content

    # Write back updated file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"✅ Added Tailwind import to the top of {file_path}.")

def add_gradient_text_to_app(file_path="src/App.jsx"):
    """
    Inserts a gradient TailwindCSS <h1> text before the closing </> tag in App.jsx.
    """

    # TailwindCSS gradient text
    gradient_text = '''
     <div className="flex justify-center items-center mb-10 mt-10">
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
    
        <div className="float-left pt-100 pl-50  bg-green-100 h-[600px] w-[900px] "> 
            <div class="relative w-70 h-10 bg-red-300 rounded-md float-left">
                <div className="absolute inset-0 bg-blue-500 flex items-center justify-center text-white rounded-md">
                  Hello React
                </div>
                <div className="absolute inset-0 bg-rose-500 flex items-center justify-center text-white rounded-md origin-right rotate-[30deg]">
                    Hello Vie
                </div>
                <div className="absolute inset-0 bg-emerald-500 flex items-center justify-center text-white rounded-md origin-right rotate-[60deg]">
                  Hello Tailwindcss 4
                </div>
                <div className="absolute inset-0 bg-amber-300 flex items-center justify-center text-white rounded-md origin-right rotate-[90deg]">
                  Hello React
                </div>
                <div className="absolute inset-0 bg-pink-600 flex items-center justify-center text-white rounded-md origin-right rotate-[120deg]">
                  Hello Vite
                </div>     
                <div className="absolute inset-0 bg-red-700 flex items-center justify-center text-white rounded-md origin-right rotate-[150deg]">
                  Hello Tailwindcss 4
                </div>      
                <div className="absolute inset-0 bg-blue-800 flex items-center justify-center text-white rounded-md origin-right rotate-[180deg]">
                  Hello React
                </div>
            </div>
        </div>
    '''

    try:
        # Read the file content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Insert gradient_text before the closing </> fragment
        updated_content = re.sub(r'(</>)', gradient_text + r'\1', content, count=1)

        # Write the updated content back to the file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated_content)

        print(f"✅ Successfully added gradient text to {file_path}")

    except FileNotFoundError:
        print(f"❌ Error: File not found at {file_path}")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")



def add_tailwind_text_to_app(file_path="src/App.jsx"):
    """
    Appends a TailwindCSS-styled <h1> text before the closing JSX fragment tag </> in App.jsx
    """
    tailwind_text = '''
      <h1 className="text-2xl font-bold text-blue-500">
        Welcome to React, TailwindCSS and Vite
      </h1>
    '''

    # Read current content
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Insert tailwind_text before the first closing fragment tag
    updated_content = re.sub(r'(</>)', tailwind_text + r'\1', content, count=1)

    # Write back to the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"{file_path} updated with TailwindCSS text!")
def run(cmd):
    print(f"> {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def append_to_file(path, content):
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)

def main():
    #project = "tailwindcss4"
    # Check if directory exists
    # Check if directory exists
    
    
# Ask for a directory name
    dir_name = input("Enter the React project directory name: ").strip()
    run(f"npm create vite@latest {dir_name} -- --template react")
    # Check if directory exists
    if not os.path.isdir(dir_name):
        print(f"Directory '{dir_name}' does not exist.")
        return
     # Change to the specified directory
    
    os.chdir(dir_name)
    print(f"Changed to directory: {os.getcwd()}")
    #os.chdir(project)

    run("npm install tailwindcss @tailwindcss/vite")

    # Update vite.config.js (or create one if missing)
    vite_config = textwrap.dedent("""
    import { defineConfig } from "vite";
    import react from "@vitejs/plugin-react";
    import tailwindcss from "@tailwindcss/vite";

    export default defineConfig({
      plugins: [
        react(),
        tailwindcss(),
      ],
    });
    """).strip()
    write_file("vite.config.js", vite_config)

    add_tailwind_import_to_css()
    #add_gradient_text_to_app()
    print("\n✅ Setup done: Vite + React + Tailwind CSS v4")
    print("\n✅ npm run dev command to startup the server......")
    run_npm_dev_windows()



if __name__ == "__main__":
    main()
