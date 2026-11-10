#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wiener Dienst - Google Ads 10/10 Quality Score Generator
Builds 27 production-ready, pixel-perfect HTML pages + sitemap.xml + robots.txt
"""

import os
import json
from datetime import datetime

# Common Configuration
DOMAIN = "https://wiener-dienst.at"
PHONE_DISPLAY = "0660 606 0775"
PHONE_TEL = "+436606060775"
EMAIL = "office@wiener-dienst.at"
FORMSPREE_ACTION = "https://formspree.io/f/mvkoaggb"

# Vienna Shield SVG (Wiener Wappen: Red shield with white cross)
VIENNA_SHIELD_SVG = """<svg class="w-10 h-10 sm:w-11 sm:h-11 translate-y-[3px] shrink-0 drop-shadow-sm group-hover:scale-105 transition" viewBox="0 0 100 120" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Wiener Wappen Kalkan Logo">
    <path d="M8 8H92V72C92 98 50 116 50 116C50 116 8 98 8 72V8Z" fill="#DC2626" stroke="#991B1B" stroke-width="4"/>
    <rect x="42" y="20" width="16" height="76" fill="white" rx="1"/>
    <rect x="20" y="44" width="60" height="16" fill="white" rx="1"/>
</svg>"""

# 22 Targeted Keywords
KEYWORDS = [
    {
        "file": "entruempelung-wien.html",
        "kw": "Entrümpelung Wien",
        "badge": "Ihr Wiener Fachbetrieb Nr. 1 • 100% Fixpreis-Garantie",
        "h1": "Entrümpelung Wien",
        "title": "Entrümpelung Wien | Wiener Dienst – Räumungsfirma zum Fixpreis",
        "meta_desc": "Professionelle Entrümpelung Wien zum garantierten Fixpreis. Kostenlose Besichtigung in allen 23 Bezirken, besenreine Übergabe & Wertanrechnung. ☎ 0660 606 0775",
        "category": "Räumung & Entrümpelung",
        "hero_lead": "Ihr verlässlicher Wiener Traditionsbetrieb für besenreine Räumungen und Entrümpelungen in allen 23 Wiener Gemeindebezirken. Keine versteckten Kosten, 0 € Anfahrt und persönliche Handschlagqualität.",
        "calc_default": "Wohnungentrümpelung wien",
        "detail_content": """
        <p>Eine <strong>Entrümpelung Wien</strong> erfordert Erfahrung, zügiges Anpacken und absolute Kostentransparenz. Ob eine verwinkelte Altbauwohnung im 7. Bezirk Neubau ohne Personenlift, ein weitläufiges Einfamilienhaus in Döbling oder ein vollgeräumtes Kellerabteil in Favoriten: Unser eingespieltes Wiener Team meistert jede Herausforderung schnell, diskret und vorschriftsgemäß nach den Vorgaben der MA 48.</p>
        <p>Wir wissen, dass eine Räumung oft mit emotionalen oder zeitlich drängenden Situationen einhergeht – sei es nach einem Todesfall, vor einer Schlüsselübergabe an Wiener Wohnen oder beim Umzug ins Pflegeheim. Bei <strong>Wiener Dienst</strong> erhalten Sie daher alles aus einer Hand: von der kostenlosen Besichtigung vor Ort über die fachgerechte Demontage bis zur besenreinen Endreinigung.</p>
        """,
        "faqs": [
            ("Was kostet eine Entrümpelung Wien im Durchschnitt?",
             "Die Kosten für eine professionelle Entrümpelung Wien richten sich nach dem Volumen, dem Stockwerk (mit/ohne Lift) und eventuellen Demontagearbeiten. Wir bieten eine 100% kostenlose Besichtigung an und erstellen Ihnen direkt vor Ort ein verbindliches Festpreisangebot ohne spätere Nachforderungen."),
            ("Wie schnell kann eine Entrümpelung in Wien durchgeführt werden?",
             "Oft können wir bereits am Tag Ihrer Anfrage eine kostenlose Vor-Ort-Besichtigung durchführen. Die eigentliche Entrümpelung Wien erfolgt je nach Dringlichkeit innerhalb von 24 bis 48 Stunden – auf Wunsch auch an Samstagen ohne Wochenendaufschlag."),
            ("Gibt es eine Wertanrechnung für noch brauchbare Möbel?",
             "Ja! Verwertbare Möbelstücke, Antiquitäten, Gemälde, Porzellan oder Sammlerobjekte schätzen wir fair und rechnen deren Gegenwert direkt 1:1 von den Räumungskosten ab. In vielen Fällen reduziert sich der Endpreis dadurch erheblich oder wird sogar komplett kostenfrei."),
            ("Übernehmen Sie auch die besenreine Übergabe an Wiener Wohnen oder Hausverwaltungen?",
             "Selbstverständlich. Wir übergeben jede Wohnung garantiert besenrein und nach allen spezifischen Vorgaben der Hausverwaltung oder von Wiener Wohnen inklusive Dokumentation und Protokollierung.")
        ]
    },
    {
        "file": "wien-entruempelung.html",
        "kw": "Wien Entrümpelung",
        "badge": "Express-Service in allen 23 Bezirken • 0 € Anfahrt",
        "h1": "Wien Entrümpelung",
        "title": "Wien Entrümpelung | Wiener Dienst – Schnell, Günstig & Besenrein",
        "meta_desc": "Ihre verlässliche Wien Entrümpelung zum transparenten Pauschalpreis. Wohnungen, Häuser, Keller & Gewerbe. Gratis Besichtigung! ☎ 0660 606 0775",
        "category": "Räumung & Entrümpelung",
        "hero_lead": "Kompetente Partner für jede Wien Entrümpelung mit Fixpreis-Versprechen. Wir räumen blitzschnell, zuverlässig und hinterlassen jedes Objekt garantiert besenrein.",
        "calc_default": "Wohnungentrümpelung wien",
        "detail_content": """
        <p>Für eine reibungslose <strong>Wien Entrümpelung</strong> setzen private Eigentümer, Mieter und Hausverwaltungen auf unsere Handschlagqualität. Wir kennen die Wiener Parkplatzsituation, organisieren bei Bedarf Halteverbotszonen und transportieren selbst schwerste Möbelstücke schonend durch Altbautreppenhäuser.</p>
        <p>Alle anfallenden Abfälle werden nach den strengen Richtlinien der Wiener MA 48 sorgfältig getrennt (Sperrmüll, Altmetall, Altholz, Bauschutt, Problemstoffe) und umweltschonend den offiziellen Wiener Recyclinghöfen zugeführt.</p>
        """,
        "faqs": [
            ("Muss ich bei der Wien Entrümpelung selbst anwesend sein?",
             "Nein, Ihre persönliche Anwesenheit während der gesamten Arbeit ist nicht zwingend erforderlich. Nach der Schlüsselübergabe und Vorbesprechung führen wir die Wien Entrümpelung eigenständig durch und rufen Sie zur gemeinsamen besenreinen Endabnahme an."),
            ("Werden Halteverbotszonen in Wien von Ihnen organisiert?",
             "Ja, bei Bedarf beantragen und errichten wir für den Einsatztag vorschriftsmäßige Halteverbotszonen vor Ihrem Wiener Gebäude, damit der Abtransport zügig und ohne Verkehrsbehinderung erfolgen kann."),
            ("Wie funktioniert die Abrechnung bei der Wien Entrümpelung?",
             "Bei uns gilt: Was vereinbart wurde, gilt. Sie erhalten vorab einen schriftlichen Fixpreis. Erst nach erfolgreicher und besenreiner Fertigstellung und Ihrer vollen Zufriedenheit erfolgt die Bezahlung."),
            ("Entsorgen Sie auch Sondermüll und Elektrogeräte fachgerecht?",
             "Ja, Elektrogeräte, Farben, Lacke und sonstige Problemstoffe werden strikt getrennt und vorschriftsmäßig über die autorisierten Entsorgungsstellen der Stadt Wien entsorgt.")
        ]
    },
    {
        "file": "entruempelung-firma.html",
        "kw": "Entrümpelung firma",
        "badge": "Zertifizierte Entrümpelung Firma Wien • 100% Versichert",
        "h1": "Entrümpelung firma",
        "title": "Entrümpelung firma Wien | Wiener Dienst – Geprüfter Fachbetrieb",
        "meta_desc": "Geprüfte Entrümpelung firma in Wien mit Handschlagqualität. Fixpreis-Garantie, Wertanrechnung & 0 € Besichtigung. Jetzt anrufen: ☎ 0660 606 0775",
        "category": "Fachbetrieb Wien",
        "hero_lead": "Als etablierte Entrümpelung firma in Wien bieten wir Ihnen Full-Service-Leistungen mit vollumfänglicher Betriebshaftpflichtversicherung und verbindlichen Pauschalpreisen.",
        "calc_default": "Wohnungentrümpelung wien",
        "detail_content": """
        <p>Die Wahl der richtigen <strong>Entrümpelung firma</strong> schützt Sie vor bösen Überraschungen wie versteckten Stundensätzen oder illegal entsorgtem Müll. Wiener Dienst ist ein voll konzessionierter Fachbetrieb mit langjähriger Erfahrung in ganz Wien und Niederösterreich.</p>
        <p>Unsere Mitarbeiter sind fest angestellt, geschult und arbeiten mit höchster Sorgfalt, um Stiegenhäuser, Aufzüge und Türen während der Räumung vor jeglichen Beschädigungen zu schützen.</p>
        """,
        "faqs": [
            ("Warum sollte ich eine gewerbliche Entrümpelung firma beauftragen?",
             "Eine seriöse Entrümpelung firma bietet Ihnen volle Haftungssicherheit, ordentliche Rechnungen für den Steuerausgleich, geschultes Personal und garantiert eine umweltgerechte Mülltrennung nach MA 48 Standards."),
            ("Ist die Besichtigung durch Ihre Entrümpelung firma wirklich kostenlos?",
             "Ja, zu 100%. Unsere Fachberater kommen unverbindlich und kostenfrei in alle 23 Wiener Bezirke sowie ins Wiener Umland, um den Umfang exakt einzuschätzen."),
            ("Welche Versicherungsdeckung hat Ihre Entrümpelung firma?",
             "Wir verfügen über eine umfassende Betriebshaftpflichtversicherung, die eventuelle Schäden am Gebäude, im Stiegenhaus oder an Nachbarobjekten vollumfänglich abdeckt."),
            ("Bietet Ihre Entrümpelung firma auch Firmen- und Büroräumungen an?",
             "Ja, neben privaten Haushalten räumen wir auch Büros, Geschäftslokale, Lagerhallen und Ordinationen inklusive Demontage von Trennwänden und Altaktenvernichtung nach DSGVO.")
        ]
    },
    {
        "file": "raeumung-wien.html",
        "kw": "Räumung Wien",
        "badge": "Professionelle Räumung Wien • Schnell, Diskret & Günstig",
        "h1": "Räumung Wien",
        "title": "Räumung Wien | Wiener Dienst – Schnell & Besenrein zum Fixpreis",
        "meta_desc": "Zuverlässige Räumung Wien vom Fachmann. Wohnungsräumung, Kellerräumung, Verlassenschaftsräumung mit Wertausgleich. Gratis Besichtigung! ☎ 0660 606 0775",
        "category": "Räumung & Entrümpelung",
        "hero_lead": "Professionelle Räumung Wien für Wohnungen, Häuser, Keller und Dachböden. Profitieren Sie von unserer Fixpreis-Garantie und kostenloser Besichtigung.",
        "calc_default": "Wohnungentrümpelung wien",
        "detail_content": """
        <p>Jede <strong>Räumung Wien</strong> bringt individuelle Anforderungen mit sich: vom Abbau massiver Einbauküchen über das Entfernen von verklebten Teppichböden bis hin zum Abtransport sperriger Möbel. Wiener Dienst wickelt jeden Auftrag zügig und strukturiert ab.</p>
        <p>Wir arbeiten termingerecht und übergeben das Objekt besenrein, sodass Sie sich entspannt um die nächsten Schritte wie Sanierung, Verkauf oder Wohnungsrückgabe kümmern können.</p>
        """,
        "faqs": [
            ("Wie läuft eine professionelle Räumung Wien ab?",
             "Nach Ihrer Kontaktaufnahme führen wir eine kostenlose Vor-Ort-Besichtigung durch, berechnen etwaige Wertanrechnungen und vereinbaren einen Fixtermin. Am Einsatztag räumen unsere Fachkräfte das Objekt vollständig aus und übergeben es besenrein."),
            ("Können Sie auch schwere Möbel wie Klaviere oder Tresore bei der Räumung Wien entsorgen?",
             "Ja, unser Team verfügt über professionelle Hebe- und Transportwerkzeuge für schwere Lasten wie Klaviere, massive Tresore oder gewerbliche Geräte."),
            ("Wie lange dauert eine durchschnittliche Wohnungsräumung in Wien?",
             "Eine Standardwohnung mit 60 bis 80 m² räumen wir in der Regel innerhalb eines einzigen Werktages komplett aus."),
            ("Muss vor der Räumung Wien alles in Kisten gepackt werden?",
             "Nein, Sie müssen überhaupt nichts vorbereiten. Wenn Sie möchten, übernehmen wir auch das komplette Einpacken von Kleinteilen, Geschirr und Hausrat.")
        ]
    },
    {
        "file": "raeumungsfirma.html",
        "kw": "Räumungsfirma",
        "badge": "Ihre Nr. 1 Räumungsfirma in Wien • Handschlagqualität",
        "h1": "Räumungsfirma",
        "title": "Räumungsfirma Wien | Wiener Dienst – Seriös, Pünktlich, Fixpreis",
        "meta_desc": "Ihre zuverlässige Räumungsfirma in Wien. Besenreine Räumung von Wohnungen, Kellern, Verlassenschaften. 0 € Besichtigung! ☎ 0660 606 0775",
        "category": "Fachbetrieb Wien",
        "hero_lead": "Als renommierte Räumungsfirma in Wien stehen wir für Verlässlichkeit, Schnelligkeit und absolute Preissicherheit. Jetzt kostenlose Besichtigung sichern!",
        "calc_default": "Wohnungentrümpelung wien",
        "detail_content": """
        <p>Als qualifizierte <strong>Räumungsfirma</strong> sind wir Ihr Partner, wenn es um zügige Entlastung bei Räumungsprojekten geht. Wir garantieren Ihnen absolute Handschlagqualität: transparente Angebote ohne kleingedruckte Überraschungen und termintreue Erledigung.</p>
        <p>Dank modernem Fuhrpark und flexiblen Teams sind wir auch für kurzfristige Notfälle oder Räumungen mit straffen Fristen stets einsatzbereit.</p>
        """,
        "faqs": [
            ("Woran erkenne ich eine seriöse Räumungsfirma in Wien?",
             "Eine seriöse Räumungsfirma verlangt niemals Vorauskasse ohne Besichtigung, bietet schriftliche Fixpreis-Angebote mit genauer Leistungsaufstellung, verfügt über Firmenanschrift und Versicherung und garantiert eine vorschriftsmäßige Entsorgung."),
            ("Bietet Ihre Räumungsfirma auch Wochenendtermine an?",
             "Ja, wir führen Räumungen auf Wunsch gerne samstags oder sonntags durch – ohne zusätzliche Sonderzuschläge für die Wochenendarbeit."),
            ("Was geschieht mit noch brauchbaren Dingen bei der Räumungsfirma?",
             "Verwertbare Stücke führen wir dem Second-Hand-Kreislauf oder sozialen Einrichtungen zu und rechnen deren Wert fair gegen die Gesamtkosten an."),
            ("Erhalte ich nach der Räumung eine offizielle Entsorgungsbestätigung?",
             "Ja, auf Wunsch stellen wir Ihnen für Hausverwaltungen oder Behörden eine schriftliche Bestätigung über die ordnungsgemäße Entsorgung nach MA 48 Vorgaben aus.")
        ]
    },
    {
        "file": "moebel-abholen-lassen.html",
        "kw": "Möbel abholen lassen",
        "badge": "Express Möbelabholung Wien • Schnell, Günstig & Bequem",
        "h1": "Möbel abholen lassen",
        "title": "Möbel abholen lassen Wien | Wiener Dienst – Schnell & Günstig",
        "meta_desc": "Alte Möbel abholen lassen in Wien: Couch, Schrank, Bett, Küche & Sperrmüll. Schnell, bequem & zum günstigen Fixpreis ab 0 €. ☎ 0660 606 0775",
        "category": "Möbel & Sperrmüll",
        "hero_lead": "Sie möchten unkompliziert alte Möbel abholen lassen in Wien? Wir tragen Ihre Möbel direkt aus der Wohnung – egal welches Stockwerk – und entsorgen fachgerecht.",
        "calc_default": "Möbel abholen lassen",
        "detail_content": """
        <p>Wer in Wien alte <strong>Möbel abholen lassen</strong> möchte, kennt das Problem: Schleppen durch enge Stiegenhäuser, kein passender Transporter und weite Wege zum nächsten Mistplatz. Wiener Dienst nimmt Ihnen diese schwere Arbeit komplett ab.</p>
        <p>Ob einzelne Polstercouch, sperrige Schrankwand, defekte Waschmaschine oder die alte Einbauküche: Unsere Träger packen kräftig an, demontieren Möbelteile fachgerecht und laden alles direkt in unsere LKW ein.</p>
        """,
        "faqs": [
            ("Muss ich die Möbel selbst auf die Straße stellen?",
             "Nein, keineswegs! Unser Team trägt alle Möbel direkt aus Ihren Wohnräumen, dem Keller oder dem Dachboden – auch bei Altbauten ohne Aufzug im 4. Stock."),
            ("Können Sie auch Einbauküchen und Schränke abbauen?",
             "Ja, unsere Handwerker übernehmen gerne die fachgerechte Demontage von Schränken, Regalsystemen und kompletten Einbauküchen inklusive Abklemmen von Elektrogeräten."),
            ("Wie schnell kann ich Möbel abholen lassen in Wien?",
             "In vielen Fällen ist eine Abholung noch am selben Tag oder innerhalb von 24 Stunden möglich. Schicken Sie uns einfach ein Foto per WhatsApp für ein Sofort-Angebot!"),
            ("Was kostet es, einzelne Möbel abholen zu lassen?",
             "Einzelne Stücke holen wir bereits ab einem günstigen Pauschalpreis ab. Bei hochwertigen gebrauchten Designmöbeln oder Antiquitäten ist oft sogar eine kostenlose Abholung möglich.")
        ]
    },
    {
        "file": "wohnungentruempelung-wien.html",
        "kw": "Wohnungentrümpelung wien",
        "badge": "Spezialist für Wohnungentrümpelung Wien • Besenrein",
        "h1": "Wohnungentrümpelung wien",
        "title": "Wohnungentrümpelung Wien | Wiener Dienst – Besenrein zum Fixpreis",
        "meta_desc": "Seriöse Wohnungentrümpelung Wien. Gemeindewohnung, Eigentum, Mietwohnung besenrein geräumt. Kostenlose Besichtigung! ☎ 0660 606 0775",
        "category": "Wohnungsräumung",
        "hero_lead": "Ihre professionelle Wohnungentrümpelung wien mit Fixpreis-Garantie. Wir räumen Einzimmerwohnungen ebenso wie Großwohnungen zügig und absolut zuverlässig.",
        "calc_default": "Wohnungentrümpelung wien",
        "detail_content": """
        <p>Eine <strong>Wohnungentrümpelung wien</strong> ist Vertrauenssache. Seit vielen Jahren räumen wir Miet-, Genossenschafts- und Eigentumswohnungen in sämtlichen 23 Wiener Bezirken zügig, diskret und besenrein.</p>
        <p>Vom Entfernen alter Vorhänge und Karniesen über das Herausreißen von Spannteppichen bis hin zum Abbau von Hochbetten und Küchenzeilen: Wir hinterlassen die Räumlichkeiten in einwandfreiem Zustand für die reibungslose Übergabe.</p>
        """,
        "faqs": [
            ("Was beinhaltet eine komplette Wohnungentrümpelung wien?",
             "Wir demontieren alle Möbel, packen Hausrat und Kleinteile ein, räumen Nebenräume wie Keller- oder Dachbodenabteile und übergeben die Wohnung besenrein gefegt."),
            ("Entfernen Sie auch Bodenbeläge, Wandvertäfelungen und Fliesen?",
             "Ja, wir führen auch sämtliche Vorbereitungsarbeiten durch, wie das Entfernen von PVC, Teppichen, Laminat, Wandfliesen, Deckenpaneelen und Tapeten."),
            ("Wie verhält es sich mit Wertgegenständen, die während der Räumung gefunden werden?",
             "Sollten bei der Wohnungentrümpelung persönliche Dokumente, Bargeld oder Schmuck auftauchen, werden diese selbstverständlich sofort separat gesichert und Ihnen übergeben."),
            ("Gibt es eine Fixpreis-Garantie bei der Wohnungentrümpelung wien?",
             "Ja, nach der kostenlosen Vor-Ort-Besichtigung erhalten Sie ein schriftliches Pauschalangebot mit Festpreisgarantie – ohne Risiko versteckter Zusatzkosten.")
        ]
    },
    {
        "file": "wohnungsraumung-wien.html",
        "kw": "Wohnungsraumung Wien",
        "badge": "Wohnungsraumung Wien zum Fixpreis • Übergabegarantie",
        "h1": "Wohnungsraumung Wien",
        "title": "Wohnungsraumung Wien | Wiener Dienst – Pünktlich & Besenrein",
        "meta_desc": "Fachgerechte Wohnungsraumung Wien für private und gewerbliche Kunden. Besenrein, termingerecht & mit Wertanrechnung. ☎ 0660 606 0775",
        "category": "Wohnungsräumung",
        "hero_lead": "Verlässliche Wohnungsraumung Wien mit Qualitätsversprechen. Wir garantieren die besenreine Übergabe termingerecht für Hausverwaltung oder Eigentümer.",
        "calc_default": "Wohnungentrümpelung wien",
        "detail_content": """
        <p>Bei einer anstehenden <strong>Wohnungsraumung Wien</strong> unterstützen wir Sie von A bis Z. Unser erfahrenes Wiener Entrümpelungsteam kümmert sich um den kompletten Abbau, Transport und die umweltgerechte Mülltrennung.</p>
        <p>Egal ob Delogierungsräumung, Umzug ins Seniorenheim oder Verlassenschaft: Wir begegnen jedem Auftrag mit Respekt, Diskretion und höchster handwerklicher Effizienz.</p>
        """,
        "faqs": [
            ("Wie schnell bekommen wir einen Termin für die Wohnungsraumung Wien?",
             "Wir können meist am selben Tag besichtigen und den Auftrag innerhalb von 24 bis 48 Stunden abschließen."),
            ("Was tun, wenn die Wohnung sehr vollgestellt ist?",
             "Kein Problem. Unsere Teams sind auf vollgestellte Wohnungen und Härtefälle spezialisiert und verfügen über die notwendige Ausrüstung und Personalkapazität."),
            ("Bieten Sie Unterstützung bei der Schlüsselübergabe an?",
             "Ja, auf Wunsch können wir die besenreine Wohnung direkt an Ihren Vermieter oder die Hausverwaltung übergeben."),
            ("Was kostet eine Wohnungsraumung Wien im Schnitt?",
             "Die Kosten beginnen bei einfachen Räumungen schon bei wenigen Hundert Euro und sinken durch Wertanrechnung oft bis auf 0 €.")
        ]
    },
    {
        "file": "keller-entruempelung.html",
        "kw": "Keller Entrümpelung",
        "badge": "Keller Entrümpelung Wien • Schnell Platz schaffen",
        "h1": "Keller Entrümpelung",
        "title": "Keller Entrümpelung Wien | Wiener Dienst – Schnell & Günstig",
        "meta_desc": "Keller Entrümpelung Wien zum Festpreis. Wir räumen feuchte Keller, enge Holzabteile & Brandschutzhindernisse besenrein. ☎ 0660 606 0775",
        "category": "Keller & Dachboden",
        "hero_lead": "Befreien Sie Ihr Kellerabteil! Unsere Keller Entrümpelung in Wien schafft schnell wieder Ordnung – auch in feuchten, engen oder verwinkelten Kellern.",
        "calc_default": "Keller Entrümpelung",
        "detail_content": """
        <p>Über die Jahre sammeln sich im Keller Kartons, alte Elektrogeräte, Reifen und Sperrmüll an. Eine professionelle <strong>Keller Entrümpelung</strong> in Wien stellt sicher, dass Fluchtwege frei bleiben und Sie Ihren Stauraum wieder optimal nutzen können.</p>
        <p>Wir räumen Kellerabteile jeder Größe in Zinshäusern, Genossenschaftsbauten und Einfamilienhäusern. Auch Schimmelbefall, Feuchtigkeit oder schwere Einlagerungen stellen für unsere geschützten Mitarbeiter kein Hindernis dar.</p>
        """,
        "faqs": [
            ("Wie läuft eine Keller Entrümpelung in Wien ab?",
             "Sie zeigen uns Ihr Kellerabteil, wir nennen Ihnen den Fixpreis und tragen anschließend sämtliches Gerümpel über die Kellertreppe nach oben zum LKW."),
            ("Entrümpeln Sie auch feuchte oder verschimmelte Keller?",
             "Ja, mit entsprechender Schutzkleidung und professionellen Arbeitsmitteln räumen wir auch feuchte Kellerabteile sicher und vorschriftsmäßig."),
            ("Muss ich die Gegenstände im Keller vorsortieren?",
             "Nein, Sie müssen nur anzeigen, was entsorgt werden soll und was Sie behalten möchten. Den Rest erledigen wir."),
            ("Was kostet eine Kellerräumung in Wien?",
             "Kleine Kellerabteile räumen wir oft schon ab 140 € bis 250 € pauschal inklusive aller Entsorgungsgebühren.")
        ]
    },
    {
        "file": "keller-raeumung.html",
        "kw": "Keller Räumung",
        "badge": "Zuverlässige Keller Räumung Wien • Besenrein ab 140 €",
        "h1": "Keller Räumung",
        "title": "Keller Räumung Wien | Wiener Dienst – Fixpreis & Besenrein",
        "meta_desc": "Professionelle Keller Räumung in ganz Wien. Schnelle Räumung von Kellerabteilen, Schutzräumen & Gewölben. 0 € Besichtigung! ☎ 0660 606 0775",
        "category": "Keller & Dachboden",
        "hero_lead": "Effiziente Keller Räumung in allen 23 Wiener Bezirken. Wir räumen Altbaukeller, Gewölbe und moderne Kellerboxen besenrein zum verbindlichen Pauschalpreis.",
        "calc_default": "Keller Entrümpelung",
        "detail_content": """
        <p>Mit unserer <strong>Keller Räumung</strong> schaffen Sie im Handumdrehen neuen Platz. In vielen Wiener Altbauten sind Kellerzugänge steil und dunkel – überlassen Sie das mühsame Schleppen von schweren Kisten und Regalen unseren geübten Fachkräften.</p>
        <p>Wir fegen den Keller nach getaner Arbeit gründlich aus und entsorgen alle Altstoffe ordnungsgemäß bei den Sammelzentren der MA 48.</p>
        """,
        "faqs": [
            ("Räumen Sie auch größere Gewölbekeller in Wiener Zinshäusern?",
             "Ja, wir sind für Keller jeder Größenordnung ausgerüstet – vom kleinen 3 m² Holzverschlag bis zum 300 m² Zinshaus-Gewölbekeller."),
            ("Wie schnell ist ein Kellerabteil geräumt?",
             "Ein herkömmliches Kellerabteil ist meist innerhalb von 1 bis 3 Stunden komplett ausgeräumt und besenrein übergeben."),
            ("Können Sie alte Regale und Einbauten im Keller demontieren?",
             "Ja, wir zerlegen Holz- und Metallregale, Werkbänke oder Zwischenwände fachgerecht vor Ort."),
            ("Wie erfolgt die Abrechnung der Keller Räumung?",
             "Nach Besichtigung oder Fotoübermittlung per WhatsApp erhalten Sie einen garantierten Fixpreis inklusive Anfahrt und Entsorgung.")
        ]
    },
    {
        "file": "verlassenschaften-wien.html",
        "kw": "Verlassenschaften Wien",
        "badge": "Verlassenschaften Wien mit Wertanrechnung • Seriös & Diskret",
        "h1": "Verlassenschaften Wien",
        "title": "Verlassenschaften Wien | Wiener Dienst – Räumung & Ankauf",
        "meta_desc": "Diskrete Abwicklung von Verlassenschaften Wien. Räumung, Ankauf & hohe Wertanrechnung für Antiquitäten, Möbel, Kunst. ☎ 0660 606 0775",
        "category": "Verlassenschaft & Nachlass",
        "hero_lead": "Einfühlsame und professionelle Betreuung bei Verlassenschaften Wien. Wir bieten faire Wertermittlung, Gegenverrechnung und besenreine Räumung aus einer Hand.",
        "calc_default": "Verlassenschaften Wien",
        "detail_content": """
        <p>Der Verlust eines Angehörigen ist eine schwierige Lebensphase. Bei der Abwicklung von <strong>Verlassenschaften Wien</strong> stehen wir Ihnen mit Taktgefühl, Fachwissen und absoluter Verlässlichkeit zur Seite.</p>
        <p>Wir sichten den gesamten Nachlass gemeinsam mit Ihnen, schätzen Antiquitäten, Gemälde, Silber, Porzellan, Schmuck, Uhren und hochwertige Designmöbel realistisch ein und rechnen diese Werte transparent gegen die Räumungskosten an.</p>
        """,
        "faqs": [
            ("Wie funktioniert die Wertanrechnung bei Verlassenschaften Wien?",
             "Unser Sachverständiger begutachtet den Nachlass vor Ort. Verwertbare Gegenstände werden mit marktüblichen Preisen bewertet und direkt von den Räumungskosten abgezogen."),
            ("Können Verlassenschaften in Wien auch kostenlos geräumt werden?",
             "Ja! Wenn der Wert der vorhandenen Antiquitäten, Sammlerstücke und Möbel die eigentlichen Entrümpelungskosten übersteigt, ist eine Gratisräumung oder sogar eine Barauszahlung an Sie möglich."),
            ("Wie gehen Sie mit persönlichen Dokumenten und Erinnerungsstücken um?",
             "Wir arbeiten mit äußerster Sorgfalt und Diskretion. Gefundene Fotos, Briefe, Sparbücher oder Urkunden werden stets gesammelt und Ihnen persönlich überreicht."),
            ("Übernehmen Sie auch die Koordination mit Notaren oder Verlassenschaftsverwaltern?",
             "Ja, wir arbeiten regelmäßig mit Wiener Notariaten und Nachlasskuratoren zusammen und erstellen transparente Abrechnungen für das Verlassenschaftsverfahren.")
        ]
    },
    {
        "file": "hausraeumung-wien.html",
        "kw": "Hausräumung Wien",
        "badge": "Komplette Hausräumung Wien • Vom Keller bis zum Dach",
        "h1": "Hausräumung Wien",
        "title": "Hausräumung Wien | Wiener Dienst – Besenrein zum Fixpreis",
        "meta_desc": "Komplette Hausräumung Wien & NÖ zum garantierten Fixpreis. Einfamilienhäuser, Villen, Gärten & Garagen. Gratis Besichtigung! ☎ 0660 606 0775",
        "category": "Haus & Großobjekt",
        "hero_lead": "Ganzheitliche Hausräumung Wien vom Fachbetrieb. Wir räumen Häuser, Dachböden, Schuppen und Garagen besenrein vor Verkauf oder Sanierung.",
        "calc_default": "Hausräumung Wien",
        "detail_content": """
        <p>Eine <strong>Hausräumung Wien</strong> erfordert exakte Planung und schlagkräftige Teams. Oft müssen mehrere Etagen, Dachboden, Keller, Gartenhütte und Doppelgarage gleichzeitig beräumt werden.</p>
        <p>Wiener Dienst stellt die passenden LKW-Kapazitäten bereit, demontiert alte Einbauten und kümmert sich um die ordnungsgemäße Sortierung und Entsorgung aller Materialfraktionen.</p>
        """,
        "faqs": [
            ("Wie lange dauert eine komplette Hausräumung in Wien?",
             "Je nach Größe des Hauses und Füllgrad benötigen wir für ein durchschnittliches Einfamilienhaus in der Regel 1 bis maximal 3 Werktage."),
            ("Räumen Sie auch Nebengebäude, Garagen und den Garten?",
             "Ja, wir beräumen das gesamte Anwesen inklusive Schuppen, Gartenlauben, Garagen, Werkstätten und Außenbereichen."),
            ("Können alte Holzöfen oder Ölradiatoren entsorgt werden?",
             "Ja, wir demontieren und entsorgen auch alte Heizkörper, Öfen und feste Einbauten fachgerecht nach Umweltstandards."),
            ("Gibt es ein kostenloses Angebot vor Ort?",
             "Ja, bei einer Hausräumung ist eine Vor-Ort-Besichtigung unerlässlich und bei uns immer zu 100% kostenlos und unverbindlich.")
        ]
    },
    {
        "file": "haus-entruempelung-wien.html",
        "kw": "Haus Entrümpelung Wien",
        "badge": "Haus Entrümpelung Wien & Umland • Besenrein garantiert",
        "h1": "Haus Entrümpelung Wien",
        "title": "Haus Entrümpelung Wien | Wiener Dienst – Festpreis-Garantie",
        "meta_desc": "Zuverlässige Haus Entrümpelung Wien. Gründliche Räumung vom Keller bis zum Dachboden zum fairen Festpreis. Jetzt anfragen: ☎ 0660 606 0775",
        "category": "Haus & Großobjekt",
        "hero_lead": "Professionelle Haus Entrümpelung Wien mit Handschlagqualität. Wir machen Ihr Haus schnell wieder bezugs- oder verkaufsbereit.",
        "calc_default": "Hausräumung Wien",
        "detail_content": """
        <p>Bei der <strong>Haus Entrümpelung Wien</strong> fallen häufig große Mengen gemischter Abfälle an: alte Möbel, Elektrogeräte, Baureste und Gartenabfälle. Wir trennen alles penibel und halten so die Entsorgungskosten für Sie minimal.</p>
        <p>Nutzen Sie unseren bequemen Rundum-Service: Besichtigung, Wertausgleich, Demontage und besenreine Übergabe aus einer Hand.</p>
        """,
        "faqs": [
            ("Was kostet eine Haus Entrümpelung in Wien?",
             "Die Gesamtkosten hängen von der Kubikmeterzahl und den Einbauten ab. Wir erstellen nach der Gratis-Besichtigung einen verbindlichen Festpreis."),
            ("Können Sie auch Teppiche und Deckenvertäfelungen entfernen?",
             "Ja, wir bieten auch leichte Abbrucharbeiten und das Entfernen von Paneelen, Teppichen und Einbauten an."),
            ("Was passiert mit wertvollem Inventar im Haus?",
             "Wir prüfen Antiquitäten, Werkzeuge oder Maschinen auf ihren Wiederverkaufswert und verrechnen diesen direkt mit dem Räumungspreis."),
            ("Sind Sie auch im Wiener Umland (z.B. Klosterneuburg, Mödling) tätig?",
             "Ja, wir sind in allen Wiener Bezirken sowie im gesamten Umland von Niederösterreich ohne Anfahrtsaufschlag im Einsatz.")
        ]
    },
    {
        "file": "gemeinde-wohnung-entruempelung.html",
        "kw": "Gemeinde Wohnung Entrümpelung",
        "badge": "Wiener Wohnen Spezialist • 100% Abnahmegarantie",
        "h1": "Gemeinde Wohnung Entrümpelung",
        "title": "Gemeinde Wohnung Entrümpelung | Wiener Wohnen Übergabe",
        "meta_desc": "Gemeinde Wohnung Entrümpelung nach strengen Wiener Wohnen Richtlinien. Fliesen, Teppich, Küchen-Rückbau & besenrein. ☎ 0660 606 0775",
        "category": "Wiener Wohnen",
        "hero_lead": "Experte für die Gemeinde Wohnung Entrümpelung in Wien. Wir kennen alle Vorgaben von Wiener Wohnen und garantieren eine mängelfreie Schlüsselübergabe.",
        "calc_default": "Gemeinde Wohnung Entrümpelung",
        "detail_content": """
        <p>Die Rückgabe einer Gemeindewohnung an Wiener Wohnen ist an strenge Auflagen gebunden. Eine <strong>Gemeinde Wohnung Entrümpelung</strong> umfasst meist nicht nur das Ausräumen der Möbel, sondern den kompletten Rückbau von Einbauten.</p>
        <p>Wir entfernen nicht genehmigte Raumteiler, Holzdecken, verklebte Böden, Tapeten und Einbauküchen vorschriftsmäßig, sodass Sie bei der Endbegehung keine Beanstandungen befürchten müssen.</p>
        """,
        "faqs": [
            ("Welche Vorgaben von Wiener Wohnen müssen beachtet werden?",
             "Wiener Wohnen verlangt in der Regel die vollständige Beseitigung aller privaten Einbauten, Laminatböden, Wandpaneele und Tapeten sowie eine besenreine Übergabe inklusive Kellerabteil."),
            ("Garantieren Sie die Abnahme durch Wiener Wohnen?",
             "Ja, wir haben jahrelange Erfahrung mit Wiener Wohnen Wohnungsübergaben und garantieren die Einhaltung sämtlicher Rückbau-Richtlinien."),
            ("Was geschieht mit der alten Küche in der Gemeindewohnung?",
             "Wir demontieren die Küchenelemente, verschließen die Wasseranschlüsse fachgerecht und entsorgen alle Altteile."),
            ("Wie schnell kann eine Gemeindewohnung übergeben werden?",
             "Normalerweise benötigen wir für die komplette Entrümpelung und den Rückbau einer Gemeindewohnung nur 1 bis 2 Werktage.")
        ]
    },
    {
        "file": "dachbodenentruempelung.html",
        "kw": "Dachbodenentrümpelung",
        "badge": "Dachbodenentrümpelung Wien • Brandschutz & Platzgewinn",
        "h1": "Dachbodenentrümpelung",
        "title": "Dachbodenentrümpelung Wien | Wiener Dienst – Schnell & Sicher",
        "meta_desc": "Dachbodenentrümpelung Wien zum Festpreis. Wir räumen historische Dachböden, Taubenkot & Sperrmüll brandschutzgerecht. ☎ 0660 606 0775",
        "category": "Keller & Dachboden",
        "hero_lead": "Professionelle Dachbodenentrümpelung in Wien. Wir beräumen Dachböden sicher, zügig und vorschriftsgemäß nach Brandschutzauflagen.",
        "calc_default": "Dachbodenentrümpelung",
        "detail_content": """
        <p>Wiener Zinshaus-Dachböden sind oft verwinkelt, staubig und schwer zugänglich. Unsere <strong>Dachbodenentrümpelung</strong> sorgt für saubere, brandschutzsichere Dachgeschosse vor einem Ausbau oder der behördlichen Überprüfung.</p>
        <p>Wir tragen alte Kisten, Möbel, Bretter und Gerümpel sicher durch die Dachluken und Stiegenhäuser nach unten und hinterlassen den Dachboden gründlich gekehrt.</p>
        """,
        "faqs": [
            ("Räumen Sie auch Dachböden ohne Lift in den oberen Stockwerken?",
             "Ja, unsere kräftigen Mitarbeiter sind auf Altbauten ohne Aufzug spezialisiert und transportieren alle Gegenstände sicher nach unten."),
            ("Entfernen Sie auch Taubenkot oder stark verschmutzte Bereiche?",
             "Ja, wir führen auch Entrümpelungen bei starker Verschmutzung durch Tauben unter Einhaltung strenger Hygiene- und Arbeitsschutzmaßnahmen durch."),
            ("Was kostet eine Dachbodenentrümpelung in Wien?",
             "Die Kosten beginnen je nach Menge und Zugänglichkeit bei etwa 190 € und werden vorab transparent festgelegt."),
            ("Muss der Brandschutzbeauftragte der Hausverwaltung informiert werden?",
             "Wir räumen so, dass die Fluchtwege und Brandschutzbestimmungen der Stadt Wien zu 100% erfüllt werden.")
        ]
    },
    {
        "file": "gemeinde-wohnungsraeumung.html",
        "kw": "Gemeinde wohnungsräumung",
        "badge": "Gemeinde wohnungsräumung Wien • Wiener Wohnen konform",
        "h1": "Gemeinde wohnungsräumung",
        "title": "Gemeinde wohnungsräumung Wien | Wiener Dienst – Fixpreis",
        "meta_desc": "Ihre Gemeinde wohnungsräumung in Wien mit besenreiner Übergabegarantie. Rückbau nach Richtlinien von Wiener Wohnen. ☎ 0660 606 0775",
        "category": "Wiener Wohnen",
        "hero_lead": "Reibungslose Gemeinde wohnungsräumung in ganz Wien. Wir sorgen für die fristgerechte und beanstandungsfreie Rückgabe an Wiener Wohnen.",
        "calc_default": "Gemeinde Wohnung Entrümpelung",
        "detail_content": """
        <p>Bei einer <strong>Gemeinde wohnungsräumung</strong> in Wien sind genaue Fristen einzuhalten. Unser Service umfasst das vollständige Ausräumen der Wohnbereiche sowie des zugehörigen Kellerabteils.</p>
        <p>Wir demontieren Deckenleuchten, Gardinenstangen, Spiegelschränke und Bodenbeläge nach den Vorgaben der Wohnungsinspektoren von Wiener Wohnen.</p>
        """,
        "faqs": [
            ("Müssen Tapeten bei der Gemeinde wohnungsräumung abgezogen werden?",
             "Wenn Wiener Wohnen den Rückbau in den Ursprungszustand verlangt, entfernen wir alle Tapetenschichten fachgerecht."),
            ("Werden Bohrlöcher verspachtelt?",
             "Ja, auf Wunsch verschließen und verspachteln wir alle Dübellöcher in Wänden und Decken."),
            ("Wie läuft die Terminabstimmung mit Wiener Wohnen?",
             "Wir richten uns exakt nach Ihrem offiziellen Rückgabetermin, sodass Sie die Wohnung pünktlich übergeben können."),
            ("Was kostet die Gemeinde wohnungsräumung?",
             "Durch Wertanrechnung von gepflegtem Hausrat können wir viele Gemeindewohnungen extrem preiswert oder sogar kostenlos räumen.")
        ]
    },
    {
        "file": "verlassenschaftsraeumung.html",
        "kw": "Verlassenschaftsräumung",
        "badge": "Verlassenschaftsräumung Wien • Mit Sachwert-Ankauf",
        "h1": "Verlassenschaftsräumung",
        "title": "Verlassenschaftsräumung Wien | Wiener Dienst – Seriös & Fair",
        "meta_desc": "Seriöse Verlassenschaftsräumung Wien mit fairer Wertanrechnung. Kostenlose Schätzung vor Ort für Antiquitäten & Nachlässe. ☎ 0660 606 0775",
        "category": "Verlassenschaft & Nachlass",
        "hero_lead": "Einfühlsame und diskrete Verlassenschaftsräumung in Wien. Wir bewerten Antiquitäten und Nachlässe fair und rechnen diese direkt an.",
        "calc_default": "Verlassenschaften Wien",
        "detail_content": """
        <p>Eine <strong>Verlassenschaftsräumung</strong> verlangt Feingefühl und geschultes Auge. Häufig befinden sich unter altem Hausrat wertvolle Sammlerstücke, historische Gemälde, Goldschmuck oder echtes Silberbesteck.</p>
        <p>Unsere Experten prüfen jeden Nachlass vor Ort. Durch unsere direkte Wertanrechnung sparen Sie bares Geld bei der Räumung.</p>
        """,
        "faqs": [
            ("Welche Gegenstände können bei der Verlassenschaftsräumung angerechnet werden?",
             "Antiquitäten, Altwaren, Uhren, Münzen, Schmuck, Bronzefiguren, Designklassiker der 50er bis 70er Jahre, Gemälde und Musikinstrumente."),
            ("Wie schnell kann eine Verlassenschaftsräumung durchgeführt werden?",
             "Meist innerhalb von wenigen Tagen nach der Besichtigung räumen wir die gesamte Liegenschaft besenrein aus."),
            ("Arbeiten Sie auch mit Notaren und Erbgemeinschaften zusammen?",
             "Ja, wir erstellen transparente Angebote und Rechnungen zur Vorlage bei Erben, Gerichten und Nachlassverwaltern."),
            ("Ist die Erstbesichtigung der Verlassenschaft kostenfrei?",
             "Ja, unsere Begutachtung und Beratung vor Ort ist in ganz Wien und Niederösterreich zu 100% kostenlos.")
        ]
    },
    {
        "file": "verlassenschafts-entruempelung.html",
        "kw": "Verlassenschafts Entrümpelung",
        "badge": "Diskrete Verlassenschafts Entrümpelung Wien • Fixpreis",
        "h1": "Verlassenschafts Entrümpelung",
        "title": "Verlassenschafts Entrümpelung Wien | Wiener Dienst",
        "meta_desc": "Kompetente Verlassenschafts Entrümpelung in Wien. Wertanrechnung, diskrete Räumung & besenreine Übergabe zum Fixpreis. ☎ 0660 606 0775",
        "category": "Verlassenschaft & Nachlass",
        "hero_lead": "Ihre verlässliche Verlassenschafts Entrümpelung in Wien. Wir entlasten Angehörige umfassend und sorgen für transparente Abwicklung.",
        "calc_default": "Verlassenschaften Wien",
        "detail_content": """
        <p>Bei der <strong>Verlassenschafts Entrümpelung</strong> in Wien übernehmen wir die komplette Entrümpelung aller Räume, Nebenräume und Garagen. Wir sortieren Unbrauchbares aus und bewahren Wertvolles.</p>
        <p>Verlassen Sie sich auf unsere Wiener Handschlagqualität und die termingerechte Übergabe der Immobilie an den Vermieter oder Käufer.</p>
        """,
        "faqs": [
            ("Muss die Verlassenschafts Entrümpelung sofort bezahlt werden?",
             "Nein, die Bezahlung erfolgt erst nach vollständiger und besenreiner Erledigung der Arbeiten."),
            ("Können Sie auch Teilleistungen bei Verlassenschaften erbringen?",
             "Ja, wir können auch nur Teilbereiche wie Keller, Dachboden oder einzelne Zimmer entrümpeln."),
            ("Was passiert mit nicht verwertbarem Hausrat?",
             "Dieser wird vorschriftsgemäß getrennt und den offiziellen Abfallwirtschaftszentren der Stadt Wien zugeführt."),
            ("Bieten Sie einen Ankauf von ganzen Sammlungen an?",
             "Ja, wir kaufen auch ganze Sammlungen, Nachlässe und Antiquitätenbestände gegen Barzahlung oder Verrechnung an.")
        ]
    },
    {
        "file": "nachlassraeumung.html",
        "kw": "Nachlassräumung",
        "badge": "Nachlassräumung Wien • Würdevoll, Diskret & Fachgerecht",
        "h1": "Nachlassräumung",
        "title": "Nachlassräumung Wien | Wiener Dienst – Mit Wertausgleich",
        "meta_desc": "Würdevolle Nachlassräumung in Wien mit Wertausgleich. Seriöse Schätzung, besenreine Räumung & Fixpreis-Garantie. ☎ 0660 606 0775",
        "category": "Verlassenschaft & Nachlass",
        "hero_lead": "Pietätvolle und professionelle Nachlassräumung in Wien. Wir unterstützen Sie in schweren Zeiten mit verlässlicher Wertanrechnung und besenreiner Übergabe.",
        "calc_default": "Verlassenschaften Wien",
        "detail_content": """
        <p>Eine <strong>Nachlassräumung</strong> erfordert Fingerspitzengefühl und Professionalität. Wir helfen Erben und Nachlassverwaltern bei der zügigen und wirtschaftlichen Abwicklung von Wohnungs- und Hausnachlässen.</p>
        <p>Unser Sachverständiger schätzt alle werthaltigen Gegenstände transparent ein, sodass Sie maximale Kostenvorteile genießen.</p>
        """,
        "faqs": [
            ("Wie läuft die Nachlassräumung bei mehreren Erben ab?",
             "Wir erstellen ein klares, aufgeschlüsseltes Angebot mit Wertanrechnungspositionen, das für alle Erben transparent und nachvollziehbar ist."),
            ("Können bestimmte Möbelstücke an andere Adressen geliefert werden?",
             "Ja, wir können Erinnerungsstücke gerne innerhalb von Wien oder nach Niederösterreich an Ihre Wunschadresse transportieren."),
            ("Was kostet eine durchschnittliche Nachlassräumung?",
             "Häufig decken die vorhandenen Werte einen Großteil der Kosten ab, sodass die Nachlassräumung oft sehr günstig oder kostenlos ausfällt."),
            ("Wer haftet bei Schäden im Stiegenhaus?",
             "Unsere Betriebshaftpflichtversicherung deckt sämtliche Transportschäden lückenlos ab.")
        ]
    },
    {
        "file": "nachlass-entruempelung.html",
        "kw": "Nachlass Entrümpelung",
        "badge": "Nachlass Entrümpelung Wien • Schnell & Besenrein",
        "h1": "Nachlass Entrümpelung",
        "title": "Nachlass Entrümpelung Wien | Wiener Dienst – Fixpreis",
        "meta_desc": "Diskrete Nachlass Entrümpelung in Wien. Schnelle Räumung von Nachlässen zum Festpreis mit Wertanrechnung. Gratis Angebot! ☎ 0660 606 0775",
        "category": "Verlassenschaft & Nachlass",
        "hero_lead": "Fachgerechte Nachlass Entrümpelung in ganz Wien. Wir sorgen für die schnelle, besenreine Beräumung von Nachlassimmobilien.",
        "calc_default": "Verlassenschaften Wien",
        "detail_content": """
        <p>Oft muss nach einem Erbfall die Wohnung schnell geräumt werden, um laufende Mietkosten zu stoppen. Unsere <strong>Nachlass Entrümpelung</strong> in Wien garantiert Ihnen kurzfristige Termine und fixe Pauschalpreise.</p>
        <p>Wir arbeiten diskret mit neutralen Fahrzeugen und übergeben die Räumlichkeiten pünktlich im geforderten Zustand.</p>
        """,
        "faqs": [
            ("Wie schnell können Sie mit der Nachlass Entrümpelung beginnen?",
             "Im Eilfall können wir innerhalb von 24 Stunden nach der Erstbesichtigung mit den Arbeiten starten."),
            ("Müssen persönliche Unterlagen vorher aussortiert werden?",
             "Es ist von Vorteil, wenn Sie persönliche Papiere vorab sichten; sollte während der Arbeit Wichtiges gefunden werden, händigen wir es Ihnen sofort aus."),
            ("Können Sie auch Tresore oder Waffenschränke aus Nachlässen entsorgen?",
             "Ja, wir demontieren und transportieren auch schwerste Sicherheitsschränke gesetzeskonform ab."),
            ("Erhalte ich eine ordnungsgemäße Rechnung für das Finanzamt?",
             "Selbstverständlich erhalten Sie eine detaillierte Firmenrechnung, die Sie bei der Erbschaftssteuer oder dem Nachlassgericht einreichen können.")
        ]
    },
    {
        "file": "messie-raeumung.html",
        "kw": "Messie Räumung",
        "badge": "100% Diskrete Messie Räumung Wien • Ohne Vorurteile",
        "h1": "Messie Räumung",
        "title": "Messie Räumung Wien | Wiener Dienst – Diskret & Gründlich",
        "meta_desc": "100% diskrete Messie Räumung Wien ohne Vorurteile. Professionelle Entrümpelung, Geruchsneutralisation & besenrein. ☎ 0660 606 0775",
        "category": "Spezialräumung",
        "hero_lead": "Diskrete, respektvolle Messie Räumung in Wien. Wir helfen schnell und unvoreingenommen bei extrem vollen oder vernachlässigten Wohnungen.",
        "calc_default": "Messie Entrümpelung",
        "detail_content": """
        <p>Eine <strong>Messie Räumung</strong> erfordert enormes Einfühlungsvermögen, Diskretion und spezielle Arbeitsschutzmaßnahmen. Wiener Dienst nähert sich jeder Situation ohne Wertung und mit vollem Respekt gegenüber den Betroffenen.</p>
        <p>Wir arbeiten zügig mit neutralen Fahrzeugen, desinfizieren bei Bedarf, entsorgen verdorbene Materialien und führen eine gründliche Grundreinigung durch, um die Wohnung wieder bewohnbar zu machen.</p>
        """,
        "faqs": [
            ("Wie diskret erfolgt die Messie Räumung in Wien?",
             "Unsere Mitarbeiter treten neutral auf, unsere Fahrzeuge sind unauffällig und wir wahren zu 100% die Privatsphäre gegenüber Nachbarn und Dritten."),
            ("Führen Sie auch Desinfektionen und Geruchsneutralisation durch?",
             "Ja, wir führen auf Wunsch eine professionelle Ozonbehandlung und Desinfektion durch, um Gerüche und Keime nachhaltig zu beseitigen."),
            ("Können Angehörige den Auftrag erteilen?",
             "Ja, wir arbeiten eng mit Angehörigen, Sachwaltern und Betreuern zusammen, um die bestmögliche Lösung zu finden."),
            ("Was kostet eine Messie Räumung in Wien?",
             "Aufgrund der individuellen Situation vereinbaren wir nach diskreter Vorabbesichtigung einen fairen und verbindlichen Pauschalpreis.")
        ]
    },
    {
        "file": "messie-entruempelung.html",
        "kw": "Messie Entrümpelung",
        "badge": "Professionelle Messie Entrümpelung Wien • Schnelle Hilfe",
        "h1": "Messie Entrümpelung",
        "title": "Messie Entrümpelung Wien | Wiener Dienst – Respektvoll & Diskret",
        "meta_desc": "Verständnisvolle Messie Entrümpelung Wien. Gründliche Räumung von Härtefällen zum fairen Festpreis. Kostenlose Erstberatung! ☎ 0660 606 0775",
        "category": "Spezialräumung",
        "hero_lead": "Zuverlässige Messie Entrümpelung in allen 23 Wiener Bezirken. Wir schaffen wieder Licht, Luft und Ordnung – schnell, diskret und professionell.",
        "calc_default": "Messie Entrümpelung",
        "detail_content": """
        <p>Wenn Wohnungen über Jahre hinweg überfüllt wurden, ist eine professionelle <strong>Messie Entrümpelung</strong> der einzige Ausweg. Wir räumen selbst extremste Anhäufungen von Müll, Unrat und Zeitungen schnell und sicher aus.</p>
        <p>Unser geschultes Team verfügt über Schutzbekleidung, modernste Werkzeuge und die nötige Logistik, um auch große Mengen innerhalb kürzester Zeit abzutransportieren.</p>
        """,
        "faqs": [
            ("Wie lange dauert eine Messie Entrümpelung?",
             "Dank starker Teams schaffen wir selbst stark betroffene Wohnungen meist innerhalb von 1 bis maximal 2 Tagen."),
            ("Können wichtige Dokumente gerettet werden?",
             "Ja, wir suchen auf Wunsch gezielt nach Ausweisen, Verträgen, Ersparnissen oder Schlüsseln und trennen diese sorgfältig ab."),
            ("Entfernen Sie auch stark verschmutzte Böden und Teppiche?",
             "Ja, wir entfernen kontaminierte Teppichböden, PVC-Beläge und Tapeten restlos und entsorgen diese fachgerecht."),
            ("Gibt es ein kostenloses Erstgespräch?",
             "Ja, wir beraten Sie absolut diskret und unverbindlich vor Ort oder telefonisch.")
        ]
    }
]

ALL_22_LIST = [k["kw"] for k in KEYWORDS]

def generate_header(active_file="index.html"):
    """Generates the pixel-perfect header according to master prompt rules."""
    # Build desktop nav links
    nav_links = f"""
        <a href="index.html" class="px-3 py-2 rounded-lg {'text-wienRed-600 bg-wienRed-50 font-bold' if active_file == 'index.html' else 'hover:bg-slate-100 hover:text-wienRed-600'} transition whitespace-nowrap">Startseite</a>
        <a href="index.html#preisrechner" class="px-3 py-2 rounded-lg hover:bg-slate-100 hover:text-wienRed-600 transition inline-flex items-center gap-1.5 whitespace-nowrap">
            <i class="fa-solid fa-calculator text-wienRed-600 text-xs"></i>
            <span>Preisrechner</span>
        </a>
        <a href="index.html#leistungen" class="px-3 py-2 rounded-lg hover:bg-slate-100 hover:text-wienRed-600 transition whitespace-nowrap">Leistungen</a>
        <a href="index.html#keyword-index" class="px-3 py-2 rounded-lg hover:bg-slate-100 hover:text-wienRed-600 transition whitespace-nowrap">22 Spezial-Seiten</a>
        <a href="index.html#faq" class="px-3 py-2 rounded-lg hover:bg-slate-100 hover:text-wienRed-600 transition whitespace-nowrap">FAQ</a>
        <a href="kontakt.html" class="px-4 py-2 rounded-xl {'bg-wienRed-600 text-white font-bold shadow-md shadow-wienRed-600/20' if active_file == 'kontakt.html' else 'bg-slate-100 hover:bg-wienRed-600 hover:text-white text-navy-900 font-bold'} transition inline-flex items-center gap-1.5 whitespace-nowrap">
            <i class="fa-regular fa-address-card"></i>
            <span>Kontakt</span>
        </a>
    """
    
    return f"""
    <!-- TOP URGENCY / TRUST BAR (SINGLE LINE) -->
    <div class="bg-navy-950 text-white text-xs py-2 px-4 border-b border-slate-800/80">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4 overflow-x-auto no-scrollbar whitespace-nowrap">
            <div class="flex items-center gap-5 shrink-0">
                <span class="inline-flex items-center text-emerald-400 font-semibold">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping mr-2"></span>
                    Heute noch freie Besichtigungstermine in allen 23 Wiener Bezirken!
                </span>
                <span class="hidden md:inline-flex items-center text-slate-300 font-medium">
                    <i class="fa-solid fa-shield-halved text-wienRed-500 mr-1.5"></i> Handschlagqualität &amp; 100% Fixpreis-Garantie
                </span>
            </div>
            <div class="flex items-center gap-4 ml-auto shrink-0">
                <a href="mailto:{EMAIL}" onclick="trackConversion('email_click')" class="hover:text-wienRed-400 transition inline-flex items-center gap-1.5 text-slate-200 font-medium">
                    <i class="fa-solid fa-envelope text-wienRed-500"></i>
                    <span>{EMAIL}</span>
                </a>
                <span class="text-slate-700">|</span>
                <a href="tel:{PHONE_TEL}" onclick="trackConversion('phone_click')" class="font-bold text-amber-400 hover:text-amber-300 transition inline-flex items-center gap-1.5">
                    <i class="fa-solid fa-phone-volume"></i>
                    <span>{PHONE_DISPLAY}</span>
                </a>
            </div>
        </div>
    </div>

    <!-- STICKY HEADER / NAVIGATION (STRICT SINGLE-LINE UI/UX) -->
    <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md shadow-sm border-b border-slate-200/90">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between gap-3 xl:gap-6">
            
            <!-- Brand Logo (Guaranteed Single-Line Subtitle & Vienna Shield SVG) -->
            <a href="index.html" class="flex items-center gap-3 group shrink-0">
                {VIENNA_SHIELD_SVG}
                <div class="flex flex-col justify-center shrink-0">
                    <div class="flex items-center gap-1 leading-none">
                        <span class="text-lg sm:text-2xl font-black tracking-tight text-navy-900 whitespace-nowrap">WIENER</span>
                        <span class="text-lg sm:text-2xl font-black tracking-tight text-wienRed-600 whitespace-nowrap">DIENST</span>
                    </div>
                    <span class="text-[10px] sm:text-[11px] font-bold uppercase tracking-wider text-slate-500 whitespace-nowrap leading-none mt-1.5">
                        ENTRÜMPELUNG &amp; RÄUMUNGSFIRMA WIEN
                    </span>
                </div>
            </a>

            <!-- Desktop Navigation Links (Strictly 1 Row, Never Wraps) -->
            <nav class="hidden lg:flex items-center justify-center gap-1 xl:gap-1.5 text-[13px] xl:text-sm font-semibold text-slate-700 whitespace-nowrap shrink-0">
                {nav_links}
            </nav>

            <!-- Mobile Menu Toggle Button (No Header CTAs) -->
            <div class="flex items-center lg:hidden shrink-0">
                <button onclick="toggleMobileMenu()" class="w-11 h-11 flex items-center justify-center rounded-xl border border-slate-200 text-slate-700 hover:bg-slate-100 shrink-0" aria-label="Menü">
                    <i class="fa-solid fa-bars text-lg"></i>
                </button>
            </div>
        </div>

        <!-- Mobile Menu Dropdown -->
        <div id="mobile-menu" class="hidden lg:hidden bg-white border-t border-slate-200 px-4 pt-3 pb-5 space-y-2 shadow-xl">
            <a href="index.html" class="w-full text-left px-3 py-2.5 rounded-lg font-bold text-navy-900 hover:bg-slate-100 flex items-center justify-between">
                <span><i class="fa-solid fa-house text-wienRed-600 mr-2"></i> Startseite</span>
                <i class="fa-solid fa-chevron-right text-xs text-slate-400"></i>
            </a>
            <a href="index.html#preisrechner" class="block px-3 py-2.5 rounded-lg font-semibold text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-calculator text-wienRed-600 mr-2"></i> Interaktiver Preisrechner
            </a>
            <a href="index.html#leistungen" class="block px-3 py-2.5 rounded-lg font-semibold text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-broom text-wienRed-600 mr-2"></i> Leistungen Overview
            </a>
            <a href="index.html#keyword-index" class="block px-3 py-2.5 rounded-lg font-semibold text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-layer-group text-wienRed-600 mr-2"></i> Alle 22 Spezial-Seiten
            </a>
            <a href="kontakt.html" class="w-full text-left px-3 py-2.5 rounded-lg font-bold text-wienRed-600 bg-wienRed-50 hover:bg-wienRed-100 flex items-center justify-between">
                <span><i class="fa-solid fa-headset mr-2"></i> Kontakt-Seite öffnen</span>
                <i class="fa-solid fa-arrow-right text-xs"></i>
            </a>
        </div>
    </header>
    """

def generate_quick_switcher(active_file="index.html"):
    """Generates the 22 keywords quick switcher bar linking to real .html pages."""
    chips = []
    for item in KEYWORDS:
        is_active = (item["file"] == active_file)
        if is_active:
            chip = f'<a href="{item["file"]}" class="kw-chip shrink-0 px-2.5 py-1 rounded-md bg-wienRed-600 text-white font-bold transition shadow-sm">{item["kw"]}</a>'
        else:
            chip = f'<a href="{item["file"]}" class="kw-chip shrink-0 px-2.5 py-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-200 transition">{item["kw"]}</a>'
        chips.append(chip)
    
    chips_html = "\n".join(chips)
    return f"""
    <!-- ALL 22 KEYWORDS QUICK-SWITCHER BAR -->
    <div class="bg-slate-900 border-b border-slate-800 py-2.5 px-4">
        <div class="max-w-7xl mx-auto flex items-center gap-1.5 overflow-x-auto no-scrollbar text-xs whitespace-nowrap">
            <span class="text-amber-400 font-bold whitespace-nowrap flex items-center gap-1 shrink-0 mr-1">
                <i class="fa-solid fa-bolt"></i> 22 Spezial-Seiten Direktwahl:
            </span>
            {chips_html}
        </div>
    </div>
    """

def generate_floating_docks(current_kw="Entrümpelung Wien"):
    """Generates desktop sliding dock and mobile sticky dock."""
    wa_msg = f"Hallo Wiener Dienst! Ich bitte um ein unverbindliches Fixpreis-Angebot für: {current_kw}."
    wa_encoded = wa_msg.replace(" ", "%20")
    
    return f"""
    <!-- STICKY MOBILE CONVERSION BAR (3-BUTTON FIXED BOTTOM) -->
    <div class="fixed bottom-0 left-0 right-0 z-50 lg:hidden bg-navy-950/95 backdrop-blur-md border-t border-slate-800 px-3 py-2 pb-[calc(0.5rem+env(safe-area-inset-bottom,0px))] shadow-2xl">
        <div class="grid grid-cols-3 gap-2 max-w-md mx-auto">
            <a href="tel:{PHONE_TEL}" onclick="trackConversion('phone_click')" class="h-12 bg-wienRed-600 hover:bg-wienRed-700 text-white font-extrabold rounded-xl flex flex-col items-center justify-center shadow-md active:scale-95 transition">
                <i class="fa-solid fa-phone-volume text-sm mb-0.5 ring-icon"></i>
                <span class="text-[10px] uppercase font-bold tracking-wider leading-none">Anrufen</span>
            </a>
            <a href="https://wa.me/{PHONE_TEL.replace('+', '')}?text={wa_encoded}" target="_blank" rel="noopener" onclick="trackConversion('whatsapp_click')" class="h-12 bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold rounded-xl flex flex-col items-center justify-center shadow-md active:scale-95 transition">
                <i class="fa-brands fa-whatsapp text-base mb-0.5"></i>
                <span class="text-[10px] uppercase font-bold tracking-wider leading-none">WhatsApp</span>
            </a>
            <a href="kontakt.html" class="h-12 bg-amber-400 hover:bg-amber-300 text-navy-950 font-extrabold rounded-xl flex flex-col items-center justify-center shadow-md active:scale-95 transition">
                <i class="fa-solid fa-envelope text-sm mb-0.5"></i>
                <span class="text-[10px] uppercase font-bold tracking-wider leading-none">Kontakt</span>
            </a>
        </div>
    </div>

    <!-- STICKY DESKTOP FLOATING DOCK (RIGHT-SIDE SLIDING: translate-x-[162px] hover:translate-x-0 w-[215px] h-12) -->
    <div class="hidden lg:flex fixed top-1/2 -translate-y-1/2 right-0 z-50 flex-col gap-2.5 items-end">
        <!-- 1. Anrufen -->
        <a href="tel:{PHONE_TEL}" onclick="trackConversion('phone_click')"
           class="w-[215px] h-12 translate-x-[162px] hover:translate-x-0 transition-all duration-300 ease-out bg-wienRed-600 hover:bg-wienRed-700 text-white font-bold text-xs rounded-l-2xl shadow-xl flex items-center px-4 gap-3 shrink-0">
            <i class="fa-solid fa-phone text-base shrink-0 ring-icon"></i>
            <div class="whitespace-nowrap overflow-hidden">
                <span class="block text-[10px] text-red-100 font-semibold leading-none">Sofort Anrufen</span>
                <span class="text-xs font-black">{PHONE_DISPLAY}</span>
            </div>
        </a>
        <!-- 2. WhatsApp -->
        <a href="https://wa.me/{PHONE_TEL.replace('+', '')}?text={wa_encoded}" target="_blank" rel="noopener" onclick="trackConversion('whatsapp_click')"
           class="w-[215px] h-12 translate-x-[162px] hover:translate-x-0 transition-all duration-300 ease-out bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs rounded-l-2xl shadow-xl flex items-center px-4 gap-3 shrink-0">
            <i class="fa-brands fa-whatsapp text-lg shrink-0"></i>
            <div class="whitespace-nowrap overflow-hidden">
                <span class="block text-[10px] text-emerald-100 font-semibold leading-none">WhatsApp Chat</span>
                <span class="text-xs font-black">Fotos &amp; Preisanfrage</span>
            </div>
        </a>
        <!-- 3. E-Mail -->
        <a href="mailto:{EMAIL}" onclick="trackConversion('email_click')"
           class="w-[215px] h-12 translate-x-[162px] hover:translate-x-0 transition-all duration-300 ease-out bg-navy-950 hover:bg-slate-900 border-l border-y border-slate-700 text-white font-bold text-xs rounded-l-2xl shadow-xl flex items-center px-4 gap-3 shrink-0">
            <i class="fa-solid fa-envelope text-base text-amber-400 shrink-0"></i>
            <div class="whitespace-nowrap overflow-hidden">
                <span class="block text-[10px] text-slate-300 font-semibold leading-none">E-Mail senden</span>
                <span class="text-xs font-black">{EMAIL}</span>
            </div>
        </a>
    </div>
    """

def generate_calculator(current_kw="Entrümpelung Wien"):
    """Generates the interactive price calculator with the 3 badges."""
    return f"""
    <!-- INTERACTIVE PRICE & VOLUME CALCULATOR (3 CLEAN BADGES) -->
    <section id="preisrechner" class="py-14 bg-white border-b border-slate-200">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="bg-gradient-to-br from-slate-900 to-navy-950 text-white rounded-3xl p-6 sm:p-10 shadow-2xl border border-slate-800">
                <div class="text-center max-w-2xl mx-auto mb-8">
                    <span class="bg-amber-400 text-navy-950 text-xs font-black uppercase px-3.5 py-1 rounded-full shadow">
                        Interaktiver Schnell-Rechner Wien
                    </span>
                    <h2 class="text-2xl sm:text-3xl font-black mt-3">
                        In 3 Klicks zur Kosteneinschätzung für {current_kw}
                    </h2>
                    <p class="text-xs sm:text-sm text-slate-300 mt-1">
                        Wählen Sie Objektart und Umfang – übertragen Sie Ihre Auswahl direkt ins Formular oder per WhatsApp!
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <!-- Step 1 -->
                    <div class="bg-white/5 border border-white/10 rounded-2xl p-5">
                        <label class="block text-xs font-bold uppercase tracking-wider text-amber-400 mb-2">1. Was soll geräumt werden?</label>
                        <select id="calc-type" onchange="updateCalculator()" class="w-full bg-slate-800 text-white border border-slate-700 rounded-xl px-3.5 py-3 text-sm font-semibold outline-none focus:border-amber-400">
                            <option value="Wohnungentrümpelung wien" data-base="390">Wohnungentrümpelung Wien</option>
                            <option value="Gemeinde Wohnung Entrümpelung" data-base="390">Gemeinde Wohnung Entrümpelung</option>
                            <option value="Verlassenschaften Wien" data-base="0">Verlassenschaften Wien (Wertausgleich)</option>
                            <option value="Hausräumung Wien" data-base="790">Hausräumung Wien / Haus Entrümpelung</option>
                            <option value="Keller Entrümpelung" data-base="140">Keller Entrümpelung / Keller Räumung</option>
                            <option value="Dachbodenentrümpelung" data-base="190">Dachbodenentrümpelung</option>
                            <option value="Möbel abholen lassen" data-base="95">Einzelne Möbel abholen lassen</option>
                            <option value="Messie Entrümpelung" data-base="490">Diskrete Messie Entrümpelung</option>
                        </select>
                    </div>

                    <!-- Step 2 -->
                    <div class="bg-white/5 border border-white/10 rounded-2xl p-5">
                        <label class="block text-xs font-bold uppercase tracking-wider text-amber-400 mb-2">2. Geschätzte Größe / Menge</label>
                        <select id="calc-size" onchange="updateCalculator()" class="w-full bg-slate-800 text-white border border-slate-700 rounded-xl px-3.5 py-3 text-sm font-semibold outline-none focus:border-amber-400">
                            <option value="Klein (bis 20 m² / Einzelmöbel)" data-mult="1">Klein (bis 20 m² / Einzelmöbel)</option>
                            <option value="Mittel (25–65 m² / 2–3 Zimmer)" data-mult="1.6" selected>Mittel (25–65 m² / 2–3 Zimmer)</option>
                            <option value="Groß (70–120 m² / großes Objekt)" data-mult="2.4">Groß (70–120 m² / großes Objekt)</option>
                            <option value="Kompletthaus / Großobjekt" data-mult="3.2">Kompletthaus / Gewerbeobjekt</option>
                        </select>
                    </div>

                    <!-- Step 3 -->
                    <div class="bg-white/5 border border-white/10 rounded-2xl p-5">
                        <label class="block text-xs font-bold uppercase tracking-wider text-amber-400 mb-2">3. Wertgegenstände vorhanden?</label>
                        <select id="calc-value" onchange="updateCalculator()" class="w-full bg-slate-800 text-white border border-slate-700 rounded-xl px-3.5 py-3 text-sm font-semibold outline-none focus:border-amber-400">
                            <option value="Keine Wertanrechnung">Keine verwertbaren Gegenstände</option>
                            <option value="Gut erhaltene Möbel / Elektrogeräte">Gut erhaltene Möbel / Hausrat</option>
                            <option value="Antiquitäten / Sammlerstücke / Nachlass">Antiquitäten / Sammlerstücke / Nachlass</option>
                        </select>
                    </div>
                </div>

                <!-- Calculator Result Bar with 3 Clean Badges -->
                <div class="mt-6 bg-white/10 border border-white/15 rounded-2xl p-5 flex flex-col md:flex-row items-center justify-between gap-4">
                    <div>
                        <!-- 3 Badges Requirement -->
                        <div class="flex flex-wrap items-center gap-2 mb-2">
                            <span id="calc-badge-service" class="bg-wienRed-600/30 text-wienRed-200 border border-wienRed-500/40 text-[11px] px-2.5 py-1 rounded-full font-semibold">Wohnungentrümpelung</span>
                            <span id="calc-badge-size" class="bg-slate-800 text-slate-300 border border-slate-700 text-[11px] px-2.5 py-1 rounded-full font-semibold">Mittel (25–65 m²)</span>
                            <span id="calc-badge-value" class="bg-amber-400/20 text-amber-300 border border-amber-400/30 text-[11px] px-2.5 py-1 rounded-full font-semibold">Keine Wertanrechnung</span>
                        </div>
                        <div class="text-xs uppercase tracking-wider text-slate-300 font-semibold">Unverbindliche Orientierung &amp; Status:</div>
                        <div id="calc-output-text" class="text-lg sm:text-xl font-black text-amber-300 mt-0.5">
                            Kostenlose Besichtigung + Fixpreis vor Ort (Bei Wertausgleich oft ab 0 €!)
                        </div>
                    </div>
                    <div class="flex flex-wrap gap-3 w-full md:w-auto">
                        <button onclick="applyCalculatorToForm()" class="flex-1 md:flex-initial bg-wienRed-600 hover:bg-wienRed-700 text-white font-extrabold text-xs sm:text-sm px-5 py-3.5 rounded-xl transition shadow-md">
                            Auswahl ins Formular
                        </button>
                        <a id="calc-wa-btn" href="https://wa.me/{PHONE_TEL.replace('+', '')}?text=Hallo%20Wiener%20Dienst!" target="_blank" rel="noopener" onclick="trackConversion('whatsapp_click')"
                           class="flex-1 md:flex-initial bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs sm:text-sm px-5 py-3.5 rounded-xl transition flex items-center justify-center gap-2 shadow-md">
                            <i class="fa-brands fa-whatsapp text-base"></i> Per WhatsApp senden
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """

def generate_footer(active_file="index.html"):
    """Generates the footer containing direct links to all 22 pages, kontakt, impressum, datenschutz."""
    footer_links = []
    for item in KEYWORDS:
        is_active = (item["file"] == active_file)
        cls = "text-wienRed-400 font-bold" if is_active else "text-slate-400 hover:text-white"
        footer_links.append(f'<a href="{item["file"]}" class="{cls} text-[11px] bg-slate-900 hover:bg-slate-800 px-2.5 py-1 rounded border border-slate-800 transition whitespace-nowrap">{item["kw"]}</a>')
    
    footer_links_html = "\n".join(footer_links)
    
    return f"""
    <!-- FOOTER -->
    <footer class="bg-navy-950 text-slate-400 py-12 border-t border-slate-800 text-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
                <div>
                    <div class="flex items-center gap-2 text-lg font-black text-white mb-2">
                        {VIENNA_SHIELD_SVG}
                        <span>WIENER <span class="text-wienRed-500">DIENST</span></span>
                    </div>
                    <p class="leading-relaxed mb-3">
                        Ihre geprüfte <strong>Entrümpelung firma</strong> &amp; <strong>Räumungsfirma</strong> in Wien (1010–1230 Wien) und Niederösterreich. Handschlagqualität &amp; 100% Fixpreis-Garantie.
                    </p>
                    <p class="text-white font-bold mb-1">Tel: <a href="tel:{PHONE_TEL}" class="text-amber-400 hover:underline">{PHONE_DISPLAY}</a></p>
                    <p class="text-white font-bold">E-Mail: <a href="mailto:{EMAIL}" class="text-wienRed-400 hover:underline">{EMAIL}</a></p>
                </div>
                <div class="md:col-span-2">
                    <div class="font-bold text-white uppercase tracking-wider mb-3">Alle 22 Keyword-Landingpages (Direkt-Index)</div>
                    <div class="flex flex-wrap gap-1.5">
                        {footer_links_html}
                    </div>
                </div>
                <div>
                    <div class="font-bold text-white uppercase tracking-wider mb-3">Rechtliches &amp; Kontakt</div>
                    <ul class="space-y-2">
                        <li><a href="index.html" class="hover:text-white transition">Startseite (Index)</a></li>
                        <li><a href="kontakt.html" class="hover:text-white transition">Kontakt &amp; Vor-Ort-Termin</a></li>
                        <li><a href="impressum.html" class="hover:text-white transition">Impressum (ECG/UGB)</a></li>
                        <li><a href="datenschutz.html" class="hover:text-white transition">Datenschutzerklärung (DSGVO)</a></li>
                    </ul>
                </div>
            </div>
            <div class="pt-6 border-t border-slate-800/80 text-center sm:text-left flex flex-col sm:flex-row justify-between gap-2">
                <span>© 2026 {DOMAIN.replace('https://', '')} – Entrümpelung Wien &amp; Räumungsfirma.</span>
                <span>Alle 23 Wiener Bezirke • 0 € Anfahrt • MA 48 vorschriftsmäßig • Fixpreis-Garantie</span>
            </div>
        </div>
    </footer>
    """

def generate_scripts():
    """Generates standard tracking, mobile menu, calculator and formspree AJAX scripts."""
    return f"""
    <script>
        // Google Ads & Analytics DataLayer
        window.dataLayer = window.dataLayer || [];

        function trackConversion(eventType) {{
            window.dataLayer.push({{
                event: 'wiener_dienst_interaction',
                interaction_type: eventType,
                timestamp: new Date().toISOString()
            }});
        }}

        function toggleMobileMenu() {{
            const menu = document.getElementById('mobile-menu');
            if (menu) menu.classList.toggle('hidden');
        }}

        // Interactive Price Calculator
        function updateCalculator() {{
            const typeSelect = document.getElementById('calc-type');
            const sizeSelect = document.getElementById('calc-size');
            const valSelect = document.getElementById('calc-value');
            const outText = document.getElementById('calc-output-text');
            const waBtn = document.getElementById('calc-wa-btn');

            const badgeService = document.getElementById('calc-badge-service');
            const badgeSize = document.getElementById('calc-badge-size');
            const badgeValue = document.getElementById('calc-badge-value');

            if (!typeSelect || !sizeSelect || !valSelect) return;

            const serviceName = typeSelect.value;
            const sizeName = sizeSelect.value;
            const valName = valSelect.value;

            if (badgeService) badgeService.textContent = serviceName;
            if (badgeSize) badgeSize.textContent = sizeName;
            if (badgeValue) badgeValue.textContent = valName;

            if (valName.includes('Antiquitäten') || serviceName.includes('Verlassenschaften')) {{
                outText.textContent = `${{serviceName}}: Durch Wertanrechnung oft ab 0 € (Gratis-Räumung möglich!) – Jetzt Besichtigung sichern!`;
            }} else {{
                const base = parseInt(typeSelect.selectedOptions[0].dataset.base || "150", 10);
                const mult = parseFloat(sizeSelect.selectedOptions[0].dataset.mult || "1");
                const estimate = Math.round((base * mult) / 10) * 10;
                outText.textContent = `${{serviceName}} (${{sizeName}}): Richtwert ab ca. ${{estimate}} € inkl. Anfahrt & Entsorgung (Fixpreis nach Vor-Ort-Besichtigung)`;
            }}

            const msg = `Hallo Wiener Dienst! Meine Auswahl im Preisrechner: Leistung: ${{serviceName}}, Größe: ${{sizeName}}, Wertausgleich: ${{valName}}. Bitte um ein Angebot!`;
            if (waBtn) waBtn.href = `https://wa.me/{PHONE_TEL.replace('+', '')}?text=${{encodeURIComponent(msg)}}`;
        }}

        function applyCalculatorToForm() {{
            const serviceName = document.getElementById('calc-type').value;
            const sizeName = document.getElementById('calc-size').value;
            const valName = document.getElementById('calc-value').value;

            const selectEl = document.getElementById('hero-service-select');
            if (selectEl) {{
                for (let i = 0; i < selectEl.options.length; i++) {{
                    if (selectEl.options[i].value.toLowerCase().includes(serviceName.toLowerCase())) {{
                        selectEl.selectedIndex = i;
                        break;
                    }}
                }}
            }}
            const msgBox = document.getElementById('hero-message-box');
            if (msgBox) {{
                msgBox.value = `Rechner-Auswahl: ${{serviceName}} | Umfang: ${{sizeName}} | Wertgegenstände: ${{valName}}`;
            }}
            
            const formSection = document.getElementById('hero-lead-form');
            if (formSection) {{
                formSection.scrollIntoView({{ behavior: 'smooth' }});
                const nameInput = formSection.querySelector('input[name="name"]');
                if (nameInput) setTimeout(() => nameInput.focus(), 400);
            }}
        }}

        // AJAX Formspree submission handler that redirects to danke.html
        function bindFormspreeAjax(formId) {{
            const form = document.getElementById(formId);
            if (!form) return;
            form.addEventListener('submit', async function(e) {{
                e.preventDefault();
                const btn = form.querySelector('button[type="submit"]');
                const origText = btn ? btn.innerHTML : 'Senden';
                if (btn) {{
                    btn.disabled = true;
                    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Wird gesendet...';
                }}

                try {{
                    const res = await fetch(form.action, {{
                        method: 'POST',
                        body: new FormData(form),
                        headers: {{ 'Accept': 'application/json' }}
                    }});
                    if (res.ok) {{
                        window.dataLayer.push({{
                            event: 'google_ads_lead_conversion',
                            formId: formId,
                            timestamp: new Date().toISOString()
                        }});
                        window.location.href = 'danke.html';
                    }} else {{
                        form.submit();
                    }}
                }} catch (err) {{
                    form.submit();
                }} finally {{
                    if (btn) {{
                        btn.disabled = false;
                        btn.innerHTML = origText;
                    }}
                }}
            }});
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            updateCalculator();
            bindFormspreeAjax('hero-lead-form');
            bindFormspreeAjax('secondary-lead-form');
            bindFormspreeAjax('contact-page-form');
        }});
    </script>
    """

def generate_schema_jsonld(item):
    """Generates MovingCompany + Service and FAQPage Schema.org markup for exact match 10/10 Quality Score."""
    kw = item["kw"]
    file_name = item["file"]
    
    faq_entities = []
    for q, a in item["faqs"]:
        faq_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
        
    schema_data = [
        {
            "@context": "https://schema.org",
            "@type": ["MovingCompany", "LocalBusiness"],
            "name": f"Wiener Dienst - {kw}",
            "url": f"{DOMAIN}/{file_name}",
            "telephone": PHONE_TEL,
            "email": EMAIL,
            "priceRange": "€€",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Wien",
                "postalCode": "1010",
                "addressCountry": "AT"
            },
            "areaServed": [
                "1010 Wien", "1020 Wien", "1030 Wien", "1040 Wien", "1050 Wien", "1060 Wien",
                "1070 Wien", "1080 Wien", "1090 Wien", "1100 Wien", "1110 Wien", "1120 Wien",
                "1130 Wien", "1140 Wien", "1150 Wien", "1160 Wien", "1170 Wien", "1180 Wien",
                "1190 Wien", "1200 Wien", "1210 Wien", "1220 Wien", "1230 Wien", "Niederösterreich"
            ],
            "openingHoursSpecification": {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                "opens": "07:00",
                "closes": "22:00"
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "4.9",
                "reviewCount": "384"
            },
            "makesOffer": {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": kw,
                    "serviceType": f"Entrümpelung & Räumung: {kw}",
                    "provider": {
                        "@type": "LocalBusiness",
                        "name": "Wiener Dienst"
                    }
                }
            }
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_entities
        }
    ]
    return f"""
    <script type="application/ld+json">
    {json.dumps(schema_data[0], ensure_ascii=False, indent=2)}
    </script>
    <script type="application/ld+json">
    {json.dumps(schema_data[1], ensure_ascii=False, indent=2)}
    </script>
    """

def build_keyword_page(item):
    """Builds a complete, 600-800+ word Austrian German dedicated keyword page."""
    kw = item["kw"]
    file_name = item["file"]
    badge = item["badge"]
    title = item["title"]
    meta_desc = item["meta_desc"]
    hero_lead = item["hero_lead"]
    detail_content = item["detail_content"]
    faqs = item["faqs"]
    
    wa_msg = f"Hallo Wiener Dienst! Ich bitte um ein Fixpreis-Angebot für: {kw}."
    wa_encoded = wa_msg.replace(" ", "%20")
    
    # 4 FAQ Accordion items
    faq_accordion_html = []
    for idx, (q, a) in enumerate(faqs):
        is_open = "open" if idx == 0 else ""
        faq_accordion_html.append(f"""
        <details class="group bg-white rounded-2xl border border-slate-200 p-5" {is_open}>
            <summary class="font-extrabold text-navy-900 cursor-pointer flex items-center justify-between text-base sm:text-lg">
                <span>{q}</span>
                <i class="fa-solid fa-chevron-down text-wienRed-600 group-open:rotate-180 transition"></i>
            </summary>
            <p class="text-sm text-slate-600 mt-3 leading-relaxed">
                {a}
            </p>
        </details>
        """)
    faq_html = "\n".join(faq_accordion_html)

    # 22 Hub cards
    hub_cards = []
    for other in KEYWORDS:
        is_active = (other["file"] == file_name)
        active_border = "border-2 border-wienRed-600 bg-wienRed-50/50" if is_active else "border border-slate-200 bg-white hover:border-wienRed-600/50"
        hub_cards.append(f"""
        <a href="{other['file']}" class="p-4 rounded-2xl {active_border} transition block group shadow-sm hover:shadow-md">
            <div class="flex items-center justify-between gap-2">
                <span class="text-xs font-black {'text-wienRed-600' if is_active else 'text-navy-900 group-hover:text-wienRed-600'} transition">{other['kw']}</span>
                <i class="fa-solid fa-arrow-right text-[11px] {'text-wienRed-600' if is_active else 'text-slate-400 group-hover:text-wienRed-600'} transition"></i>
            </div>
            <p class="text-[11px] text-slate-500 mt-1 line-clamp-1">Fixpreis &amp; 0 € Besichtigung in Wien</p>
        </a>
        """)
    hub_html = "\n".join(hub_cards)

    page_html = f"""<!DOCTYPE html>
