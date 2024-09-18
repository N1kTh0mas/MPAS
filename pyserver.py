from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/play-audio', methods=['POST'])
def play_audio():
    data = request.json
    
    # Extract the message, mode, and other relevant data from the request
    message = data.get('message')
    speaker_mode = data.get('speaker_mode')
    spanish = data.get('spanish')
    alarm_type = data.get('alarm_type', None)  # Only for modes 2 and 3
    alarm_amount = data.get('alarm_amount', None)  # Only for modes 2 and 3
    speaker_ids = data.get('speaker_ids')

    # Prepare the arguments for the Python script
    script_args = [
        'python3', 'SoundHandler.py',
        message,
        str(spanish),  # Convert to string to pass as argument
        str(speaker_ids),  # List of speaker IDs
        str(speaker_mode)  # Speaker mode (1, 2, or 3)
    ]

    if speaker_mode in ['2', '3']:  # Only for modes 2 or 3
        script_args.append(alarm_type)
        script_args.append(str(alarm_amount))

    try:
        # Execute the Python script with the provided arguments
        subprocess.run(script_args, check=True)
        return jsonify({'status': 'success', 'message': 'Audio command sent to speaker'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
