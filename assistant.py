"""Assistante virtuelle vocale (Darija) pour medecins."""

import argparse
import datetime
import random

import pyttsx3
import speech_recognition as sr


INTENTS = {
    "salam": [
        "salam",
        "salama",
        "sbah",
        "massa",
        "kifach",
        "labas",
    ],
    "rdv": [
        "rendez-vous",
        "rdv",
        "nwa3ed",
        "mo3id",
        "mou3id",
        "hdd",
    ],
    "symptomes": [
        "wja3",
        "sda3",
        "dawkh",
        "homa",
        "sokhan",
        "khtan",
        "dique",
        "k7a",
    ],
    "ordonnance": [
        "dwa",
        "dawa",
        "ordonnance",
        "wasfa",
        "tibb",
    ],
    "urgence": [
        "isti3jal",
        "istinja",
        "tari2",
        "moustachfa",
        "s3af",
        "rou7",
    ],
    "farewell": [
        "bslama",
        "m3a salama",
        "chokran",
        "allah y3tik",
    ],
}

RESPONSES = {
    "salam": [
        "Salam docteur, kidayr? chno n9dar n3awen?",
        "Salam, ana m3ak. chno bghiti tdir daba?",
    ],
    "rdv": [
        "Wach bghiti ntsajjel rendez-vous? 3tini smiya w nhar li bghiti.",
        "N9dar n7جز ليك mo3id. 3tini nhar w sa3a li mnassbin.",
    ],
    "symptomes": [
        "3afak wassif liya l3alamat: fin wja3? w ch7al mn nhar?",
        "Chno kayn mn 3alamat? 3tini tafasil 3la l7ala.",
    ],
    "ordonnance": [
        "N9dar nktb wasfa wla n3awed 3la dawa. chno smit dawa?",
        "Wach bghiti t7dith l'ordonnance? 3tini smiyat l-adwiya.",
    ],
    "urgence": [
        "Ila l7ala khatira, 3afak sir l'moustachfa qrib wla 3ayet 141.",
        "Hadi katban 7ala مستعجلة. 3afak t2akkad mn s3af f l7in.",
    ],
    "farewell": [
        "Bslama docteur, ila 7tajt chi 7aja ana hna.",
        "Allah y3tik se77a, ana m3ak ay wa9t.",
    ],
    "fallback": [
        "Ma fhemtch mzyan. 3afak 3awed b klam wadeh.",
        "Smah li, n9dar n3awed? chno bghiti tdir?",
    ],
}


def speak(text: str) -> None:
    engine = pyttsx3.init()
    engine.setProperty("rate", 165)
    engine.say(text)
    engine.runAndWait()


def listen() -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio, language="ar-MA")


def normalize(text: str) -> str:
    return text.lower().strip()


def detect_intent(text: str) -> str:
    normalized = normalize(text)
    for intent, keywords in INTENTS.items():
        if any(keyword in normalized for keyword in keywords):
            return intent
    return "fallback"


def craft_response(intent: str) -> str:
    response_pool = RESPONSES.get(intent, RESPONSES["fallback"])
    timestamp = datetime.datetime.now().strftime("%H:%M")
    base = random.choice(response_pool)
    if intent == "rdv":
        return f"{base} (Lwa9t daba: {timestamp})"
    return base


def run_text_mode(text: str) -> str:
    intent = detect_intent(text)
    return craft_response(intent)


def main() -> None:
    parser = argparse.ArgumentParser(description="Assistante virtuelle vocale (Darija) pour medecins")
    parser.add_argument("--text", help="Dkhil text باش تجاوبك assistante")
    parser.add_argument("--silent", action="store_true", help="Ma tf3lch sawt")
    args = parser.parse_args()

    if args.text:
        user_text = args.text
    else:
        user_text = listen()

    reply = run_text_mode(user_text)
    print(f"User: {user_text}")
    print(f"Assistant: {reply}")

    if not args.silent:
        speak(reply)


if __name__ == "__main__":
    main()
