# Assistante virtuelle vocale (Darija) pour medecins

Had l-projet kay3ti assistante virtuelle vocale b darija lmgharbiya, mوجهة lmedecins bach t3awn f l-istقبال, l-ordonnances, w tdir triage sريع.

## Chno katdir?
- Tkhrej jawabat b darija 3la salam, rendez-vous, l-a3rad (symptomes), wasfa (ordonnance), w l-7الات المستعجلة.
- Tqdar tkhddem b text wla b sawt.

## Ist3mal

```bash
pip install -r requirements.txt
python assistant.py --text "salam docteur"
```

Bash tkhddem b sawt (microphone):

```bash
python assistant.py
```

Ila bghiti bla sawt:

```bash
python assistant.py --text "bghit n7جز rendez-vous" --silent
```

## Nmajdijat (examples)
- "salam docteur, labas?"
- "bghit n7جز rdv nhar tlata"
- "3ndi sda3 w s3ayba f nfas"
- "wach t9dar t3awd 3la wasfa?"
- "had l7ala musta3jla?"

## Mola7adat
- L-recognition kayst3mel Google Speech API (language: ar-MA).
- Ila bghiti tbdl l-intents w l-jawab, qdar t3ddl `INTENTS` w `RESPONSES` f `assistant.py`.