<html lang="de-AT" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Primary SEO & Google Ads 10/10 Quality Score Meta Tags -->
    <title>{title}</title>
    <meta name="description" content="{meta_desc}">
    <meta name="keywords" content="{kw}, Entrümpelung Wien, Entrümpelung firma, Räumung Wien, Räumungsfirma, Wiener Dienst, Besenrein zum Fixpreis">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
    <link rel="canonical" href="{DOMAIN}/{file_name}">
    <!-- Wiener Wappen / Shield Favicon -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 115'%3E%3Cpath d='M8 6 H92 V48 C92 80 50 106 50 109 C50 106 8 80 8 48 Z' fill='%23ffffff'/%3E%3Cpath d='M12 10 H43 V46 H12 Z' fill='%23ff0000'/%3E%3Cpath d='M57 10 H88 V46 H57 Z' fill='%23ff0000'/%3E%3Cpath d='M12 58 H43 V100 C26 89 13 74 12 58 Z' fill='%23ff0000'/%3E%3Cpath d='M57 58 H88 C87 74 74 89 57 100 Z' fill='%23ff0000'/%3E%3C/svg%3E">


    <!-- Open Graph / Social -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="{DOMAIN}/{file_name}">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="de_AT">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts: Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                    }},
                    colors: {{
                        wienRed: {{
                            50: '#fef2f2',
                            100: '#fee2e2',
                            500: '#ef4444',
                            600: '#dc2626',
                            700: '#b91c1c',
                            800: '#991b1b',
                            900: '#7f1d1d',
                        }},
                        navy: {{
                            800: '#1e293b',
                            900: '#0f172a',
                            950: '#020617',
                        }}
                    }}
                }}
            }}
        }}
    </script>

    <style>
        body {{ font-family: 'Inter', sans-serif; }}
        .hero-pattern {{
            background-color: #0f172a;
            background-image: radial-gradient(at 0% 0%, rgba(220, 38, 38, 0.22) 0px, transparent 50%),
                              radial-gradient(at 100% 100%, rgba(30, 58, 138, 0.35) 0px, transparent 50%);
        }}
        @keyframes pulse-ring {{
            0% {{ transform: scale(0.96); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }}
            70% {{ transform: scale(1); box-shadow: 0 0 0 12px rgba(34, 197, 94, 0); }}
            100% {{ transform: scale(0.96); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }}
        }}
        .whatsapp-pulse {{ animation: pulse-ring 2s infinite; }}
        @keyframes phone-ring {{
            0%, 50%, 100% {{ transform: rotate(0deg); }}
            10%, 30% {{ transform: rotate(14deg); }}
            20%, 40% {{ transform: rotate(-12deg); }}
        }}
        .ring-icon {{ animation: phone-ring 2.5s infinite; }}
        .no-scrollbar::-webkit-scrollbar {{ display: none; }}
        .no-scrollbar {{ -ms-overflow-style: none; scrollbar-width: none; }}
    </style>

    {generate_schema_jsonld(item)}
