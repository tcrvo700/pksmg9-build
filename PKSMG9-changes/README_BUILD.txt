PKSMG9 - PKSM with the Ultra Sun/Ultra Moon Gen 8/9 expansion (WORK IN PROGRESS, step 2 of 7)
==========================================================================================

NOT READY TO PLAY YET. Done so far: app name/ID, limits, ability list, Pokemon stats table.
Still to do: move type/PP data, item names, forms, Pokedex check (see chat).

New app identity (so your original PKSM is not touched)
  Name:          PKSMG9
  Unique ID:     0xEC190   (original PKSM: 0xEC100)  -> title ID 000400000EC19000
  Product code:  CTR-HB-PKG9
  Data folder:   /3ds/PKSMG9  (original uses /3ds/PKSM)
  Auto-update:   turned OFF (it would install the original PKSM)

How to use these files
  1. Get the full PKSM 10.4.2 source WITH its submodules:
       git clone --recursive https://github.com/FlagBrew/PKSM.git
       cd PKSM && git checkout 10.4.2
  2. Copy everything from this folder into that PKSM folder, say yes to overwrite.
     (the "core" folder here goes into PKSM/core)
  3. Install devkitPro with the 3ds-dev package, plus makerom and bannertool.
  4. In the PKSM folder run:  make
  5. The .cia is created as PKSMG9.cia. Install it with FBI.

Always test with a COPY of your save.
