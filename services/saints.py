#!/usr/bin/env python
import sys
import urllib2
from   time import sleep
import json
from   datetime import datetime, date, time

saints_list =                                                           \
         [{'name' : 'Abel',                'day' : 5 , 'month' : 8},    \
          {'name' : 'Abella',              'day' : 5 , 'month' : 8},    \
          {'name' : 'Abraham',             'day' : 20, 'month' : 12},   \
          {'name' : 'Achille',             'day' : 12, 'month' : 5},    \
          {'name' : 'Ada',                 'day' : 4 , 'month' : 12},   \
          {'name' : 'Adelaide',            'day' : 16, 'month' : 12},   \
          {'name' : 'Adele',               'day' : 24, 'month' : 12},   \
          {'name' : 'Adeline',             'day' : 20, 'month' : 10},   \
          {'name' : 'Adelphe',             'day' : 11, 'month' : 9},    \
          {'name' : 'Adnette',             'day' : 4 , 'month' : 12},   \
          {'name' : 'Adolphe',             'day' : 30, 'month' : 6},    \
          {'name' : 'Adrien',              'day' : 8 , 'month' : 9},    \
          {'name' : 'Adrienne',            'day' : 8 , 'month' : 9},    \
          {'name' : 'Agathe',              'day' : 5 , 'month' : 2},    \
          {'name' : 'Aglaee',              'day' : 1 , 'month' : 11},   \
          {'name' : 'Agnes',               'day' : 21, 'month' : 1},    \
          {'name' : 'Aimable',             'day' : 18, 'month' : 10},   \
          {'name' : 'Aime',                'day' : 13, 'month' : 9},    \
          {'name' : 'Aimee',               'day' : 20, 'month' : 2},    \
          {'name' : 'Alain',               'day' : 9 , 'month' : 9},    \
          {'name' : 'Alban',               'day' : 22, 'month' : 6},    \
          {'name' : 'Albane',              'day' : 22, 'month' : 6},    \
          {'name' : 'Albe',                'day' : 22, 'month' : 6},    \
          {'name' : 'Alberic',             'day' : 15, 'month' : 11},   \
          {'name' : 'Albert',              'day' : 15, 'month' : 11},   \
          {'name' : 'Alberta',             'day' : 15, 'month' : 11},   \
          {'name' : 'Alberte',             'day' : 15, 'month' : 11},   \
          {'name' : 'Albin',               'day' : 1 , 'month' : 3},    \
          {'name' : 'Alda',                'day' : 26, 'month' : 4},    \
          {'name' : 'Aldo',                'day' : 99, 'month' : 99},   \
          {'name' : 'Alethe',              'day' : 4 , 'month' : 4},    \
          {'name' : 'Alette',              'day' : 4 , 'month' : 4},    \
          {'name' : 'Alex',                'day' : 22, 'month' : 4},    \
          {'name' : 'Alexandra',           'day' : 22, 'month' : 4},    \
          {'name' : 'Alexandre',           'day' : 22, 'month' : 4},    \
          {'name' : 'Alexane',             'day' : 17, 'month' : 2},    \
          {'name' : 'Alexia',              'day' : 9 , 'month' : 1},    \
          {'name' : 'Alexis',              'day' : 17, 'month' : 2},    \
          {'name' : 'Alfred',              'day' : 15, 'month' : 8},    \
          {'name' : 'Alice',               'day' : 16, 'month' : 12},   \
          {'name' : 'Alida',               'day' : 26, 'month' : 4},    \
          {'name' : 'Alienor',             'day' : 25, 'month' : 6},    \
          {'name' : 'Aline',               'day' : 20, 'month' : 10},   \
          {'name' : 'Alix',                'day' : 9 , 'month' : 1},    \
          {'name' : 'Alizee',              'day' : 16, 'month' : 12},   \
          {'name' : 'Allison',             'day' : 99, 'month' : 99},   \
          {'name' : 'Alois',               'day' : 21, 'month' : 6},    \
          {'name' : 'Alphonse',            'day' : 1 , 'month' : 8},    \
          {'name' : 'Amael',               'day' : 24, 'month' : 5},    \
          {'name' : 'Amalric',             'day' : 99, 'month' : 99},   \
          {'name' : 'Amand',               'day' : 6 , 'month' : 2},    \
          {'name' : 'Amandine',            'day' : 9 , 'month' : 7},    \
          {'name' : 'Amaury',              'day' : 15, 'month' : 1},    \
          {'name' : 'Ambroise',            'day' : 7 , 'month' : 12},   \
          {'name' : 'Ame',                 'day' : 13, 'month' : 9},    \
          {'name' : 'Amedee',              'day' : 30, 'month' : 3},    \
          {'name' : 'Amelie',              'day' : 19, 'month' : 9},    \
          {'name' : 'Amos',                'day' : 31, 'month' : 3},    \
          {'name' : 'Amour',               'day' : 9 , 'month' : 8},    \
          {'name' : 'Anais',               'day' : 26, 'month' : 7},    \
          {'name' : 'Anastasie',           'day' : 10, 'month' : 3},    \
          {'name' : 'Anatole',             'day' : 3 , 'month' : 7},    \
          {'name' : 'Andoche',             'day' : 24, 'month' : 9},    \
          {'name' : 'Andre',               'day' : 30, 'month' : 11},   \
          {'name' : 'Andree',              'day' : 30, 'month' : 11},   \
          {'name' : 'Andrea',              'day' : 30, 'month' : 11},   \
          {'name' : 'Ange',                'day' : 5 , 'month' : 5},    \
          {'name' : 'Angele',              'day' : 27, 'month' : 1},    \
          {'name' : 'Angeline',            'day' : 27, 'month' : 1},    \
          {'name' : 'Angelique',           'day' : 27, 'month' : 1},    \
          {'name' : 'Anicet',              'day' : 17, 'month' : 4},    \
          {'name' : 'Anna',                'day' : 26, 'month' : 7},    \
          {'name' : 'Annabelle',           'day' : 26, 'month' : 7},    \
          {'name' : 'Anne',                'day' : 26, 'month' : 7},    \
          {'name' : 'Annette',             'day' : 99, 'month' : 99},   \
          {'name' : 'Annaelle',            'day' : 26, 'month' : 7},    \
          {'name' : 'Anneliese',           'day' : 99, 'month' : 99},   \
          {'name' : 'Annick',              'day' : 26, 'month' : 7},    \
          {'name' : 'Annie',               'day' : 26, 'month' : 7},    \
          {'name' : 'Annonciade',          'day' : 25, 'month' : 3},    \
          {'name' : 'Anouchka',            'day' : 26, 'month' : 7},    \
          {'name' : 'Anouck',              'day' : 26, 'month' : 7},    \
          {'name' : 'Anselme',             'day' : 21, 'month' : 4},    \
          {'name' : 'Anthelme',            'day' : 26, 'month' : 6},    \
          {'name' : 'Anthony',             'day' : 17, 'month' : 1},    \
          {'name' : 'Antoine',             'day' : 5 , 'month' : 7},    \
          {'name' : 'Antoine (ab.)',       'day' : 99, 'month' : 99},   \
          {'name' : 'Antoine (de Padoue)', 'day' : 13, 'month' : 6},    \
          {'name' : 'Antoinette',          'day' : 28, 'month' : 2},    \
          {'name' : 'Antonin',             'day' : 2 , 'month' : 5},    \
          {'name' : 'Antony',              'day' : 17, 'month' : 1},    \
          {'name' : 'Apollinaire',         'day' : 12, 'month' : 9},    \
          {'name' : 'Apolline',            'day' : 9 , 'month' : 2},    \
          {'name' : 'Apollos',             'day' : 25, 'month' : 1},    \
          {'name' : 'Aquiline',            'day' : 99, 'month' : 99},   \
          {'name' : 'Arcadius',            'day' : 1 , 'month' : 8},    \
          {'name' : 'Arcady',              'day' : 1 , 'month' : 8},    \
          {'name' : 'Archibald',           'day' : 1 , 'month' : 11},   \
          {'name' : 'Ariane',              'day' : 18, 'month' : 9},    \
          {'name' : 'Aricie',              'day' : 99, 'month' : 99},   \
          {'name' : 'Arielle',             'day' : 1 , 'month' : 10},   \
          {'name' : 'Aristide',            'day' : 31, 'month' : 8},    \
          {'name' : 'Arlette',             'day' : 17, 'month' : 7},    \
          {'name' : 'Armance',             'day' : 8 , 'month' : 6},    \
          {'name' : 'Armand',              'day' : 8 , 'month' : 6},    \
          {'name' : 'Armande',             'day' : 8 , 'month' : 6},    \
          {'name' : 'Armel',               'day' : 16, 'month' : 8},    \
          {'name' : 'Armela',              'day' : 16, 'month' : 8},    \
          {'name' : 'Armelle',             'day' : 16, 'month' : 8},    \
          {'name' : 'Armistice',           'day' : 14, 'month' : 7},    \
          {'name' : 'Arnaud',              'day' : 10, 'month' : 2},    \
          {'name' : 'Arnold',              'day' : 14, 'month' : 8},    \
          {'name' : 'Arnould',             'day' : 18, 'month' : 7},    \
          {'name' : 'Arsene',              'day' : 19, 'month' : 7},    \
          {'name' : 'Arthur',              'day' : 15, 'month' : 11},   \
          {'name' : 'Ashley',              'day' : 99, 'month' : 99},   \
          {'name' : 'Astrid',              'day' : 27, 'month' : 11},   \
          {'name' : 'Athanase',            'day' : 2 , 'month' : 5},    \
          {'name' : 'Aubert',              'day' : 10, 'month' : 9},    \
          {'name' : 'Aubierge',            'day' : 7 , 'month' : 7},    \
          {'name' : 'Aubin',               'day' : 1 , 'month' : 3},    \
          {'name' : 'Aude',                'day' : 18, 'month' : 11},   \
          {'name' : 'Audrey',              'day' : 23, 'month' : 6},    \
          {'name' : 'Augusta',             'day' : 24, 'month' : 11},   \
          {'name' : 'Auguste',             'day' : 29, 'month' : 2},    \
          {'name' : 'Augustin',            'day' : 28, 'month' : 8},    \
          {'name' : 'Augustine',           'day' : 28, 'month' : 8},    \
          {'name' : 'Aure',                'day' : 4 , 'month' : 10},   \
          {'name' : 'Aurele',              'day' : 15, 'month' : 10},   \
          {'name' : 'Aurelie',             'day' : 15, 'month' : 10},   \
          {'name' : 'Aurelien',            'day' : 16, 'month' : 6},    \
          {'name' : 'Auriane',             'day' : 4 , 'month' : 10},   \
          {'name' : 'Aurianne',            'day' : 4 , 'month' : 10},   \
          {'name' : 'Aurore',              'day' : 13, 'month' : 12},   \
          {'name' : 'Avit',                'day' : 5 , 'month' : 2},    \
          {'name' : 'Axel',                'day' : 21, 'month' : 3},    \
          {'name' : 'Axelle',              'day' : 21, 'month' : 3},    \
          {'name' : 'Aymar',               'day' : 29, 'month' : 5},    \
          {'name' : 'Aymeric',             'day' : 4 , 'month' : 11},   \
          {'name' : 'Babette',             'day' : 17, 'month' : 11},   \
          {'name' : 'Babine',              'day' : 31, 'month' : 3},    \
          {'name' : 'Baptiste',            'day' : 24, 'month' : 6},    \
          {'name' : 'Barbara',             'day' : 4 , 'month' : 12},   \
          {'name' : 'Barbe',               'day' : 4 , 'month' : 12},   \
          {'name' : 'Barberine',           'day' : 4 , 'month' : 12},   \
          {'name' : 'Barnabe',             'day' : 11, 'month' : 6},    \
          {'name' : 'Barnard',             'day' : 23, 'month' : 1},    \
          {'name' : 'Barthelemy',          'day' : 24, 'month' : 8},    \
          {'name' : 'Bartolome',           'day' : 24, 'month' : 8},    \
          {'name' : 'Basile',              'day' : 2 , 'month' : 1},    \
          {'name' : 'Bastien',             'day' : 20, 'month' : 1},    \
          {'name' : 'Bathylle',            'day' : 30, 'month' : 1},    \
          {'name' : 'Baudouin',            'day' : 17, 'month' : 10},   \
          {'name' : 'Beatrice',            'day' : 13, 'month' : 2},    \
          {'name' : 'Benedicte',           'day' : 16, 'month' : 3},    \
          {'name' : 'Benjamin',            'day' : 31, 'month' : 3},    \
          {'name' : 'Benjamine',           'day' : 31, 'month' : 3},    \
          {'name' : 'Benoit',              'day' : 11, 'month' : 7},    \
          {'name' : 'Benoit-Joseph',       'day' : 16, 'month' : 4},    \
          {'name' : 'Berenger',            'day' : 26, 'month' : 5},    \
          {'name' : 'Berengere',           'day' : 26, 'month' : 5},    \
          {'name' : 'Berenice',            'day' : 4 , 'month' : 2},    \
          {'name' : 'Bernadette',          'day' : 18, 'month' : 2},    \
          {'name' : 'Bernard',             'day' : 20, 'month' : 8},    \
          {'name' : 'Bernard (de C.)',     'day' : 20, 'month' : 8},    \
          {'name' : 'Bernard (de M.)',     'day' : 15, 'month' : 6},    \
          {'name' : 'Bernardin',           'day' : 20, 'month' : 5},    \
          {'name' : 'Berthe',              'day' : 4 , 'month' : 7},    \
          {'name' : 'Bertille',            'day' : 16, 'month' : 10},   \
          {'name' : 'Bertin',              'day' : 16, 'month' : 10},   \
          {'name' : 'Bertrand',            'day' : 6 , 'month' : 9},    \
          {'name' : 'Bettina',             'day' : 17, 'month' : 11},   \
          {'name' : 'Betty',               'day' : 17, 'month' : 11},   \
          {'name' : 'Bienvenue',           'day' : 30, 'month' : 10},   \
          {'name' : 'Billy',               'day' : 10, 'month' : 1},    \
          {'name' : 'Blaise',              'day' : 3 , 'month' : 2},    \
          {'name' : 'Blanca',              'day' : 9 , 'month' : 7},    \
          {'name' : 'Blanche',             'day' : 3 , 'month' : 10},   \
          {'name' : 'Blandine',            'day' : 2 , 'month' : 6},    \
          {'name' : 'Bluette',             'day' : 5 , 'month' : 10},   \
          {'name' : 'Bonaventure',         'day' : 15, 'month' : 7},    \
          {'name' : 'Boniface',            'day' : 5 , 'month' : 6},    \
          {'name' : 'Boris',               'day' : 2 , 'month' : 5},    \
          {'name' : 'Briac',               'day' : 18, 'month' : 12},   \
          {'name' : 'Brice',               'day' : 13, 'month' : 11},   \
          {'name' : 'Brieuc',              'day' : 1 , 'month' : 5},    \
          {'name' : 'Brigitte',            'day' : 23, 'month' : 7},    \
          {'name' : 'Bruno',               'day' : 6 , 'month' : 10},   \
          {'name' : 'Calliste',            'day' : 14, 'month' : 10},   \
          {'name' : 'Calvin',              'day' : 99, 'month' : 99},   \
          {'name' : 'Camille(f)',          'day' : 14, 'month' : 7},    \
          {'name' : 'Camille(m)',          'day' : 14, 'month' : 7},    \
          {'name' : 'Candide',             'day' : 3 , 'month' : 10},   \
          {'name' : 'Candice',             'day' : 14, 'month' : 6},    \
          {'name' : 'Candy',               'day' : 99, 'month' : 99},   \
          {'name' : 'Capucine',            'day' : 5 , 'month' : 10},   \
          {'name' : 'Carine',              'day' : 7 , 'month' : 11},   \
          {'name' : 'Carl',                'day' : 4 , 'month' : 11},   \
          {'name' : 'Carlos',              'day' : 4 , 'month' : 11},   \
          {'name' : 'Carmen',              'day' : 16, 'month' : 7},    \
          {'name' : 'Carmine',             'day' : 16, 'month' : 7},    \
          {'name' : 'Carole',              'day' : 17, 'month' : 7},    \
          {'name' : 'Caroline',            'day' : 17, 'month' : 7},    \
          {'name' : 'Casimir',             'day' : 4 , 'month' : 3},    \
          {'name' : 'Cassandra',           'day' : 99, 'month' : 99},   \
          {'name' : 'Cassandre',           'day' : 99, 'month' : 99},   \
          {'name' : 'Catherine',           'day' : 25, 'month' : 11},   \
          {'name' : 'Catherine',           'day' : 29, 'month' : 4},    \
          {'name' : 'Cathy',               'day' : 29, 'month' : 4},    \
          {'name' : 'Cecile',              'day' : 22, 'month' : 11},   \
          {'name' : 'Cedric',              'day' : 7 , 'month' : 1},    \
          {'name' : 'Celeste(f)',          'day' : 14, 'month' : 10},   \
          {'name' : 'Celeste(m)',          'day' : 14, 'month' : 10},   \
          {'name' : 'Celestin',            'day' : 19, 'month' : 5},    \
          {'name' : 'Celia',               'day' : 22, 'month' : 11},   \
          {'name' : 'Celine',              'day' : 21, 'month' : 10},   \
          {'name' : 'Cesar',               'day' : 26, 'month' : 8},    \
          {'name' : 'Cesarine',            'day' : 12, 'month' : 1},    \
          {'name' : 'Chantal',             'day' : 12, 'month' : 12},   \
          {'name' : 'Charles',             'day' : 4 , 'month' : 11},   \
          {'name' : 'Charlette',           'day' : 4 , 'month' : 11},   \
          {'name' : 'Charley',             'day' : 4 , 'month' : 11},   \
          {'name' : 'Charlotte',           'day' : 17, 'month' : 7},    \
          {'name' : 'Charly',              'day' : 4 , 'month' : 11},   \
          {'name' : 'Chloe',               'day' : 17, 'month' : 7},    \
          {'name' : 'Christel',            'day' : 24, 'month' : 7},    \
          {'name' : 'Christian',           'day' : 12, 'month' : 11},   \
          {'name' : 'Christiane(Nino)',    'day' : 15, 'month' : 12},   \
          {'name' : 'Christine',           'day' : 24, 'month' : 7},    \
          {'name' : 'Christophe',          'day' : 21, 'month' : 8},    \
          {'name' : 'Clair',               'day' : 8 , 'month' : 11},   \
          {'name' : 'Claire',              'day' : 11, 'month' : 8},    \
          {'name' : 'Clara',               'day' : 11, 'month' : 8},    \
          {'name' : 'Clarence',            'day' : 12, 'month' : 8},    \
          {'name' : 'Clarisse',            'day' : 12, 'month' : 8},    \
          {'name' : 'Claude(H)',           'day' : 15, 'month' : 2},    \
          {'name' : 'Claude(F)',           'day' : 6 , 'month' : 6},    \
          {'name' : 'Claudette',           'day' : 6 , 'month' : 6},    \
          {'name' : 'Claudia',             'day' : 6 , 'month' : 6},    \
          {'name' : 'Claudine',            'day' : 6 , 'month' : 6},    \
          {'name' : 'Claudius',            'day' : 6 , 'month' : 6},    \
          {'name' : 'Clea',                'day' : 99, 'month' : 99},   \
          {'name' : 'Clelia',              'day' : 13, 'month' : 7},    \
          {'name' : 'Clemence',            'day' : 21, 'month' : 3},    \
          {'name' : 'Clement',             'day' : 23, 'month' : 11},   \
          {'name' : 'Clementine',          'day' : 23, 'month' : 11},   \
          {'name' : 'Clet',                'day' : 26, 'month' : 4},    \
          {'name' : 'Clotilde',            'day' : 4 , 'month' : 6},    \
          {'name' : 'Clovis',              'day' : 25, 'month' : 8},    \
          {'name' : 'Colette',             'day' : 6 , 'month' : 3},    \
          {'name' : 'Colin',               'day' : 6 , 'month' : 12},   \
          {'name' : 'Colombe',             'day' : 31, 'month' : 12},   \
          {'name' : 'COme',                'day' : 26, 'month' : 9},    \
          {'name' : 'Conrad',              'day' : 26, 'month' : 11},   \
          {'name' : 'Constance',           'day' : 8 , 'month' : 4},    \
          {'name' : 'Constant',            'day' : 23, 'month' : 9},    \
          {'name' : 'Constantin',          'day' : 21, 'month' : 5},    \
          {'name' : 'Cora',                'day' : 18, 'month' : 5},    \
          {'name' : 'Coralie',             'day' : 18, 'month' : 5},    \
          {'name' : 'Corentin',            'day' : 12, 'month' : 12},   \
          {'name' : 'Corinna',             'day' : 18, 'month' : 5},    \
          {'name' : 'Corinne',             'day' : 18, 'month' : 5},    \
          {'name' : 'Corneille',           'day' : 16, 'month' : 9},    \
          {'name' : 'Cyprien',             'day' : 16, 'month' : 9},    \
          {'name' : 'Cyriaque',            'day' : 8 , 'month' : 8},    \
          {'name' : 'Cyrille',             'day' : 18, 'month' : 3},    \
          {'name' : 'Dahlia',              'day' : 5 , 'month' : 10},   \
          {'name' : 'Daisy',               'day' : 16, 'month' : 11},   \
          {'name' : 'Damien',              'day' : 26, 'month' : 9},    \
          {'name' : 'Daniel',              'day' : 11, 'month' : 12},   \
          {'name' : 'Daniele',             'day' : 11, 'month' : 12},   \
          {'name' : 'Danielle',            'day' : 11, 'month' : 12},   \
          {'name' : 'Danitza',             'day' : 11, 'month' : 12},   \
          {'name' : 'Danny',               'day' : 11, 'month' : 12},   \
          {'name' : 'Daphnee',             'day' : 99, 'month' : 99},   \
          {'name' : 'Daria',               'day' : 25, 'month' : 10},   \
          {'name' : 'Darius',              'day' : 25, 'month' : 10},   \
          {'name' : 'David',               'day' : 29, 'month' : 12},   \
          {'name' : 'Davy',                'day' : 20, 'month' : 9},    \
          {'name' : 'Deborah',             'day' : 21, 'month' : 9},    \
          {'name' : 'Delphin',             'day' : 24, 'month' : 12},   \
          {'name' : 'Delphine',            'day' : 26, 'month' : 11},   \
          {'name' : 'Denis',               'day' : 9 , 'month' : 10},   \
          {'name' : 'Denise',              'day' : 15, 'month' : 5},    \
          {'name' : 'Desire',              'day' : 8 , 'month' : 5},    \
          {'name' : 'Diane',               'day' : 9 , 'month' : 6},    \
          {'name' : 'Didier',              'day' : 23, 'month' : 5},    \
          {'name' : 'Diego',               'day' : 13, 'month' : 11},   \
          {'name' : 'Dietrich',            'day' : 1 , 'month' : 7},    \
          {'name' : 'Dieudonne',           'day' : 10, 'month' : 8},    \
          {'name' : 'Dimitri',             'day' : 26, 'month' : 10},   \
          {'name' : 'Dirk',                'day' : 1 , 'month' : 7},    \
          {'name' : 'Dolores',             'day' : 15, 'month' : 9},    \
          {'name' : 'Dominique(H)',        'day' : 8 , 'month' : 8},    \
          {'name' : 'Dominique(F)',        'day' : 8 , 'month' : 8},    \
          {'name' : 'Domitille',           'day' : 7 , 'month' : 5},    \
          {'name' : 'Domnin',              'day' : 21, 'month' : 7},    \
          {'name' : 'Donald',              'day' : 15, 'month' : 7},    \
          {'name' : 'Donatien',            'day' : 24, 'month' : 5},    \
          {'name' : 'Donovan',             'day' : 99, 'month' : 99},   \
          {'name' : 'Dora',                'day' : 9 , 'month' : 11},   \
          {'name' : 'Dorian',              'day' : 25, 'month' : 10},   \
          {'name' : 'Dorine',              'day' : 9 , 'month' : 11},   \
          {'name' : 'Doris',               'day' : 6 , 'month' : 2},    \
          {'name' : 'Dorothee',            'day' : 6 , 'month' : 2},    \
          {'name' : 'Dylan',               'day' : 99, 'month' : 99},   \
          {'name' : 'Edgar',               'day' : 8 , 'month' : 7},    \
          {'name' : 'edith',               'day' : 16, 'month' : 9},    \
          {'name' : 'Edma',                'day' : 20, 'month' : 11},   \
          {'name' : 'Edmee',               'day' : 20, 'month' : 11},   \
          {'name' : 'Edmond',              'day' : 20, 'month' : 11},   \
          {'name' : 'edouard',             'day' : 5 , 'month' : 1},    \
          {'name' : 'edouardine',          'day' : 5 , 'month' : 1},    \
          {'name' : 'Edwige',              'day' : 16, 'month' : 10},   \
          {'name' : 'eleazar',             'day' : 1 , 'month' : 8},    \
          {'name' : 'eleonore',            'day' : 25, 'month' : 6},    \
          {'name' : 'Elfi',                'day' : 8 , 'month' : 12},   \
          {'name' : 'Elfried',             'day' : 8 , 'month' : 12},   \
          {'name' : 'eliane',              'day' : 4 , 'month' : 7},    \
          {'name' : 'elia',                'day' : 4 , 'month' : 7},    \
          {'name' : 'elie',                'day' : 20, 'month' : 7},    \
          {'name' : 'eliette',             'day' : 20, 'month' : 7},    \
          {'name' : 'eline',               'day' : 18, 'month' : 8},    \
          {'name' : 'elisabeth',           'day' : 17, 'month' : 11},   \
          {'name' : 'elise',               'day' : 17, 'month' : 11},   \
          {'name' : 'elisee',              'day' : 14, 'month' : 6},    \
          {'name' : 'Ella',                'day' : 1 , 'month' : 2},    \
          {'name' : 'Ellenita',            'day' : 1 , 'month' : 2},    \
          {'name' : 'elodie',              'day' : 22, 'month' : 10},   \
          {'name' : 'eloi',                'day' : 1 , 'month' : 12},   \
          {'name' : 'Elphege',             'day' : 12, 'month' : 3},    \
          {'name' : 'Elsa',                'day' : 17, 'month' : 11},   \
          {'name' : 'Elsy',                'day' : 17, 'month' : 11},   \
          {'name' : 'Elvire',              'day' : 16, 'month' : 7},    \
          {'name' : 'emeline',             'day' : 27, 'month' : 10},   \
          {'name' : 'emeric',              'day' : 4 , 'month' : 11},   \
          {'name' : 'emile',               'day' : 22, 'month' : 5},    \
          {'name' : 'emilie',              'day' : 19, 'month' : 9},    \
          {'name' : 'Emilio',              'day' : 22, 'month' : 5},    \
          {'name' : 'emilien',             'day' : 12, 'month' : 11},   \
          {'name' : 'emilienne',           'day' : 5 , 'month' : 1},    \
          {'name' : 'Emma',                'day' : 19, 'month' : 4},    \
          {'name' : 'Emmanuel',            'day' : 25, 'month' : 12},   \
          {'name' : 'Emmanuelle',          'day' : 25, 'month' : 12},   \
          {'name' : 'Enguerran',           'day' : 25, 'month' : 10},   \
          {'name' : 'Enrique',             'day' : 13, 'month' : 7},    \
          {'name' : 'ephrem',              'day' : 9 , 'month' : 6},    \
          {'name' : 'eric',                'day' : 18, 'month' : 5},    \
          {'name' : 'Erich',               'day' : 18, 'month' : 5},    \
          {'name' : 'Erika',               'day' : 18, 'month' : 5},    \
          {'name' : 'Ernest',              'day' : 7 , 'month' : 11},   \
          {'name' : 'Ernestine',           'day' : 7 , 'month' : 11},   \
          {'name' : 'Erwan',               'day' : 19, 'month' : 5},    \
          {'name' : 'Erwin',               'day' : 19, 'month' : 5},    \
          {'name' : 'Esperance',           'day' : 1 , 'month' : 8},    \
          {'name' : 'Estelle',             'day' : 11, 'month' : 5},    \
          {'name' : 'Esther',              'day' : 1 , 'month' : 7},    \
          {'name' : 'etienne',             'day' : 26, 'month' : 12},   \
          {'name' : 'etienne Harding',     'day' : 17, 'month' : 4},    \
          {'name' : 'etoile',              'day' : 11, 'month' : 5},    \
          {'name' : 'Eudes',               'day' : 19, 'month' : 8},    \
          {'name' : 'Eugene',              'day' : 13, 'month' : 7},    \
          {'name' : 'Eugenie',             'day' : 7 , 'month' : 2},    \
          {'name' : 'Eulalie',             'day' : 12, 'month' : 2},    \
          {'name' : 'Eurielle',            'day' : 1 , 'month' : 10},   \
          {'name' : 'Eusebe',              'day' : 2 , 'month' : 8},    \
          {'name' : 'Eva',                 'day' : 6 , 'month' : 9},    \
          {'name' : 'Evan',                'day' : 99, 'month' : 99},   \
          {'name' : 'Evariste',            'day' : 26, 'month' : 10},   \
          {'name' : 'Eve',                 'day' : 6 , 'month' : 9},    \
          {'name' : 'evelyne',             'day' : 6 , 'month' : 9},    \
          {'name' : 'evrard',              'day' : 14, 'month' : 8},    \
          {'name' : 'Fabien',              'day' : 20, 'month' : 1},    \
          {'name' : 'Fabienne',            'day' : 20, 'month' : 1},    \
          {'name' : 'Fabiola',             'day' : 27, 'month' : 12},   \
          {'name' : 'Fabrice',             'day' : 22, 'month' : 8},    \
          {'name' : 'Fanchon',             'day' : 9 , 'month' : 3},    \
          {'name' : 'Fanny',               'day' : 26, 'month' : 12},   \
          {'name' : 'Faustin',             'day' : 15, 'month' : 2},    \
          {'name' : 'Felicie',             'day' : 7 , 'month' : 3},    \
          {'name' : 'Felicien',            'day' : 9 , 'month' : 6},    \
          {'name' : 'Felicite',            'day' : 7 , 'month' : 3},    \
          {'name' : 'Felix',               'day' : 12, 'month' : 2},    \
          {'name' : 'Ferdinand',           'day' : 30, 'month' : 5},    \
          {'name' : 'Fernand',             'day' : 27, 'month' : 6},    \
          {'name' : 'Fernande',            'day' : 27, 'month' : 6},    \
          {'name' : 'Ferreol',             'day' : 16, 'month' : 6},    \
          {'name' : 'Fiacre',              'day' : 30, 'month' : 8},    \
          {'name' : 'Fidele',              'day' : 24, 'month' : 4},    \
          {'name' : 'Fiona',               'day' : 99, 'month' : 99},   \
          {'name' : 'Firmin',              'day' : 11, 'month' : 10},   \
          {'name' : 'Flamine',             'day' : 2 , 'month' : 5},    \
          {'name' : 'Flavie',              'day' : 7 , 'month' : 5},    \
          {'name' : 'Flavien',             'day' : 18, 'month' : 2},    \
          {'name' : 'Fleur',               'day' : 5 , 'month' : 10},   \
          {'name' : 'Flora',               'day' : 24, 'month' : 11},   \
          {'name' : 'Flore',               'day' : 24, 'month' : 11},   \
          {'name' : 'Florence',            'day' : 1 , 'month' : 12},   \
          {'name' : 'Florent',             'day' : 3 , 'month' : 1},    \
          {'name' : 'Florent',             'day' : 4 , 'month' : 7},    \
          {'name' : 'Florentin',           'day' : 24, 'month' : 10},   \
          {'name' : 'Florian',             'day' : 4 , 'month' : 5},    \
          {'name' : 'Fortunat',            'day' : 24, 'month' : 4},    \
          {'name' : 'France',              'day' : 4 , 'month' : 10},   \
          {'name' : 'Francelin',           'day' : 4 , 'month' : 10},   \
          {'name' : 'Franceline',          'day' : 4 , 'month' : 10},   \
          {'name' : 'Francette',           'day' : 4 , 'month' : 10},   \
          {'name' : 'Francine',            'day' : 4 , 'month' : 10},   \
          {'name' : 'Francis',             'day' : 4 , 'month' : 10},   \
          {'name' : 'Francisque',          'day' : 4 , 'month' : 10},   \
          {'name' : 'Franck',              'day' : 4 , 'month' : 10},   \
          {'name' : 'Francois',            'day' : 4 , 'month' : 10},   \
          {'name' : 'Francois(d\'Assises)','day' : 4 , 'month' : 10},   \
          {'name' : 'Francois(de Paul)',   'day' : 2 , 'month' : 4},    \
          {'name' : 'Francois(de Sales)',  'day' : 24, 'month' : 1},    \
          {'name' : 'Francois-Xavier',     'day' : 3 , 'month' : 12},   \
          {'name' : 'Francoise',           'day' : 9 , 'month' : 3},    \
          {'name' : 'Francoise-Xaviere',   'day' : 22, 'month' : 12},   \
          {'name' : 'Frankie',             'day' : 4 , 'month' : 10},   \
          {'name' : 'Franklin',            'day' : 4 , 'month' : 10},   \
          {'name' : 'Freddy',              'day' : 18, 'month' : 7},    \
          {'name' : 'Frederic',            'day' : 18, 'month' : 7},    \
          {'name' : 'Frederique',          'day' : 18, 'month' : 7},    \
          {'name' : 'Frida',               'day' : 18, 'month' : 7},    \
          {'name' : 'Fulbert',             'day' : 10, 'month' : 4},    \
          {'name' : 'Gabin',               'day' : 19, 'month' : 2},    \
          {'name' : 'Gabriel',             'day' : 19, 'month' : 9},    \
          {'name' : 'Gabrielle',           'day' : 29, 'month' : 9},    \
          {'name' : 'Gaby',                'day' : 29, 'month' : 9},    \
          {'name' : 'Gael',                'day' : 17, 'month' : 12},   \
          {'name' : 'Gaelle',              'day' : 17, 'month' : 12},   \
          {'name' : 'Gaetan',              'day' : 7 , 'month' : 8},    \
          {'name' : 'Gaetane',             'day' : 7 , 'month' : 8},    \
          {'name' : 'Gall',                'day' : 16, 'month' : 10},   \
          {'name' : 'Garry',               'day' : 99, 'month' : 99},   \
          {'name' : 'Gaspard',             'day' : 28, 'month' : 12},   \
          {'name' : 'Gaston',              'day' : 6 , 'month' : 2},    \
          {'name' : 'Gatien',              'day' : 18, 'month' : 12},   \
          {'name' : 'Gaud',                'day' : 29, 'month' : 7},    \
          {'name' : 'Gautier',             'day' : 9 , 'month' : 4},    \
          {'name' : 'Gelase',              'day' : 21, 'month' : 11},   \
          {'name' : 'Genevieve',           'day' : 3 , 'month' : 1},    \
          {'name' : 'Genn',                'day' : 18, 'month' : 10},   \
          {'name' : 'Geoffrey',            'day' : 8 , 'month' : 11},   \
          {'name' : 'Geoffroy',            'day' : 8 , 'month' : 11},   \
          {'name' : 'Georges',             'day' : 23, 'month' : 4},    \
          {'name' : 'Georgette',           'day' : 23, 'month' : 4},    \
          {'name' : 'Georgine',            'day' : 23, 'month' : 4},    \
          {'name' : 'Gerald',              'day' : 5 , 'month' : 12},   \
          {'name' : 'Geraldine',           'day' : 5 , 'month' : 12},   \
          {'name' : 'Gerard',              'day' : 3 , 'month' : 10},   \
          {'name' : 'Geraud',              'day' : 13, 'month' : 10},   \
          {'name' : 'Germain(d\'A.)',      'day' : 31, 'month' : 7},    \
          {'name' : 'Germain(de P.)',      'day' : 28, 'month' : 5},    \
          {'name' : 'Germaine',            'day' : 15, 'month' : 6},    \
          {'name' : 'Geronima',            'day' : 30, 'month' : 9},    \
          {'name' : 'Gertrude',            'day' : 16, 'month' : 11},   \
          {'name' : 'Gervais',             'day' : 19, 'month' : 6},    \
          {'name' : 'Gervaise',            'day' : 19, 'month' : 6},    \
          {'name' : 'Gery',                'day' : 11, 'month' : 8},    \
          {'name' : 'Ghislain',            'day' : 10, 'month' : 10},   \
          {'name' : 'Ghislaine',           'day' : 10, 'month' : 10},   \
          {'name' : 'Gilbert',             'day' : 4 , 'month' : 2},    \
          {'name' : 'Gilberte',            'day' : 11, 'month' : 8},    \
          {'name' : 'Gildas',              'day' : 29, 'month' : 1},    \
          {'name' : 'Gilles',              'day' : 1 , 'month' : 9},    \
          {'name' : 'Ginette',             'day' : 3 , 'month' : 1},    \
          {'name' : 'Gina',                'day' : 21, 'month' : 6},    \
          {'name' : 'Gino',                'day' : 21, 'month' : 6},    \
          {'name' : 'Giraud',              'day' : 20, 'month' : 4},    \
          {'name' : 'Gisane',              'day' : 99, 'month' : 99},   \
          {'name' : 'Gisele',              'day' : 7 , 'month' : 5},    \
          {'name' : 'Godefroy',            'day' : 8 , 'month' : 11},   \
          {'name' : 'Gontran',             'day' : 28, 'month' : 3},    \
          {'name' : 'Gonzague',            'day' : 21, 'month' : 6},    \
          {'name' : 'Goulven',             'day' : 1 , 'month' : 6},    \
          {'name' : 'Grace',               'day' : 21, 'month' : 8},    \
          {'name' : 'Gracieuse',           'day' : 21, 'month' : 8},    \
          {'name' : 'Gregoire',            'day' : 3 , 'month' : 9},    \
          {'name' : 'Gregory',             'day' : 3 , 'month' : 9},    \
          {'name' : 'Guennole',            'day' : 3 , 'month' : 3},    \
          {'name' : 'Guewen',              'day' : 18, 'month' : 10},   \
          {'name' : 'Guillaume',           'day' : 10, 'month' : 1},    \
          {'name' : 'Guillem',             'day' : 10, 'month' : 1},    \
          {'name' : 'Guillemette',         'day' : 10, 'month' : 1},    \
          {'name' : 'Gustave',             'day' : 7 , 'month' : 10},   \
          {'name' : 'Guy',                 'day' : 12, 'month' : 6},    \
          {'name' : 'Gwenael',             'day' : 3 , 'month' : 11},   \
          {'name' : 'Gwenaelle',           'day' : 3 , 'month' : 11},   \
          {'name' : 'Gwendoline',          'day' : 14, 'month' : 10},   \
          {'name' : 'Gwenola',             'day' : 3 , 'month' : 3},    \
          {'name' : 'Gwladys',             'day' : 29, 'month' : 3},    \
          {'name' : 'Habib',               'day' : 27, 'month' : 3},    \
          {'name' : 'Hadrien',             'day' : 8 , 'month' : 9},    \
          {'name' : 'Hans',                'day' : 24, 'month' : 6},    \
          {'name' : 'Harold',              'day' : 1 , 'month' : 11},   \
          {'name' : 'Harry',               'day' : 13, 'month' : 7},    \
          {'name' : 'Hedwige',             'day' : 16, 'month' : 10},   \
          {'name' : 'Helena',              'day' : 18, 'month' : 8},    \
          {'name' : 'Helene',              'day' : 18, 'month' : 8},    \
          {'name' : 'Heliena',             'day' : 18, 'month' : 8},    \
          {'name' : 'Helyette',            'day' : 20, 'month' : 7},    \
          {'name' : 'Henri',               'day' : 13, 'month' : 7},    \
          {'name' : 'Henriette',           'day' : 13, 'month' : 7},    \
          {'name' : 'Herbert',             'day' : 20, 'month' : 3},    \
          {'name' : 'Hermance',            'day' : 28, 'month' : 8},    \
          {'name' : 'Hermann',             'day' : 25, 'month' : 9},    \
          {'name' : 'Hermes',              'day' : 28, 'month' : 8},    \
          {'name' : 'Hermine',             'day' : 9 , 'month' : 7},    \
          {'name' : 'Herve',               'day' : 17, 'month' : 6},    \
          {'name' : 'Hilaire',             'day' : 13, 'month' : 1},    \
          {'name' : 'Hilda',               'day' : 17, 'month' : 11},   \
          {'name' : 'Hippolyte',           'day' : 13, 'month' : 8},    \
          {'name' : 'Honorat',             'day' : 16, 'month' : 1},    \
          {'name' : 'Honore',              'day' : 16, 'month' : 5},    \
          {'name' : 'Honorine',            'day' : 27, 'month' : 2},    \
          {'name' : 'Hortense',            'day' : 5 , 'month' : 10},   \
          {'name' : 'Hubert',              'day' : 3 , 'month' : 11},   \
          {'name' : 'Hugo',                'day' : 1 , 'month' : 4},    \
          {'name' : 'Hugues',              'day' : 1 , 'month' : 4},    \
          {'name' : 'Huguette',            'day' : 1 , 'month' : 4},    \
          {'name' : 'Hyacinthe',           'day' : 17, 'month' : 8},    \
          {'name' : 'Iadine',              'day' : 3 , 'month' : 2},    \
          {'name' : 'Ida',                 'day' : 13, 'month' : 4},    \
          {'name' : 'Ignace(de L.)',       'day' : 31, 'month' : 7},    \
          {'name' : 'Igor',                'day' : 5 , 'month' : 6},    \
          {'name' : 'Ilse',                'day' : 99, 'month' : 99},   \
          {'name' : 'Ilona',               'day' : 99, 'month' : 99},   \
          {'name' : 'Imre',                'day' : 4 , 'month' : 11},   \
          {'name' : 'Ines',                'day' : 10, 'month' : 9},    \
          {'name' : 'Ingrid',              'day' : 2 , 'month' : 9},    \
          {'name' : 'Innocent',            'day' : 28, 'month' : 12},   \
          {'name' : 'Irene',               'day' : 5 , 'month' : 4},    \
          {'name' : 'Irenee',              'day' : 28, 'month' : 6},    \
          {'name' : 'Iris',                'day' : 4 , 'month' : 9},    \
          {'name' : 'Irma',                'day' : 9 , 'month' : 7},    \
          {'name' : 'Irma(de S.)',         'day' : 4 , 'month' : 9},    \
          {'name' : 'Isaac',               'day' : 20, 'month' : 12},   \
          {'name' : 'Isabeau',             'day' : 99, 'month' : 99},   \
          {'name' : 'Isabelle',            'day' : 22, 'month' : 2},    \
          {'name' : 'Isaie',               'day' : 9 , 'month' : 5},    \
          {'name' : 'Isaline',             'day' : 99, 'month' : 99},   \
          {'name' : 'Isidore',             'day' : 4 , 'month' : 4},    \
          {'name' : 'Ivan',                'day' : 24, 'month' : 6},    \
          {'name' : 'Ivana',               'day' : 99, 'month' : 99},   \
          {'name' : 'J.-B. de la S',       'day' : 7 , 'month' : 4},    \
          {'name' : 'Jacinthe',            'day' : 30, 'month' : 1},    \
          {'name' : 'Jackie',              'day' : 8 , 'month' : 2},    \
          {'name' : 'Jacob',               'day' : 20, 'month' : 12},   \
          {'name' : 'Jacqueline',          'day' : 8 , 'month' : 2},    \
          {'name' : 'Jacques',             'day' : 25, 'month' : 7},    \
          {'name' : 'Jacques(Min.)',       'day' : 3 , 'month' : 5},    \
          {'name' : 'Jacquette',           'day' : 8 , 'month' : 2},    \
          {'name' : 'Jacquine',            'day' : 25, 'month' : 7},    \
          {'name' : 'Jacquotte',           'day' : 8 , 'month' : 2},    \
          {'name' : 'James',               'day' : 25, 'month' : 7},    \
          {'name' : 'Jane',                'day' : 30, 'month' : 5},    \
          {'name' : 'Jaouen',              'day' : 2 , 'month' : 3},    \
          {'name' : 'Jasmine',             'day' : 5 , 'month' : 10},   \
          {'name' : 'Jason',               'day' : 99, 'month' : 99},   \
          {'name' : 'Jarod',               'day' : 99, 'month' : 99},   \
          {'name' : 'Jean',                'day' : 27, 'month' : 12},   \
          {'name' : 'Jean(de Capistran)',  'day' : 23, 'month' : 10},   \
          {'name' : 'Jean-Baptiste',       'day' : 24, 'month' : 6},    \
          {'name' : 'Jean de Dieu',        'day' : 8 , 'month' : 3},    \
          {'name' : 'Jeanne',              'day' : 8 , 'month' : 5},    \
          {'name' : 'Jeanne',              'day' : 30, 'month' : 5},    \
          {'name' : 'Jeanne(de C.)',       'day' : 12, 'month' : 12},   \
          {'name' : 'Jeannette',           'day' : 30, 'month' : 5},    \
          {'name' : 'Jeannine',            'day' : 8 , 'month' : 5},    \
          {'name' : 'Jenny',               'day' : 8 , 'month' : 5},    \
          {'name' : 'Jeremie',             'day' : 1 , 'month' : 5},    \
          {'name' : 'JerOme',              'day' : 30, 'month' : 9},    \
          {'name' : 'Jessica',             'day' : 4 , 'month' : 11},   \
          {'name' : 'Jessy',               'day' : 4 , 'month' : 11},   \
          {'name' : 'Jim',                 'day' : 25, 'month' : 7},    \
          {'name' : 'Joachim',             'day' : 26, 'month' : 7},    \
          {'name' : 'Jocelyne',            'day' : 13, 'month' : 12},   \
          {'name' : 'Joel',                'day' : 13, 'month' : 7},    \
          {'name' : 'Joelle',              'day' : 13, 'month' : 7},    \
          {'name' : 'Joevin',              'day' : 2 , 'month' : 3},    \
          {'name' : 'Johanne',             'day' : 30, 'month' : 5},    \
          {'name' : 'John',                'day' : 24, 'month' : 7},    \
          {'name' : 'Johnatan',            'day' : 99, 'month' : 99},   \
          {'name' : 'Johnny',              'day' : 24, 'month' : 7},    \
          {'name' : 'Jordanne',            'day' : 13, 'month' : 2},    \
          {'name' : 'Joris',               'day' : 26, 'month' : 7},    \
          {'name' : 'Jose',                'day' : 19, 'month' : 3},    \
          {'name' : 'Joseph',              'day' : 19, 'month' : 3},    \
          {'name' : 'Josephine',           'day' : 19, 'month' : 3},    \
          {'name' : 'Josette',             'day' : 19, 'month' : 3},    \
          {'name' : 'Josiane',             'day' : 19, 'month' : 3},    \
          {'name' : 'Josselin',            'day' : 13, 'month' : 12},   \
          {'name' : 'Josseline',           'day' : 13, 'month' : 12},   \
          {'name' : 'Josue',               'day' : 1 , 'month' : 9},    \
          {'name' : 'Juanita',             'day' : 8 , 'month' : 5},    \
          {'name' : 'Jude',                'day' : 28, 'month' : 10},   \
          {'name' : 'Judicael',            'day' : 17, 'month' : 12},   \
          {'name' : 'Judith',              'day' : 5 , 'month' : 5},    \
          {'name' : 'Jules',               'day' : 12, 'month' : 4},    \
          {'name' : 'Julianne',            'day' : 99, 'month' : 99},   \
          {'name' : 'Julie',               'day' : 8 , 'month' : 4},    \
          {'name' : 'Julien',              'day' : 2 , 'month' : 8},    \
          {'name' : 'Julienne',            'day' : 16, 'month' : 2},    \
          {'name' : 'Juliette',            'day' : 30, 'month' : 7},    \
          {'name' : 'Juste',               'day' : 14, 'month' : 10},   \
          {'name' : 'Justin',              'day' : 1 , 'month' : 6},    \
          {'name' : 'Justine',             'day' : 12, 'month' : 3},    \
          {'name' : 'Juvenal',             'day' : 3 , 'month' : 5},    \
          {'name' : 'Karelle',             'day' : 7 , 'month' : 11},   \
          {'name' : 'Karen',               'day' : 7 , 'month' : 11},   \
          {'name' : 'Karina',              'day' : 7 , 'month' : 11},   \
          {'name' : 'Karine',              'day' : 7 , 'month' : 11},   \
          {'name' : 'Kassandra',           'day' : 99, 'month' : 99},   \
          {'name' : 'Katel',               'day' : 24, 'month' : 3},    \
          {'name' : 'Katia',               'day' : 25, 'month' : 11},   \
          {'name' : 'Katy',                'day' : 24, 'month' : 3},    \
          {'name' : 'Ketty',               'day' : 24, 'month' : 3},    \
          {'name' : 'Kevin',               'day' : 3 , 'month' : 6},    \
          {'name' : 'Killian',             'day' : 8 , 'month' : 7},    \
          {'name' : 'Kurt',                'day' : 26, 'month' : 11},   \
          {'name' : 'L\'Annonciation',     'day' : 25, 'month' : 3},    \
          {'name' : 'Laetitia',            'day' : 18, 'month' : 8},    \
          {'name' : 'Lambert',             'day' : 17, 'month' : 9},    \
          {'name' : 'Landry',              'day' : 10, 'month' : 6},    \
          {'name' : 'Lara',                'day' : 26, 'month' : 3},    \
          {'name' : 'Larissa',             'day' : 26, 'month' : 3},    \
          {'name' : 'Laura',               'day' : 10, 'month' : 8},    \
          {'name' : 'Lauranne',            'day' : 10, 'month' : 8},    \
          {'name' : 'Laure',               'day' : 10, 'month' : 8},    \
          {'name' : 'Laurence',            'day' : 10, 'month' : 8},    \
          {'name' : 'Laurent',             'day' : 10, 'month' : 8},    \
          {'name' : 'Laurentine',          'day' : 10, 'month' : 8},    \
          {'name' : 'Laurette',            'day' : 10, 'month' : 8},    \
          {'name' : 'Lauriane',            'day' : 13, 'month' : 2},    \
          {'name' : 'Laurie',              'day' : 10, 'month' : 8},    \
          {'name' : 'Lazare',              'day' : 23, 'month' : 2},    \
          {'name' : 'Lea',                 'day' : 22, 'month' : 3},    \
          {'name' : 'Leger',               'day' : 2 , 'month' : 10},   \
          {'name' : 'Lelia',               'day' : 22, 'month' : 3},    \
          {'name' : 'Lena',                'day' : 18, 'month' : 8},    \
          {'name' : 'Lenaic',              'day' : 18, 'month' : 8},    \
          {'name' : 'Leo',                 'day' : 6 , 'month' : 11},   \
          {'name' : 'Leon',                'day' : 10, 'month' : 11},   \
          {'name' : 'Leonard',             'day' : 6 , 'month' : 11},   \
          {'name' : 'Leone',               'day' : 10, 'month' : 11},   \
          {'name' : 'Leonce',              'day' : 18, 'month' : 6},    \
          {'name' : 'Leonie',              'day' : 10, 'month' : 11},   \
          {'name' : 'Leonilde',            'day' : 10, 'month' : 11},   \
          {'name' : 'Leonore',             'day' : 99, 'month' : 99},   \
          {'name' : 'Leontine',            'day' : 10, 'month' : 11},   \
          {'name' : 'Leopold',             'day' : 15, 'month' : 11},   \
          {'name' : 'Leslie',              'day' : 17, 'month' : 11},   \
          {'name' : 'Lexane',              'day' : 99, 'month' : 99},   \
          {'name' : 'Lia',                 'day' : 22, 'month' : 3},    \
          {'name' : 'Lidwine',             'day' : 14, 'month' : 4},    \
          {'name' : 'Lila',                'day' : 22, 'month' : 3},    \
          {'name' : 'Lilian',              'day' : 4 , 'month' : 7},    \
          {'name' : 'Liliane',             'day' : 4 , 'month' : 7},    \
          {'name' : 'Lily',                'day' : 17, 'month' : 11},   \
          {'name' : 'Linda',               'day' : 28, 'month' : 8},    \
          {'name' : 'Line',                'day' : 20, 'month' : 10},   \
          {'name' : 'Lionel',              'day' : 10, 'month' : 11},   \
          {'name' : 'Lisa',                'day' : 17, 'month' : 11},   \
          {'name' : 'Lisbeth',             'day' : 17, 'month' : 11},   \
          {'name' : 'Lise',                'day' : 17, 'month' : 11},   \
          {'name' : 'Lisette',             'day' : 17, 'month' : 11},   \
          {'name' : 'Lizzie',              'day' : 17, 'month' : 11},   \
          {'name' : 'Logan',               'day' : 99, 'month' : 99},   \
          {'name' : 'Loic',                'day' : 25, 'month' : 8},    \
          {'name' : 'Lois',                'day' : 21, 'month' : 6},    \
          {'name' : 'Lola',                'day' : 15, 'month' : 9},    \
          {'name' : 'Lolita',              'day' : 15, 'month' : 9},    \
          {'name' : 'Lolve',               'day' : 99, 'month' : 99},   \
          {'name' : 'Loraine',             'day' : 30, 'month' : 5},    \
          {'name' : 'Lore',                'day' : 25, 'month' : 6},    \
          {'name' : 'Loreline',            'day' : 99, 'month' : 99},   \
          {'name' : 'Louis',               'day' : 25, 'month' : 8},    \
          {'name' : 'Louis(de G.)',        'day' : 21, 'month' : 6},    \
          {'name' : 'Louis-Marie',         'day' : 28, 'month' : 4},    \
          {'name' : 'Louise',              'day' : 15, 'month' : 3},    \
          {'name' : 'Loup',                'day' : 29, 'month' : 7},    \
          {'name' : 'Luana',               'day' : 99, 'month' : 99},   \
          {'name' : 'Luc',                 'day' : 18, 'month' : 10},   \
          {'name' : 'Lucas',               'day' : 18, 'month' : 10},   \
          {'name' : 'Luce',                'day' : 13, 'month' : 12},   \
          {'name' : 'Lucette',             'day' : 13, 'month' : 12},   \
          {'name' : 'Lucie',               'day' : 13, 'month' : 12},   \
          {'name' : 'Lucien',              'day' : 8 , 'month' : 1},    \
          {'name' : 'Lucienne',            'day' : 8 , 'month' : 1},    \
          {'name' : 'Lucille',             'day' : 16, 'month' : 2},    \
          {'name' : 'Lucrece',             'day' : 15, 'month' : 3},    \
          {'name' : 'Ludmilla',            'day' : 16, 'month' : 9},    \
          {'name' : 'Ludovic',             'day' : 25, 'month' : 8},    \
          {'name' : 'Ludwig',              'day' : 25, 'month' : 8},    \
          {'name' : 'Lydia',               'day' : 3 , 'month' : 8},    \
          {'name' : 'Lydie',               'day' : 3 , 'month' : 8},    \
          {'name' : 'Lydiane',             'day' : 3 , 'month' : 8},    \
          {'name' : 'Lynda',               'day' : 20, 'month' : 10},   \
          {'name' : 'Macrine',             'day' : 6 , 'month' : 7},    \
          {'name' : 'Maddy',               'day' : 22, 'month' : 7},    \
          {'name' : 'Madeleine',           'day' : 22, 'month' : 7},    \
          {'name' : 'Mael',                'day' : 24, 'month' : 5},    \
          {'name' : 'Maelle',              'day' : 24, 'month' : 5},    \
          {'name' : 'Maeva',               'day' : 99, 'month' : 99},   \
          {'name' : 'Magali',              'day' : 22, 'month' : 7},    \
          {'name' : 'Magalie',             'day' : 22, 'month' : 7},    \
          {'name' : 'Magaly',              'day' : 22, 'month' : 7},    \
          {'name' : 'Maggy',               'day' : 22, 'month' : 7},    \
          {'name' : 'Magloire',            'day' : 24, 'month' : 10},   \
          {'name' : 'Maite',               'day' : 7 , 'month' : 6},    \
          {'name' : 'Malo',                'day' : 15, 'month' : 11},   \
          {'name' : 'Manoel',              'day' : 25, 'month' : 12},   \
          {'name' : 'Manon',               'day' : 15, 'month' : 8},    \
          {'name' : 'Manuel',              'day' : 26, 'month' : 12},   \
          {'name' : 'Marc',                'day' : 25, 'month' : 4},    \
          {'name' : 'Marceau',             'day' : 16, 'month' : 1},    \
          {'name' : 'Marcel',              'day' : 16, 'month' : 1},    \
          {'name' : 'Marcelle',            'day' : 31, 'month' : 1},    \
          {'name' : 'Marcellin',           'day' : 6 , 'month' : 4},    \
          {'name' : 'Marcelline',          'day' : 17, 'month' : 7},    \
          {'name' : 'Marcien',             'day' : 25, 'month' : 8},    \
          {'name' : 'Margaux',             'day' : 16, 'month' : 11},   \
          {'name' : 'Margot',              'day' : 16, 'month' : 11},   \
          {'name' : 'Marguerite-M',        'day' : 16, 'month' : 11},   \
          {'name' : 'Marguerite',          'day' : 20, 'month' : 7},    \
          {'name' : 'Maria',               'day' : 15, 'month' : 8},    \
          {'name' : 'Mariam',              'day' : 15, 'month' : 8},    \
          {'name' : 'Marianne',            'day' : 9 , 'month' : 7},    \
          {'name' : 'Marie',               'day' : 1 , 'month' : 1},    \
          {'name' : 'Marie',               'day' : 15, 'month' : 8},    \
          {'name' : 'Marie-Eve',           'day' : 99, 'month' : 99},   \
          {'name' : 'Marie-France',        'day' : 99, 'month' : 99},   \
          {'name' : 'Marie-Josee',         'day' : 99, 'month' : 99},   \
          {'name' : 'Marie-Madeleine',     'day' : 22, 'month' : 7},    \
          {'name' : 'Marie-Line',          'day' : 18, 'month' : 9},    \
          {'name' : 'Marielle',            'day' : 15, 'month' : 8},    \
          {'name' : 'Marien',              'day' : 30, 'month' : 4},    \
          {'name' : 'Mariette',            'day' : 6 , 'month' : 7},    \
          {'name' : 'Marika',              'day' : 99, 'month' : 99},   \
          {'name' : 'Marilyne',            'day' : 15, 'month' : 8},    \
          {'name' : 'Marin',               'day' : 4 , 'month' : 9},    \
          {'name' : 'Marina',              'day' : 20, 'month' : 7},    \
          {'name' : 'Marine',              'day' : 20, 'month' : 7},    \
          {'name' : 'Marinette',           'day' : 20, 'month' : 7},    \
          {'name' : 'Mario',               'day' : 99, 'month' : 99},   \
          {'name' : 'Marion',              'day' : 15, 'month' : 8},    \
          {'name' : 'Marissa',             'day' : 99, 'month' : 99},   \
          {'name' : 'Marius',              'day' : 19, 'month' : 1},    \
          {'name' : 'Marjolaine',          'day' : 15, 'month' : 8},    \
          {'name' : 'Marjorie',            'day' : 20, 'month' : 7},    \
          {'name' : 'Marlene',             'day' : 15, 'month' : 8},    \
          {'name' : 'Marthe',              'day' : 29, 'month' : 7},    \
          {'name' : 'Martial',             'day' : 30, 'month' : 6},    \
          {'name' : 'Martin',              'day' : 11, 'month' : 11},   \
          {'name' : 'Martine',             'day' : 30, 'month' : 1},    \
          {'name' : 'Martinien',           'day' : 2 , 'month' : 7},    \
          {'name' : 'Mary',                'day' : 15, 'month' : 8},    \
          {'name' : 'Maryline',            'day' : 15, 'month' : 8},    \
          {'name' : 'Maryan',              'day' : 99, 'month' : 99},   \
          {'name' : 'Maryse',              'day' : 15, 'month' : 8},    \
          {'name' : 'Maryvonne',           'day' : 15, 'month' : 8},    \
          {'name' : 'Mateo',               'day' : 21, 'month' : 9},    \
          {'name' : 'Materne',             'day' : 14, 'month' : 9},    \
          {'name' : 'Mathias',             'day' : 14, 'month' : 5},    \
          {'name' : 'Mathilde',            'day' : 14, 'month' : 3},    \
          {'name' : 'Mathurin',            'day' : 1 , 'month' : 11},   \
          {'name' : 'Matthieu',            'day' : 21, 'month' : 9},    \
          {'name' : 'Maud',                'day' : 14, 'month' : 3},    \
          {'name' : 'Maude',               'day' : 14, 'month' : 3},    \
          {'name' : 'Maurice',             'day' : 22, 'month' : 9},    \
          {'name' : 'Mauricette',          'day' : 22, 'month' : 9},    \
          {'name' : 'Maxence',             'day' : 14, 'month' : 4},    \
          {'name' : 'Maxime',              'day' : 14, 'month' : 4},    \
          {'name' : 'Maximilien',          'day' : 12, 'month' : 3},    \
          {'name' : 'Maximilien Kolb',     'day' : 14, 'month' : 8},    \
          {'name' : 'Maximin',             'day' : 29, 'month' : 5},    \
          {'name' : 'Mayeul',              'day' : 11, 'month' : 5},    \
          {'name' : 'Maylis',              'day' : 99, 'month' : 99},   \
          {'name' : 'Medard',              'day' : 8 , 'month' : 6},    \
          {'name' : 'Megan',               'day' : 99, 'month' : 99},   \
          {'name' : 'Melaine',             'day' : 6 , 'month' : 1},    \
          {'name' : 'Melaine',             'day' : 26, 'month' : 1},    \
          {'name' : 'Melanie',             'day' : 26, 'month' : 1},    \
          {'name' : 'Melissa',             'day' : 99, 'month' : 99},   \
          {'name' : 'Melodie',             'day' : 99, 'month' : 99},   \
          {'name' : 'Melvin',              'day' : 99, 'month' : 99},   \
          {'name' : 'Melyna',              'day' : 99, 'month' : 99},   \
          {'name' : 'Meredith',            'day' : 99, 'month' : 99},   \
          {'name' : 'Meriadec',            'day' : 7 , 'month' : 6},    \
          {'name' : 'Meryl',               'day' : 99, 'month' : 99},   \
          {'name' : 'Michael',             'day' : 29, 'month' : 9},    \
          {'name' : 'Michel',              'day' : 29, 'month' : 9},    \
          {'name' : 'Michele',             'day' : 29, 'month' : 9},    \
          {'name' : 'Micheline',           'day' : 19, 'month' : 6},    \
          {'name' : 'Michelle',            'day' : 29, 'month' : 9},    \
          {'name' : 'Miguel',              'day' : 29, 'month' : 9},    \
          {'name' : 'Mikael',              'day' : 29, 'month' : 9},    \
          {'name' : 'Mike',                'day' : 29, 'month' : 9},    \
          {'name' : 'Mildred',             'day' : 13, 'month' : 7},    \
          {'name' : 'Milene',              'day' : 19, 'month' : 8},    \
          {'name' : 'Milo',                'day' : 99, 'month' : 99},   \
          {'name' : 'Miloud',              'day' : 22, 'month' : 5},    \
          {'name' : 'Mireille',            'day' : 15, 'month' : 8},    \
          {'name' : 'Miriam',              'day' : 15, 'month' : 8},    \
          {'name' : 'Modeste',             'day' : 24, 'month' : 2},    \
          {'name' : 'Moise',               'day' : 4 , 'month' : 9},    \
          {'name' : 'Monica',              'day' : 27, 'month' : 8},    \
          {'name' : 'Monique',             'day' : 27, 'month' : 8},    \
          {'name' : 'Morgane',             'day' : 8 , 'month' : 10},   \
          {'name' : 'Mortimer',            'day' : 99, 'month' : 99},   \
          {'name' : 'Morvan',              'day' : 22, 'month' : 9},    \
          {'name' : 'Moshe',               'day' : 4 , 'month' : 9},    \
          {'name' : 'Muguet',              'day' : 1 , 'month' : 5},    \
          {'name' : 'Muguette',            'day' : 1 , 'month' : 5},    \
          {'name' : 'Murielle',            'day' : 15, 'month' : 8},    \
          {'name' : 'Mylene',              'day' : 15, 'month' : 8},    \
          {'name' : 'Myriam',              'day' : 15, 'month' : 8},    \
          {'name' : 'Myrtille',            'day' : 5 , 'month' : 10},   \
          {'name' : 'Nadette',             'day' : 18, 'month' : 2},    \
          {'name' : 'Nadege',              'day' : 18, 'month' : 9},    \
          {'name' : 'Nadia',               'day' : 18, 'month' : 9},    \
          {'name' : 'Nadine',              'day' : 18, 'month' : 2},    \
          {'name' : 'Nahum',               'day' : 1 , 'month' : 12},   \
          {'name' : 'Nancy',               'day' : 26, 'month' : 7},    \
          {'name' : 'Narcisse',            'day' : 29, 'month' : 10},   \
          {'name' : 'Natacha',             'day' : 26, 'month' : 8},    \
          {'name' : 'Natalya',             'day' : 99, 'month' : 99},   \
          {'name' : 'Nathalie',            'day' : 27, 'month' : 7},    \
          {'name' : 'Nathan',              'day' : 24, 'month' : 8},    \
          {'name' : 'Nathanaelle',         'day' : 24, 'month' : 8},    \
          {'name' : 'Neil',                'day' : 99, 'month' : 99},   \
          {'name' : 'Nello',               'day' : 25, 'month' : 12},   \
          {'name' : 'Nelly',               'day' : 18, 'month' : 8},    \
          {'name' : 'Nestor',              'day' : 26, 'month' : 2},    \
          {'name' : 'Nicolas',             'day' : 6 , 'month' : 12},   \
          {'name' : 'Nicole',              'day' : 6 , 'month' : 3},    \
          {'name' : 'Nicoletta',           'day' : 6 , 'month' : 3},    \
          {'name' : 'Nikita',              'day' : 31, 'month' : 1},    \
          {'name' : 'Ninon',               'day' : 6 , 'month' : 12},   \
          {'name' : 'Nina',                'day' : 14, 'month' : 1},    \
          {'name' : 'Ninon',               'day' : 15, 'month' : 12},   \
          {'name' : 'Noe',                 'day' : 10, 'month' : 11},   \
          {'name' : 'Noel',                'day' : 25, 'month' : 12},   \
          {'name' : 'Noeline',             'day' : 99, 'month' : 99},   \
          {'name' : 'Noelle',              'day' : 25, 'month' : 12},   \
          {'name' : 'Noemie',              'day' : 21, 'month' : 8},    \
          {'name' : 'Nolwenn',             'day' : 6 , 'month' : 7},    \
          {'name' : 'Nora',                'day' : 25, 'month' : 6},    \
          {'name' : 'Norbert',             'day' : 6 , 'month' : 6},    \
          {'name' : 'Oceane',              'day' : 26, 'month' : 7},    \
          {'name' : 'Octave',              'day' : 20, 'month' : 11},   \
          {'name' : 'Octavie',             'day' : 20, 'month' : 11},   \
          {'name' : 'Octavien',            'day' : 6 , 'month' : 8},    \
          {'name' : 'Odette',              'day' : 20, 'month' : 4},    \
          {'name' : 'Odile',               'day' : 14, 'month' : 12},   \
          {'name' : 'Odilon',              'day' : 4 , 'month' : 1},    \
          {'name' : 'Olga',                'day' : 11, 'month' : 7},    \
          {'name' : 'Olive',               'day' : 5 , 'month' : 3},    \
          {'name' : 'Olivette',            'day' : 5 , 'month' : 3},    \
          {'name' : 'Olivia',              'day' : 5 , 'month' : 3},    \
          {'name' : 'Olivier',             'day' : 12, 'month' : 7},    \
          {'name' : 'Ombeline',            'day' : 21, 'month' : 8},    \
          {'name' : 'Omer',                'day' : 9 , 'month' : 9},    \
          {'name' : 'Ophelie',             'day' : 99, 'month' : 99},   \
          {'name' : 'Oriane',              'day' : 4 , 'month' : 10},   \
          {'name' : 'Orianne',             'day' : 4 , 'month' : 10},   \
          {'name' : 'Oscar',               'day' : 3 , 'month' : 2},    \
          {'name' : 'Oswald',              'day' : 5 , 'month' : 8},    \
          {'name' : 'Otmar',               'day' : 16, 'month' : 11},   \
          {'name' : 'Pablo',               'day' : 29, 'month' : 6},    \
          {'name' : 'Paco',                'day' : 24, 'month' : 1},    \
          {'name' : 'PacOme',              'day' : 9 , 'month' : 5},    \
          {'name' : 'Pamela',              'day' : 16, 'month' : 2},    \
          {'name' : 'Pamphile',            'day' : 16, 'month' : 2},    \
          {'name' : 'Paola',               'day' : 26, 'month' : 1},    \
          {'name' : 'Paquerette',          'day' : 5 , 'month' : 10},   \
          {'name' : 'Paquita',             'day' : 12, 'month' : 12},   \
          {'name' : 'Paquito',             'day' : 24, 'month' : 1},    \
          {'name' : 'Parfait',             'day' : 18, 'month' : 4},    \
          {'name' : 'Pascal',              'day' : 17, 'month' : 5},    \
          {'name' : 'Pascale',             'day' : 17, 'month' : 5},    \
          {'name' : 'Paterne',             'day' : 15, 'month' : 4},    \
          {'name' : 'Patrice',             'day' : 17, 'month' : 3},    \
          {'name' : 'Patricia',            'day' : 17, 'month' : 3},    \
          {'name' : 'Patrick',             'day' : 17, 'month' : 3},    \
          {'name' : 'Paul',                'day' : 29, 'month' : 6},    \
          {'name' : 'Paula',               'day' : 26, 'month' : 1},    \
          {'name' : 'Paule',               'day' : 26, 'month' : 1},    \
          {'name' : 'Paulette',            'day' : 26, 'month' : 1},    \
          {'name' : 'Paulin',              'day' : 11, 'month' : 1},    \
          {'name' : 'Pauline',             'day' : 26, 'month' : 1},    \
          {'name' : 'Peggy',               'day' : 8 , 'month' : 1},    \
          {'name' : 'Pelagie',             'day' : 8 , 'month' : 10},   \
          {'name' : 'Perlette',            'day' : 16, 'month' : 10},   \
          {'name' : 'Pernelle',            'day' : 31, 'month' : 5},    \
          {'name' : 'Peroline',            'day' : 31, 'month' : 5},    \
          {'name' : 'Perpetue',            'day' : 7 , 'month' : 3},    \
          {'name' : 'Perrette',            'day' : 31, 'month' : 5},    \
          {'name' : 'Perrine',             'day' : 31, 'month' : 5},    \
          {'name' : 'Perry',               'day' : 99, 'month' : 99},   \
          {'name' : 'Pervenche',           'day' : 5 , 'month' : 10},   \
          {'name' : 'Peter',               'day' : 29, 'month' : 6},    \
          {'name' : 'Philibert',           'day' : 20, 'month' : 8},    \
          {'name' : 'Philiberte',          'day' : 20, 'month' : 8},    \
          {'name' : 'Philippe',            'day' : 3 , 'month' : 5},    \
          {'name' : 'Philippine',          'day' : 3 , 'month' : 5},    \
          {'name' : 'Pierre',              'day' : 29, 'month' : 6},    \
          {'name' : 'Pierrette',           'day' : 29, 'month' : 6},    \
          {'name' : 'Pierrick',            'day' : 29, 'month' : 6},    \
          {'name' : 'Pietro',              'day' : 29, 'month' : 6},    \
          {'name' : 'Piotr',               'day' : 29, 'month' : 6},    \
          {'name' : 'Placie',              'day' : 5 , 'month' : 10},   \
          {'name' : 'Pol',                 'day' : 12, 'month' : 3},    \
          {'name' : 'Polycarpe',           'day' : 23, 'month' : 2},    \
          {'name' : 'Primael',             'day' : 15, 'month' : 5},    \
          {'name' : 'Prisca',              'day' : 18, 'month' : 1},    \
          {'name' : 'Priscille',           'day' : 16, 'month' : 1},    \
          {'name' : 'Privat',              'day' : 21, 'month' : 8},    \
          {'name' : 'Prosper',             'day' : 25, 'month' : 6},    \
          {'name' : 'Prudence',            'day' : 6 , 'month' : 5},    \
          {'name' : 'Quentin',             'day' : 31, 'month' : 10},   \
          {'name' : 'Quitterie',           'day' : 22, 'month' : 5},    \
          {'name' : 'Rabi',                'day' : 99, 'month' : 99},   \
          {'name' : 'Rachel',              'day' : 15, 'month' : 1},    \
          {'name' : 'Rachilde',            'day' : 23, 'month' : 11},   \
          {'name' : 'Radegonde',           'day' : 13, 'month' : 8},    \
          {'name' : 'Rainier',             'day' : 17, 'month' : 6},    \
          {'name' : 'Raissa',              'day' : 5 , 'month' : 9},    \
          {'name' : 'Ralph',               'day' : 21, 'month' : 6},    \
          {'name' : 'Raoul',               'day' : 7 , 'month' : 7},    \
          {'name' : 'Raphael',             'day' : 29, 'month' : 9},    \
          {'name' : 'Raphaelle',           'day' : 29, 'month' : 9},    \
          {'name' : 'Raymond',             'day' : 7 , 'month' : 1},    \
          {'name' : 'Raymonde',            'day' : 7 , 'month' : 1},    \
          {'name' : 'Rebecca',             'day' : 23, 'month' : 3},    \
          {'name' : 'Reginald',            'day' : 17, 'month' : 9},    \
          {'name' : 'Regine',              'day' : 23, 'month' : 10},   \
          {'name' : 'Regis',               'day' : 16, 'month' : 6},    \
          {'name' : 'Regnault',            'day' : 16, 'month' : 9},    \
          {'name' : 'Reine',               'day' : 7 , 'month' : 9},    \
          {'name' : 'Rejane',              'day' : 23, 'month' : 10},   \
          {'name' : 'Remi',                'day' : 15, 'month' : 1},    \
          {'name' : 'Renald',              'day' : 17, 'month' : 9},    \
          {'name' : 'Renaud',              'day' : 17, 'month' : 9},    \
          {'name' : 'Renauld',             'day' : 17, 'month' : 9},    \
          {'name' : 'Rene',                'day' : 19, 'month' : 10},   \
          {'name' : 'Renee',               'day' : 19, 'month' : 10},   \
          {'name' : 'Richard',             'day' : 3 , 'month' : 4},    \
          {'name' : 'Rita',                'day' : 22, 'month' : 5},    \
          {'name' : 'Robert',              'day' : 30, 'month' : 4},    \
          {'name' : 'Roberte',             'day' : 30, 'month' : 4},    \
          {'name' : 'Robin',               'day' : 30, 'month' : 4},    \
          {'name' : 'Roch',                'day' : 16, 'month' : 8},    \
          {'name' : 'Rodolphe',            'day' : 21, 'month' : 6},    \
          {'name' : 'Rodrigue',            'day' : 13, 'month' : 3},    \
          {'name' : 'Rogatien',            'day' : 24, 'month' : 5},    \
          {'name' : 'Roger',               'day' : 30, 'month' : 12},   \
          {'name' : 'Roland',              'day' : 15, 'month' : 9},    \
          {'name' : 'Rolande',             'day' : 13, 'month' : 5},    \
          {'name' : 'Romain',              'day' : 28, 'month' : 2},    \
          {'name' : 'Roman',               'day' : 99, 'month' : 99},   \
          {'name' : 'Romaric',             'day' : 10, 'month' : 12},   \
          {'name' : 'Romeo',               'day' : 25, 'month' : 2},    \
          {'name' : 'Romuald',             'day' : 19, 'month' : 6},    \
          {'name' : 'Ronald',              'day' : 17, 'month' : 9},    \
          {'name' : 'Ronan',               'day' : 1 , 'month' : 6},    \
          {'name' : 'Roparz',              'day' : 30, 'month' : 4},    \
          {'name' : 'Rosalie',             'day' : 4 , 'month' : 9},    \
          {'name' : 'Rosana',              'day' : 23, 'month' : 8},    \
          {'name' : 'Rose',                'day' : 23, 'month' : 8},    \
          {'name' : 'Roselyne',            'day' : 17, 'month' : 1},    \
          {'name' : 'Roseline',            'day' : 17, 'month' : 1},    \
          {'name' : 'Rosemonde',           'day' : 30, 'month' : 4},    \
          {'name' : 'Rosette',             'day' : 23, 'month' : 8},    \
          {'name' : 'Rosine',              'day' : 11, 'month' : 3},    \
          {'name' : 'Rosita',              'day' : 23, 'month' : 8},    \
          {'name' : 'Rosy',                'day' : 23, 'month' : 8},    \
          {'name' : 'Roxanne',             'day' : 99, 'month' : 99},   \
          {'name' : 'Rozenn',              'day' : 23, 'month' : 8},    \
          {'name' : 'Rudy',                'day' : 21, 'month' : 6},    \
          {'name' : 'Ruffin',              'day' : 14, 'month' : 6},    \
          {'name' : 'Sabine',              'day' : 29, 'month' : 8},    \
          {'name' : 'Sabrina',             'day' : 29, 'month' : 8},    \
          {'name' : 'Sacha',               'day' : 30, 'month' : 8},    \
          {'name' : 'Salomon',             'day' : 25, 'month' : 6},    \
          {'name' : 'Salvatore',           'day' : 18, 'month' : 3},    \
          {'name' : 'Samson',              'day' : 28, 'month' : 7},    \
          {'name' : 'Samuel',              'day' : 20, 'month' : 8},    \
          {'name' : 'Samy',                'day' : 20, 'month' : 8},    \
          {'name' : 'Sandie',              'day' : 2 , 'month' : 4},    \
          {'name' : 'Sandra',              'day' : 2 , 'month' : 4},    \
          {'name' : 'Sandrine',            'day' : 2 , 'month' : 4},    \
          {'name' : 'Sandy',               'day' : 2 , 'month' : 4},    \
          {'name' : 'Sara',                'day' : 9 , 'month' : 10},   \
          {'name' : 'Saturnin',            'day' : 20, 'month' : 11},   \
          {'name' : 'Sebastien',           'day' : 20, 'month' : 1},    \
          {'name' : 'Segolene',            'day' : 24, 'month' : 7},    \
          {'name' : 'Selma',               'day' : 21, 'month' : 4},    \
          {'name' : 'Seraphin',            'day' : 12, 'month' : 10},   \
          {'name' : 'Serge',               'day' : 7 , 'month' : 10},   \
          {'name' : 'Sergine',             'day' : 7 , 'month' : 10},   \
          {'name' : 'Servan',              'day' : 1 , 'month' : 7},    \
          {'name' : 'Servane',             'day' : 1 , 'month' : 7},    \
          {'name' : 'Severin',             'day' : 27, 'month' : 11},   \
          {'name' : 'Severine',            'day' : 27, 'month' : 11},   \
          {'name' : 'Sheila',              'day' : 22, 'month' : 11},   \
          {'name' : 'Sibille',             'day' : 9 , 'month' : 10},   \
          {'name' : 'Sidoine',             'day' : 14, 'month' : 11},   \
          {'name' : 'Sidonie',             'day' : 14, 'month' : 11},   \
          {'name' : 'Siegfried',           'day' : 22, 'month' : 8},    \
          {'name' : 'Sigolene',            'day' : 99, 'month' : 99},   \
          {'name' : 'Silvere',             'day' : 20, 'month' : 6},    \
          {'name' : 'Simeon',              'day' : 18, 'month' : 2},    \
          {'name' : 'Simon',               'day' : 28, 'month' : 10},   \
          {'name' : 'Simone',              'day' : 28, 'month' : 10},   \
          {'name' : 'Sofia',               'day' : 25, 'month' : 5},    \
          {'name' : 'Soizic',              'day' : 24, 'month' : 1},    \
          {'name' : 'Solal',               'day' : 99, 'month' : 99},   \
          {'name' : 'Solange',             'day' : 10, 'month' : 5},    \
          {'name' : 'Soledad',             'day' : 11, 'month' : 10},   \
          {'name' : 'Solenne',             'day' : 17, 'month' : 10},   \
          {'name' : 'Soline',              'day' : 17, 'month' : 10},   \
          {'name' : 'Sonia',               'day' : 18, 'month' : 9},    \
          {'name' : 'Sophie',              'day' : 25, 'month' : 5},    \
          {'name' : 'Sophien',             'day' : 99, 'month' : 99},   \
          {'name' : 'Stanislas',           'day' : 11, 'month' : 4},    \
          {'name' : 'Stella',              'day' : 11, 'month' : 5},    \
          {'name' : 'Stehane',             'day' : 26, 'month' : 12},   \
          {'name' : 'Stephanie',           'day' : 26, 'month' : 12},   \
          {'name' : 'Steve',               'day' : 26, 'month' : 12},   \
          {'name' : 'Suzanne',             'day' : 11, 'month' : 8},    \
          {'name' : 'Suzel',               'day' : 11, 'month' : 8},    \
          {'name' : 'Suzette',             'day' : 11, 'month' : 8},    \
          {'name' : 'Suzon',               'day' : 11, 'month' : 8},    \
          {'name' : 'Suzy',                'day' : 11, 'month' : 8},    \
          {'name' : 'Svetlana',            'day' : 20, 'month' : 3},    \
          {'name' : 'Sybil',               'day' : 9 , 'month' : 11},   \
          {'name' : 'Sylvain',             'day' : 4 , 'month' : 5},    \
          {'name' : 'Sylvaine',            'day' : 4 , 'month' : 5},    \
          {'name' : 'Sylvestre',           'day' : 31, 'month' : 12},   \
          {'name' : 'Sylvette',            'day' : 5 , 'month' : 11},   \
          {'name' : 'Sylvia',              'day' : 5 , 'month' : 11},   \
          {'name' : 'Sylviane',            'day' : 5 , 'month' : 11},   \
          {'name' : 'Sylvianne',           'day' : 5 , 'month' : 11},   \
          {'name' : 'Sylvie',              'day' : 5 , 'month' : 11},   \
          {'name' : 'Symphorien',          'day' : 22, 'month' : 8},    \
          {'name' : 'Tabatha',             'day' : 99, 'month' : 99},   \
          {'name' : 'Tabhita',             'day' : 99, 'month' : 99},   \
          {'name' : 'Tamara',              'day' : 1 , 'month' : 5},    \
          {'name' : 'Tanguy',              'day' : 19, 'month' : 11},   \
          {'name' : 'Tania',               'day' : 12, 'month' : 1},    \
          {'name' : 'Tara',                'day' : 99, 'month' : 99},   \
          {'name' : 'Tarsice',             'day' : 15, 'month' : 1},    \
          {'name' : 'Tatiana',             'day' : 12, 'month' : 1},    \
          {'name' : 'Tatienne',            'day' : 12, 'month' : 1},    \
          {'name' : 'Teddy',               'day' : 5 , 'month' : 1},    \
          {'name' : 'Teresa',              'day' : 15, 'month' : 10},   \
          {'name' : 'Tessa',               'day' : 17, 'month' : 12},   \
          {'name' : 'Thaddee',             'day' : 28, 'month' : 10},   \
          {'name' : 'Thecle',              'day' : 24, 'month' : 9},    \
          {'name' : 'Theodore',            'day' : 9 , 'month' : 11},   \
          {'name' : 'Theophane',           'day' : 2 , 'month' : 2},    \
          {'name' : 'Theophile',           'day' : 20, 'month' : 12},   \
          {'name' : 'Theotime',            'day' : 99, 'month' : 99},   \
          {'name' : 'Therese',             'day' : 1 , 'month' : 10},   \
          {'name' : 'Therese',             'day' : 15, 'month' : 10},   \
          {'name' : 'Thibaud',             'day' : 8 , 'month' : 7},    \
          {'name' : 'Thiebaud',            'day' : 8 , 'month' : 7},    \
          {'name' : 'Thierry',             'day' : 1 , 'month' : 7},    \
          {'name' : 'Thomas',              'day' : 3 , 'month' : 7},    \
          {'name' : 'Thomas (d\'Aquin)',   'day' : 28, 'month' : 1},    \
          {'name' : 'Tino',                'day' : 14, 'month' : 2},    \
          {'name' : 'Tino',                'day' : 21, 'month' : 5},    \
          {'name' : 'Timothee',            'day' : 99, 'month' : 99},   \
          {'name' : 'Tiphaine',            'day' : 6 , 'month' : 1},    \
          {'name' : 'Titouan',             'day' : 99, 'month' : 99},   \
          {'name' : 'Toussaint',           'day' : 1 , 'month' : 11},   \
          {'name' : 'Toussainte',          'day' : 1 , 'month' : 11},   \
          {'name' : 'Tristan',             'day' : 12, 'month' : 11},   \
          {'name' : 'Tudal',               'day' : 1 , 'month' : 12},   \
          {'name' : 'Tudi',                'day' : 9 , 'month' : 5},    \
          {'name' : 'Ugo',                 'day' : 1 , 'month' : 4},    \
          {'name' : 'Ulrich',              'day' : 10, 'month' : 7},    \
          {'name' : 'Urbain',              'day' : 19, 'month' : 12},   \
          {'name' : 'Urielle',             'day' : 1 , 'month' : 10},   \
          {'name' : 'Ursula',              'day' : 21, 'month' : 10},   \
          {'name' : 'Ursule',              'day' : 21, 'month' : 10},   \
          {'name' : 'Valentin',            'day' : 14, 'month' : 2},    \
          {'name' : 'Valentine',           'day' : 25, 'month' : 7},    \
          {'name' : 'Valere',              'day' : 14, 'month' : 6},    \
          {'name' : 'Valerie',             'day' : 28, 'month' : 4},    \
          {'name' : 'Valery',              'day' : 1 , 'month' : 4},    \
          {'name' : 'Vanessa',             'day' : 4 , 'month' : 2},    \
          {'name' : 'Vanina',              'day' : 4 , 'month' : 2},    \
          {'name' : 'Vassili',             'day' : 2 , 'month' : 1},    \
          {'name' : 'Venceslas',           'day' : 28, 'month' : 9},    \
          {'name' : 'Vera',                'day' : 18, 'month' : 9},    \
          {'name' : 'Verane',              'day' : 11, 'month' : 11},   \
          {'name' : 'Veronique',           'day' : 4 , 'month' : 2},    \
          {'name' : 'Vianney',             'day' : 4 , 'month' : 8},    \
          {'name' : 'Vickie',              'day' : 99, 'month' : 99},   \
          {'name' : 'Victoire',            'day' : 15, 'month' : 11},   \
          {'name' : 'Victor',              'day' : 21, 'month' : 7},    \
          {'name' : 'Victorien',           'day' : 23, 'month' : 3},    \
          {'name' : 'Vincent',             'day' : 22, 'month' : 1},    \
          {'name' : 'Vincent(de Paul)',    'day' : 27, 'month' : 9},    \
          {'name' : 'Vinciane',            'day' : 11, 'month' : 9},    \
          {'name' : 'Violaine',            'day' : 5 , 'month' : 10},   \
          {'name' : 'Violette',            'day' : 5 , 'month' : 10},   \
          {'name' : 'Virgile',             'day' : 10, 'month' : 10},   \
          {'name' : 'Virginie',            'day' : 7 , 'month' : 1},    \
          {'name' : 'Viridiana',           'day' : 1 , 'month' : 2},    \
          {'name' : 'Vital',               'day' : 4 , 'month' : 11},   \
          {'name' : 'Viviane',             'day' : 2 , 'month' : 12},   \
          {'name' : 'Vivien',              'day' : 10, 'month' : 3},    \
          {'name' : 'Vladimir',            'day' : 15, 'month' : 7},    \
          {'name' : 'Walter',              'day' : 9 , 'month' : 4},    \
          {'name' : 'Weena',               'day' : 16, 'month' : 5},    \
          {'name' : 'Wenceslas',           'day' : 28, 'month' : 9},    \
          {'name' : 'Wendy',               'day' : 99, 'month' : 99},   \
          {'name' : 'Werner',              'day' : 19, 'month' : 4},    \
          {'name' : 'Wesley',              'day' : 99, 'month' : 99},   \
          {'name' : 'Wilfried',            'day' : 12, 'month' : 10},   \
          {'name' : 'William',             'day' : 10, 'month' : 1},    \
          {'name' : 'Willy',               'day' : 10, 'month' : 1},    \
          {'name' : 'Winnoc',              'day' : 6 , 'month' : 11},   \
          {'name' : 'Wladimir',            'day' : 15, 'month' : 7},    \
          {'name' : 'Wolfgang',            'day' : 31, 'month' : 10},   \
          {'name' : 'Wulfran',             'day' : 20, 'month' : 3},    \
          {'name' : 'Xavier',              'day' : 3 , 'month' : 12},   \
          {'name' : 'Xaviere',             'day' : 22, 'month' : 12},   \
          {'name' : 'Yann',                'day' : 27, 'month' : 12},   \
          {'name' : 'Yannick',             'day' : 27, 'month' : 12},   \
          {'name' : 'Yoann',               'day' : 24, 'month' : 6},    \
          {'name' : 'Yolaine',             'day' : 99, 'month' : 99},   \
          {'name' : 'Yolande',             'day' : 11, 'month' : 6},    \
          {'name' : 'Youri',               'day' : 23, 'month' : 4},    \
          {'name' : 'Ysaline',             'day' : 99, 'month' : 99},   \
          {'name' : 'Yvan',                'day' : 27, 'month' : 12},   \
          {'name' : 'Yves',                'day' : 19, 'month' : 5},    \
          {'name' : 'Yvette',              'day' : 13, 'month' : 1},    \
          {'name' : 'Yvon',                'day' : 19, 'month' : 5},    \
          {'name' : 'Yvonne',              'day' : 19, 'month' : 5},    \
          {'name' : 'Zacharie',            'day' : 5 , 'month' : 11},   \
          {'name' : 'Zelie',               'day' : 17, 'month' : 10},   \
          {'name' : 'Zephirin',            'day' : 20, 'month' : 12},   \
          {'name' : 'Zita',                'day' : 27, 'month' : 4},    \
          {'name' : 'Zoe',                 'day' : 2 , 'month' : 5}];

class Saints():

    def get_current(self):

        message = ""
        today_saints = [];
        count = 0

        for saint in saints_list:
            if saint['day'] == datetime.now().day and saint['month'] == datetime.now().month:
                today_saints.append(saint['name']);

        for count in range(len(today_saints)):
            if (count == 0):
                message = "Bonne fete aux " + today_saints[count]
            elif (count < len(today_saints) - 1):
                message = message + ', ' + today_saints[count]
            elif (count == len(today_saints) - 1):
                message = message + ' et ' + today_saints[count]
                
        return message

if __name__ == '__main__':
    s = Saints()
    print (s.get_current())