</head>
<body class="bg-slate-50 text-slate-900 antialiased pb-24 lg:pb-0 selection:bg-wienRed-600 selection:text-white">

    {generate_header(active_file=file_name)}
    {generate_quick_switcher(active_file=file_name)}

    <!-- BREADCRUMB NAVIGATION -->
    <div class="bg-slate-100 border-b border-slate-200 py-2.5 px-4 text-xs font-semibold">
        <div class="max-w-7xl mx-auto flex items-center gap-2 text-slate-600">
            <a href="index.html" class="hover:text-wienRed-600 flex items-center gap-1 font-bold text-navy-900">
                <i class="fa-solid fa-house text-wienRed-600"></i> Startseite
            </a>
            <span class="text-slate-400">/</span>
            <span class="text-slate-500">Spezial-Seiten</span>
            <span class="text-slate-400">/</span>
            <span class="text-wienRed-600 font-extrabold">{kw}</span>
        </div>
    </div>

    <!-- HERO SECTION (DEDICATED EXACT MATCH LANDING PAGE) -->
    <section class="hero-pattern text-white pt-8 pb-16 lg:py-20 relative overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">
                
                <!-- Left Column -->
                <div class="lg:col-span-7 space-y-6">
                    <div class="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm border border-white/15 px-3.5 py-1.5 rounded-full text-xs sm:text-sm font-semibold text-amber-300">
                        <i class="fa-solid fa-star text-amber-400"></i>
                        <span>{badge}</span>
                    </div>

                    <!-- EXACT MATCH H1 -->
                    <h1 class="text-3xl sm:text-5xl lg:text-[50px] font-black tracking-tight leading-[1.12]">
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-white via-white to-amber-300">{kw}</span> – Ihr Fachbetrieb in Wien zum Fixpreis!
                    </h1>

                    <!-- FIRST PARAGRAPH WITH EXACT MATCH FIRST SENTENCE IN STRONG -->
                    <p class="text-base sm:text-lg text-slate-300 leading-relaxed max-w-2xl">
                        <strong>{kw} gesucht?</strong> Als bestbewertete <strong>Entrümpelung firma</strong> und <strong>Räumungsfirma</strong> in Wien garantieren wir Ihnen eine 100% kostenlose Besichtigung, transparente Pauschalpreise ohne versteckte Zusatzkosten und eine besenreine Übergabe in allen 23 Wiener Bezirken!
                    </p>

                    <!-- 4 Core Value Pillars -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1">
                        <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl p-3">
                            <div class="w-9 h-9 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center shrink-0">
                                <i class="fa-solid fa-calendar-check"></i>
                            </div>
                            <div>
                                <div class="font-bold text-sm text-white">Gratis Besichtigung in Wien</div>
                                <div class="text-xs text-slate-400">0 € Anfahrt in allen 23 Bezirken</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl p-3">
                            <div class="w-9 h-9 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center shrink-0">
                                <i class="fa-solid fa-coins"></i>
                            </div>
                            <div>
                                <div class="font-bold text-sm text-white">Hohe Wertanrechnung</div>
                                <div class="text-xs text-slate-400">Verrechnung für Möbel &amp; Antiquitäten</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl p-3">
                            <div class="w-9 h-9 rounded-lg bg-wienRed-500/20 text-wienRed-400 flex items-center justify-center shrink-0">
                                <i class="fa-solid fa-broom"></i>
                            </div>
                            <div>
                                <div class="font-bold text-sm text-white">100% Besenrein &amp; Fixpreis</div>
                                <div class="text-xs text-slate-400">Wiener Wohnen / Übergabegarantie</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl p-3">
                            <div class="w-9 h-9 rounded-lg bg-sky-500/20 text-sky-400 flex items-center justify-center shrink-0">
                                <i class="fa-solid fa-bolt"></i>
                            </div>
                            <div>
                                <div class="font-bold text-sm text-white">24h Express-Service</div>
                                <div class="text-xs text-slate-400">Schnelle Termine oft noch heute</div>
                            </div>
                        </div>
                    </div>

                    <!-- HERO BUTTONS (EQUAL HEIGHT: h-[68px], grid-cols-2) -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5 pt-2">
                        <a href="tel:{PHONE_TEL}" onclick="trackConversion('phone_click')" class="h-14 sm:h-[68px] w-full inline-flex items-center justify-center gap-3 bg-wienRed-600 hover:bg-wienRed-700 text-white font-extrabold text-base sm:text-lg px-4 sm:px-6 rounded-2xl shadow-lg shadow-wienRed-600/30 transition transform hover:-translate-y-0.5">
                            <i class="fa-solid fa-phone-volume text-xl ring-icon shrink-0"></i>
                            <div class="text-left">
                                <span class="block text-[11px] uppercase tracking-wider font-semibold text-wienRed-100">Sofort-Termin für {kw}</span>
                                <span>{PHONE_DISPLAY}</span>
                            </div>
                        </a>
                        <a href="https://wa.me/{PHONE_TEL.replace('+', '')}?text={wa_encoded}" target="_blank" rel="noopener" onclick="trackConversion('whatsapp_click')"
                           class="h-14 sm:h-[68px] w-full inline-flex items-center justify-center gap-3 bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-base sm:text-lg px-4 sm:px-6 rounded-2xl shadow-lg shadow-emerald-600/30 transition transform hover:-translate-y-0.5">
                            <i class="fa-brands fa-whatsapp text-2xl shrink-0"></i>
                            <div class="text-left">
                                <span class="block text-[11px] uppercase tracking-wider font-semibold text-emerald-100">Fotos senden = Sofort-Preis</span>
                                <span>WhatsApp Direkt-Chat</span>
                            </div>
                        </a>
                    </div>
                </div>

                <!-- Right Column: Formspree Lead Form -->
                <div class="lg:col-span-5">
                    <div class="bg-white text-slate-900 rounded-3xl shadow-2xl p-6 sm:p-8 border-2 border-wienRed-600/20 relative">
                        <div class="absolute -top-3.5 right-6 bg-amber-400 text-navy-950 text-xs font-black uppercase px-3 py-1 rounded-full shadow">
                            Rückruf in 15 Minuten
                        </div>

                        <h2 class="text-xl sm:text-2xl font-extrabold text-navy-900 mb-1">
                            Fixpreis-Angebot für {kw}
                        </h2>
                        <p class="text-xs sm:text-sm text-slate-600 mb-5">
                            Unverbindliche Anfrage an <strong>wiener-dienst.at</strong> senden:
                        </p>

                        <form id="hero-lead-form" action="{FORMSPREE_ACTION}" method="POST" class="space-y-3.5">
                            <input type="hidden" name="_subject" value="Google Ads Anfrage [{kw}] - wiener-dienst.at">
                            <input type="hidden" name="zielseite_keyword" value="{kw}">
                            <input type="hidden" name="_next" value="{DOMAIN}/danke.html">

                            <div>
                                <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Ihr Name *</label>
                                <input type="text" name="name" required placeholder="Vor- und Nachname"
                                       class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm font-medium">
                            </div>

                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                <div>
                                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Telefonnummer *</label>
                                    <input type="tel" name="telefon" required placeholder="0660..."
                                           class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm font-medium">
                                </div>
                                <div>
                                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Bezirk / PLZ in Wien *</label>
                                    <input type="text" name="plz_bezirk" required placeholder="z.B. 1100 Wien"
                                           class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm font-medium">
                                </div>
                            </div>

                            <div>
                                <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Gewünschte Leistung</label>
                                <select name="leistung" id="hero-service-select"
                                        class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm font-semibold bg-slate-50 text-slate-800">
                                    <option value="{kw}" selected>{kw} (Aktuelle Seite)</option>
                                    <option value="Wohnungentrümpelung Wien">Wohnungentrümpelung Wien</option>
                                    <option value="Gemeinde Wohnung Entrümpelung">Gemeinde Wohnung Entrümpelung</option>
                                    <option value="Verlassenschaften Wien">Verlassenschaften Wien</option>
                                    <option value="Hausräumung Wien">Hausräumung Wien</option>
                                    <option value="Keller Entrümpelung">Keller Entrümpelung</option>
                                    <option value="Möbel abholen lassen">Möbel abholen lassen</option>
                                    <option value="Messie Entrümpelung">Messie Entrümpelung</option>
                                </select>
                            </div>

                            <div>
                                <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Details / E-Mail (Optional)</label>
                                <textarea name="nachricht" id="hero-message-box" rows="2" placeholder="Wohnungsgröße, Stockwerk, Lift vorhanden oder Wunschtermin..."
                                          class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm"></textarea>
                            </div>

                            <button type="submit"
                                    class="w-full bg-gradient-to-r from-wienRed-600 to-wienRed-700 hover:from-wienRed-700 hover:to-wienRed-800 text-white font-black text-base py-4 rounded-xl shadow-lg shadow-wienRed-600/30 transition flex items-center justify-center gap-2">
                                <span>JETZT FIXPREIS FÜR {kw} ANFRAGEN</span>
                                <i class="fa-solid fa-paper-plane"></i>
                            </button>
                        </form>
                    </div>
                </div>

            </div>
        </div>
    </section>

    {generate_calculator(current_kw=kw)}

    <!-- DETAILED SEO & VALUE SECTION (AUSTRIAN GERMAN CONTENT: 600-800+ WORDS) -->
    <section class="py-16 bg-white border-b border-slate-200">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="prose prose-slate max-w-none text-slate-700 leading-relaxed space-y-6">
                <!-- EXACT MATCH H2 -->
                <h2 class="text-2xl sm:text-3xl font-black text-navy-900 tracking-tight">
                    Warum Wiener Dienst Ihre erste Wahl für {kw} ist
                </h2>
                
                {detail_content}

                <!-- 3-STEP PROCESS CARDS -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 my-8 not-prose">
                    <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200 shadow-sm">
                        <div class="w-10 h-10 rounded-xl bg-wienRed-50 text-wienRed-600 font-black text-lg flex items-center justify-center mb-3">1</div>
                        <h3 class="font-black text-navy-900 text-base mb-1">Gratis Vor-Ort-Besichtigung</h3>
                        <p class="text-xs text-slate-600">Wir kommen kostenlos zu Ihnen in ganz Wien (1010–1230) und erstellen vor Ort ein verbindliches Fixpreis-Angebot für <strong>{kw}</strong>.</p>
                    </div>
                    <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200 shadow-sm">
                        <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-600 font-black text-lg flex items-center justify-center mb-3">2</div>
                        <h3 class="font-black text-navy-900 text-base mb-1">Faire Gegenverrechnung</h3>
                        <p class="text-xs text-slate-600">Verwertbare Möbel, Antiquitäten und Sammlerstücke rechnen wir direkt gegen die Kosten Ihrer Räumung an – oft bis zu 0 €!</p>
                    </div>
                    <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200 shadow-sm">
                        <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 font-black text-lg flex items-center justify-center mb-3">3</div>
                        <h3 class="font-black text-navy-900 text-base mb-1">100% Besenreine Übergabe</h3>
                        <p class="text-xs text-slate-600">Nach getaner Arbeit übergeben wir das Objekt pünktlich und garantiert besenrein – auch nach strengen Wiener Wohnen Richtlinien.</p>
                    </div>
                </div>

                <!-- VIENNA DISTRICTS COVERAGE -->
                <!-- EXACT MATCH H3 -->
                <h3 class="text-xl sm:text-2xl font-black text-navy-900 mt-8 mb-4">
                    Einsatzgebiet für {kw} in allen 23 Wiener Gemeindebezirken
                </h3>
                <p>
                    Wir sind täglich mit unseren Räumungs-Teams in ganz Wien und im Umland von Niederösterreich für Sie unterwegs. Egal in welchem Wiener Bezirk Sie sich befinden – für <strong>{kw}</strong> fallen bei uns <strong>0 € Anfahrtskosten</strong> an:
                </p>
                
                <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2.5 text-xs font-medium not-prose my-6">
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1010 Innere Stadt</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1020 Leopoldstadt</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1030 Landstraße</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1040 Wieden</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1050 Margareten</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1060 Mariahilf</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1070 Neubau</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1080 Josefstadt</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1090 Alsergrund</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1100 Favoriten</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1110 Simmering</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1120 Meidling</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1130 Hietzing</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1140 Penzing</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1150 Rudolfsheim-F.</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1160 Ottakring</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1170 Hernals</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1180 Währing</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1190 Döbling</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1200 Brigittenau</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1210 Floridsdorf</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1220 Donaustadt</div>
                    <div class="bg-slate-100 p-2.5 rounded-lg border border-slate-200">1230 Liesing</div>
                    <div class="bg-wienRed-50 text-wienRed-700 font-bold p-2.5 rounded-lg border border-wienRed-200">Niederösterreich (Umland)</div>
                </div>

                <!-- PRICING GUIDE TABLE -->
                <h3 class="text-xl sm:text-2xl font-black text-navy-900 mt-8 mb-4">
                    Transparente Kostenübersicht für {kw} in Wien
                </h3>
                <p>
                    Bei uns gibt es keine versteckten Kosten. Wir garantieren Ihnen vor Auftragsbeginn einen verbindlichen Pauschalpreis mit Handschlagqualität:
                </p>

                <div class="overflow-x-auto not-prose my-6 border border-slate-200 rounded-2xl shadow-sm">
                    <table class="w-full text-left text-xs sm:text-sm">
                        <thead class="bg-navy-900 text-white uppercase tracking-wider text-[11px]">
                            <tr>
                                <th class="p-3.5">Leistungsumfang</th>
                                <th class="p-3.5">Typische Dauer</th>
                                <th class="p-3.5">Besonderheit</th>
                                <th class="p-3.5">Richtpreis</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-200 bg-white">
                            <tr>
                                <td class="p-3.5 font-bold text-navy-900">{kw} (Klein / Einzelzimmer)</td>
                                <td class="p-3.5 text-slate-600">2 – 4 Stunden</td>
                                <td class="p-3.5 text-slate-600">Inkl. Tragearbeit &amp; Entsorgung</td>
                                <td class="p-3.5 font-bold text-wienRed-600">ab 150 €</td>
                            </tr>
                            <tr class="bg-slate-50">
                                <td class="p-3.5 font-bold text-navy-900">{kw} (Standard-Wohnung 2–3 Zimmer)</td>
                                <td class="p-3.5 text-slate-600">1 Arbeitstag</td>
                                <td class="p-3.5 text-slate-600">Besenrein &amp; Demontage</td>
                                <td class="p-3.5 font-bold text-wienRed-600">ab 390 €</td>
                            </tr>
                            <tr>
                                <td class="p-3.5 font-bold text-navy-900">{kw} mit hoher Wertanrechnung</td>
                                <td class="p-3.5 text-slate-600">Individuell</td>
                                <td class="p-3.5 text-slate-600">Gegenverrechnung von Antiquitäten/Möbeln</td>
                                <td class="p-3.5 font-bold text-emerald-600">oft ab 0 € (Gratis!)</td>
                            </tr>
                            <tr class="bg-slate-50">
                                <td class="p-3.5 font-bold text-navy-900">{kw} (Komplettes Haus / Großräumung)</td>
                                <td class="p-3.5 text-slate-600">1 – 2 Tage</td>
                                <td class="p-3.5 text-slate-600">Keller, Dachboden, Garage &amp; Garten</td>
                                <td class="p-3.5 font-bold text-wienRed-600">Fixpreis nach Besichtigung</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

            </div>

        </div>
    </section>

    <!-- FAQ SECTION (TAILORED 4 QUESTIONS FOR THIS KEYWORD) -->
    <section class="py-16 bg-slate-50 border-b border-slate-200">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-10">
                <span class="text-wienRed-600 font-bold text-xs uppercase tracking-widest bg-wienRed-50 px-3 py-1 rounded-full border border-wienRed-200">Häufige Fragen</span>
                <h2 class="text-2xl sm:text-3xl font-black text-navy-900 mt-3">
                    Wichtige Antworten zu {kw}
                </h2>
                <p class="text-sm text-slate-600 mt-1">Hier finden Sie alle Fakten rund um unsere Arbeit als Räumungsfirma in Wien:</p>
            </div>

            <div class="space-y-4">
                {faq_html}
            </div>
        </div>
    </section>

    <!-- ALL 22 KEYWORDS HUB -->
    <section class="py-16 bg-white border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-10">
                <span class="text-xs font-extrabold uppercase tracking-widest text-wienRed-600">Google Ads 10/10 Zielseiten-Index</span>
                <h2 class="text-2xl sm:text-3xl font-black text-navy-900 mt-1">
                    Alle 22 Keyword-Landingpages auf einen Klick
                </h2>
                <p class="text-sm text-slate-600 mt-1">
                    Jede Seite bietet eigenständigen, vollwertigen Inhalt mit Preistabelle und speziellem Formular:
                </p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
                {hub_html}
            </div>
        </div>
    </section>

    {generate_floating_docks(current_kw=kw)}
    {generate_footer(active_file=file_name)}
    {generate_scripts()}

