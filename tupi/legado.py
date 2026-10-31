"""Heurísticas recuperadas do Colab de março/2026. Não validadas linguisticamente.
Use apenas para propor candidatos, nunca para substituir a forma original.
"""

import re
import unicodedata


def clean_text(s):
    if s is None:
        return ""
    s = str(s)
    s = unicodedata.normalize("NFC", s)
    replacements = {
        "’": "'",
        "‘": "'",
        "´": "'",
        "`": "'",
        "ʹ": "'",
        "′": "'",
        "ʻ": "'",
        "–": "-",
        "—": "-",
        "‑": "-",
        "‐": "-",
        "−": "-",
        "“": '"',
        "”": '"',
        "…": "...",
    }
    for a, b in replacements.items():
        s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"-{2,}", "-", s)
    s = re.sub(r"\s*-\s*", "-", s)
    s = re.sub(r"\s*'\s*", "'", s)
    return s


def convert_j_to_circumflex_i(s):
    return s.replace("J", "Î").replace("j", "î")


def replace_qc_to_ks(s):
    s = re.sub(r"QÜ", "KÛ", s)
    s = re.sub(r"GÜ", "GÛ", s)
    s = re.sub(r"qü", "kû", s)
    s = re.sub(r"gü", "gû", s)
    s = re.sub(r"QU", "K", s)
    s = re.sub(r"qu", "k", s)
    s = re.sub(r"C(?=[EIYÉÍÝÊĨỸ])", "S", s)
    s = re.sub(r"c(?=[eiyéíýêĩỹ])", "s", s)
    s = re.sub(r"C", "K", s)
    s = re.sub(r"c", "k", s)
    return s


def replace_s_variants(s):
    s = s.replace("Ç", "S").replace("ç", "s")
    s = re.sub(r"SS", "S", s)
    s = re.sub(r"ss", "s", s)
    return s


def convert_specific_gu_semivowels(s):
    patterns = [
        (r"(^|[-'])GUA", r"\1GÛA"),
        (r"(^|[-'])GUE", r"\1GÛE"),
        (r"(^|[-'])GUI", r"\1GÛI"),
        (r"(^|[-'])GUY", r"\1GÛY"),
        (r"(^|[-'])GOA", r"\1GÛA"),
        (r"(^|[-'])GOE", r"\1GÛE"),
        (r"(^|[-'])GOI", r"\1GÛI"),
        (r"(^|[-'])GOY", r"\1GÛY"),
        (r"(^|[-'])KUA", r"\1KÛA"),
        (r"(^|[-'])KUE", r"\1KÛE"),
        (r"(^|[-'])KUI", r"\1KÛI"),
        (r"(^|[-'])KUY", r"\1KÛY"),
    ]
    for pat, rep in patterns:
        s = re.sub(pat, rep, s)
    return s


def convert_common_suffixes(s):
    s = s.replace("MIRI", "MIRĨ")
    return s


term_overrides = {
    "AI": "AÎ",
    "AIBA": "AÍBA",
    "AIB-ARA": "AÍB-ARA",
    "AIB-E": "AÍB-E",
    "AIB'-I": "AÍB'-I",
    "AIA": "ÃÎA",
    "AIA-PUÃ": "ÃÎA-PUÃ",
    "AI-BARA": "ÃÎ-BARA",
    "AI-BA-Ú": "ÃÎ-BA-Ú",
    "AI-BORA": "ÃÎ-BORA",
    "AI-ÇABA": "AÎ-SABA",
    "AI-ÇY-YRA": "AÎ-SY-YRA",
    "AI-GOERA": "AÎ-GÛERA",
    "AI-IOARA": "ÃÎ-IOARA",
    "AIPI": "AÎPI",
    "AIPI-MAKASERA": "AÎPI-MAKASERA",
    "AIPI-MIXIRA": "AÎPI-MIXIRA",
    "AIPI-Y'": "AÎPI-Y'",
    "AIPÓ-BAE": "AÎPÓ-BA'E",
    "AIPÓ-ÇUI": "AÎPÓ-SUÎ",
    "AIR-A": "AÎR-A",
    "AIURU-ÍLUBA-KANGA": "AÎURU-ÎUBA-KANGA",
    "AIXO": "AÎXÓ",
    "AIÍXBA": "AÎYBA",
    "AIVY-BENA": "AÎY-BENA",
    "AMYIA": "AMYÎA",
    "AMYI-'OKA": "AMYÎ-'OKA",
    "AMYNI U": "AMYNÎÎU",
    "AMYNI-TU-YBA": "AMYNÎÎU-YBA",
    "AKAIU-TEBIRÔ": "AKAÎU-TEBIRÕ",
    "Á": "Ã",
    "Á XE": "Ã XE",
    "AÂ-NDE": "AÃ-NDE",
    "AAN E-NHÊ": "AAN-E-NHÊ",
}


def normalize_navarro(s):
    s0 = clean_text(s).upper()
    if not s0:
        return ""
    if s0 in term_overrides:
        return term_overrides[s0]
    s1 = s0
    s1 = replace_s_variants(s1)
    s1 = convert_j_to_circumflex_i(s1)
    s1 = replace_qc_to_ks(s1)
    s1 = convert_specific_gu_semivowels(s1)
    s1 = convert_common_suffixes(s1)
    replacements = {
        "GUAÇU": "GÛASU",
        "GOAÇU": "GÛASU",
        "GUASU": "GÛASU",
        "GOASU": "GÛASU",
        "GUYRA": "GÛYRA",
        "GOYRA": "GÛYRA",
        "GUARA": "GÛARA",
        "GOARA": "GÛARA",
        "GUERA": "GÛERA",
        "GOERA": "GÛERA",
        "GUATA": "GÛATA",
        "GOATA": "GÛATA",
    }
    for a, b in replacements.items():
        s1 = s1.replace(a, b)
    s1 = re.sub(r"-{2,}", "-", s1)
    s1 = re.sub(r"\s+", " ", s1).strip()
    return s1
