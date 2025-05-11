# 定义种子模式/种子正则

seed_patterns = {
    "Add": [
        "\badd\b",
        "\badded\b",
        "\badd\s+in\b",
        "\bintroduce\b"
    ],
    "CollectLayer": [
        "\bcollect\s*(?:aqueous|organic|desired)?\s*layer\b",
        "\bcollect\s*fraction\b"
    ],
    "Concentrate": [
        "\bconcentrate\b",
        "\bevaporat(?:e|ed|ing)\b",
        "\brotavap\b"
    ],
    "Degas": [
        "\bdegas\b",
        "\bpurg(?:e|ed|ing)\b"
    ],
    "DrySolid": [
        "\bdry\s+the\s+solid\b",
        "\bdried\s+solid\b"
    ],
    "DrySolution": [
        "\bdry\s+(?:the\s+)?solution\b",
        "\bdry\s+(?:the\s+)?organic\s+layer\b",
        "\bdried\s+over\b"
    ],
    "Extract": [
        "\bextract\b",
        "\btransfer.*into\s+a\s*different\s*solvent\b"
    ],
    "Filter": [
        "\bfilter\b",
        "\bfiltered\b",
        "\bfiltrate\b"
    ],
    "MakeSolution": [
        "\bmake\s+a?\s*solution\b",
        "\bmix(?:ed|ing)?\b",
        "\bprepare\s+a?\s*solution\b"
    ],
    "Microwave": [
        "\bmicrowave\b"
    ],
    "Partition": [
        "\bpartition\b",
        "\badd\s+two\s+immiscible\s+solvents\b"
    ],
    "PH": [
        "\bph\b",
        "\bneutralize\b",
        "\badjust\s+ph\b"
    ],
    "PhaseSeparation": [
        "\bphase\s+separation\b",
        "\bseparate\s+the\s+(?:aqueous|organic)\s+phase\b"
    ],
    "Purify": [
        "\bpurify\b",
        "\bpurification\b"
    ],
    "Quench": [
        "\bquench\b",
        "\bstop\s+reaction\b"
    ],
    "Recrystallize": [
        "\brecrystalliz(?:e|ed|ation)\b"
    ],
    "Reflux": [
        "\breflux\b"
    ],
    "SetTemperature": [
        "\bset\s+temperature\b",
        "\bheat\s+to\b",
        "\bcool\s+to\b"
    ],
    "Sonicate": [
        "\bsonicat(?:e|ed|ion)\b",
        "\bsonic\s+treatment\b"
    ],
    "Stir": [
        "\bstir\b",
        "\bstirr(?:ed|ing)\b"
    ],
    "Triturate": [
        "\btriturat(?:e|ed|ion)\b"
    ],
    "Wait": [
        "\bstood\s+for\b",
        "\bwait(?:ed|ing)?\b",
        "\bleave\s+(?:the\s+)?reaction\b"
    ],
    "Wash": [
        "\bwash\b",
        "\bwashed\b"
    ],
    "Yield": [
        "\byield\b",
        "\bobtain(?:ed)?\b"
    ],
    "FollowOtherProcedure": [
        "\bfollow\s+(?:the\s+)?procedure\b",
        "\bprocedure\s+described\s+elsewhere\b"
    ],
    "InvalidAction": [
        "\bunknown\s+action\b",
        "\bunsupported\s+operation\b"
    ],
    "NoAction": [
        "\bno\s+action\b",
        "\bno\s+actual\s+step\b"
    ],
    "yield": [
        "\byield\b"
    ],
    "reaction": [
        "\breaction\b"
    ],
    "catalyst": [
        "\bcatalyst\b"
    ],
    "degradation": [
        "\bdegradation\b"
    ],
    "transformation": [
        "\btransformation\b"
    ],
    "transmission": [
        "\btransmission\b"
    ],
    "obtained": [
        "\bobtained\b"
    ],
    "mitochondrial": [
        "\bmitochondrial\b"
    ],
    "disinfection": [
        "\bdisinfection\b"
    ],
    "detected": [
        "\bdetected\b"
    ],
    "formation": [
        "\bformation\b"
    ],
    "condensation": [
        "\bcondensation\b"
    ],
    "reactions": [
        "\breactions\b"
    ],
    "production": [
        "\bproduction\b"
    ],
    "conversion": [
        "\bconversion\b"
    ],
    "contamination": [
        "\bcontamination\b"
    ],
    "yields": [
        "\byields\b"
    ],
    "maintenance": [
        "\bmaintenance\b"
    ],
    "Transmission": [
        "\bTransmission\b"
    ],
    "removal": [
        "\bremoval\b"
    ],
    "Krebs cycle": [
        "\bKrebs\ cycle\b"
    ],
    "precipitation": [
        "\bprecipitation\b"
    ],
    "transfére": [
        "\btransfére\b"
    ],
    "chemical reactions": [
        "\bchemical\ reactions\b"
    ],
    "catalysts": [
        "\bcatalysts\b"
    ],
    "Krebs": [
        "\bKrebs\b"
    ],
    "produced": [
        "\bproduced\b"
    ],
    "release": [
        "\brelease\b"
    ],
    "digestion": [
        "\bdigestion\b"
    ],
    "separation": [
        "\bseparation\b"
    ],
    "fabrication": [
        "\bfabrication\b"
    ],
    "refluxing": [
        "\brefluxing\b"
    ],
    "mitochondrial function": [
        "\bmitochondrial\ function\b"
    ],
    "removed": [
        "\bremoved\b"
    ],
    "interaction": [
        "\binteraction\b"
    ],
    "annulation": [
        "\bannulation\b"
    ],
    "Chemistry": [
        "\bChemistry\b"
    ],
    "fermentation": [
        "\bfermentation\b"
    ],
    "reflux": [
        "\breflux\b"
    ],
    "enzymes": [
        "\benzymes\b"
    ],
    "preparation": [
        "\bpreparation\b"
    ],
    "hydrolysis": [
        "\bhydrolysis\b"
    ],
    "isolated": [
        "\bisolated\b"
    ],
    "heating": [
        "\bheating\b"
    ],
    "maintenance of phosphate": [
        "\bmaintenance\ of\ phosphate\b"
    ],
    "conduct chemical transformation": [
        "\bconduct\ chemical\ transformation\b"
    ],
    "activation": [
        "\bactivation\b"
    ],
    "hydrolyzed": [
        "\bhydrolyzed\b"
    ],
    "metabolism": [
        "\bmetabolism\b"
    ],
    "freezing": [
        "\bfreezing\b"
    ],
    "Intermediate 6": [
        "\bIntermediate\ 6\b"
    ],
    "Oxygen": [
        "\bOxygen\b"
    ],
    "melting": [
        "\bmelting\b"
    ],
    "bromination": [
        "\bbromination\b"
    ],
    "loading": [
        "\bloading\b"
    ],
    "contaminants": [
        "\bcontaminants\b"
    ],
    "injection": [
        "\binjection\b"
    ],
    "D": [
        "\bD\b"
    ],
    "maintenance of the environment": [
        "\bmaintenance\ of\ the\ environment\b"
    ],
    "synthesized": [
        "\bsynthesized\b"
    ],
    "intramolecular": [
        "\bintramolecular\b"
    ],
    "Intermediates": [
        "\bIntermediates\b"
    ],
    "selectively": [
        "\bselectively\b"
    ],
    "converted to desired products": [
        "\bconverted\ to\ desired\ products\b"
    ],
    "Hydrolysis": [
        "\bHydrolysis\b"
    ],
    "transféred": [
        "\btransféred\b"
    ],
    "extracted": [
        "\bextracted\b"
    ],
    "corrosion": [
        "\bcorrosion\b"
    ],
    "recovered": [
        "\brecovered\b"
    ],
    "exchange": [
        "\bexchange\b"
    ],
    "reproduction": [
        "\breproduction\b"
    ],
    "solvent": [
        "\bsolvent\b"
    ],
    "production of nickel": [
        "\bproduction\ of\ nickel\b"
    ],
    "production of lithium": [
        "\bproduction\ of\ lithium\b"
    ],
    "bromine": [
        "\bbromine\b"
    ],
    "treated": [
        "\btreated\b"
    ],
    "mitochondrial membrane": [
        "\bmitochondrial\ membrane\b"
    ],
    "maintenance of oxidation": [
        "\bmaintenance\ of\ oxidation\b"
    ],
    "Desilylation": [
        "\bDesilylation\b"
    ],
    "migration": [
        "\bmigration\b"
    ],
    "Oxygenation": [
        "\bOxygenation\b"
    ],
    "infection": [
        "\binfection\b"
    ],
    "isolation": [
        "\bisolation\b"
    ],
    "substitution": [
        "\bsubstitution\b"
    ],
    "binding": [
        "\bbinding\b"
    ],
    "purification": [
        "\bpurification\b"
    ],
    "trapping": [
        "\btrapping\b"
    ],
    "deprotection": [
        "\bdeprotection\b"
    ],
    "observed": [
        "\bobserved\b"
    ],
    "generated": [
        "\bgenerated\b"
    ],
    "conducting": [
        "\bconducting\b"
    ],
    "inhibited": [
        "\binhibited\b"
    ],
    "transférer": [
        "\btransférer\b"
    ],
    "substrate": [
        "\bsubstrate\b"
    ],
    "Removal": [
        "\bRemoval\b"
    ],
    "converted": [
        "\bconverted\b"
    ],
    "hydrosilylation": [
        "\bhydrosilylation\b"
    ],
    "transféring": [
        "\btransféring\b"
    ],
    "failure": [
        "\bfailure\b"
    ]
}