</body>
</html>
"""
    return page_html

print("Generator functions prepared.")

def build_index_page():
    """Generates the master index.html."""
    item = KEYWORDS[0] # Default to Entrümpelung Wien for primary index
    kw = "Entrümpelung Wien"
    title = "Entrümpelung Wien & Räumungsfirma | Wiener Dienst – Besenrein zum Fixpreis"
    meta_desc = "Ihre seriöse Entrümpelung Firma & Räumungsfirma in Wien. Kostenlose Besichtigung in allen 23 Bezirken, besenreine Übergabe, Fixpreis-Garantie & Wertanrechnung. ☎ 0660 606 0775"
    
    wa_msg = "Hallo Wiener Dienst! Ich bitte um ein unverbindliches Angebot für eine Entrümpelung in Wien."
    wa_encoded = wa_msg.replace(" ", "%20")
    
    # 22 Hub cards for index.html
    hub_cards = []
    for other in KEYWORDS:
        hub_cards.append(f"""
        <a href="{other['file']}" class="p-4 rounded-2xl border border-slate-200 bg-white hover:border-wienRed-600/50 transition block group shadow-sm hover:shadow-md">
            <div class="flex items-center justify-between gap-2">
                <span class="text-xs font-black text-navy-900 group-hover:text-wienRed-600 transition">{other['kw']}</span>
                <i class="fa-solid fa-arrow-right text-[11px] text-slate-400 group-hover:text-wienRed-600 transition"></i>
            </div>
            <p class="text-[11px] text-slate-500 mt-1 line-clamp-1">Fixpreis &amp; 0 € Besichtigung in Wien</p>
        </a>
        """)
    hub_html = "\n".join(hub_cards)

    page_html = f"""<!DOCTYPE html>
