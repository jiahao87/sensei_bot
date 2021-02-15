import six
from google.cloud import texttospeech, storage, speech
from google.cloud import translate_v2 as translate

from config import GOOGLE_APPLICATION_CREDENTIALS, LANGUAGE_CODE, TEXTTOSPEECH_NAME

import os


if GOOGLE_APPLICATION_CREDENTIALS is not None:
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS


def synthesize_text(text, filename):
    """
    Synthesizes speech from the input string of text
    """
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code=LANGUAGE_CODE,
        name=TEXTTOSPEECH_NAME,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        # pitch=0,  # adjust pitch
        speaking_rate=0.9  # adjust rate of speaking, with 1 being normal
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    with open(filename, "wb") as out:
        out.write(response.audio_content)


def translate_text(text, target=LANGUAGE_CODE[:2]):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)
    return result["translatedText"]


def upload_file(filename, bucket_name):
    """
    Upload file to Google Storage
    """
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(filename)
    # Uploading from local file without open()
    blob.upload_from_filename(filename)


def transcribe_voice(filename, bucket_name):
    """
    Transcribes an audio recording to text
    """
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    # gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
    gcs_uri = f"gs://{bucket_name}/{filename}"

    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code=LANGUAGE_CODE,
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    response_text = ' '.join([result.alternatives[0].transcript for result in response.results])
    return response_text
