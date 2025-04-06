import os

# Define the folder structure
folders = [
    "bank-signup-form/public",
    "bank-signup-form/src/components",
    "bank-signup-form/src/translations"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Define files and their content
files = {
    "bank-signup-form/public/index.html": """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Bank Signup</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
""",
    "bank-signup-form/src/index.js": """import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
""",
    "bank-signup-form/src/App.jsx": """import React from "react";
import SignUpForm from "./SignUpForm";

const App = () => {
  return <SignUpForm />;
};

export default App;
""",
    "bank-signup-form/src/translations/lang.js": """export const translations = {
  en: {
    title: "Bank Account Sign-Up",
    name: "Full Name",
    email: "Email",
    phone: "Phone Number",
    pan: "PAN Card Number",
    submit: "Submit",
    next: "Next",
    back: "Back",
    invalidPan: "Invalid PAN Card format (e.g., ABCDE1234F)",
    langToggle: "Switch to Hindi",
    success: "Form submitted successfully!",
  },
  hi: {
    title: "बैंक खाता साइन-अप",
    name: "पूरा नाम",
    email: "ईमेल",
    phone: "फ़ोन नंबर",
    pan: "पैन कार्ड नंबर",
    submit: "जमा करें",
    next: "आगे",
    back: "पीछे",
    invalidPan: "अमान्य पैन कार्ड प्रारूप (उदा: ABCDE1234F)",
    langToggle: "अंग्रेज़ी में बदलें",
    success: "फॉर्म सफलतापूर्वक सबमिट हुआ!",
  },
};
""",
    "bank-signup-form/src/components/ProgressBar.jsx": """import React from "react";

const ProgressBar = ({ step }) => {
  const getWidth = () => {
    switch (step) {
      case 1: return "33%";
      case 2: return "66%";
      case 3: return "100%";
      default: return "0%";
    }
  };

  return (
    <div className="w-full bg-gray-200 dark:bg-gray-700 h-2 rounded mb-6">
      <div
        className="bg-blue-600 h-2 rounded transition-all duration-500"
        style={{ width: getWidth() }}
      ></div>
    </div>
  );
};

export default ProgressBar;
""",
    "bank-signup-form/src/components/Step1.jsx": """import React from "react";

const Step1 = ({ formData, handleChange, t }) => {
  return (
    <>
      <div>
        <label>{t.name}</label>
        <input
          type="text"
          name="name"
          required
          className="w-full p-2 mt-1 rounded border bg-transparent border-gray-300 dark:border-gray-600"
          value={formData.name}
          onChange={handleChange}
        />
      </div>
      <div>
        <label>{t.email}</label>
        <input
          type="email"
          name="email"
          required
          className="w-full p-2 mt-1 rounded border bg-transparent border-gray-300 dark:border-gray-600"
          value={formData.email}
          onChange={handleChange}
        />
      </div>
    </>
  );
};

export default Step1;
""",
    "bank-signup-form/src/components/Step2.jsx": """import React from "react";

const Step2 = ({ formData, handleChange, panError, t }) => {
  return (
    <>
      <div>
        <label>{t.phone}</label>
        <input
          type="tel"
          name="phone"
          required
          className="w-full p-2 mt-1 rounded border bg-transparent border-gray-300 dark:border-gray-600"
          value={formData.phone}
          onChange={handleChange}
        />
      </div>
      <div>
        <label>{t.pan}</label>
        <input
          type="text"
          name="pan"
          maxLength={10}
          required
          className={\`w-full p-2 mt-1 rounded border bg-transparent \${panError ? "border-red-500 dark:border-red-400" : "border-gray-300 dark:border-gray-600"}\`}
          value={formData.pan}
          onChange={handleChange}
        />
        {panError && <p className="text-red-500 text-sm mt-1">{panError}</p>}
      </div>
    </>
  );
};

export default Step2;
""",
    "bank-signup-form/src/components/Step3.jsx": """import React from "react";

const Step3 = ({ formData, t }) => {
  return (
    <div className="space-y-2 text-sm">
      <p><strong>{t.name}:</strong> {formData.name}</p>
      <p><strong>{t.email}:</strong> {formData.email}</p>
      <p><strong>{t.phone}:</strong> {formData.phone}</p>
      <p><strong>{t.pan}:</strong> {formData.pan}</p>
    </div>
  );
};

export default Step3;
""",
    "bank-signup-form/src/SignUpForm.jsx": "",  # We'll add this next
}

# Write files
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

"✅ Basic project structure and files (except SignUpForm.jsx) created!"