<html lang="de-AT" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Primary SEO & Google Ads 10/10 Quality Score Meta Tags -->
    <title>{title}</title>
    <meta name="description" content="{meta_desc}">
    <meta name="keywords" content="Entrümpelung Wien, Entrümpelung firma, Räumung Wien, Räumungsfirma, Möbel abholen lassen, Wohnungentrümpelung wien, Wohnungsraumung Wien, Keller Entrümpelung, Keller Räumung, Verlassenschaften Wien, Hausräumung Wien, Haus Entrümpelung Wien, Gemeinde Wohnung Entrümpelung, Dachbodenentrümpelung, Gemeinde wohnungsräumung, Wien Entrümpelung, Verlassenschaftsräumung, Verlassenschafts Entrümpelung, Nachlassräumung, Nachlass Entrümpelung, Messie Räumung, Messie Entrümpelung">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
    <link rel="canonical" href="{DOMAIN}/">
    <!-- Wiener Wappen / Shield Favicon -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 115'%3E%3Cpath d='M8 6 H92 V48 C92 80 50 106 50 109 C50 106 8 80 8 48 Z' fill='%23ffffff'/%3E%3Cpath d='M12 10 H43 V46 H12 Z' fill='%23ff0000'/%3E%3Cpath d='M57 10 H88 V46 H57 Z' fill='%23ff0000'/%3E%3Cpath d='M12 58 H43 V100 C26 89 13 74 12 58 Z' fill='%23ff0000'/%3E%3Cpath d='M57 58 H88 C87 74 74 89 57 100 Z' fill='%23ff0000'/%3E%3C/svg%3E">


    <!-- Open Graph / Social -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="{DOMAIN}/">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="de_AT">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts: Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                    }},
                    colors: {{
                        wienRed: {{
                            50: '#fef2f2',
                            100: '#fee2e2',
                            500: '#ef4444',
                            600: '#dc2626',
                            700: '#b91c1c',
                            800: '#991b1b',
                            900: '#7f1d1d',
                        }},
                        navy: {{
                            800: '#1e293b',
                            900: '#0f172a',
                            950: '#020617',
                        }}
                    }}
                }}
            }}
        }}
    </script>

    <style>
        body {{ font-family: 'Inter', sans-serif; }}
        .hero-pattern {{
            background-color: #0f172a;
            background-image: radial-gradient(at 0% 0%, rgba(220, 38, 38, 0.22) 0px, transparent 50%),
                              radial-gradient(at 100% 100%, rgba(30, 58, 138, 0.35) 0px, transparent 50%);
        }}
        @keyframes pulse-ring {{
            0% {{ transform: scale(0.96); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }}
            70% {{ transform: scale(1); box-shadow: 0 0 0 12px rgba(34, 197, 94, 0); }}
            100% {{ transform: scale(0.96); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }}
        }}
        .whatsapp-pulse {{ animation: pulse-ring 2s infinite; }}
        @keyframes phone-ring {{
            0%, 50%, 100% {{ transform: rotate(0deg); }}
            10%, 30% {{ transform: rotate(14deg); }}
            20%, 40% {{ transform: rotate(-12deg); }}
        }}
        .ring-icon {{ animation: phone-ring 2.5s infinite; }}
        .no-scrollbar::-webkit-scrollbar {{ display: none; }}
        .no-scrollbar {{ -ms-overflow-style: none; scrollbar-width: none; }}
    </style>

    {generate_schema_jsonld(item)}
