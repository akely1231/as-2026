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
    ZAKAZNIK ||--o{ OBJEDNAVKA : "zadává"
    OBJEDNAVKA ||--|{ POLOZKA : "obsahuje"
    PRODUKT ||--o{ POLOZKA : "je v"

    ZAKAZNIK {
        int id PK
        string jmeno
        string prijmeni
        string mesto
        string email
    }
    OBJEDNAVKA {
        int cislo PK
        date datum
        int id_zakaznika FK
    }
    PRODUKT {
        int id PK
        string nazev
    }
    POLOZKA {
        int id_objednavky FK
    }
```
