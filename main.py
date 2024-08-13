import streamlit as st
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

ua=UserAgent()

headers={
    "user-agent": ua.random
}

takimlar=['Fenerbahçe', 'Galatasaray', 'Beşiktaş', 'Trabzonspor', 'Sivasspor', 'Başakşehir', 'Manchester United', 
       'Manchester City', 'Liverpool', 'Real Madrid', 'Barcelona', 'PSG', 'Bayern Munich', 'Juventus', 
       'Atletico Madrid', 'Borussia Dortmund', 'Chelsea', 'Arsenal', 'Inter Milan', 'AC Milan', 'Roma', 
       'Tottenham', 'Napoli', 'Athletic Bilbao', 'Sevilla']

takimlarIsim=['fenerbahce-istanbul-fb', 'galatasaray-istanbul-gs', 'besiktas-istanbul-bjk', 'trabzonspor', 'sivasspor', 
               'istanbul-basaksehir-fk-ibb', 'manchester-united-manutd', 'manchester-city-city', 'fc-liverpool-lfc', 
               'real-madrid-real', 'fc-barcelona-barca', 'fc-paris-saint-germain-psg', 'fc-bayern-munchen-fcb', 
               'juventus-turin-juve', 'atletico-madrid-atleti', 'borussia-dortmund-bvb', 'fc-chelsea-cfc', 'fc-arsenal-afc',
               'inter-mailand-inter', 'ac-mailand-milan', 'as-rom-roma', 'tottenham-hotspur-spurs', 'ssc-neapel-napoli',
               'athletic-bilbao-athlet', 'fc-sevilla-sevill']

takimlarKod=[36, 141, 114, 449, 2381, 6890, 985, 281, 31, 418, 131, 583, 27, 506, 13, 16, 631, 11, 46, 5, 12, 148, 6195, 621, 368]
ilkTakim=st.sidebar.selectbox("Takım Seçiniz",takimlar,takimlar.index('Fenerbahçe'))
ikinciTakim=st.sidebar.selectbox("Takım Seçiniz",takimlar,takimlar.index('Chelsea'))

buton=st.sidebar.button('Karşılaştır')

ilkTakimIsim=takimlarIsim[takimlar.index(ilkTakim)]
ikinciTakimIsim=takimlarIsim[takimlar.index(ikinciTakim)]

st.title(f'{ilkTakim} - {ikinciTakim} Karşılaştırma')

ilkTakimKod=takimlarKod[takimlar.index(ilkTakim)]
ikinciTakimKod=takimlarKod[takimlar.index(ikinciTakim)]

if buton:
    if ilkTakim==ikinciTakim:
        st.sidebar.error('Aynı takımı seçtiniz. Lütfen farklı takımlar seçiniz.')
    else:    
        url=f'https://www.transfermarkt.com.tr/vergleich-{ilkTakim}-{ikinciTakim}/vereinsvergleich/statistik/{ilkTakimKod}_{ikinciTakimKod}'

        page=requests.get(url=url,headers=headers)
        htmlPage=BeautifulSoup(page.content,"html.parser")

        data=htmlPage.find_all('div',attrs={'class':'vereinsname'})

        takimlar=[]
        for i in data:
            takimlar.append(i.text)

        ilkTakim=takimlar[0].replace('\n','')
        ikinciTakim=takimlar[1].replace('\n','')

        data=htmlPage.find_all('span',attrs={'class':'datenundfakten_bar'})

        takimBilgiler=[]
        for i in data:
            takimBilgiler.append(i.text)

        ilkTakimKadroDegeri=takimBilgiler[0]
        ikinciTakimKadroDegeri=takimBilgiler[1]
        ilkTakimPiyasaDegeri=takimBilgiler[2]
        ikinciTakimPiyasaDegeri=takimBilgiler[3]
        ilkTakimYasOrt=takimBilgiler[4]
        ikinciTakimYasOrt=takimBilgiler[5]
        ilkTakimMilliOyuncuSayisi=takimBilgiler[6]
        ikinciTakimMilliOyuncuSayisi=takimBilgiler[7]
        ilkTakimUmitMilliOyuncuSayisi=takimBilgiler[8]
        ikinciTakimUmitMilliOyuncuSayisi=takimBilgiler[9]
        ilkTakimLejyonerSayisi=takimBilgiler[10]
        ikinciTakimLejyonerSayisi=takimBilgiler[11]
        ilkTakimKulüpUyesiSayisi=takimBilgiler[12]
        ikinciTakimKulüpUyesiSayisi=takimBilgiler[13]

        st.write('')
        col1, col2 = st.columns(2)
        
        with col1:
            st.write('Takım Adı: ',ilkTakim)
            st.write('Kadro Değeri: ',ilkTakimKadroDegeri)
            st.write('Piyasa Değeri: ',ilkTakimPiyasaDegeri)
            st.write('Yaş Ortalaması: ',ilkTakimYasOrt)
            st.write('Milli Oyuncu Sayısı: ',ilkTakimMilliOyuncuSayisi)
            st.write('Ümit Milli Oyuncu Sayısı: ',ilkTakimUmitMilliOyuncuSayisi)
            st.write('Lejyoner Sayısı: ',ilkTakimLejyonerSayisi)
            st.write('Kulüp Üyesi Sayısı: ',ilkTakimKulüpUyesiSayisi)
        with col2:
            st.write('Takım Adı: ',ikinciTakim)
            st.write('Kadro Değeri: ',ikinciTakimKadroDegeri)
            st.write('Piyasa Değeri: ',ikinciTakimPiyasaDegeri)
            st.write('Yaş Ortalaması: ',ikinciTakimYasOrt)
            st.write('Milli Oyuncu Sayısı: ',ikinciTakimMilliOyuncuSayisi)
            st.write('Ümit Milli Oyuncu Sayısı: ',ikinciTakimUmitMilliOyuncuSayisi)
            st.write('Lejyoner Sayısı: ',ikinciTakimLejyonerSayisi)
            st.write('Kulüp Üyesi Sayısı: ',ikinciTakimKulüpUyesiSayisi)
        