</head>
<body class="bg-slate-50 text-slate-900 antialiased pb-24 lg:pb-0 selection:bg-wienRed-600 selection:text-white">

    {generate_header(active_file="index.html")}
    {generate_quick_switcher(active_file="index.html")}

    <!-- HERO SECTION -->
    <section id="top" class="hero-pattern text-white pt-8 pb-16 lg:py-20 relative overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">
                
                <!-- Left Column -->
                <div class="lg:col-span-7 space-y-6">
                    <div class="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm border border-white/15 px-3.5 py-1.5 rounded-full text-xs sm:text-sm font-semibold text-amber-300">
                        <i class="fa-solid fa-star text-amber-400"></i>
                        <span>4.9/5 ★ (384 Bewertungen) • Geprüfte Entrümpelung Firma &amp; Räumungsfirma Wien</span>
                    </div>

                    <h1 class="text-3xl sm:text-5xl lg:text-[52px] font-black tracking-tight leading-[1.12]">
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-white via-white to-amber-300">Entrümpelung Wien</span> &amp; seriöse <span class="text-wienRed-500 underline decoration-wienRed-500/40">Räumungsfirma</span> zum Fixpreis!
                    </h1>

                    <p class="text-base sm:text-lg text-slate-300 leading-relaxed max-w-2xl">
                        Ihr Wiener Fachbetrieb für <strong>Entrümpelung Wien</strong>, <strong>Räumung Wien</strong>, <strong>Wohnungentrümpelung wien</strong>, <strong>Wohnungsraumung Wien</strong>, <strong>Verlassenschaften Wien</strong>, <strong>Keller Entrümpelung</strong> sowie <strong>Gemeinde Wohnung Entrümpelung</strong>. Kostenlose Besichtigung &amp; besenreine Übergabe – oft noch am selben Tag!
                    </p>

                    <!-- 4 Core Value Pillars -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1">
                        <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl p-3">
                            <div class="w-9 h-9 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center shrink-0">
                                <i class="fa-solid fa-calendar-check"></i>
                            </div>
                            <div>
                                <div class="font-bold text-sm text-white">Gratis Besichtigung in Wien</div>
                                <div class="text-xs text-slate-400">0 € Anfahrt in allen 23 Bezirken</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl p-3">
                            <div class="w-9 h-9 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center shrink-0">
                                <i class="fa-solid fa-coins"></i>
                            </div>
                            <div>
                                <div class="font-bold text-sm text-white">Hohe Wertanrechnung</div>
                                <div class="text-xs text-slate-400">Verlassenschaften &amp; Nachlass Ankauf</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl p-3">
                            <div class="w-9 h-9 rounded-lg bg-wienRed-500/20 text-wienRed-400 flex items-center justify-center shrink-0">
                                <i class="fa-solid fa-broom"></i>
                            </div>
                            <div>
                                <div class="font-bold text-sm text-white">100% Besenrein &amp; Fixpreis</div>
                                <div class="text-xs text-slate-400">Wiener Wohnen / Gemeinde konform</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl p-3">
                            <div class="w-9 h-9 rounded-lg bg-sky-500/20 text-sky-400 flex items-center justify-center shrink-0">
                                <i class="fa-solid fa-bolt"></i>
                            </div>
                            <div>
                                <div class="font-bold text-sm text-white">24h Express-Service</div>
                                <div class="text-xs text-slate-400">Schnell Möbel abholen lassen</div>
                            </div>
                        </div>
                    </div>

                    <!-- HERO BUTTONS (EQUAL HEIGHT: h-[68px], grid-cols-2) -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5 pt-2">
                        <a href="tel:{PHONE_TEL}" onclick="trackConversion('phone_click')" class="h-14 sm:h-[68px] w-full inline-flex items-center justify-center gap-3 bg-wienRed-600 hover:bg-wienRed-700 text-white font-extrabold text-base sm:text-lg px-4 sm:px-6 rounded-2xl shadow-lg shadow-wienRed-600/30 transition transform hover:-translate-y-0.5">
                            <i class="fa-solid fa-phone-volume text-xl ring-icon shrink-0"></i>
                            <div class="text-left">
                                <span class="block text-[11px] uppercase tracking-wider font-semibold text-wienRed-100">Sofort-Termin &amp; Auskunft</span>
                                <span>{PHONE_DISPLAY}</span>
                            </div>
                        </a>
                        <a href="https://wa.me/{PHONE_TEL.replace('+', '')}?text={wa_encoded}" target="_blank" rel="noopener" onclick="trackConversion('whatsapp_click')"
                           class="h-14 sm:h-[68px] w-full inline-flex items-center justify-center gap-3 bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-base sm:text-lg px-4 sm:px-6 rounded-2xl shadow-lg shadow-emerald-600/30 transition transform hover:-translate-y-0.5">
                            <i class="fa-brands fa-whatsapp text-2xl shrink-0"></i>
                            <div class="text-left">
                                <span class="block text-[11px] uppercase tracking-wider font-semibold text-emerald-100">Fotos senden = Sofort-Preis</span>
                                <span>WhatsApp Direkt-Chat</span>
                            </div>
                        </a>
                    </div>
                </div>

                <!-- Right Column: Formspree Lead Form -->
                <div class="lg:col-span-5">
                    <div class="bg-white text-slate-900 rounded-3xl shadow-2xl p-6 sm:p-8 border-2 border-wienRed-600/20 relative">
                        <div class="absolute -top-3.5 right-6 bg-amber-400 text-navy-950 text-xs font-black uppercase px-3 py-1 rounded-full shadow">
                            Rückruf in 15 Minuten
                        </div>

                        <h2 class="text-xl sm:text-2xl font-extrabold text-navy-900 mb-1">
                            Kostenloses Fixpreis-Angebot
                        </h2>
                        <p class="text-xs sm:text-sm text-slate-600 mb-5">
                            Unverbindliche Anfrage an <strong>wiener-dienst.at</strong> senden:
                        </p>

                        <form id="hero-lead-form" action="{FORMSPREE_ACTION}" method="POST" class="space-y-3.5">
                            <input type="hidden" name="_subject" value="Google Ads Anfrage (Startseite) - wiener-dienst.at">
                            <input type="hidden" name="zielseite_keyword" value="Startseite (Entrümpelung Wien)">
                            <input type="hidden" name="_next" value="{DOMAIN}/danke.html">

                            <div>
                                <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Ihr Name *</label>
                                <input type="text" name="name" required placeholder="Vor- und Nachname"
                                       class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm font-medium">
                            </div>

                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                <div>
                                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Telefonnummer *</label>
                                    <input type="tel" name="telefon" required placeholder="0660..."
                                           class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm font-medium">
                                </div>
                                <div>
                                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">PLZ / Bezirk in Wien *</label>
                                    <input type="text" name="plz_bezirk" required placeholder="z.B. 1010 Wien"
                                           class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm font-medium">
                                </div>
                            </div>

                            <div>
                                <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Gewünschte Leistung</label>
                                <select name="leistung" id="hero-service-select"
                                        class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm font-semibold bg-slate-50 text-slate-800">
                                    <option value="Entrümpelung Wien" selected>Entrümpelung Wien / Räumung Wien</option>
                                    <option value="Wohnungentrümpelung wien">Wohnungentrümpelung Wien</option>
                                    <option value="Gemeinde Wohnung Entrümpelung">Gemeinde Wohnung Entrümpelung</option>
                                    <option value="Verlassenschaften Wien">Verlassenschaften Wien (Wertausgleich)</option>
                                    <option value="Hausräumung Wien">Hausräumung Wien</option>
                                    <option value="Keller Entrümpelung">Keller Entrümpelung / Dachboden</option>
                                    <option value="Möbel abholen lassen">Möbel abholen lassen</option>
                                    <option value="Messie Entrümpelung">Messie Entrümpelung (Diskret)</option>
                                </select>
                            </div>

                            <div>
                                <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Details / E-Mail (Optional)</label>
                                <textarea name="nachricht" id="hero-message-box" rows="2" placeholder="Wohnungsgröße, Stockwerk, Lift vorhanden oder Wunschtermin..."
                                          class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm"></textarea>
                            </div>

                            <button type="submit"
                                    class="w-full bg-gradient-to-r from-wienRed-600 to-wienRed-700 hover:from-wienRed-700 hover:to-wienRed-800 text-white font-black text-base py-4 rounded-xl shadow-lg shadow-wienRed-600/30 transition flex items-center justify-center gap-2">
                                <span>JETZT KOSTENLOS ANFRAGEN</span>
                                <i class="fa-solid fa-paper-plane"></i>
                            </button>
                        </form>
                    </div>
                </div>

            </div>
        </div>
    </section>

    {generate_calculator(current_kw="Wien")}

    <!-- CORE SERVICES CLUSTERS -->
    <section id="leistungen" class="py-16 bg-slate-50 border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-12">
                <span class="text-wienRed-600 font-extrabold text-xs uppercase tracking-widest bg-wienRed-50 px-3.5 py-1.5 rounded-full border border-wienRed-200">
                    Alle 22 Fachbereiche unter einem Dach
                </span>
                <h2 class="text-3xl sm:text-4xl font-black text-navy-900 mt-4">
                    Ihre Entrümpelung Firma &amp; Räumungsfirma für Wien
                </h2>
                <p class="text-slate-600 mt-2 text-base">
                    Wählen Sie Ihren Fachbereich für detaillierte Informationen, Richtpreise und Sofort-Beratung:
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-7">
                <!-- Cluster 1 -->
                <article class="bg-white rounded-3xl p-7 shadow-sm hover:shadow-xl border border-slate-200 transition flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-wienRed-50 text-wienRed-600 flex items-center justify-center text-xl mb-4">
                            <i class="fa-solid fa-building"></i>
                        </div>
                        <h3 class="text-xl font-extrabold text-navy-900 mb-2">
                            Wohnungentrümpelung Wien &amp; Wohnungsraumung Wien
                        </h3>
                        <p class="text-sm text-slate-600 mb-4 leading-relaxed">
                            Ob 1-Zimmer-Wohnung oder großer Altbau: Wir erledigen Ihre <strong>Wohnungentrümpelung wien</strong> und <strong>Wohnungsraumung Wien</strong> inklusive Demontage von Küchen, Einbauschränken und Böden besenrein zum Fixpreis.
                        </p>
                    </div>
                    <a href="wohnungentruempelung-wien.html" class="w-full py-3 rounded-xl bg-slate-100 hover:bg-wienRed-600 hover:text-white font-bold text-xs uppercase tracking-wider transition text-center block">
                        Spezial-Seite: Wohnungentrümpelung →
                    </a>
                </article>

                <!-- Cluster 2 -->
                <article class="bg-white rounded-3xl p-7 shadow-sm hover:shadow-xl border border-slate-200 transition flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-wienRed-50 text-wienRed-600 flex items-center justify-center text-xl mb-4">
                            <i class="fa-solid fa-key"></i>
                        </div>
                        <h3 class="text-xl font-extrabold text-navy-900 mb-2">
                            Gemeinde Wohnung Entrümpelung &amp; Gemeinde wohnungsräumung
                        </h3>
                        <p class="text-sm text-slate-600 mb-4 leading-relaxed">
                            100% Wiener-Wohnen-konforme <strong>Gemeinde Wohnung Entrümpelung</strong> und <strong>Gemeinde wohnungsräumung</strong>. Wir entfernen Tapeten, Fliesen, Laminat, Zwischendecken und übergeben besenrein für die Endabnahme.
                        </p>
                    </div>
                    <a href="gemeinde-wohnung-entruempelung.html" class="w-full py-3 rounded-xl bg-slate-100 hover:bg-wienRed-600 hover:text-white font-bold text-xs uppercase tracking-wider transition text-center block">
                        Spezial-Seite: Gemeindewohnung →
                    </a>
                </article>

                <!-- Cluster 3 -->
                <article class="bg-white rounded-3xl p-7 shadow-sm hover:shadow-xl border border-slate-200 transition flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-wienRed-50 text-wienRed-600 flex items-center justify-center text-xl mb-4">
                            <i class="fa-solid fa-scale-balanced"></i>
                        </div>
                        <h3 class="text-xl font-extrabold text-navy-900 mb-2">
                            Verlassenschaften Wien, Verlassenschaftsräumung &amp; Nachlassräumung
                        </h3>
                        <p class="text-sm text-slate-600 mb-4 leading-relaxed">
                            Seriöse Abwicklung für <strong>Verlassenschaften Wien</strong>, <strong>Verlassenschaftsräumung</strong>, <strong>Verlassenschafts Entrümpelung</strong>, <strong>Nachlassräumung</strong> &amp; <strong>Nachlass Entrümpelung</strong> mit hoher Wertanrechnung vor Ort!
                        </p>
                    </div>
                    <a href="verlassenschaften-wien.html" class="w-full py-3 rounded-xl bg-slate-100 hover:bg-wienRed-600 hover:text-white font-bold text-xs uppercase tracking-wider transition text-center block">
                        Spezial-Seite: Verlassenschaft &amp; Nachlass →
                    </a>
                </article>

                <!-- Cluster 4 -->
                <article class="bg-white rounded-3xl p-7 shadow-sm hover:shadow-xl border border-slate-200 transition flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-wienRed-50 text-wienRed-600 flex items-center justify-center text-xl mb-4">
                            <i class="fa-solid fa-boxes-stacked"></i>
                        </div>
                        <h3 class="text-xl font-extrabold text-navy-900 mb-2">
                            Keller Entrümpelung, Keller Räumung &amp; Dachbodenentrümpelung
                        </h3>
                        <p class="text-sm text-slate-600 mb-4 leading-relaxed">
                            Schaffen Sie wieder Platz! Wir übernehmen jede <strong>Keller Entrümpelung</strong>, <strong>Keller Räumung</strong> sowie <strong>Dachbodenentrümpelung</strong> in Wien – auch ohne Lift aus jedem Stockwerk oder engen Kellerabteilen.
                        </p>
                    </div>
                    <a href="keller-entruempelung.html" class="w-full py-3 rounded-xl bg-slate-100 hover:bg-wienRed-600 hover:text-white font-bold text-xs uppercase tracking-wider transition text-center block">
                        Spezial-Seite: Keller &amp; Dachboden →
                    </a>
                </article>

                <!-- Cluster 5 -->
                <article class="bg-white rounded-3xl p-7 shadow-sm hover:shadow-xl border border-slate-200 transition flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-wienRed-50 text-wienRed-600 flex items-center justify-center text-xl mb-4">
                            <i class="fa-solid fa-house-chimney"></i>
                        </div>
                        <h3 class="text-xl font-extrabold text-navy-900 mb-2">
                            Hausräumung Wien &amp; Haus Entrümpelung Wien
                        </h3>
                        <p class="text-sm text-slate-600 mb-4 leading-relaxed">
                            Komplette <strong>Hausräumung Wien</strong> und <strong>Haus Entrümpelung Wien</strong> vom Keller über die Garage und den Garten bis zum Dachboden. Ideal vor Verkauf, Sanierung oder Übergabe.
                        </p>
                    </div>
                    <a href="hausraeumung-wien.html" class="w-full py-3 rounded-xl bg-slate-100 hover:bg-wienRed-600 hover:text-white font-bold text-xs uppercase tracking-wider transition text-center block">
                        Spezial-Seite: Hausräumung Wien →
                    </a>
                </article>

                <!-- Cluster 6 -->
                <article class="bg-white rounded-3xl p-7 shadow-sm hover:shadow-xl border border-slate-200 transition flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-wienRed-50 text-wienRed-600 flex items-center justify-center text-xl mb-4">
                            <i class="fa-solid fa-couch"></i>
                        </div>
                        <h3 class="text-xl font-extrabold text-navy-900 mb-2">
                            Möbel abholen lassen, Messie Räumung &amp; Messie Entrümpelung
                        </h3>
                        <p class="text-sm text-slate-600 mb-4 leading-relaxed">
                            Kurzfristig alte <strong>Möbel abholen lassen</strong> (Sofa, Kasten, Küche, Sperrmüll) oder 100% diskrete <strong>Messie Räumung</strong> &amp; <strong>Messie Entrümpelung</strong> mit neutralen Fahrzeugen in ganz Wien.
                        </p>
                    </div>
                    <a href="moebel-abholen-lassen.html" class="w-full py-3 rounded-xl bg-slate-100 hover:bg-wienRed-600 hover:text-white font-bold text-xs uppercase tracking-wider transition text-center block">
                        Spezial-Seite: Möbel &amp; Messie-Hilfe →
                    </a>
                </article>
            </div>
        </div>
    </section>

    <!-- 22 KEYWORDS HUB ON HOMEPAGE -->
    <section id="keyword-index" class="py-16 bg-white border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-10">
                <span class="text-xs font-extrabold uppercase tracking-widest text-wienRed-600">Google Ads 10/10 Zielseiten-Index</span>
                <h2 class="text-2xl sm:text-3xl font-black text-navy-900 mt-1">
                    Alle 22 Keyword-Landingpages auf einen Klick
                </h2>
                <p class="text-sm text-slate-600 mt-1">
                    Jede Seite bietet eigenständigen, vollwertigen Inhalt mit Preistabelle und speziellem Formular:
                </p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
                {hub_html}
            </div>
        </div>
    </section>

    <!-- FAQ SECTION -->
    <section id="faq" class="py-16 bg-slate-50 border-b border-slate-200">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-10">
                <span class="text-wienRed-600 font-bold text-xs uppercase tracking-widest bg-wienRed-50 px-3 py-1 rounded-full border border-wienRed-200">Häufige Fragen</span>
                <h2 class="text-2xl sm:text-3xl font-black text-navy-900 mt-3">
                    Wichtige Antworten Ihrer Entrümpelung Firma &amp; Räumungsfirma Wien
                </h2>
            </div>
            <div class="space-y-4">
                <details class="group bg-white rounded-2xl border border-slate-200 p-5" open>
                    <summary class="font-extrabold text-navy-900 cursor-pointer flex items-center justify-between text-base sm:text-lg">
                        <span>Wie schnell sind Entrümpelung Wien, Räumung Wien oder Möbel abholen lassen möglich?</span>
                        <i class="fa-solid fa-chevron-down text-wienRed-600 group-open:rotate-180 transition"></i>
                    </summary>
                    <p class="text-sm text-slate-600 mt-3 leading-relaxed">
                        Wir bieten kostenlose Besichtigungen in allen 23 Wiener Bezirken oft noch am selben Tag an. Eine komplette <strong>Wohnungentrümpelung wien</strong>, <strong>Wohnungsraumung Wien</strong>, <strong>Keller Entrümpelung</strong> oder das <strong>Möbel abholen lassen</strong> führen wir innerhalb von 24 bis 48 Stunden durch.
                    </p>
                </details>
                <details class="group bg-white rounded-2xl border border-slate-200 p-5">
                    <summary class="font-extrabold text-navy-900 cursor-pointer flex items-center justify-between text-base sm:text-lg">
                        <span>Wie läuft eine Verlassenschaftsräumung bzw. Nachlassräumung mit Wertanrechnung ab?</span>
                        <i class="fa-solid fa-chevron-down text-wienRed-600 group-open:rotate-180 transition"></i>
                    </summary>
                    <p class="text-sm text-slate-600 mt-3 leading-relaxed">
                        Bei <strong>Verlassenschaften Wien</strong>, <strong>Verlassenschaftsräumung</strong>, <strong>Verlassenschafts Entrümpelung</strong>, <strong>Nachlassräumung</strong> und <strong>Nachlass Entrümpelung</strong> schätzen wir Antiquitäten, Bilder, Schmuck und Möbel kostenlos vor Ort. Der Wert wird direkt vom Fixpreis abgezogen.
                    </p>
                </details>
                <details class="group bg-white rounded-2xl border border-slate-200 p-5">
                    <summary class="font-extrabold text-navy-900 cursor-pointer flex items-center justify-between text-base sm:text-lg">
                        <span>Was beinhaltet die Gemeinde Wohnung Entrümpelung / Gemeinde wohnungsräumung?</span>
                        <i class="fa-solid fa-chevron-down text-wienRed-600 group-open:rotate-180 transition"></i>
                    </summary>
                    <p class="text-sm text-slate-600 mt-3 leading-relaxed">
                        Unsere <strong>Gemeinde Wohnung Entrümpelung</strong> und <strong>Gemeinde wohnungsräumung</strong> erfüllt sämtliche Vorgaben von Wiener Wohnen: Entfernung von Einbauküchen, Bodenbelägen, Tapeten, Holzdecken, Fliesen sowie besenreine Übergabe inkl. Kellerabteil.
                    </p>
                </details>
            </div>
        </div>
    </section>

    {generate_floating_docks(current_kw="Entrümpelung Wien")}
    {generate_footer(active_file="index.html")}
    {generate_scripts()}

