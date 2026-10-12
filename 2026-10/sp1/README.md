SP1 kroužky
10

nemá zarovnané 
sloupce mezera mezi IT 2 
nema dostatecne velke sloupce


zaci: PK id_zaka
krouzky: PK id_krouzku
prihlasky: PK id_prihlasky, FK id_zaka → zaci, FK id_krouzku → krouzky

```mermaid
erDiagram
    ZAK {
        int id_zaka PK
        string jmeno
        string prijmeni
        string trida
    }

    KROUZEK {
        int id_krouzku PK
        string nazev
        string vedouci
        string den
        string cas
        string mistnost
        int cena_kc
    }

    PRIHLASKA {
        int id_prihlasky PK
        int id_zaka FK
        int id_krouzku FK
        string zaplaceno
    }

    ZAK ||--o{ PRIHLASKA : ma
    KROUZEK ||--o{ PRIHLASKA : obsahuje
```

```sql
SELECT nazev, cena
FROM krouzky
WHERE cena > 500;
```