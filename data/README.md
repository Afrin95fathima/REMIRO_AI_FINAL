# Data Directory

This directory stores user session data and career analysis results.

## Structure

- User profile data is stored as JSON files
- Each user session creates a unique data file
- Data is automatically cleaned up based on retention policies

## Privacy

All user data is:
- Stored locally
- Encrypted when possible
- Subject to user consent
- Deletable upon request

## File Naming Convention

Files are named using the pattern: `{username}_{session_id}.json`

Example: `john_doe_1234567890.json`