</body>
</html>
"""
    return page_html

def build_kontakt_page():
    """Generates the dedicated kontakt.html page."""
    title = "Kontakt & Besichtigung | Wiener Dienst – Räumungsfirma Wien"
    meta_desc = "Kontaktieren Sie Wiener Dienst für Ihre Entrümpelung & Räumung in Wien. Kostenlose Vor-Ort-Besichtigung in allen 23 Bezirken. ☎ 0660 606 0775"
    
    wa_msg = "Hallo Wiener Dienst! Ich möchte eine kostenlose Besichtigung in Wien anfragen."
    wa_encoded = wa_msg.replace(" ", "%20")
    
    page_html = f"""<!DOCTYPE html>
<html lang="de-AT" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="{DOMAIN}/kontakt.html">
    <!-- Wiener Wappen / Shield Favicon -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 115'%3E%3Cpath d='M8 6 H92 V48 C92 80 50 106 50 109 C50 106 8 80 8 48 Z' fill='%23ffffff'/%3E%3Cpath d='M12 10 H43 V46 H12 Z' fill='%23ff0000'/%3E%3Cpath d='M57 10 H88 V46 H57 Z' fill='%23ff0000'/%3E%3Cpath d='M12 58 H43 V100 C26 89 13 74 12 58 Z' fill='%23ff0000'/%3E%3Cpath d='M57 58 H88 C87 74 74 89 57 100 Z' fill='%23ff0000'/%3E%3C/svg%3E">

    <meta name="robots" content="index, follow">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Inter', 'sans-serif'] }},
                    colors: {{
                        wienRed: {{ 50: '#fef2f2', 100: '#fee2e2', 500: '#ef4444', 600: '#dc2626', 700: '#b91c1c', 800: '#991b1b', 900: '#7f1d1d' }},
                        navy: {{ 800: '#1e293b', 900: '#0f172a', 950: '#020617' }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ font-family: 'Inter', sans-serif; }}
        .hero-pattern {{
            background-color: #0f172a;
            background-image: radial-gradient(at 0% 0%, rgba(220, 38, 38, 0.22) 0px, transparent 50%),
                              radial-gradient(at 100% 100%, rgba(30, 58, 138, 0.35) 0px, transparent 50%);
        }}
        @keyframes phone-ring {{
            0%, 50%, 100% {{ transform: rotate(0deg); }}
            10%, 30% {{ transform: rotate(14deg); }}
            20%, 40% {{ transform: rotate(-12deg); }}
        }}
        .ring-icon {{ animation: phone-ring 2.5s infinite; }}
        .no-scrollbar::-webkit-scrollbar {{ display: none; }}
        .no-scrollbar {{ -ms-overflow-style: none; scrollbar-width: none; }}
    </style>
</head>
<body class="bg-slate-50 text-slate-900 antialiased pb-24 lg:pb-0 selection:bg-wienRed-600 selection:text-white">

    {generate_header(active_file="kontakt.html")}
    {generate_quick_switcher(active_file="kontakt.html")}

    <!-- BREADCRUMB -->
    <div class="bg-slate-100 border-b border-slate-200 py-2.5 px-4 text-xs font-semibold">
        <div class="max-w-7xl mx-auto flex items-center gap-2 text-slate-600">
            <a href="index.html" class="hover:text-wienRed-600 flex items-center gap-1 font-bold text-navy-900">
                <i class="fa-solid fa-house text-wienRed-600"></i> Startseite
            </a>
            <span class="text-slate-400">/</span>
            <span class="text-wienRed-600 font-extrabold">Kontakt &amp; Vor-Ort-Termin</span>
        </div>
    </div>

    <!-- KONTAKT HERO & FORM -->
    <section class="py-16 bg-white border-b border-slate-200">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-12">
                <span class="bg-wienRed-50 text-wienRed-600 border border-wienRed-200 text-xs font-bold uppercase px-3 py-1 rounded-full">
                    Persönlicher Kundenservice Wien
                </span>
                <h1 class="text-3xl sm:text-5xl font-black text-navy-900 mt-3">
                    Kontaktieren Sie Wiener Dienst
                </h1>
                <p class="text-slate-600 text-base mt-2">
                    Kostenlose Besichtigung, 100% Fixpreis-Garantie und unverbindliche Beratung in allen 23 Wiener Bezirken und Niederösterreich.
                </p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
                <!-- Contact info cards -->
                <div class="lg:col-span-5 space-y-6">
                    <div class="p-6 rounded-3xl bg-slate-50 border border-slate-200 shadow-sm space-y-6">
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded-2xl bg-wienRed-100 text-wienRed-600 flex items-center justify-center text-xl shrink-0">
                                <i class="fa-solid fa-phone-volume ring-icon"></i>
                            </div>
                            <div>
                                <div class="text-xs font-bold uppercase text-slate-500">Telefonische Sofort-Beratung</div>
                                <a href="tel:{PHONE_TEL}" class="text-xl font-black text-navy-900 hover:text-wienRed-600 transition block mt-0.5">{PHONE_DISPLAY}</a>
                                <p class="text-xs text-slate-600 mt-1">Montag bis Sonntag: 07:00 – 22:00 Uhr</p>
                            </div>
                        </div>

                        <div class="flex items-start gap-4 pt-4 border-t border-slate-200">
                            <div class="w-12 h-12 rounded-2xl bg-emerald-100 text-emerald-600 flex items-center justify-center text-2xl shrink-0">
                                <i class="fa-brands fa-whatsapp"></i>
                            </div>
                            <div>
                                <div class="text-xs font-bold uppercase text-slate-500">WhatsApp Foto-Schätzung</div>
                                <a href="https://wa.me/{PHONE_TEL.replace('+', '')}?text={wa_encoded}" target="_blank" rel="noopener" class="text-lg font-black text-emerald-700 hover:underline block mt-0.5">Chat starten &amp; Fotos senden</a>
                                <p class="text-xs text-slate-600 mt-1">Fotos schicken = Richtpreis in 15 Min erhalten!</p>
                            </div>
                        </div>

                        <div class="flex items-start gap-4 pt-4 border-t border-slate-200">
                            <div class="w-12 h-12 rounded-2xl bg-slate-200 text-slate-700 flex items-center justify-center text-xl shrink-0">
                                <i class="fa-solid fa-envelope"></i>
                            </div>
                            <div>
                                <div class="text-xs font-bold uppercase text-slate-500">E-Mail Anfrage</div>
                                <a href="mailto:{EMAIL}" class="text-base font-bold text-navy-900 hover:text-wienRed-600 transition block mt-0.5">{EMAIL}</a>
                                <p class="text-xs text-slate-600 mt-1">Antwort innerhalb von maximal 2 Stunden</p>
                            </div>
                        </div>

                        <div class="flex items-start gap-4 pt-4 border-t border-slate-200">
                            <div class="w-12 h-12 rounded-2xl bg-amber-100 text-amber-700 flex items-center justify-center text-xl shrink-0">
                                <i class="fa-solid fa-location-dot"></i>
                            </div>
                            <div>
                                <div class="text-xs font-bold uppercase text-slate-500">Einsatzgebiet &amp; Standort</div>
                                <div class="text-base font-bold text-navy-900 mt-0.5">Wien (1010–1230) &amp; NÖ</div>
                                <p class="text-xs text-slate-600 mt-1">0 € Anfahrt in allen 23 Wiener Gemeindebezirken</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Contact Formspree Form -->
                <div class="lg:col-span-7">
                    <div class="bg-white rounded-3xl p-8 border-2 border-slate-200 shadow-xl">
                        <h2 class="text-2xl font-black text-navy-900 mb-2">Unverbindliche Anfrage senden</h2>
                        <p class="text-xs sm:text-sm text-slate-600 mb-6">Füllen Sie das Formular aus – wir melden uns umgehend bei Ihnen zurück:</p>

                        <form id="contact-page-form" action="{FORMSPREE_ACTION}" method="POST" class="space-y-4">
                            <input type="hidden" name="_subject" value="Neue Kontakt-Anfrage - wiener-dienst.at">
                            <input type="hidden" name="zielseite_keyword" value="Kontaktseite">
                            <input type="hidden" name="_next" value="{DOMAIN}/danke.html">

                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Ihr Name *</label>
                                    <input type="text" name="name" required placeholder="Vor- und Nachname"
                                           class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm">
                                </div>
                                <div>
                                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Telefonnummer *</label>
                                    <input type="tel" name="telefon" required placeholder="z.B. +43 660..."
                                           class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm">
                                </div>
                            </div>

                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">E-Mail-Adresse</label>
                                    <input type="email" name="email" placeholder="name@beispiel.at"
                                           class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm">
                                </div>
                                <div>
                                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">PLZ / Bezirk in Wien *</label>
                                    <input type="text" name="plz_bezirk" required placeholder="z.B. 1020 Wien"
                                           class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm">
                                </div>
                            </div>

                            <div>
                                <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Gewünschte Leistung *</label>
                                <select name="leistung" required
                                        class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm font-semibold bg-slate-50">
                                    <option value="Entrümpelung Wien" selected>Entrümpelung Wien</option>
                                    <option value="Wohnungentrümpelung Wien">Wohnungentrümpelung Wien</option>
                                    <option value="Gemeinde Wohnung Entrümpelung">Gemeinde Wohnung Entrümpelung</option>
                                    <option value="Verlassenschaften Wien">Verlassenschaften Wien (Wertausgleich)</option>
                                    <option value="Hausräumung Wien">Hausräumung Wien</option>
                                    <option value="Keller Entrümpelung">Keller Entrümpelung / Dachboden</option>
                                    <option value="Möbel abholen lassen">Möbel abholen lassen</option>
                                    <option value="Messie Entrümpelung">Messie Entrümpelung (Diskret)</option>
                                    <option value="Sonstige Räumung">Sonstige Räumung</option>
                                </select>
                            </div>

                            <div>
                                <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Ihre Nachricht / Objektangaben</label>
                                <textarea name="nachricht" rows="4" placeholder="Wohnungsgröße, Stockwerk, Lift vorhanden, Wunschtermin für Besichtigung..."
                                          class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:border-wienRed-600 focus:ring-2 focus:ring-wienRed-600/20 outline-none text-sm"></textarea>
                            </div>

                            <button type="submit"
                                    class="w-full bg-gradient-to-r from-wienRed-600 to-wienRed-700 hover:from-wienRed-700 hover:to-wienRed-800 text-white font-black text-base py-4 rounded-xl shadow-lg transition flex items-center justify-center gap-2">
                                <span>ANFRAGE ABSENDEN</span>
                                <i class="fa-solid fa-paper-plane"></i>
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>

    {generate_floating_docks(current_kw="Kontakt")}
    {generate_footer(active_file="kontakt.html")}
    {generate_scripts()}

</body>
</html>
"""
    return page_html

def build_danke_page():
    """Generates the conversion tracking thank-you page."""
    page_html = f"""<!DOCTYPE html>
<html lang="de-AT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vielen Dank für Ihre Anfrage! | Wiener Dienst</title>
    <meta name="robots" content="noindex, follow">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <script>
        // Google Ads Conversion Event
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({{
            event: 'google_ads_lead_conversion',
            timestamp: new Date().toISOString()
        }});

        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Inter', 'sans-serif'] }},
                    colors: {{
                        wienRed: {{ 600: '#dc2626', 700: '#b91c1c' }},
                        navy: {{ 900: '#0f172a', 950: '#020617' }}
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-navy-950 text-white min-h-screen flex items-center justify-center p-4">

    <div class="max-w-2xl w-full bg-slate-900 border border-slate-800 rounded-3xl p-8 sm:p-12 text-center shadow-2xl space-y-6">
        <div class="w-20 h-20 rounded-full bg-emerald-500/20 border-2 border-emerald-400 text-emerald-400 flex items-center justify-center text-4xl mx-auto shadow-lg shadow-emerald-500/10">
            <i class="fa-solid fa-check"></i>
        </div>

        <h1 class="text-3xl sm:text-4xl font-black tracking-tight text-white">
            Vielen Dank! Ihre Anfrage ist erfolgreich bei uns eingegangen.
        </h1>

        <p class="text-slate-300 text-base sm:text-lg leading-relaxed">
            Unser Dispositions-Team von <strong>wiener-dienst.at</strong> prüft Ihre Angaben und ruft Sie in der Regel innerhalb der nächsten <strong>15 Minuten</strong> zurück, um alle Details oder einen kostenlosen Besichtigungstermin zu vereinbaren.
        </p>

        <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs sm:text-sm text-slate-300 text-left space-y-2">
            <div class="font-bold text-amber-300 flex items-center gap-2">
                <i class="fa-solid fa-camera"></i> Möchten Sie uns vorab Fotos senden?
            </div>
            <p>
                Klicken Sie einfach unten auf WhatsApp und senden Sie uns ein paar Bilder der zu räumenden Räumlichkeiten oder Möbelstücke – so erhalten Sie noch schneller eine präzise Kosteneinschätzung!
            </p>
        </div>

        <div class="flex flex-col sm:flex-row justify-center gap-4 pt-2">
            <a href="https://wa.me/{PHONE_TEL.replace('+', '')}?text=Hallo%20Wiener%20Dienst!%20Ich%20habe%20gerade%20das%20Formular%20ausgef%C3%BCllt%20und%20sende%20hier%20Fotos." target="_blank" rel="noopener"
               class="bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold px-6 py-4 rounded-2xl flex items-center justify-center gap-2 shadow-lg transition">
                <i class="fa-brands fa-whatsapp text-2xl"></i>
                <span>Fotos per WhatsApp senden</span>
            </a>
            <a href="tel:{PHONE_TEL}" class="bg-wienRed-600 hover:bg-wienRed-700 text-white font-extrabold px-6 py-4 rounded-2xl flex items-center justify-center gap-2 shadow-lg transition">
                <i class="fa-solid fa-phone"></i>
                <span>Direkt anrufen: {PHONE_DISPLAY}</span>
            </a>
        </div>

        <div class="pt-4 border-t border-slate-800">
            <a href="index.html" class="text-xs font-bold text-slate-400 hover:text-white underline transition">
                ← Zurück zur Startseite (wiener-dienst.at)
            </a>
        </div>
    </div>

</body>
</html>
"""
    return page_html

def build_impressum_page():
    """Generates the Austrian ECG / UGB compliant impressum.html."""
    page_html = f"""<!DOCTYPE html>
<html lang="de-AT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Impressum | Wiener Dienst – Entrümpelung &amp; Räumungsfirma Wien</title>
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{DOMAIN}/impressum.html">
    <!-- Wiener Wappen / Shield Favicon -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 115'%3E%3Cpath d='M8 6 H92 V48 C92 80 50 106 50 109 C50 106 8 80 8 48 Z' fill='%23ffffff'/%3E%3Cpath d='M12 10 H43 V46 H12 Z' fill='%23ff0000'/%3E%3Cpath d='M57 10 H88 V46 H57 Z' fill='%23ff0000'/%3E%3Cpath d='M12 58 H43 V100 C26 89 13 74 12 58 Z' fill='%23ff0000'/%3E%3Cpath d='M57 58 H88 C87 74 74 89 57 100 Z' fill='%23ff0000'/%3E%3C/svg%3E">


    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Inter', 'sans-serif'] }},
                    colors: {{
                        wienRed: {{ 50: '#fef2f2', 600: '#dc2626', 700: '#b91c1c' }},
                        navy: {{ 900: '#0f172a', 950: '#020617' }}
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-slate-50 text-slate-900 antialiased selection:bg-wienRed-600 selection:text-white">

    {generate_header(active_file="impressum.html")}
    {generate_quick_switcher(active_file="impressum.html")}

    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div class="bg-white rounded-3xl p-8 sm:p-12 border border-slate-200 shadow-sm space-y-6">
            <h1 class="text-3xl font-black text-navy-900">Impressum</h1>
            <p class="text-xs text-slate-500">Angaben gemäß § 5 E-Commerce-Gesetz (ECG), § 14 Unternehmensgesetzbuch (UGB) und Offenlegungspflicht gemäß § 25 Mediengesetz.</p>

            <div class="space-y-4 text-sm text-slate-700 leading-relaxed">
                <div>
                    <h2 class="font-bold text-navy-900 text-base">Medieninhaber &amp; Betreiber der Website:</h2>
                    <p class="mt-1">
                        <strong>Wiener Dienst</strong><br>
                        Gewerbliche Räumung, Entrümpelung, Nachlassverwertung &amp; Dienstleistungen in Wien und Niederösterreich
                    </p>
                </div>

                <div>
                    <h2 class="font-bold text-navy-900 text-base">Standort / Anschrift:</h2>
                    <p class="mt-1">
                        Wien, Österreich<br>
                        Tätigkeitsbereich: Sämtliche 23 Wiener Gemeindebezirke (1010–1230) und Umgebung
                    </p>
                </div>

                <div>
                    <h2 class="font-bold text-navy-900 text-base">Kontakt:</h2>
                    <p class="mt-1">
                        Telefon: <a href="tel:{PHONE_TEL}" class="text-wienRed-600 font-bold hover:underline">{PHONE_DISPLAY}</a><br>
                        WhatsApp: <a href="https://wa.me/{PHONE_TEL.replace('+', '')}" class="text-emerald-600 font-bold hover:underline">{PHONE_DISPLAY}</a><br>
                        E-Mail: <a href="mailto:{EMAIL}" class="text-wienRed-600 font-bold hover:underline">{EMAIL}</a><br>
                        Website: <a href="{DOMAIN}" class="text-wienRed-600 hover:underline">{DOMAIN}</a>
                    </p>
                </div>

                <div>
                    <h2 class="font-bold text-navy-900 text-base">Gewerberechtliche Vorschriften:</h2>
                    <p class="mt-1">
                        Berufsrecht: Gewerbeordnung (GewO 1994), abrufbar unter www.ris.bka.gv.at<br>
                        Aufsichtsbehörde: Magistrat der Stadt Wien / zuständige Gewerbebehörde<br>
                        Kammerzugehörigkeit: Wirtschaftskammer Wien (WKO)
                    </p>
                </div>

                <div>
                    <h2 class="font-bold text-navy-900 text-base">EU-Streitschlichtung:</h2>
                    <p class="mt-1">
                        Verbraucher haben die Möglichkeit, Beschwerden an die Online-Streitbeilegungsplattform der EU zu richten: 
                        <a href="https://ec.europa.eu/consumers/odr" target="_blank" rel="noopener" class="text-wienRed-600 underline">https://ec.europa.eu/consumers/odr</a>. 
                        Sie können allfällige Beschwerde auch an die oben angegebene E-Mail-Adresse richten.
                    </p>
                </div>

                <div>
                    <h2 class="font-bold text-navy-900 text-base">Haftung für Inhalte dieser Webseite:</h2>
                    <p class="mt-1">
                        Wir entwickeln die Inhalte dieser Webseite ständig weiter und bemühen uns um korrekte und aktuelle Informationen. Sollten Ihnen problematische oder rechtswidrige Inhalte auffallen, bitten wir Sie, uns umgehend zu kontaktieren.
                    </p>
                </div>
            </div>

            <div class="pt-6 border-t border-slate-200">
                <a href="index.html" class="text-sm font-bold text-wienRed-600 hover:underline">← Zurück zur Startseite</a>
            </div>
        </div>
    </div>

    {generate_floating_docks(current_kw="Impressum")}
    {generate_footer(active_file="impressum.html")}
    {generate_scripts()}

</body>
</html>
"""
    return page_html

def build_datenschutz_page():
    """Generates the Austrian DSGVO / TKG compliant datenschutz.html."""
    page_html = f"""<!DOCTYPE html>
<html lang="de-AT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Datenschutzerklärung (DSGVO) | Wiener Dienst</title>
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{DOMAIN}/datenschutz.html">
    <!-- Wiener Wappen / Shield Favicon -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 115'%3E%3Cpath d='M8 6 H92 V48 C92 80 50 106 50 109 C50 106 8 80 8 48 Z' fill='%23ffffff'/%3E%3Cpath d='M12 10 H43 V46 H12 Z' fill='%23ff0000'/%3E%3Cpath d='M57 10 H88 V46 H57 Z' fill='%23ff0000'/%3E%3Cpath d='M12 58 H43 V100 C26 89 13 74 12 58 Z' fill='%23ff0000'/%3E%3Cpath d='M57 58 H88 C87 74 74 89 57 100 Z' fill='%23ff0000'/%3E%3C/svg%3E">


    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Inter', 'sans-serif'] }},
                    colors: {{
                        wienRed: {{ 50: '#fef2f2', 600: '#dc2626', 700: '#b91c1c' }},
                        navy: {{ 900: '#0f172a', 950: '#020617' }}
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-slate-50 text-slate-900 antialiased selection:bg-wienRed-600 selection:text-white">

    {generate_header(active_file="datenschutz.html")}
    {generate_quick_switcher(active_file="datenschutz.html")}

    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div class="bg-white rounded-3xl p-8 sm:p-12 border border-slate-200 shadow-sm space-y-6">
            <h1 class="text-3xl font-black text-navy-900">Datenschutzerklärung (DSGVO)</h1>
            <p class="text-xs text-slate-500">Stand: November 2026 • Gültig für wiener-dienst.at nach EU-DSGVO und österreichischem TKG 2021.</p>

            <div class="space-y-4 text-sm text-slate-700 leading-relaxed">
                <div>
                    <h2 class="font-bold text-navy-900 text-base">1. Verantwortliche Stelle:</h2>
                    <p class="mt-1">
                        Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO):<br>
                        <strong>Wiener Dienst</strong><br>
                        Wien, Österreich<br>
                        E-Mail: <a href="mailto:{EMAIL}" class="text-wienRed-600 hover:underline">{EMAIL}</a><br>
                        Telefon: <a href="tel:{PHONE_TEL}" class="text-wienRed-600 hover:underline">{PHONE_DISPLAY}</a>
                    </p>
                </div>

                <div>
                    <h2 class="font-bold text-navy-900 text-base">2. Erhebung und Verarbeitung personenbezogener Daten:</h2>
                    <p class="mt-1">
                        Wir verarbeiten personenbezogene Daten, die Sie uns im Rahmen einer Kontaktaufnahme (über unser Online-Formular, per Telefon, WhatsApp oder E-Mail) freiwillig mitteilen (z.B. Name, Telefonnummer, E-Mail-Adresse, Wiener Bezirk/Adresse und Angaben zum Räumungsumfang).
                    </p>
                    <p class="mt-1">
                        <strong>Zweck:</strong> Die Datenverarbeitung erfolgt ausschließlich zur Bearbeitung Ihrer Anfrage, zur Erstellung eines verbindlichen Fixpreis-Angebots und zur Durchführung der vereinbarten Entrümpelungsdienstleistung (Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO – Vertragserfüllung bzw. vorvertragliche Maßnahmen).
                    </p>
                </div>

                <div>
                    <h2 class="font-bold text-navy-900 text-base">3. Kontaktaufnahme über Formspree:</h2>
                    <p class="mt-1">
                        Für die technische Weiterleitung unserer Kontaktformulare nutzen wir den Dienst <strong>Formspree</strong> (Formspree Inc., USA). Wenn Sie ein Formular absenden, werden die eingegebenen Daten über eine verschlüsselte SSL-Verbindung an die Server von Formspree übertragen und per E-Mail an uns weitergeleitet. Die Daten werden ausschließlich für den Kontaktzweck verarbeitet.
                    </p>
                </div>

                <div>
                    <h2 class="font-bold text-navy-900 text-base">4. WhatsApp Business:</h2>
                    <p class="mt-1">
                        Wenn Sie uns freiwillig per WhatsApp kontaktieren (z.B. zur Übermittlung von Fotos für eine Kostenschätzung), erfolgt die Datenverarbeitung über WhatsApp Ireland Limited. Wir nutzen die Daten ausschließlich zur Angebotserstellung und löschen Konversationen nach Abschluss des Auftrags.
                    </p>
                </div>

                <div>
                    <h2 class="font-bold text-navy-900 text-base">5. Google Ads &amp; Conversion Tracking:</h2>
                    <p class="mt-1">
                        Zur statistischen Erfassung der Werbewirksamkeit nutzen wir Google Ads Conversion Tracking (Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland). Dabei werden Interaktionen (wie das Absenden eines Anfrageformulars oder Anrufklicks) gemessen, um unsere Werbekampagnen zu optimieren. Es werden keine sensiblen Profildaten an unbefugte Dritte verkauft.
                    </p>
                </div>

                <div>
                    <h2 class="font-bold text-navy-900 text-base">6. Ihre Rechte als betroffene Person:</h2>
                    <p class="mt-1">
                        Ihnen stehen nach der DSGVO die Rechte auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch zu. Wenn Sie der Ansicht sind, dass die Verarbeitung Ihrer Daten gegen das Datenschutzrecht verstößt, können Sie sich bei der österreichischen Datenschutzbehörde beschweren:
                    </p>
                    <p class="mt-1">
                        <strong>Österreichische Datenschutzbehörde</strong><br>
                        Barichgasse 40-42, 1030 Wien<br>
                        Web: <a href="https://www.dsb.gv.at" target="_blank" rel="noopener" class="text-wienRed-600 underline">www.dsb.gv.at</a>
                    </p>
                </div>
            </div>

            <div class="pt-6 border-t border-slate-200">
                <a href="index.html" class="text-sm font-bold text-wienRed-600 hover:underline">← Zurück zur Startseite</a>
            </div>
        </div>
    </div>

    {generate_floating_docks(current_kw="Datenschutz")}
    {generate_footer(active_file="datenschutz.html")}
    {generate_scripts()}

</body>
</html>
"""
    return page_html

def build_sitemap():
    """Generates sitemap.xml covering all 27 pages."""
    today = datetime.now().strftime("%Y-%m-%d")
    urls = []
    
    # 1. Main Index
    urls.append(f"""  <url>
    <loc>{DOMAIN}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>""")

    # 2. 22 Keyword Landing Pages
    for item in KEYWORDS:
        urls.append(f"""  <url>
    <loc>{DOMAIN}/{item['file']}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>""")

    # 3. Conversion & Legal Pages
    legal_pages = [
        ("kontakt.html", "0.8"),
        ("impressum.html", "0.5"),
        ("datenschutz.html", "0.5"),
        ("danke.html", "0.3")
    ]
    for page, prio in legal_pages:
        urls.append(f"""  <url>
    <loc>{DOMAIN}/{page}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{prio}</priority>
  </url>""")

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{"\n".join(urls)}
</urlset>
"""
    return sitemap_content

def build_robots_txt():
    """Generates robots.txt linking to sitemap.xml."""
    return f"""User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""

def main():
    print("Starting site generation for wiener-dienst.at...")
    
    # 1. Generate index.html
    index_html = build_index_page()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
    print("Generated: index.html")

    # 2. Generate 22 Dedicated Keyword Landing Pages
    for item in KEYWORDS:
        page_html = build_keyword_page(item)
        with open(item["file"], "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f"Generated: {item['file']} ({item['kw']})")

    # 3. Generate 4 Conversion & Legal Pages
    with open("kontakt.html", "w", encoding="utf-8") as f:
        f.write(build_kontakt_page())
    print("Generated: kontakt.html")

    with open("danke.html", "w", encoding="utf-8") as f:
        f.write(build_danke_page())
    print("Generated: danke.html")

    with open("impressum.html", "w", encoding="utf-8") as f:
        f.write(build_impressum_page())
    print("Generated: impressum.html")

    with open("datenschutz.html", "w", encoding="utf-8") as f:
        f.write(build_datenschutz_page())
    print("Generated: datenschutz.html")

    # 4. Generate Technical SEO files
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(build_sitemap())
    print("Generated: sitemap.xml")

    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(build_robots_txt())
    print("Generated: robots.txt")

    print("\nSUCCESS: All 27 HTML pages + sitemap.xml + robots.txt generated successfully!")

if __name__ == "__main__":
    main()
