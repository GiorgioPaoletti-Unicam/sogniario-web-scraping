<p align="center">
  <img src="https://forthebadge.com/images/badges/0-percent-optimized.svg"/>
  <img src="https://forthebadge.com/images/badges/made-with-python.svg"/>
  <img src="https://forthebadge.com/images/badges/powered-by-black-magic.svg"/><br><br>
    <b>Sogniario Web Scraping</b>, progetto realizzato in <b>Python</b> per il corso di laurea <b>L-31</b> presso <b>Unicam</b>, <i>nell'anno accademico 2020/2021</i>, realizzato dallo studente Giorgio Paoletti durante lo <b>Stage</b> interno all'Università.
    <br><br><b>
<a href="https://www.unicam.it/">• Unicam</a>
<a href="https://github.com/GiorgioPaoletti-Unicam/sogniario-web-scraping">• Sogniario Web Scraping</a>
</b></p>

# 📝 Panoramica e funzionalità <a name = "panoramica"></a>

**Il progetto nasce con l'obbiettivo di aumentare il quantitativo di dati raccolti dal progetto [Sogniario](https://github.com/GiorgioPaoletti-Unicam/sogniario) attraverso la tecnica del Web Scraping.**

Il progetto è composto da 3 componenti

- **Scraper**: Si occupa dell'estrazione di sogni da siti terzi e salvataggio su DataBase;
- **Analyzer**: Elabora i sogni e ne estrae le dipendenze tra i soggetti che compongono il testo del sogno. Inoltre salva tale elaborazione per un eventuale visulizzazione;
- **Visualizer**: Si occupa della visualizzazione di una lista dei sogni tramite una semplice pagina web che dia la possibilità di selezionare un sogno e visulizzarne graficamente le dipendenze.

# 🧰 Tecnologie utilizzate<a name = "tecno"></a>

Il progetto è stato scritto tramite l'ausilio del linguaggio **[Python](https://www.python.org/)**.
Per gestire la raccolta dei dati sui siti Web terzi si è utilizzato il **Web crawler [Scrapy](https://docs.scrapy.org/)** che è stato affiancato al **javascript rendering service [Splash](https://splash.readthedocs.io/)** che tramite script scritti in linguaggio **[Lua](https://www.lua.org/)** ha permesso la raccolta dati anche su siti in JavaScript. 

Per l'elaborazione del linguaggio naturale e la visualizzazione grafica delle dipendenze è stata utilizzata la libreria python **[SpaCy](https://spacy.io/)**.

Per quanto concerne la persistenza delle informazioni si è deciso di sfruttare i servizi offerti dal DBMS non relazionale MongoDB tramite la libreria pthon **[PyMongo](https://docs.mongodb.com/drivers/pymongo/)**.

Per la costruzione delle Api che permettono la visulizzazione della lista dei sogni raccolti e la relativa visualizzazione delle dipendenze si è sfruttato il micro web framework **[Flask](http://flask.palletsprojects.com/)**. 

# ⚙ Autori <a name = "autori"></a>

- [Giorgio Paoletti](https://github.com/GiorgioPaoletti-Unicam)
