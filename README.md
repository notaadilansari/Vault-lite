Vault Lite 🔐
A File-Based Credential Manager
Vault Lite is a simplified, Command Line Interface (CLI) application built as part of the Python Winter Sprint 2026 (Core Track). This project focuses on mastering Python File I/O and JSON data persistence, simulating the core logic of a backend credential management system.
🚀 Overview
The goal of Vault Lite is to provide a structured way to store, retrieve, and update account credentials (Website, Username, and Password) using a local JSON file.
Core Learning Objectives:
Implementing persistent storage using json.
Structuring a loop-based CLI menu.
Basic CRUD (Create, Read, Update) operations in Python.
✨ Features
Persistent Storage: Data is saved in vault_data.json and remains available even after the program restarts.
Add Credentials: Securely save a website name, username, and password.
View Credentials: List all stored entries in a readable format.
Update Credentials: Modify passwords for existing entries.
Loop-based Navigation: A continuous menu system for seamless user experience.
🛠️ Technical Implementation
Credential Format
All data is stored in a structured JSON format to ensure compatibility and ease of reading:
Website
Username
Password
File Storage
The program automatically creates and manages a file named: vault_data.json.# Vault-lite
