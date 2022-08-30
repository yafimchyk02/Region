from django.urls import path
from home import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('home/', views.homepage, name='Главная'),
    path('info/', views.info_page, name='info'),
    path('kontacts/', views.kontacts_page, name='kontacts'),
    path('katalog_common/', views.katalog_common, name='Общий каталог'),
    path('k_plugam/', views.k_plugam, name='К плугам'),
    path('PPO9/', views.PPO8, name='ППО-8-40K(kverneland)'),
    path('k_boronam/', views.k_boronam, name='К боронам'),
    path('borona_bzss/', views.borona_bzss, name='БЗСС'),
    path('borona_bdt/', views.borona_bdt, name='БДТ-3, -7'),
    path('borona_diskopak/', views.borona_diskopak, name='ДИСКОПАК-6'),
    path('borona_bdn/', views.borona_bdn, name='БДН-3.0'),
    path('k_kultivatoram/', views.k_kultivatoram, name='К культиватрам'),
    path('kultiv_AKSH_6/', views.kultiv_AKSH_6, name='АКШ (-7.2, -3,6)'),
    path('kultiv_KH_5/', views.kultiv_KH_5, name='КЧ - 5.1 (-4,2)'),
    path('kultiv_KPS_6/', views.kultiv_KPS_6, name='КПС - 6'),

    path('kposevnim/', views.k_posevnim, name='К посевным агрегатам'),
    path('kposevnim/spy-6', views.posev_spy_6, name='СПУ-6'),
    path('kposevnim/skp-12', views.posev_skp_12, name='Optima Kverneland (СКП - 12)'),
    path('kposevnim/app-6a', views.posev_app_6a, name='АПП-6А'),
    path('kposevnim/app-6g', views.posev_app_6g, name='АПП - 6Г'),
    path('kposevnim/app-6d', views.posev_app_6d, name='АПП - 6Д'),
    path('kposevnim/app-6p', views.posev_app_6p, name='АПП - 6П'),
    path('kposevnim/appm-6', views.posev_appm_6, name='АППМ-6 "Берестье", MSC'),

    path('k_kosam/', views.k_kosilkam, name='К косилкам'),
    path('k_kosam/fc352', views.k_kosilkam_fc_352, name='FC 352 (KUHN, КПП-3.5 "Птичь")'),
    path('k_kosam/kdl3', views.k_kosilkam_kdl_3, name='КДЛ-3,14; -2,71 (Кроне EasyCut)'),
    path('k_kosam/disco', views.k_kosilkam_disco, name='Disco 3050, КДН-2.65 (CLAAS)'),
    path('k_kosam/kdn_210', views.k_kosilkam_kdn_210, name='КДН-210, КРН-2.1'),
    path('k_kosam/kmp_9', views.k_kosilkam_kmp_9, name='КМР-9, KDF-390 SaMASZ'),
    path('k_kosam/kpr_9', views.k_kosilkam_kpr_9, name='КПР-9 (KUHN) Гомсельмаш'),

    path('k_grabliam/', views.k_grabliam, name='К граблям'),
    path('k_grabliam/gvb_6', views.k_grabliam_gvb_6, name='ГВБ-6.2, ГВЦ-6.6 (Кроне Swadro)'),
    path('k_grabliam/liner', views.k_grabliam_liner, name='LINER-1550 Twin Profil (CLAAS)'),
    path('k_grabliam/bbp_7', views.k_grabliam_bbp_7, name='ВВР-7 (Кроне KWT)'),
    path('k_grabliam/volto', views.k_grabliam_volto, name='VOLTO 770 (Клаас)'),

    path('k_pres_pod/', views.k_pres_pod, name='К пресс-подборщикам'),
    path('prf180/', views.k_pres_pod, name='ПРФ-180'),

    path('k_korm_ubor/', views.k_korm_ubor, name='К кормоуборочным комбайнам'),
    path('k_korm_ubor/kpk_3000', views.k_korm_ubor_kpk_3000, name='КПК-3000, КГ-6 “Полесье”'),
    path('k_korm_ubor/kvk_800', views.k_korm_ubor_kvk_800, name='КВК-800 "ПАЛЕССЕ" FS80'),
    path('k_korm_ubor/kvk_8060', views.k_korm_ubor_kvk_8060, name='КВК-8060 "ПАЛЕССЕ " FS8060'),
    path('k_korm_ubor/jaguar', views.k_korm_ubor_jaguar, name='Claas Jaguar'),
    path('k_korm_ubor/john', views.k_korm_ubor_john, name='John Deere'),

    path('k_zern_ubor/', views.k_zern_ubor, name='К зерноуборочным комбайнам'),
    path('k_zern_ubor/lexion', views.k_zern_ubor_lexion, name='LEXION, MEGA, MEDION (Claas)'),

    path('k_kartosh_ubor/', views.k_kartosh_ubor, name='К картофелеуборочной технике'),
    path('k_kartosh_ubor/kth2b', views.KTH2B, name='КТН-2В'),

    path('k_rasbrasivat/', views.k_rasbrasivat, name='К разбрасывателям'),
    path('k_rasbrasivat/prt_10', views.k_rasbrasivat_prt_10, name='ПРТ-10 (7A)'),
    path('k_rasbrasivat/pmf_18', views.k_rasbrasivat_pmf_18, name='ПМФ-18, РОУМ-20'),

    path('k_traktoram/', views.k_traktoram, name='К тракторам'),
    path('k_traktoram/belarus', views.k_traktoram_belarus, name='Беларус 3022ДЦ.1'),
    path('k_traktoram/mtz', views.k_traktoram_mtz, name='МТЗ - 80,82; Беларус 1221'),

    path('metizi/', views.metizi_i_rasxod, name='Метизы и расходные материалы'),

    path(r'product/(?P<product_id>\w+)/', views.product, name='товар'),
    path(r'product_m/(?P<product_id>\w+)/', views.product_m, name='метизы'),

]
