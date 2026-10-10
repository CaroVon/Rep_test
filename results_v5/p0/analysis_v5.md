# analysis_v5 (auto-generated)

convention: diff = a - b; lower is better for every metric; diff > 0 means b (adaptive) is better.

## metric_panel

| group         | run                          | pair(a-b)             | metric   |   diff_mean |        lo |        hi |   n |
|:--------------|:-----------------------------|:----------------------|:---------|------------:|----------:|----------:|----:|
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | euc_dmd - dua_dmd     | kl       |     0.16235 |   0.01915 |   0.31103 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | euc_dmd - dua_dmd     | kl_park  |     0.29029 |   0.21279 |   0.37294 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | euc_dmd - dua_dmd     | rd       |     0.12746 |   0.09589 |   0.16089 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | euc_dmd - dua_dmd     | cf_dev   |     0.11495 |   0.07777 |   0.16546 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | euc_dmd - dua_dmd     | kl_neu   |    -0.10327 |  -0.23684 |   0.05615 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | euc_dmd - dua_dmd     | kl       |     0.11344 |  -0.06632 |   0.30918 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | euc_dmd - dua_dmd     | kl_park  |     0.29947 |   0.20929 |   0.40681 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | euc_dmd - dua_dmd     | rd       |     0.12719 |   0.09922 |   0.16214 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | euc_dmd - dua_dmd     | cf_dev   |     0.15713 |   0.10763 |   0.21939 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | euc_dmd - dua_dmd     | kl_neu   |    -0.23305 |  -0.40411 |  -0.06531 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | euc_dmd - dua_dmd     | kl       |     0.24826 |   0.0511  |   0.48715 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | euc_dmd - dua_dmd     | kl_park  |     0.28075 |   0.19718 |   0.37075 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | euc_dmd - dua_dmd     | rd       |     0.11174 |   0.08184 |   0.14066 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | euc_dmd - dua_dmd     | cf_dev   |     0.11736 |   0.07835 |   0.16915 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | euc_dmd - dua_dmd     | kl_neu   |    -0.06783 |  -0.24365 |   0.09773 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | cau_unemb - dua_unemb | kl       |    -0.62962 |  -0.88896 |  -0.38286 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | cau_unemb - dua_unemb | kl_park  |     0.1589  |   0.09233 |   0.23382 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | cau_unemb - dua_unemb | rd       |     0.08497 |   0.0553  |   0.11783 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | cau_unemb - dua_unemb | cf_dev   |     0.06711 |   0.03382 |   0.10707 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | cau_unemb - dua_unemb | kl_neu   |    -0.70402 |  -0.96209 |  -0.45909 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | cau_unemb - dua_unemb | kl       |    -0.63936 |  -0.8431  |  -0.41625 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | cau_unemb - dua_unemb | kl_park  |     0.18145 |   0.10724 |   0.26872 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | cau_unemb - dua_unemb | rd       |     0.10319 |   0.07706 |   0.13629 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | cau_unemb - dua_unemb | cf_dev   |     0.10872 |   0.0543  |   0.17672 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | cau_unemb - dua_unemb | kl_neu   |    -0.79355 |  -1.01762 |  -0.56569 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | cau_unemb - dua_unemb | kl       |    -0.5804  |  -0.85059 |  -0.37998 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | cau_unemb - dua_unemb | kl_park  |     0.1546  |   0.09475 |   0.20827 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | cau_unemb - dua_unemb | rd       |     0.09379 |   0.06028 |   0.12731 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | cau_unemb - dua_unemb | cf_dev   |     0.08559 |   0.04439 |   0.13749 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | cau_unemb - dua_unemb | kl_neu   |    -0.69566 |  -0.94743 |  -0.5071  |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | frq_unemb - dua_unemb | kl       |    14.2801  |  13.1016  |  15.2816  |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | frq_unemb - dua_unemb | kl_park  |     1.50248 |   1.41382 |   1.58981 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | frq_unemb - dua_unemb | rd       |     0.12538 |   0.10266 |   0.14351 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | frq_unemb - dua_unemb | cf_dev   |     0.52676 |   0.47    |   0.57967 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | frq_unemb - dua_unemb | kl_neu   |     5.61904 |   4.6728  |   6.6298  |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | frq_unemb - dua_unemb | kl       |    15.6409  |  14.0003  |  17.4012  |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | frq_unemb - dua_unemb | kl_park  |     1.46237 |   1.37013 |   1.56826 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | frq_unemb - dua_unemb | rd       |     0.13075 |   0.11208 |   0.14783 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | frq_unemb - dua_unemb | cf_dev   |     0.54898 |   0.50563 |   0.59746 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | frq_unemb - dua_unemb | kl_neu   |     5.7681  |   5.07162 |   6.85059 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | frq_unemb - dua_unemb | kl       |     7.25771 |   5.8705  |   8.34443 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | frq_unemb - dua_unemb | kl_park  |     1.4741  |   1.37823 |   1.56154 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | frq_unemb - dua_unemb | rd       |     0.08325 |   0.06213 |   0.10522 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | frq_unemb - dua_unemb | cf_dev   |     0.51822 |   0.44971 |   0.58566 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | frq_unemb - dua_unemb | kl_neu   |     2.80875 |   1.7572  |   3.88438 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | cau_unemb - frq_unemb | kl       |   -14.9097  | -15.9053  | -13.711   |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | cau_unemb - frq_unemb | kl_park  |    -1.34358 |  -1.40706 |  -1.27452 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | cau_unemb - frq_unemb | rd       |    -0.04041 |  -0.07123 |  -0.00715 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | cau_unemb - frq_unemb | cf_dev   |    -0.45965 |  -0.51686 |  -0.40071 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | cau_unemb - frq_unemb | kl_neu   |    -6.32307 |  -7.21607 |  -5.4189  |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | cau_unemb - frq_unemb | kl       |   -16.2803  | -17.934   | -14.6453  |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | cau_unemb - frq_unemb | kl_park  |    -1.28092 |  -1.33804 |  -1.22257 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | cau_unemb - frq_unemb | rd       |    -0.02756 |  -0.05476 |   0.0061  |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | cau_unemb - frq_unemb | cf_dev   |    -0.44026 |  -0.48247 |  -0.39534 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | cau_unemb - frq_unemb | kl_neu   |    -6.56165 |  -7.39905 |  -5.93497 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | cau_unemb - frq_unemb | kl       |    -7.83811 |  -8.8525  |  -6.53273 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | cau_unemb - frq_unemb | kl_park  |    -1.31951 |  -1.39558 |  -1.23817 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | cau_unemb - frq_unemb | rd       |     0.01055 |  -0.02667 |   0.04186 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | cau_unemb - frq_unemb | cf_dev   |    -0.43263 |  -0.51432 |  -0.34881 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | cau_unemb - frq_unemb | kl_neu   |    -3.50441 |  -4.40723 |  -2.59066 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | frq_dmd - dua_dmd     | kl       |     1.45105 |   1.0377  |   1.97667 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | frq_dmd - dua_dmd     | kl_park  |     0.78412 |   0.63493 |   0.92984 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | frq_dmd - dua_dmd     | rd       |     0.1577  |   0.12811 |   0.19131 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | frq_dmd - dua_dmd     | cf_dev   |     0.3169  |   0.24799 |   0.38349 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | frq_dmd - dua_dmd     | kl_neu   |     0.58958 |   0.34858 |   0.88917 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | frq_dmd - dua_dmd     | kl       |     0.67378 |   0.44114 |   0.94442 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | frq_dmd - dua_dmd     | kl_park  |     0.56129 |   0.44351 |   0.69075 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | frq_dmd - dua_dmd     | rd       |     0.14981 |   0.1251  |   0.17664 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | frq_dmd - dua_dmd     | cf_dev   |     0.17286 |   0.13791 |   0.21346 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | frq_dmd - dua_dmd     | kl_neu   |    -0.07689 |  -0.25621 |   0.10389 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | frq_dmd - dua_dmd     | kl       |     6.73837 |   5.07503 |   8.31415 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | frq_dmd - dua_dmd     | kl_park  |     1.33122 |   1.15583 |   1.47097 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | frq_dmd - dua_dmd     | rd       |     0.12582 |   0.09677 |   0.15412 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | frq_dmd - dua_dmd     | cf_dev   |     0.47029 |   0.38966 |   0.55115 |  60 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | frq_dmd - dua_dmd     | kl_neu   |     2.65186 |   1.87563 |   3.50442 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | euc_dmd - dua_dmd     | kl       |    -0.80284 |  -1.06708 |  -0.5261  |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | euc_dmd - dua_dmd     | kl_park  |     0.64183 |   0.47437 |   0.80292 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | euc_dmd - dua_dmd     | rd       |     0.2683  |   0.20805 |   0.3261  |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | euc_dmd - dua_dmd     | cf_dev   |     0.10071 |   0.05809 |   0.15115 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | euc_dmd - dua_dmd     | kl_neu   |    -0.88161 |  -1.03798 |  -0.72429 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | euc_dmd - dua_dmd     | kl       |    -0.91145 |  -1.25394 |  -0.59725 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | euc_dmd - dua_dmd     | kl_park  |     0.72134 |   0.54881 |   0.90244 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | euc_dmd - dua_dmd     | rd       |     0.19326 |   0.13543 |   0.25774 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | euc_dmd - dua_dmd     | cf_dev   |     0.0732  |   0.03382 |   0.11885 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | euc_dmd - dua_dmd     | kl_neu   |    -1.01803 |  -1.19339 |  -0.84397 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | euc_dmd - dua_dmd     | kl       |    -0.75099 |  -1.0459  |  -0.46318 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | euc_dmd - dua_dmd     | kl_park  |     0.87684 |   0.69456 |   1.07415 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | euc_dmd - dua_dmd     | rd       |     0.26673 |   0.20651 |   0.32726 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | euc_dmd - dua_dmd     | cf_dev   |     0.12329 |   0.07252 |   0.17792 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | euc_dmd - dua_dmd     | kl_neu   |    -1.05975 |  -1.22092 |  -0.8988  |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | cau_unemb - dua_unemb | kl       |    -1.17025 |  -1.39293 |  -0.96488 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | cau_unemb - dua_unemb | kl_park  |     0.14836 |   0.07745 |   0.22895 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | cau_unemb - dua_unemb | rd       |     0.06856 |   0.0331  |   0.10847 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | cau_unemb - dua_unemb | cf_dev   |     0.13132 |   0.08487 |   0.17963 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | cau_unemb - dua_unemb | kl_neu   |    -1.17172 |  -1.37542 |  -0.97946 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | cau_unemb - dua_unemb | kl       |    -1.24094 |  -1.48131 |  -1.01044 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | cau_unemb - dua_unemb | kl_park  |     0.13129 |   0.05863 |   0.20703 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | cau_unemb - dua_unemb | rd       |     0.09483 |   0.04689 |   0.14403 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | cau_unemb - dua_unemb | cf_dev   |     0.10259 |   0.06433 |   0.14058 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | cau_unemb - dua_unemb | kl_neu   |    -1.22273 |  -1.43582 |  -1.02835 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | cau_unemb - dua_unemb | kl       |    -1.10674 |  -1.33706 |  -0.88558 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | cau_unemb - dua_unemb | kl_park  |     0.29078 |   0.18734 |   0.40834 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | cau_unemb - dua_unemb | rd       |     0.15054 |   0.10308 |   0.20382 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | cau_unemb - dua_unemb | cf_dev   |     0.15501 |   0.10667 |   0.20721 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | cau_unemb - dua_unemb | kl_neu   |    -1.23158 |  -1.44447 |  -1.04005 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | frq_unemb - dua_unemb | kl       |     0.66426 |   0.39972 |   0.92206 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | frq_unemb - dua_unemb | kl_park  |     1.69774 |   1.54823 |   1.8425  |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | frq_unemb - dua_unemb | rd       |     0.24884 |   0.18618 |   0.3045  |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | frq_unemb - dua_unemb | cf_dev   |     0.14707 |   0.10261 |   0.19861 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | frq_unemb - dua_unemb | kl_neu   |    -1.06581 |  -1.26476 |  -0.88094 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | frq_unemb - dua_unemb | kl       |     0.52826 |   0.25746 |   0.79523 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | frq_unemb - dua_unemb | kl_park  |     1.63995 |   1.54183 |   1.74176 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | frq_unemb - dua_unemb | rd       |     0.11468 |   0.05802 |   0.17428 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | frq_unemb - dua_unemb | cf_dev   |     0.00116 |  -0.03431 |   0.03883 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | frq_unemb - dua_unemb | kl_neu   |    -1.19039 |  -1.41655 |  -0.97407 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | frq_unemb - dua_unemb | kl       |     0.49873 |   0.18982 |   0.8263  |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | frq_unemb - dua_unemb | kl_park  |     1.62503 |   1.47688 |   1.78648 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | frq_unemb - dua_unemb | rd       |     0.10289 |   0.05565 |   0.15444 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | frq_unemb - dua_unemb | cf_dev   |     0.01252 |  -0.02399 |   0.06105 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | frq_unemb - dua_unemb | kl_neu   |    -1.22805 |  -1.44488 |  -1.01964 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | cau_unemb - frq_unemb | kl       |    -1.83452 |  -2.02266 |  -1.63302 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | cau_unemb - frq_unemb | kl_park  |    -1.54938 |  -1.72247 |  -1.35434 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | cau_unemb - frq_unemb | rd       |    -0.18028 |  -0.23827 |  -0.12094 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | cau_unemb - frq_unemb | cf_dev   |    -0.01575 |  -0.08486 |   0.05045 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | cau_unemb - frq_unemb | kl_neu   |    -0.10591 |  -0.14679 |  -0.06634 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | cau_unemb - frq_unemb | kl       |    -1.7692  |  -1.89796 |  -1.63314 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | cau_unemb - frq_unemb | kl_park  |    -1.50866 |  -1.62925 |  -1.38343 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | cau_unemb - frq_unemb | rd       |    -0.01986 |  -0.09238 |   0.05279 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | cau_unemb - frq_unemb | cf_dev   |     0.10143 |   0.05996 |   0.14155 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | cau_unemb - frq_unemb | kl_neu   |    -0.03234 |  -0.06514 |   0.00437 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | cau_unemb - frq_unemb | kl       |    -1.60547 |  -1.83584 |  -1.37589 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | cau_unemb - frq_unemb | kl_park  |    -1.33425 |  -1.53731 |  -1.1335  |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | cau_unemb - frq_unemb | rd       |     0.04765 |  -0.0244  |   0.12205 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | cau_unemb - frq_unemb | cf_dev   |     0.14249 |   0.07973 |   0.19823 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | cau_unemb - frq_unemb | kl_neu   |    -0.00353 |  -0.03748 |   0.03361 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | frq_dmd - dua_dmd     | kl       |     0.50065 |   0.25628 |   0.74722 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | frq_dmd - dua_dmd     | kl_park  |     1.76539 |   1.6807  |   1.85861 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | frq_dmd - dua_dmd     | rd       |     0.05653 |   0.00716 |   0.10383 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | frq_dmd - dua_dmd     | cf_dev   |     0.01685 |   0.00071 |   0.04066 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | frq_dmd - dua_dmd     | kl_neu   |    -0.97024 |  -1.15111 |  -0.80184 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | frq_dmd - dua_dmd     | kl       |    -0.34442 |  -0.76077 |   0.04891 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | frq_dmd - dua_dmd     | kl_park  |     1.36483 |   1.17368 |   1.52792 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | frq_dmd - dua_dmd     | rd       |     0.03879 |  -0.01782 |   0.09613 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | frq_dmd - dua_dmd     | cf_dev   |     0.01518 |   0.00713 |   0.02274 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | frq_dmd - dua_dmd     | kl_neu   |    -1.1233  |  -1.32021 |  -0.9345  |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | frq_dmd - dua_dmd     | kl       |     9.5587  |   8.47553 |  10.7271  |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | frq_dmd - dua_dmd     | kl_park  |     3.46169 |   3.29794 |   3.6334  |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | frq_dmd - dua_dmd     | rd       |     0.15303 |   0.10197 |   0.20202 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | frq_dmd - dua_dmd     | cf_dev   |     0.85838 |   0.83695 |   0.87955 |  60 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | frq_dmd - dua_dmd     | kl_neu   |    -0.06548 |  -0.23111 |   0.11969 |  60 |

## capture_ratio

| group         | probe   | metric   |   n |   gap_euc_minus_dua |   gap_lo |   gap_hi | gap_defined   |   rho_cau |   rho_cau_lo |   rho_cau_hi |   rho_frq |   rho_frq_lo |   rho_frq_hi |
|:--------------|:--------|:---------|----:|--------------------:|---------:|---------:|:--------------|----------:|-------------:|-------------:|----------:|-------------:|-------------:|
| A_third_a5e-3 | ctx     | kl       | 180 |            -2.23059 |  -2.4441 |  -1.9902 | True          |    0.6044 |       0.4778 |       0.7544 |  nan      |     nan      |     nan      |
| A_third_a5e-3 | ctx     | kl_park  | 180 |            -0.00031 |  -0.0487 |   0.0529 | False         | 1600.25   |    -239.378  |     237.116  |  nan      |     nan      |     nan      |
| A_third_a5e-3 | ctx     | rd       | 180 |             0.0754  |   0.0617 |   0.0902 | True          |   -0.691  |      -0.997  |      -0.4731 |  nan      |     nan      |     nan      |
| A_third_a5e-3 | ctx     | cf_dev   | 180 |             0.01663 |  -0.0143 |   0.051  | False         |   -9.6894 |    -130.416  |     112.02   |  nan      |     nan      |     nan      |
| A_third_a5e-3 | ctx     | kl_neu   | 180 |            -1.98515 |  -2.144  |  -1.8038 | True          |    0.3863 |       0.3167 |       0.4779 |  nan      |     nan      |     nan      |
| A_third_a5e-3 | unemb   | kl       | 180 |            -0.51064 |  -0.6459 |  -0.3813 | True          |   -0.2072 |      -0.2705 |      -0.1646 |   25.2694 |      19.7844 |      34.1232 |
| A_third_a5e-3 | unemb   | kl_park  | 180 |             0.21663 |   0.1785 |   0.2578 | True          |    0.2384 |       0.1799 |       0.305  |   -5.8304 |      -7.1274 |      -4.9046 |
| A_third_a5e-3 | unemb   | rd       | 180 |             0.11296 |   0.0976 |   0.1297 | True          |    0.168  |       0.1055 |       0.2447 |   -0.0015 |      -0.1606 |       0.1416 |
| A_third_a5e-3 | unemb   | cf_dev   | 180 |             0.07849 |   0.0533 |   0.1067 | True          |   -0.1103 |      -0.1834 |      -0.0504 |   -5.7696 |      -8.9244 |      -4.0391 |
| A_third_a5e-3 | unemb   | kl_neu   | 180 |            -0.6913  |  -0.8359 |  -0.5615 | True          |   -0.0575 |      -0.0779 |      -0.0422 |    7.8451 |       6.2256 |       9.9612 |
| A_third_a5e-3 | dmd     | kl       | 180 |             0.17468 |   0.0714 |   0.2816 | True          |   -0.4518 |      -0.9785 |      -0.2699 |  -15.9131 |     -37.3067 |      -9.0615 |
| A_third_a5e-3 | dmd     | kl_park  | 180 |             0.29017 |   0.2385 |   0.3439 | True          |   -0.0632 |      -0.096  |      -0.0275 |   -2.0748 |      -2.7108 |      -1.5945 |
| A_third_a5e-3 | dmd     | rd       | 180 |             0.12213 |   0.1031 |   0.1406 | True          |    0.0067 |      -0.039  |       0.0543 |   -0.1827 |      -0.298  |      -0.0903 |
| A_third_a5e-3 | dmd     | cf_dev   | 180 |             0.12981 |   0.1032 |   0.16   | True          |   -0.1027 |      -0.1593 |      -0.0588 |   -1.4652 |      -2.2992 |      -0.9007 |
| A_third_a5e-3 | dmd     | kl_neu   | 180 |            -0.13472 |  -0.2246 |  -0.0412 | True          |    0.4589 |       0.2366 |       1.6624 |    8.8302 |       3.9775 |      31.3698 |
| C_third_a5e-3 | ctx     | kl       | 179 |            -1.32955 |  -1.516  |  -1.1373 | True          |    0.7825 |       0.6516 |       0.9452 |  nan      |     nan      |     nan      |
| C_third_a5e-3 | ctx     | kl_park  | 179 |             0.40055 |   0.3106 |   0.5009 | True          |   -2.0158 |      -2.6881 |      -1.5496 |  nan      |     nan      |     nan      |
| C_third_a5e-3 | ctx     | rd       | 179 |             0.18357 |   0.151  |   0.2149 | True          |   -0.3848 |      -0.5877 |      -0.2204 |  nan      |     nan      |     nan      |
| C_third_a5e-3 | ctx     | cf_dev   | 179 |             0.0901  |   0.0566 |   0.1249 | True          |   -3.276  |      -5.5369 |      -2.2071 |  nan      |     nan      |     nan      |
| C_third_a5e-3 | ctx     | kl_neu   | 179 |            -1.35354 |  -1.4813 |  -1.2312 | True          |    0.0913 |       0.0808 |       0.1024 |  nan      |     nan      |     nan      |
| C_third_a5e-3 | unemb   | kl       | 180 |            -1.09816 |  -1.2234 |  -0.9741 | True          |   -0.0678 |      -0.103  |      -0.0361 |    1.5134 |       1.3251 |       1.73   |
| C_third_a5e-3 | unemb   | kl_park  | 180 |             0.24088 |   0.1892 |   0.2955 | True          |    0.2106 |       0.0863 |       0.3344 |   -5.8675 |      -7.9215 |      -4.4715 |
| C_third_a5e-3 | unemb   | rd       | 180 |             0.12417 |   0.0975 |   0.1523 | True          |    0.1573 |       0.0134 |       0.2999 |   -0.2521 |      -0.7084 |       0.0901 |
| C_third_a5e-3 | unemb   | cf_dev   | 180 |             0.07676 |   0.0551 |   0.0996 | True          |   -0.689  |      -0.9711 |      -0.4986 |    0.3019 |      -0.1788 |       0.6468 |
| C_third_a5e-3 | unemb   | kl_neu   | 180 |            -1.19679 |  -1.3115 |  -1.0877 | True          |   -0.0099 |      -0.0133 |      -0.0067 |    0.0296 |       0.0114 |       0.048  |
| C_third_a5e-3 | dmd     | kl       | 180 |            -0.82176 |  -0.9978 |  -0.6474 | True          |    0.5435 |       0.4028 |       0.7377 |    4.9407 |       3.7168 |       6.721  |
| C_third_a5e-3 | dmd     | kl_park  | 180 |             0.74667 |   0.6471 |   0.8543 | True          |   -0.432  |      -0.5258 |      -0.3493 |   -1.9428 |      -2.4614 |      -1.541  |
| C_third_a5e-3 | dmd     | rd       | 180 |             0.24276 |   0.2077 |   0.2781 | True          |   -0.1895 |      -0.292  |      -0.0991 |    0.659  |       0.5261 |       0.7897 |
| C_third_a5e-3 | dmd     | cf_dev   | 180 |             0.09907 |   0.0735 |   0.1252 | True          |   -0.1775 |      -0.3417 |      -0.0501 |   -1.996  |      -3.1561 |      -1.1978 |
| C_third_a5e-3 | dmd     | kl_neu   | 180 |            -0.98646 |  -1.0866 |  -0.892  | True          |   -0.0067 |      -0.0126 |      -0.0008 |    0.2705 |       0.1812 |       0.3711 |

## advantage_regression

| group         | pair(a-b)             | metric   | model      | term   |   coef_per_SD |       lo |       hi |     R2 |   n |   n_clusters |
|:--------------|:----------------------|:---------|:-----------|:-------|--------------:|---------:|---------:|-------:|----:|-------------:|
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.01832 | -0.13099 |  0.11801 | 0.001  | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |      -0.16413 | -0.24626 | -0.06956 | 0.0841 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |       0.00381 | -0.09892 |  0.12365 | 0      | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl       | joint      | H0     |      -0.40097 | -0.69876 | -0.08199 | 0.1364 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl       | joint      | cf0    |      -0.21152 | -0.29645 | -0.10042 | 0.1364 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl       | joint      | log_pr |       0.42543 |  0.18691 |  0.68556 | 0.1364 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.15747 | -0.1979  | -0.10312 | 0.3765 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |      -0.0576  | -0.10692 |  0.00011 | 0.0504 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.15074 | -0.18716 | -0.10369 | 0.345  | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.18417 | -0.31301 | -0.06646 | 0.4061 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | joint      | cf0    |      -0.04689 | -0.08729 | -0.00177 | 0.4061 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.03288 | -0.06804 |  0.15061 | 0.4061 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.05079 | -0.06745 | -0.03329 | 0.2886 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.02364 | -0.04209 | -0.00188 | 0.0625 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.05184 | -0.06722 | -0.03502 | 0.3007 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | rd       | joint      | H0     |      -0.03203 | -0.06975 |  0.0054  | 0.3322 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | rd       | joint      | cf0    |      -0.017   | -0.03407 |  0.0012  | 0.3322 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | rd       | joint      | log_pr |      -0.01814 | -0.05365 |  0.01817 | 0.3322 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.04575 | -0.06954 | -0.02062 | 0.123  | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |      -2e-05   | -0.02149 |  0.02171 | 0      | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.05104 | -0.07506 | -0.02764 | 0.153  | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | joint      | H0     |       0.03713 | -0.02287 |  0.08757 | 0.1671 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.01429 | -0.01235 |  0.03532 | 0.1671 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | joint      | log_pr |      -0.08902 | -0.13984 | -0.02428 | 0.1671 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |       0.02741 | -0.11962 |  0.17905 | 0.0028 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.23673 | -0.30101 | -0.15343 | 0.206  | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |       0.03757 | -0.10203 |  0.17499 | 0.0052 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.33899 | -0.5967  | -0.04763 | 0.2739 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -0.28802 | -0.36696 | -0.18045 | 0.2739 | 180 |           47 |
| A_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.41584 |  0.18296 |  0.65359 | 0.2739 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl       | uni_H0     | H0     |       0.10072 | -0.0536  |  0.26751 | 0.018  | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl       | uni_cf0    | cf0    |      -0.25618 | -0.37193 | -0.13069 | 0.1166 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl       | uni_log_pr | log_pr |       0.17713 |  0.02073 |  0.37078 | 0.0558 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl       | joint      | H0     |      -1.00334 | -1.22712 | -0.74198 | 0.3839 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl       | joint      | cf0    |      -0.40323 | -0.51778 | -0.2791  | 0.3839 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl       | joint      | log_pr |       1.20696 |  0.9293  |  1.45269 | 0.3839 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.09393 | -0.13842 | -0.04509 | 0.2064 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |      -0.02739 | -0.0729  |  0.02471 | 0.0175 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.08039 | -0.12298 | -0.03327 | 0.1512 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.19898 | -0.31029 | -0.09865 | 0.2427 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | joint      | cf0    |      -0.03153 | -0.07132 |  0.00948 | 0.2427 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.11416 |  0.02309 |  0.21857 | 0.2427 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | rd       | uni_H0     | H0     |      -0.0397  | -0.05817 | -0.01404 | 0.1922 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.0166  | -0.03543 |  0.00442 | 0.0336 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.0374  | -0.05396 | -0.01341 | 0.1706 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | rd       | joint      | H0     |      -0.05466 | -0.09646 | -0.00845 | 0.216  | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | rd       | joint      | cf0    |      -0.01493 | -0.03173 |  0.00258 | 0.216  | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | rd       | joint      | log_pr |       0.0173  | -0.02311 |  0.05887 | 0.216  | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |      -0.04468 | -0.06849 | -0.01943 | 0.1247 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |       0.02395 |  0.00541 |  0.04642 | 0.0358 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |      -0.03648 | -0.06194 | -0.01119 | 0.0831 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.07404 | -0.13503 | -0.02332 | 0.1793 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | joint      | cf0    |       0.0252  |  0.00337 |  0.04724 | 0.1793 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.02853 | -0.02623 |  0.09632 | 0.1793 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |       0.11239 | -0.04547 |  0.29427 | 0.0256 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -0.30386 | -0.40798 | -0.19551 | 0.1868 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |       0.17402 |  0.00894 |  0.34678 | 0.0613 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | joint      | H0     |      -0.89915 | -1.10159 | -0.64683 | 0.459  | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -0.44191 | -0.54249 | -0.33416 | 0.459  | 180 |           47 |
| A_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | joint      | log_pr |       1.11301 |  0.85146 |  1.33796 | 0.459  | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl       | uni_H0     | H0     |      -1.9459  | -2.41101 | -1.49379 | 0.2753 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl       | uni_cf0    | cf0    |      -0.1337  | -0.6514  |  0.56278 | 0.0013 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl       | uni_log_pr | log_pr |      -1.73081 | -2.12921 | -1.29944 | 0.2178 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl       | joint      | H0     |      -3.01001 | -4.54865 | -1.44888 | 0.2841 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl       | joint      | cf0    |      -0.07754 | -0.58266 |  0.45265 | 0.2841 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl       | joint      | log_pr |       1.13243 | -0.35718 |  2.62977 | 0.2841 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.30947 | -0.33891 | -0.27806 | 0.8254 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |      -0.03569 | -0.09176 |  0.03904 | 0.011  | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.30794 | -0.33494 | -0.27911 | 0.8173 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.16306 | -0.24518 | -0.0691  | 0.8451 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.01075 | -0.01451 |  0.0428  | 0.8451 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | joint      | log_pr |      -0.15582 | -0.23757 | -0.08052 | 0.8451 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | rd       | uni_H0     | H0     |      -0.01489 | -0.02858 | -0.00085 | 0.0328 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | rd       | uni_cf0    | cf0    |       0.00995 |  0.00105 |  0.02065 | 0.0147 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.02585 | -0.03906 | -0.0127  | 0.0988 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | rd       | joint      | H0     |       0.11596 |  0.08509 |  0.14609 | 0.3239 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | rd       | joint      | cf0    |       0.02725 |  0.01758 |  0.0393  | 0.3239 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | rd       | joint      | log_pr |      -0.141   | -0.1735  | -0.1094  | 0.3239 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |       0.00932 | -0.01958 |  0.03701 | 0.0038 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |       0.14722 |  0.13997 |  0.15644 | 0.9415 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.03077 |  0.00224 |  0.05976 | 0.0411 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.06076 | -0.07785 | -0.04126 | 0.9569 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | joint      | cf0    |       0.14091 |  0.13518 |  0.14815 | 0.9569 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.06009 |  0.04146 |  0.07762 | 0.9569 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |      -0.88846 | -1.41773 | -0.31946 | 0.1109 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -2.08844 | -2.4257  | -1.68925 | 0.6126 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |      -0.95454 | -1.50005 | -0.40677 | 0.128  | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | joint      | H0     |      -1.81865 | -2.56666 | -1.1213  | 0.6992 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -2.15701 | -2.52351 | -1.81346 | 0.6992 | 180 |           47 |
| A_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | joint      | log_pr |       1.19715 |  0.50181 |  1.90744 | 0.6992 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl       | uni_H0     | H0     |       2.04662 |  1.57266 |  2.53282 | 0.2979 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl       | uni_cf0    | cf0    |      -0.12248 | -0.744   |  0.38081 | 0.0011 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl       | uni_log_pr | log_pr |       1.90794 |  1.51247 |  2.35709 | 0.2589 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl       | joint      | H0     |       2.00667 |  0.46761 |  3.65289 | 0.305  | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl       | joint      | cf0    |      -0.32569 | -0.80248 |  0.15144 | 0.305  | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl       | joint      | log_pr |       0.07453 | -1.50158 |  1.5574  | 0.305  | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | uni_H0     | H0     |       0.21554 |  0.17457 |  0.26215 | 0.5037 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | uni_cf0    | cf0    |       0.00831 | -0.04389 |  0.05171 | 0.0007 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | uni_log_pr | log_pr |       0.22755 |  0.18833 |  0.27193 | 0.5614 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | joint      | H0     |      -0.03592 | -0.13071 |  0.06631 | 0.5783 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | joint      | cf0    |      -0.04227 | -0.08616 |  0.00152 | 0.5783 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | joint      | log_pr |       0.26998 |  0.17389 |  0.36982 | 0.5783 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | rd       | uni_H0     | H0     |      -0.02481 | -0.04655 |  0.00302 | 0.0481 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | rd       | uni_cf0    | cf0    |      -0.02656 | -0.04609 | -0.00448 | 0.0551 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | rd       | uni_log_pr | log_pr |      -0.01155 | -0.03251 |  0.01704 | 0.0104 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | rd       | joint      | H0     |      -0.17062 | -0.2223  | -0.12067 | 0.2755 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | rd       | joint      | cf0    |      -0.04218 | -0.06229 | -0.02262 | 0.2755 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | rd       | joint      | log_pr |       0.1583  |  0.1067  |  0.21698 | 0.2755 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | uni_H0     | H0     |      -0.05401 | -0.07663 | -0.02431 | 0.1026 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | uni_cf0    | cf0    |      -0.12326 | -0.14082 | -0.10444 | 0.5346 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | uni_log_pr | log_pr |      -0.06726 | -0.08658 | -0.04228 | 0.1592 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | joint      | H0     |      -0.01328 | -0.06696 |  0.02782 | 0.6018 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | joint      | cf0    |      -0.11571 | -0.13606 | -0.09698 | 0.6018 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | joint      | log_pr |      -0.03157 | -0.078   |  0.02483 | 0.6018 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | uni_H0     | H0     |       1.00085 |  0.58659 |  1.39591 | 0.1704 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | uni_cf0    | cf0    |       1.78458 |  1.44446 |  2.08603 | 0.5416 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | uni_log_pr | log_pr |       1.12855 |  0.71309 |  1.51773 | 0.2166 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | joint      | H0     |       0.9195  |  0.22472 |  1.6573  | 0.6609 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | joint      | cf0    |       1.7151  |  1.40266 |  2.04925 | 0.6609 | 180 |           47 |
| A_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | joint      | log_pr |      -0.08414 | -0.77216 |  0.60618 | 0.6609 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.57987 | -1.08553 | -0.11195 | 0.0504 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |       0.42044 | -0.04567 |  0.94776 | 0.0265 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |      -0.32941 | -0.79105 |  0.10226 | 0.0163 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl       | joint      | H0     |      -2.30448 | -3.91026 | -0.97208 | 0.1291 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl       | joint      | cf0    |       0.27792 | -0.17652 |  0.76136 | 0.1291 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl       | joint      | log_pr |       1.7953  |  0.62121 |  3.2191  | 0.1291 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.28303 | -0.34183 | -0.2249  | 0.4384 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |      -0.00739 | -0.07924 |  0.08892 | 0.0003 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.26672 | -0.32177 | -0.20682 | 0.3893 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.27375 | -0.43484 | -0.11107 | 0.4405 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | joint      | cf0    |       0.02067 | -0.03062 |  0.07927 | 0.4405 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | joint      | log_pr |      -0.01186 | -0.15806 |  0.12875 | 0.4405 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.04446 | -0.05806 | -0.02671 | 0.236  | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.02321 | -0.03726 | -0.00556 | 0.0643 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.05083 | -0.06314 | -0.03506 | 0.3085 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | rd       | joint      | H0     |       0.02449 | -0.01386 |  0.0664  | 0.3365 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | rd       | joint      | cf0    |      -0.01116 | -0.02427 |  0.00269 | 0.3365 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | rd       | joint      | log_pr |      -0.07177 | -0.10554 | -0.03596 | 0.3365 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.00881 | -0.04199 |  0.02152 | 0.0025 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.10453 |  0.07935 |  0.12392 | 0.3506 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |       0.00215 | -0.02925 |  0.03417 | 0.0001 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.00539 | -0.08761 |  0.07357 | 0.3625 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.1079  |  0.08282 |  0.12921 | 0.3625 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | joint      | log_pr |      -0.01431 | -0.09376 |  0.06465 | 0.3625 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |      -0.30112 | -0.61986 |  0.03562 | 0.0564 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.50411 | -0.8051  | -0.22063 | 0.158  | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |      -0.25614 | -0.57361 |  0.08496 | 0.0408 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -1.08644 | -1.76502 | -0.48205 | 0.2438 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -0.57953 | -0.86672 | -0.30919 | 0.2438 | 180 |           47 |
| A_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.88755 |  0.43436 |  1.38676 | 0.2438 | 180 |           47 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.28045 | -0.44385 | -0.11918 | 0.0535 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |       0.41068 |  0.25425 |  0.57052 | 0.1147 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |      -0.26018 | -0.42838 | -0.07414 | 0.0461 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl       | joint      | H0     |       0.102   | -0.16347 |  0.36605 | 0.1175 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl       | joint      | cf0    |       0.47639 |  0.17558 |  0.77201 | 0.1175 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl       | joint      | log_pr |      -0.02161 | -0.22609 |  0.19987 | 0.1175 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |       0.06942 | -0.04845 |  0.17041 | 0.0094 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |      -0.01406 | -0.11849 |  0.08597 | 0.0004 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |       0.0365  | -0.06155 |  0.14344 | 0.0026 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | joint      | H0     |       0.14178 | -0.06409 |  0.31447 | 0.0179 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | joint      | cf0    |       0.11076 | -0.07478 |  0.27576 | 0.0179 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.02355 | -0.10986 |  0.17184 | 0.0179 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | rd       | uni_H0     | H0     |       0.04013 |  0.00412 |  0.06796 | 0.0291 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.02009 | -0.05849 |  0.01198 | 0.0073 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |       0.02786 | -0.0042  |  0.06191 | 0.014  | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | rd       | joint      | H0     |       0.05797 |  0.00176 |  0.10841 | 0.0375 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | rd       | joint      | cf0    |       0.03502 | -0.02622 |  0.08813 | 0.0375 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | rd       | joint      | log_pr |       0.01615 | -0.0304  |  0.06082 | 0.0375 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.01171 | -0.03724 |  0.01076 | 0.0039 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.00757 | -0.01773 |  0.03143 | 0.0016 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.01092 | -0.03898 |  0.01901 | 0.0034 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.01276 | -0.0633  |  0.03389 | 0.0052 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | joint      | cf0    |      -0.00744 | -0.06064 |  0.03989 | 0.0052 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | joint      | log_pr |      -0.00818 | -0.04385 |  0.02872 | 0.0052 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |      -0.35997 | -0.43626 | -0.28243 | 0.2931 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |       0.45929 |  0.36142 |  0.5686  | 0.4772 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |      -0.25576 | -0.34288 | -0.17428 | 0.148  | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.02132 | -0.11816 |  0.0865  | 0.4812 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | joint      | cf0    |       0.47681 |  0.32976 |  0.65323 | 0.4812 | 180 |          177 |
| C_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.05454 | -0.00853 |  0.12252 | 0.4812 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl       | uni_H0     | H0     |      -0.40324 | -0.50859 | -0.3027  | 0.2127 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl       | uni_cf0    | cf0    |       0.56713 |  0.44668 |  0.68125 | 0.4208 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl       | uni_log_pr | log_pr |      -0.33479 | -0.45902 | -0.21966 | 0.1466 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl       | joint      | H0     |       0.0892  | -0.05967 |  0.22707 | 0.4256 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl       | joint      | cf0    |       0.64786 |  0.44545 |  0.84378 | 0.4256 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl       | joint      | log_pr |       0.01835 | -0.10239 |  0.12779 | 0.4256 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | uni_H0     | H0     |       0.0345  | -0.00997 |  0.07191 | 0.0101 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |      -0.01354 | -0.06087 |  0.0327  | 0.0016 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |       0.01667 | -0.0522  |  0.07609 | 0.0024 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | joint      | H0     |       0.05939 | -0.02375 |  0.13072 | 0.0139 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.03526 | -0.05418 |  0.10959 | 0.0139 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.00429 | -0.0878  |  0.08143 | 0.0139 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | rd       | uni_H0     | H0     |       0.01826 | -0.00204 |  0.0368  | 0.01   | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.00964 | -0.03181 |  0.01144 | 0.0028 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.00908 | -0.03598 |  0.0161  | 0.0025 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | rd       | joint      | H0     |       0.0343  | -0.00671 |  0.07266 | 0.0274 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | rd       | joint      | cf0    |      -0.0018  | -0.04419 |  0.04054 | 0.0274 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | rd       | joint      | log_pr |      -0.03008 | -0.07121 |  0.00397 | 0.0274 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |       0.03833 |  0.0152  |  0.06119 | 0.0449 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |      -0.03906 | -0.06457 | -0.01672 | 0.0466 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.03607 |  0.01382 |  0.06061 | 0.0397 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | joint      | H0     |       0.01619 | -0.03028 |  0.05705 | 0.0565 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | joint      | cf0    |      -0.01609 | -0.06664 |  0.02555 | 0.0565 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.01663 | -0.01153 |  0.04676 | 0.0565 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |      -0.48663 | -0.56964 | -0.40469 | 0.378  | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |       0.63381 |  0.53617 |  0.73515 | 0.6411 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |      -0.34936 | -0.44649 | -0.25485 | 0.1948 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | joint      | H0     |      -0.0044  | -0.1116  |  0.10162 | 0.6469 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | joint      | cf0    |       0.6787  |  0.51343 |  0.85077 | 0.6469 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | joint      | log_pr |       0.07729 |  0.0185  |  0.14364 | 0.6469 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl       | uni_H0     | H0     |      -0.54633 | -0.71387 | -0.37668 | 0.2327 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl       | uni_cf0    | cf0    |       0.7133  |  0.56168 |  0.86024 | 0.3967 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl       | uni_log_pr | log_pr |      -0.32322 | -0.49057 | -0.16864 | 0.0814 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl       | joint      | H0     |      -0.02976 | -0.26779 |  0.21736 | 0.4161 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl       | joint      | cf0    |       0.81865 |  0.57774 |  1.0467  | 0.4161 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl       | joint      | log_pr |       0.20558 |  0.07052 |  0.34706 | 0.4161 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.17854 | -0.27516 | -0.07734 | 0.1101 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |       0.18172 |  0.09782 |  0.26758 | 0.1141 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.04386 | -0.12862 |  0.03738 | 0.0066 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.12606 | -0.27209 |  0.00435 | 0.1626 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.16745 |  0.07616 |  0.26115 | 0.1626 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.13383 |  0.03742 |  0.23742 | 0.1626 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | rd       | uni_H0     | H0     |       0.06342 |  0.03903 |  0.08519 | 0.0871 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.05734 | -0.08842 | -0.02787 | 0.0712 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | rd       | uni_log_pr | log_pr |       0.05956 |  0.02647 |  0.09095 | 0.0768 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | rd       | joint      | H0     |       0.03981 | -0.00299 |  0.08266 | 0.1043 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | rd       | joint      | cf0    |      -0.00595 | -0.05644 |  0.04246 | 0.1043 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | rd       | joint      | log_pr |       0.03277 | -0.00928 |  0.07561 | 0.1043 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |       0.00547 | -0.03224 |  0.03969 | 0.0011 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |      -0.0148  | -0.04013 |  0.01368 | 0.0078 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.02593 |  0.00337 |  0.04919 | 0.0238 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.0225  | -0.075   |  0.02417 | 0.0308 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | joint      | cf0    |      -0.01299 | -0.04896 |  0.02238 | 0.0308 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.03085 |  0.00404 |  0.05905 | 0.0308 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |      -0.4637  | -0.54812 | -0.37574 | 0.3396 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |       0.61318 |  0.50072 |  0.72035 | 0.5938 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |      -0.31903 | -0.42741 | -0.21887 | 0.1607 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | joint      | H0     |       0.00663 | -0.11393 |  0.12982 | 0.6045 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | joint      | cf0    |       0.68344 |  0.48932 |  0.88134 | 0.6045 | 180 |          177 |
| C_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | joint      | log_pr |       0.1042  |  0.03523 |  0.17977 | 0.6045 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl       | uni_H0     | H0     |       0.14308 | -0.00309 |  0.28268 | 0.0359 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl       | uni_cf0    | cf0    |      -0.14617 | -0.26403 | -0.04095 | 0.0375 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl       | uni_log_pr | log_pr |      -0.01157 | -0.13179 |  0.11396 | 0.0002 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl       | joint      | H0     |       0.11896 | -0.08386 |  0.32276 | 0.0775 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl       | joint      | cf0    |      -0.17079 | -0.32246 | -0.01328 | 0.0775 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl       | joint      | log_pr |      -0.18723 | -0.33665 | -0.04358 | 0.0775 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | uni_H0     | H0     |       0.21303 |  0.09681 |  0.32746 | 0.097  | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | uni_cf0    | cf0    |      -0.19525 | -0.29143 | -0.09795 | 0.0815 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | uni_log_pr | log_pr |       0.06053 | -0.04833 |  0.17273 | 0.0078 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | joint      | H0     |       0.18545 |  0.01494 |  0.35154 | 0.1229 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | joint      | cf0    |      -0.13219 | -0.26746 | -0.00451 | 0.1229 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | joint      | log_pr |      -0.12954 | -0.26346 | -0.00308 | 0.1229 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | rd       | uni_H0     | H0     |      -0.04516 | -0.07421 | -0.01692 | 0.0281 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | rd       | uni_cf0    | cf0    |       0.04771 |  0.0143  |  0.08163 | 0.0313 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | rd       | uni_log_pr | log_pr |      -0.06864 | -0.10995 | -0.02855 | 0.0648 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | rd       | joint      | H0     |      -0.00552 | -0.06005 |  0.05185 | 0.0655 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | rd       | joint      | cf0    |       0.00415 | -0.0579  |  0.06347 | 0.0655 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | rd       | joint      | log_pr |      -0.06285 | -0.11939 | -0.00369 | 0.0655 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | uni_H0     | H0     |       0.03286 | -0.00783 |  0.07724 | 0.0206 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | uni_cf0    | cf0    |      -0.02426 | -0.06405 |  0.00795 | 0.0112 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | uni_log_pr | log_pr |       0.01014 | -0.02413 |  0.04481 | 0.002  | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | joint      | H0     |       0.03869 | -0.02438 |  0.09983 | 0.023  | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | joint      | cf0    |      -0.00311 | -0.05706 |  0.04764 | 0.023  | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | joint      | log_pr |      -0.01422 | -0.05613 |  0.02545 | 0.023  | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | uni_H0     | H0     |      -0.02293 | -0.04324 | -0.00345 | 0.0247 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | uni_cf0    | cf0    |       0.02063 | -0.01295 |  0.05287 | 0.02   | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | uni_log_pr | log_pr |      -0.03033 | -0.05145 | -0.00989 | 0.0432 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | joint      | H0     |      -0.01102 | -0.0492  |  0.02807 | 0.0455 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | joint      | cf0    |      -0.00475 | -0.06459 |  0.05926 | 0.0455 | 180 |          177 |
| C_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | joint      | log_pr |      -0.02691 | -0.05212 | -0.00313 | 0.0455 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.9416  | -1.37427 | -0.55012 | 0.1162 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |       0.8389  |  0.42716 |  1.2844  | 0.0923 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |      -0.77433 | -1.15386 | -0.37235 | 0.0786 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl       | joint      | H0     |      -0.6576  | -1.3807  |  0.05214 | 0.1274 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl       | joint      | cf0    |       0.13538 | -0.53216 |  0.79905 | 0.1274 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl       | joint      | log_pr |      -0.30866 | -0.94626 |  0.29464 | 0.1274 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.30282 | -0.37917 | -0.21157 | 0.2552 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |       0.24648 |  0.1746  |  0.31846 | 0.1691 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.15126 | -0.22108 | -0.08614 | 0.0637 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.29247 | -0.42384 | -0.13308 | 0.2601 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | joint      | cf0    |       0.05045 | -0.04523 |  0.15117 | 0.2601 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.04974 | -0.03771 |  0.13932 | 0.2601 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | rd       | uni_H0     | H0     |       0.05091 |  0.0277  |  0.07474 | 0.0619 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.04118 | -0.07094 | -0.01457 | 0.0405 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |       0.06439 |  0.03428 |  0.09236 | 0.099  | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | rd       | joint      | H0     |       0.03389 | -0.00954 |  0.07529 | 0.1095 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | rd       | joint      | cf0    |       0.02149 | -0.02807 |  0.06315 | 0.1095 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | rd       | joint      | log_pr |       0.05818 |  0.02194 |  0.09516 | 0.1095 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.02005 | -0.03724 | -0.00547 | 0.08   | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.02157 |  0.00778 |  0.0358  | 0.0926 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.0125  | -0.02326 | -0.00296 | 0.0311 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.00902 | -0.03172 |  0.00922 | 0.0991 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.01644 |  0.00017 |  0.03423 | 0.0991 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | joint      | log_pr |       0.00299 | -0.00786 |  0.01432 | 0.0991 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |      -0.26496 | -0.35667 | -0.17586 | 0.1366 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |       0.31101 |  0.17419 |  0.45899 | 0.1882 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |      -0.16731 | -0.27614 | -0.07131 | 0.0545 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.07224 | -0.22646 |  0.09318 | 0.1944 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | joint      | cf0    |       0.28961 |  0.06001 |  0.54703 | 0.1944 | 180 |          177 |
| C_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.05553 | -0.02878 |  0.14017 | 0.1944 | 180 |          177 |

## predictor_corr

| group         | a         | b         | pred_i   | pred_j   |   corr |
|:--------------|:----------|:----------|:---------|:---------|-------:|
| A_third_a5e-3 | euc_dmd   | dua_dmd   | H0       | cf0      |  0.094 |
| A_third_a5e-3 | euc_dmd   | dua_dmd   | H0       | log_pr   |  0.946 |
| A_third_a5e-3 | euc_dmd   | dua_dmd   | cf0      | log_pr   |  0.2   |
| A_third_a5e-3 | cau_unemb | dua_unemb | H0       | cf0      |  0.094 |
| A_third_a5e-3 | cau_unemb | dua_unemb | H0       | log_pr   |  0.946 |
| A_third_a5e-3 | cau_unemb | dua_unemb | cf0      | log_pr   |  0.2   |
| A_third_a5e-3 | frq_unemb | dua_unemb | H0       | cf0      |  0.094 |
| A_third_a5e-3 | frq_unemb | dua_unemb | H0       | log_pr   |  0.946 |
| A_third_a5e-3 | frq_unemb | dua_unemb | cf0      | log_pr   |  0.2   |
| A_third_a5e-3 | cau_unemb | frq_unemb | H0       | cf0      |  0.094 |
| A_third_a5e-3 | cau_unemb | frq_unemb | H0       | log_pr   |  0.946 |
| A_third_a5e-3 | cau_unemb | frq_unemb | cf0      | log_pr   |  0.2   |
| A_third_a5e-3 | frq_dmd   | dua_dmd   | H0       | cf0      |  0.094 |
| A_third_a5e-3 | frq_dmd   | dua_dmd   | H0       | log_pr   |  0.946 |
| A_third_a5e-3 | frq_dmd   | dua_dmd   | cf0      | log_pr   |  0.2   |
| C_third_a5e-3 | euc_dmd   | dua_dmd   | H0       | cf0      | -0.777 |
| C_third_a5e-3 | euc_dmd   | dua_dmd   | H0       | log_pr   |  0.579 |
| C_third_a5e-3 | euc_dmd   | dua_dmd   | cf0      | log_pr   | -0.625 |
| C_third_a5e-3 | cau_unemb | dua_unemb | H0       | cf0      | -0.777 |
| C_third_a5e-3 | cau_unemb | dua_unemb | H0       | log_pr   |  0.579 |
| C_third_a5e-3 | cau_unemb | dua_unemb | cf0      | log_pr   | -0.625 |
| C_third_a5e-3 | frq_unemb | dua_unemb | H0       | cf0      | -0.777 |
| C_third_a5e-3 | frq_unemb | dua_unemb | H0       | log_pr   |  0.579 |
| C_third_a5e-3 | frq_unemb | dua_unemb | cf0      | log_pr   | -0.625 |
| C_third_a5e-3 | cau_unemb | frq_unemb | H0       | cf0      | -0.777 |
| C_third_a5e-3 | cau_unemb | frq_unemb | H0       | log_pr   |  0.579 |
| C_third_a5e-3 | cau_unemb | frq_unemb | cf0      | log_pr   | -0.625 |
| C_third_a5e-3 | frq_dmd   | dua_dmd   | H0       | cf0      | -0.777 |
| C_third_a5e-3 | frq_dmd   | dua_dmd   | H0       | log_pr   |  0.579 |
| C_third_a5e-3 | frq_dmd   | dua_dmd   | cf0      | log_pr   | -0.625 |

## null_control_summary

| group         | run                          | method    |   n_ctx |   kl_real |   kl_null |   kl_real_minus_null |    kl_lo |   kl_hi |   kl_park_real |   kl_park_null |   kl_park_real_minus_null |   kl_park_lo |   kl_park_hi |   rd_real |   rd_null |   rd_real_minus_null |   rd_lo |   rd_hi |   cf_dev_real |   cf_dev_null |   cf_dev_real_minus_null |   cf_dev_lo |   cf_dev_hi |   kl_neu_real |   kl_neu_null |   kl_neu_real_minus_null |   kl_neu_lo |   kl_neu_hi |   P1_null_end |
|:--------------|:-----------------------------|:----------|--------:|----------:|----------:|---------------------:|---------:|--------:|---------------:|---------------:|--------------------------:|-------------:|-------------:|----------:|----------:|---------------------:|--------:|--------:|--------------:|--------------:|-------------------------:|------------:|------------:|--------------:|--------------:|-------------------------:|------------:|------------:|--------------:|
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | cau_ctx   |      30 |    2.4998 |    3.0196 |              -0.5198 |  -0.8332 | -0.2828 |         1.0897 |         1.0228 |                    0.0669 |      -0.0074 |       0.1386 |    0.2236 |    0.1855 |               0.0381 |  0.0088 |  0.0597 |        0.3103 |        0.3769 |                  -0.0667 |     -0.1023 |     -0.0198 |        1.6201 |        1.4713 |                   0.1489 |      0.066  |      0.2151 |        0.0456 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | cau_dmd   |      30 |    1.3013 |    1.8693 |              -0.5681 |  -0.7533 | -0.329  |         0.6928 |         0.8515 |                   -0.1588 |      -0.2617 |      -0.0283 |    0.1993 |    0.2296 |              -0.0303 | -0.0608 |  0.002  |        0.1754 |        0.1977 |                  -0.0223 |     -0.068  |      0.0358 |        0.8789 |        0.8101 |                   0.0688 |     -0.0374 |      0.1818 |        0.1851 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | cau_unemb |      30 |    0.8821 |    0.1035 |               0.7787 |   0.6519 |  0.9264 |         0.4988 |         0.0543 |                    0.4445 |       0.323  |       0.5871 |    0.1615 |    0.0575 |               0.104  |  0.0583 |  0.1629 |        0.1098 |        0.0325 |                   0.0773 |      0.039  |      0.1301 |        0.6668 |        0.0394 |                   0.6274 |      0.5062 |      0.7605 |        0.0084 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | dua_ctx   |      30 |    3.3574 |    2.2566 |               1.1008 |   0.7251 |  1.4278 |         0.5164 |         0.3631 |                    0.1533 |       0.0952 |       0.2325 |    0.0746 |    0.0664 |               0.0081 | -0.0108 |  0.0306 |        0.1513 |        0.161  |                  -0.0098 |     -0.0265 |      0.0071 |        2.8725 |        1.5015 |                   1.371  |      1.007  |      1.6631 |        0.0849 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | dua_dmd   |      30 |    0.9191 |    0.7427 |               0.1764 |   0.095  |  0.2524 |         0.3056 |         0.2318 |                    0.0738 |       0.0311 |       0.1087 |    0.0577 |    0.0796 |              -0.0219 | -0.0336 | -0.0104 |        0.0481 |        0.0575 |                  -0.0094 |     -0.0193 |      0.0011 |        0.8062 |        0.3777 |                   0.4285 |      0.3193 |      0.5306 |        0.2339 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | dua_unemb |      30 |    1.36   |    0.1791 |               1.1808 |   0.9538 |  1.4139 |         0.2938 |         0.0602 |                    0.2337 |       0.1893 |       0.2785 |    0.0674 |    0.0213 |               0.046  |  0.0334 |  0.0584 |        0.0374 |        0.025  |                   0.0124 |      0.0025 |      0.0228 |        1.2363 |        0.1146 |                   1.1217 |      0.9139 |      1.3364 |        0.0124 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | euc_ctx   |      30 |    1.0062 |    0.5958 |               0.4105 |   0.3134 |  0.5231 |         0.5585 |         0.3284 |                    0.2301 |       0.1368 |       0.3491 |    0.157  |    0.1495 |               0.0075 | -0.0204 |  0.0429 |        0.1283 |        0.1321 |                  -0.0037 |     -0.0425 |      0.0496 |        0.8315 |        0.3649 |                   0.4667 |      0.3819 |      0.5661 |        0.0364 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | euc_dmd   |      30 |    1.1643 |    1.5278 |              -0.3635 |  -0.5273 | -0.1583 |         0.6415 |         0.7822 |                   -0.1407 |      -0.2369 |      -0.0125 |    0.1937 |    0.2314 |              -0.0377 | -0.0734 |  0.0006 |        0.1519 |        0.192  |                  -0.0401 |     -0.0755 |     -0.0013 |        0.7867 |        0.7375 |                   0.0492 |     -0.0715 |      0.1687 |        0.286  |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | euc_unemb |      30 |    0.9762 |    0.1936 |               0.7826 |   0.6663 |  0.9245 |         0.5372 |         0.1506 |                    0.3867 |       0.2643 |       0.5304 |    0.1886 |    0.0822 |               0.1064 |  0.067  |  0.1581 |        0.093  |        0.0556 |                   0.0374 |      0.0007 |      0.0913 |        0.6934 |        0.0912 |                   0.6022 |      0.4893 |      0.7288 |        0.0101 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | frq_dmd   |      30 |    2.7929 |    1.8674 |               0.9255 |   0.7311 |  1.1846 |         1.2268 |         0.8475 |                    0.3793 |       0.2636 |       0.5246 |    0.227  |    0.149  |               0.078  |  0.0416 |  0.1207 |        0.3878 |        0.3294 |                   0.0583 |      0.0336 |      0.0898 |        1.5645 |        0.8749 |                   0.6896 |      0.4929 |      0.9451 |        0.0225 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s0_abs5e-3 | frq_unemb |      30 |   16.2469 |   19.7485 |              -3.5016 |  -4.0834 | -2.8708 |         1.8716 |         1.8715 |                    0.0001 |      -0.0001 |       0.0004 |    0.1921 |    0.1726 |               0.0194 |  0.0002 |  0.0386 |        0.5786 |        0.5787 |                  -0.0001 |     -0.0002 |     -0      |        7.0746 |        8.5004 |                  -1.4259 |     -1.8698 |     -1.0498 |        0.008  |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | cau_ctx   |      30 |    1.816  |    0.8975 |               0.9185 |   0.6549 |  1.2696 |         0.7786 |         0.4052 |                    0.3733 |       0.2649 |       0.498  |    0.186  |    0.1786 |               0.0074 | -0.0092 |  0.0244 |        0.2466 |        0.1356 |                   0.111  |      0.0533 |      0.1765 |        1.29   |        0.4447 |                   0.8453 |      0.6738 |      1.0369 |        0.0243 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | cau_dmd   |      30 |    1.1367 |    1.9229 |              -0.7862 |  -0.9299 | -0.616  |         0.5525 |         0.633  |                   -0.0805 |      -0.1359 |      -0.0176 |    0.1796 |    0.1652 |               0.0144 | -0.0043 |  0.0393 |        0.1945 |        0.1807 |                   0.0137 |     -0.0315 |      0.0756 |        0.7581 |        0.6709 |                   0.0873 |     -0.0035 |      0.1963 |        0.3222 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | cau_unemb |      30 |    0.8247 |    0.1031 |               0.7215 |   0.6261 |  0.8293 |         0.4326 |         0.0389 |                    0.3937 |       0.3201 |       0.486  |    0.1551 |    0.0667 |               0.0884 |  0.059  |  0.127  |        0.1321 |        0.0352 |                   0.0969 |      0.0568 |      0.1476 |        0.6018 |        0.0487 |                   0.5531 |      0.4854 |      0.6376 |        0.0075 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | dua_ctx   |      30 |    3.1867 |    2.0779 |               1.1088 |   0.8151 |  1.4495 |         0.4699 |         0.3243 |                    0.1455 |       0.1011 |       0.2134 |    0.0843 |    0.0689 |               0.0155 | -0.0064 |  0.0467 |        0.1181 |        0.1039 |                   0.0141 |      0.0033 |      0.031  |        2.7667 |        1.3685 |                   1.3981 |      1.0976 |      1.7417 |        0.1341 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | dua_dmd   |      30 |    0.9468 |    0.7323 |               0.2145 |   0.1218 |  0.2934 |         0.3092 |         0.1846 |                    0.1247 |       0.0909 |       0.1577 |    0.059  |    0.0948 |              -0.0357 | -0.0487 | -0.0173 |        0.0488 |        0.0619 |                  -0.0131 |     -0.0268 |      0.0015 |        0.8491 |        0.3675 |                   0.4816 |      0.407  |      0.5818 |        0.2811 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | dua_unemb |      30 |    1.5313 |    0.165  |               1.3662 |   1.0805 |  1.663  |         0.3033 |         0.0273 |                    0.276  |       0.229  |       0.3304 |    0.067  |    0.0234 |               0.0436 |  0.028  |  0.0647 |        0.0402 |        0.0159 |                   0.0243 |      0.0142 |      0.0364 |        1.4175 |        0.1084 |                   1.3091 |      1.0329 |      1.5977 |        0.009  |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | euc_ctx   |      30 |    0.9426 |    0.6248 |               0.3178 |   0.2118 |  0.4316 |         0.4539 |         0.3116 |                    0.1423 |       0.0797 |       0.2198 |    0.1357 |    0.1603 |              -0.0246 | -0.0458 |  0.0014 |        0.1556 |        0.1313 |                   0.0243 |     -0.0049 |      0.0548 |        0.7454 |        0.3178 |                   0.4276 |      0.3376 |      0.5328 |        0.0569 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | euc_dmd   |      30 |    1.105  |    1.6807 |              -0.5757 |  -0.7039 | -0.4425 |         0.5515 |         0.5944 |                   -0.0429 |      -0.0861 |       0.0133 |    0.183  |    0.1595 |               0.0236 |  0.0001 |  0.0469 |        0.1865 |        0.1889 |                  -0.0024 |     -0.0436 |      0.0477 |        0.7201 |        0.6325 |                   0.0877 |      0.0141 |      0.1756 |        0.4268 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | euc_unemb |      30 |    0.9346 |    0.1075 |               0.8271 |   0.7375 |  0.9326 |         0.4807 |         0.0336 |                    0.4471 |       0.3851 |       0.5326 |    0.1728 |    0.0718 |               0.101  |  0.0754 |  0.1352 |        0.121  |        0.0375 |                   0.0835 |      0.0483 |      0.1212 |        0.6477 |        0.0549 |                   0.5928 |      0.5279 |      0.6658 |        0.0079 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | frq_dmd   |      30 |    1.6052 |    0.434  |               1.1712 |   1.0164 |  1.385  |         0.7898 |         0.2295 |                    0.5603 |       0.4728 |       0.6787 |    0.201  |    0.1182 |               0.0828 |  0.0687 |  0.095  |        0.2089 |        0.0814 |                   0.1276 |      0.0847 |      0.1733 |        0.8854 |        0.2183 |                   0.6671 |      0.5673 |      0.7918 |        0.028  |
| A_third_a5e-3 | runs/gemma1b_v5/A_s1_abs5e-3 | frq_unemb |      30 |   17.3528 |   17.2451 |               0.1078 |  -0.4342 |  0.7132 |         1.7107 |         1.7092 |                    0.0014 |       0.0001 |       0.0035 |    0.1981 |    0.1464 |               0.0518 |  0.0358 |  0.0671 |        0.5644 |        0.5643 |                   0.0001 |      0      |      0.0002 |        7.6251 |        7.6393 |                  -0.0143 |     -0.2803 |      0.2672 |        0.0078 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | cau_ctx   |      30 |    2.8065 |    2.0803 |               0.7262 |   0.3998 |  1.1603 |         1.1089 |         0.8032 |                    0.3058 |       0.2154 |       0.4107 |    0.1971 |    0.1785 |               0.0186 |  0.0012 |  0.0362 |        0.3653 |        0.2657 |                   0.0996 |      0.0524 |      0.1497 |        1.6805 |        1.0405 |                   0.64   |      0.4152 |      0.8539 |        0.0061 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | cau_dmd   |      30 |    1.2864 |    2.5611 |              -1.2748 |  -1.5065 | -1.0398 |         0.6174 |         0.8276 |                   -0.2101 |      -0.2763 |      -0.1383 |    0.1796 |    0.1992 |              -0.0196 | -0.0496 |  0.0076 |        0.1926 |        0.3048 |                  -0.1122 |     -0.1778 |     -0.0351 |        0.8061 |        0.3844 |                   0.4217 |      0.3389 |      0.5097 |        0.0105 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | cau_unemb |      30 |    0.8693 |    0.1085 |               0.7608 |   0.6648 |  0.8667 |         0.4739 |         0.0695 |                    0.4044 |       0.3352 |       0.4759 |    0.1669 |    0.0819 |               0.085  |  0.0484 |  0.1199 |        0.1492 |        0.0317 |                   0.1175 |      0.0675 |      0.1759 |        0.6249 |        0.0455 |                   0.5793 |      0.4919 |      0.6774 |        0.0095 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | dua_ctx   |      30 |    3.1011 |    2.1893 |               0.9118 |   0.5035 |  1.2773 |         0.4651 |         0.3685 |                    0.0966 |       0.0513 |       0.1409 |    0.0761 |    0.0647 |               0.0114 | -0.0167 |  0.0471 |        0.1314 |        0.1463 |                  -0.0149 |     -0.026  |     -0.0045 |        2.6381 |        1.3418 |                   1.2963 |      0.8267 |      1.6946 |        0.0011 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | dua_dmd   |      30 |    0.978  |    0.6143 |               0.3636 |   0.258  |  0.4813 |         0.3049 |         0.177  |                    0.1279 |       0.0865 |       0.1676 |    0.0619 |    0.0834 |              -0.0215 | -0.0444 |  0.0038 |        0.0494 |        0.135  |                  -0.0856 |     -0.099  |     -0.0732 |        0.8693 |        0.2697 |                   0.5996 |      0.4421 |      0.8105 |        0.0096 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | dua_unemb |      30 |    1.4522 |    0.1394 |               1.3127 |   1.0949 |  1.5777 |         0.3099 |         0.0385 |                    0.2715 |       0.2347 |       0.3119 |    0.0632 |    0.0208 |               0.0425 |  0.0281 |  0.0571 |        0.0396 |        0.0111 |                   0.0285 |      0.0202 |      0.038  |        1.3306 |        0.0837 |                   1.2469 |      1.0313 |      1.5069 |        0.0095 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | euc_ctx   |      30 |    0.9273 |    0.6219 |               0.3054 |   0.2266 |  0.3737 |         0.4692 |         0.3106 |                    0.1586 |       0.1073 |       0.2179 |    0.1499 |    0.1425 |               0.0074 | -0.0195 |  0.0375 |        0.1414 |        0.1192 |                   0.0222 |     -0.0142 |      0.0582 |        0.7153 |        0.2778 |                   0.4375 |      0.3258 |      0.5292 |        0.006  |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | euc_dmd   |      30 |    1.215  |    2.1697 |              -0.9546 |  -1.1818 | -0.7284 |         0.6005 |         0.8059 |                   -0.2054 |      -0.2747 |      -0.131  |    0.1746 |    0.1976 |              -0.0231 | -0.0538 |  0.006  |        0.1855 |        0.2995 |                  -0.114  |     -0.1688 |     -0.0533 |        0.7668 |        0.4482 |                   0.3186 |      0.2519 |      0.38   |        0.0137 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | euc_unemb |      30 |    0.99   |    0.1036 |               0.8864 |   0.7915 |  0.9829 |         0.5391 |         0.0653 |                    0.4738 |       0.402  |       0.5465 |    0.1801 |    0.0818 |               0.0983 |  0.0645 |  0.1334 |        0.1407 |        0.0345 |                   0.1062 |      0.0619 |      0.1615 |        0.6854 |        0.0411 |                   0.6443 |      0.5775 |      0.7144 |        0.0098 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | frq_dmd   |      30 |    8.1177 |    3.3446 |               4.7731 |   3.4105 |  6.097  |         1.6771 |         0.8021 |                    0.875  |       0.731  |       0.9861 |    0.1947 |    0.1036 |               0.0911 |  0.074  |  0.1103 |        0.5283 |        0.2801 |                   0.2482 |      0.1676 |      0.3115 |        3.6088 |        1.5619 |                   2.0469 |      1.5151 |      2.6192 |        0.0082 |
| A_third_a5e-3 | runs/gemma1b_v5/A_s2_abs5e-3 | frq_unemb |      30 |    8.6042 |   18.1314 |              -9.5272 | -10.2974 | -8.3933 |         1.7875 |         1.8039 |                   -0.0164 |      -0.0364 |      -0.0046 |    0.1347 |    0.0839 |               0.0508 |  0.026  |  0.0754 |        0.5625 |        0.5737 |                  -0.0112 |     -0.0275 |     -0.0027 |        4.0474 |        7.9472 |                  -3.8998 |     -4.4304 |     -3.3876 |        0.0094 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | cau_ctx   |      30 |    1.7971 |    5.6965 |              -3.8995 |  -4.607  | -3.2492 |         1.4677 |         2.3143 |                   -0.8466 |      -1.1677 |      -0.5232 |    0.2771 |    0.3138 |              -0.0367 | -0.1241 |  0.0501 |        0.5009 |        0.4215 |                   0.0793 |     -0.0146 |      0.1698 |        0.2801 |        0.496  |                  -0.2159 |     -0.3028 |     -0.1428 |        0.0004 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | cau_dmd   |      30 |    1.9753 |    7.1167 |              -5.1414 |  -6.3082 | -4.1975 |         1.6262 |         3.0146 |                   -1.3884 |      -1.874  |      -0.8824 |    0.4217 |    0.4284 |              -0.0067 | -0.1043 |  0.083  |        0.2182 |        0.0667 |                   0.1515 |      0.0716 |      0.2399 |        0.1349 |        0.1238 |                   0.011  |     -0.0248 |      0.0474 |        0      |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | cau_unemb |      30 |    0.6107 |    0.1324 |               0.4783 |   0.3538 |  0.6113 |         0.5265 |         0.1145 |                    0.412  |       0.2929 |       0.5502 |    0.103  |    0.0669 |               0.0361 | -0.0119 |  0.098  |        0.2214 |        0.0297 |                   0.1917 |      0.1323 |      0.2606 |        0.1389 |        0.0178 |                   0.121  |      0.0931 |      0.1508 |        0.0003 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | dua_ctx   |      30 |    2.1891 |    2.2911 |              -0.102  |  -0.3306 |  0.1557 |         0.4048 |         0.393  |                    0.0118 |      -0.0408 |       0.0583 |    0.0349 |    0.0401 |              -0.0052 | -0.0443 |  0.0325 |        0.15   |        0.0962 |                   0.0538 |      0.0295 |      0.0755 |        1.4338 |        0.9785 |                   0.4553 |      0.2724 |      0.667  |        0.0001 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | dua_dmd   |      30 |    2.063  |    3.7071 |              -1.6441 |  -2.1086 | -1.2307 |         0.4225 |         0.6778 |                   -0.2553 |      -0.4401 |      -0.1167 |    0.0565 |    0.0655 |              -0.009  | -0.0376 |  0.022  |        0.0628 |        0.0695 |                  -0.0066 |     -0.017  |      0.0066 |        1.0059 |        0.5439 |                   0.462  |      0.3101 |      0.6451 |        0      |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | dua_unemb |      30 |    1.7761 |    0.4528 |               1.3233 |   1.0867 |  1.58   |         0.3589 |         0.1068 |                    0.2521 |       0.1751 |       0.3451 |    0.0444 |    0.0121 |               0.0322 |  0.0047 |  0.0711 |        0.0729 |        0.0567 |                   0.0162 |     -0.0058 |      0.0438 |        1.2953 |        0.2437 |                   1.0516 |      0.797  |      1.3211 |        0.001  |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | euc_ctx   |      30 |    0.9034 |    1.0959 |              -0.1925 |  -0.4848 |  0.1002 |         0.7513 |         0.8348 |                   -0.0835 |      -0.34   |       0.1613 |    0.2033 |    0.2255 |              -0.0222 | -0.1017 |  0.0568 |        0.2853 |        0.0735 |                   0.2118 |      0.1238 |      0.3021 |        0.1851 |        0.0795 |                   0.1055 |      0.0733 |      0.1396 |        0.0002 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | euc_dmd   |      30 |    1.3055 |    5.6618 |              -4.3563 |  -5.3679 | -3.4689 |         1.1495 |         2.738  |                   -1.5885 |      -1.9636 |      -1.2499 |    0.3297 |    0.3941 |              -0.0644 | -0.1593 |  0.0288 |        0.2077 |        0.0649 |                   0.1429 |      0.0751 |      0.2169 |        0.1276 |        0.1048 |                   0.0228 |     -0.0091 |      0.0557 |        0.0001 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | euc_unemb |      30 |    0.6973 |    0.1748 |               0.5226 |   0.3469 |  0.7383 |         0.5914 |         0.1495 |                    0.442  |       0.2765 |       0.6515 |    0.1097 |    0.0827 |               0.027  | -0.0241 |  0.084  |        0.1783 |        0.0347 |                   0.1436 |      0.093  |      0.196  |        0.1556 |        0.0248 |                   0.1308 |      0.0995 |      0.1646 |        0.0003 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | frq_dmd   |      30 |    2.6042 |    0.4602 |               2.144  |   1.9194 |  2.3234 |         2.241  |         0.3657 |                    1.8753 |       1.7464 |       1.9892 |    0.1043 |    0.0104 |               0.0939 |  0.034  |  0.156  |        0.0782 |        0.1491 |                  -0.0709 |     -0.1183 |     -0.0222 |        0.0573 |        0.0592 |                  -0.002  |     -0.0312 |      0.0258 |        0.0003 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s0_abs5e-3 | frq_unemb |      30 |    2.5915 |    2.5559 |               0.0355 |  -0.5717 |  0.5403 |         2.1962 |         1.7741 |                    0.4221 |       0.1466 |       0.6926 |    0.2417 |    0.0015 |               0.2402 |  0.1609 |  0.3172 |        0.2744 |        0.6121 |                  -0.3378 |     -0.4257 |     -0.245  |        0.2759 |        0.2899 |                  -0.014  |     -0.0666 |      0.043  |        0.0003 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | cau_ctx   |      30 |    2.3683 |    1.5629 |               0.8055 |   0.3365 |  1.2662 |         1.9637 |         1.1405 |                    0.8233 |       0.4531 |       1.1828 |    0.2752 |    0.2471 |               0.0282 | -0.0719 |  0.1314 |        0.6555 |        0.2857 |                   0.3699 |      0.2719 |      0.4661 |        0.2633 |        0.1947 |                   0.0686 |      0.0275 |      0.108  |        0.0008 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | cau_dmd   |      30 |    2.1026 |    5.0325 |              -2.9299 |  -3.8931 | -1.9741 |         1.6124 |         2.4395 |                   -0.8271 |      -1.3454 |      -0.3386 |    0.3248 |    0.356  |              -0.0312 | -0.1214 |  0.054  |        0.1702 |        0.0596 |                   0.1106 |      0.0488 |      0.1798 |        0.1022 |        0.0825 |                   0.0196 |      0.0009 |      0.0392 |        0.0006 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | cau_unemb |      30 |    0.5045 |    0.1798 |               0.3247 |   0.2066 |  0.458  |         0.4446 |         0.1545 |                    0.2901 |       0.1715 |       0.4233 |    0.1329 |    0.0811 |               0.0518 | -0.0097 |  0.1223 |        0.1615 |        0.0408 |                   0.1207 |      0.0774 |      0.1697 |        0.1028 |        0.0173 |                   0.0855 |      0.064  |      0.1088 |        0.0018 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | dua_ctx   |      29 |    2.1857 |    1.7651 |               0.4206 |   0.0988 |  0.7359 |         0.4406 |         0.3021 |                    0.1385 |       0.0932 |       0.1874 |    0.0211 |    0.0318 |              -0.0107 | -0.03   |  0.0009 |        0.2484 |        0.1438 |                   0.1046 |      0.0834 |      0.1279 |        1.3106 |        0.7557 |                   0.5549 |      0.3881 |      0.7205 |        0.0002 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | dua_dmd   |      30 |    2.2706 |    3.2813 |              -1.0107 |  -1.6239 | -0.5044 |         0.5333 |         0.5561 |                   -0.0228 |      -0.1101 |       0.0584 |    0.0856 |    0.0777 |               0.0079 | -0.0186 |  0.0444 |        0.0433 |        0.0618 |                  -0.0185 |     -0.0292 |     -0.0075 |        0.8946 |        0.4331 |                   0.4615 |      0.3568 |      0.5662 |        0.0042 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | dua_unemb |      30 |    1.4809 |    0.5768 |               0.9042 |   0.706  |  1.1045 |         0.3201 |         0.121  |                    0.1991 |       0.1326 |       0.2801 |    0.0158 |    0.0127 |               0.0032 |  0.0009 |  0.0058 |        0.0704 |        0.0671 |                   0.0033 |     -0.0125 |      0.02   |        1.0597 |        0.2628 |                   0.797  |      0.6132 |      0.9825 |        0.0023 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | euc_ctx   |      30 |    0.7893 |    0.5533 |               0.236  |   0.018  |  0.4735 |         0.6812 |         0.4234 |                    0.2578 |       0.061  |       0.4671 |    0.1691 |    0.1544 |               0.0148 | -0.0679 |  0.1015 |        0.2506 |        0.0622 |                   0.1883 |      0.1222 |      0.2543 |        0.136  |        0.0643 |                   0.0716 |      0.0522 |      0.0942 |        0.0009 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | euc_dmd   |      30 |    1.6229 |    3.9805 |              -2.3576 |  -3.2097 | -1.6014 |         1.286  |         2.1009 |                   -0.8149 |      -1.3141 |      -0.3776 |    0.3069 |    0.3393 |              -0.0324 | -0.1247 |  0.0639 |        0.1468 |        0.0583 |                   0.0885 |      0.031  |      0.1541 |        0.1063 |        0.0756 |                   0.0307 |      0.0181 |      0.0442 |        0.0006 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | euc_unemb |      30 |    0.6046 |    0.1931 |               0.4115 |   0.2587 |  0.5871 |         0.5146 |         0.1612 |                    0.3534 |       0.2054 |       0.5169 |    0.1895 |    0.0758 |               0.1137 |  0.0278 |  0.202  |        0.0986 |        0.05   |                   0.0485 |      0.0099 |      0.0971 |        0.1126 |        0.0248 |                   0.0878 |      0.0659 |      0.1142 |        0.0019 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | frq_dmd   |      30 |    2.2306 |    4.799  |              -2.5684 |  -3.2393 | -1.9182 |         1.9205 |         2.2737 |                   -0.3532 |      -0.5687 |      -0.138  |    0.1005 |    0.0357 |               0.0648 |  0.0128 |  0.1222 |        0.0541 |        0.1008 |                  -0.0467 |     -0.0785 |     -0.0157 |        0.02   |        0.0968 |                  -0.0768 |     -0.1127 |     -0.0445 |        0.0006 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s1_abs5e-3 | frq_unemb |      30 |    2.3141 |    4.7039 |              -2.3899 |  -3.0175 | -1.8035 |         2.0026 |         2.8743 |                   -0.8717 |      -1.174  |      -0.5851 |    0.1635 |    0.0063 |               0.1571 |  0.0925 |  0.2243 |        0.0819 |        0.8373 |                  -0.7555 |     -0.8126 |     -0.6863 |        0.1449 |        0.4338 |                  -0.2889 |     -0.3584 |     -0.2214 |        0.0016 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | cau_ctx   |      30 |    1.7776 |    4.0876 |              -2.31   |  -2.7694 | -1.8427 |         1.4023 |         2.3207 |                   -0.9184 |      -1.2357 |      -0.584  |    0.2849 |    0.3445 |              -0.0596 | -0.1373 |  0.0105 |        0.5163 |        0.4963 |                   0.02   |     -0.0875 |      0.1282 |        0.3467 |        0.4753 |                  -0.1286 |     -0.1923 |     -0.07   |        0.0007 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | cau_dmd   |      30 |    1.8755 |    4.8648 |              -2.9893 |  -3.7763 | -2.1966 |         1.4875 |         2.5285 |                   -1.041  |      -1.4132 |      -0.6793 |    0.3374 |    0.3459 |              -0.0085 | -0.0889 |  0.0705 |        0.17   |        0.0741 |                   0.0959 |      0.0261 |      0.1786 |        0.1271 |        0.0492 |                   0.0779 |      0.0529 |      0.1022 |        0      |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | cau_unemb |      30 |    0.737  |    0.1295 |               0.6075 |   0.4269 |  0.8141 |         0.6511 |         0.1064 |                    0.5448 |       0.3701 |       0.739  |    0.1999 |    0.0697 |               0.1302 |  0.0557 |  0.2013 |        0.2141 |        0.0362 |                   0.1779 |      0.1165 |      0.2393 |        0.1497 |        0.0238 |                   0.1258 |      0.0888 |      0.1753 |        0.0002 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | dua_ctx   |      30 |    2.3899 |    2.1751 |               0.2149 |  -0.1148 |  0.5825 |         0.4154 |         0.385  |                    0.0305 |      -0.0115 |       0.0718 |    0.0493 |    0.0372 |               0.0121 | -0.0128 |  0.0447 |        0.1601 |        0.1238 |                   0.0363 |      0.0171 |      0.0548 |        1.6537 |        0.965  |                   0.6887 |      0.4104 |      1.0057 |        0.019  |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | dua_dmd   |      30 |    2.3305 |    3.2244 |              -0.894  |  -1.3022 | -0.4952 |         0.4955 |         0.5541 |                   -0.0586 |      -0.1366 |       0.022  |    0.0666 |    0.0882 |              -0.0216 | -0.0639 |  0.0207 |        0.0527 |        0.078  |                  -0.0253 |     -0.0376 |     -0.0131 |        1.1369 |        0.5411 |                   0.5958 |      0.4334 |      0.7986 |        0.001  |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | dua_unemb |      30 |    1.904  |    0.3856 |               1.5183 |   1.1982 |  1.8549 |         0.3556 |         0.0978 |                    0.2577 |       0.211  |       0.3125 |    0.039  |    0.0217 |               0.0173 |  0.0086 |  0.0298 |        0.0715 |        0.0576 |                   0.0139 |     -0.0027 |      0.0308 |        1.4365 |        0.2049 |                   1.2316 |      0.9032 |      1.6066 |        0.0003 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | euc_ctx   |      30 |    1.204  |    1.0983 |               0.1057 |  -0.1898 |  0.4433 |         0.9752 |         0.8071 |                    0.168  |      -0.1115 |       0.4563 |    0.2385 |    0.2374 |               0.0011 | -0.0864 |  0.0842 |        0.2889 |        0.1078 |                   0.1811 |      0.0971 |      0.2623 |        0.2221 |        0.1075 |                   0.1146 |      0.0746 |      0.1592 |        0.0006 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | euc_dmd   |      30 |    1.6778 |    4.4214 |              -2.7436 |  -3.3972 | -2.1015 |         1.3002 |         2.389  |                   -1.0888 |      -1.4424 |      -0.7407 |    0.3174 |    0.3415 |              -0.0241 | -0.1136 |  0.07   |        0.1643 |        0.0774 |                   0.0869 |      0.0253 |      0.1571 |        0.1519 |        0.0693 |                   0.0827 |      0.0556 |      0.1102 |        0.0001 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | euc_unemb |      30 |    0.8201 |    0.1269 |               0.6932 |   0.5037 |  0.9296 |         0.7124 |         0.1026 |                    0.6098 |       0.4305 |       0.8244 |    0.2035 |    0.0728 |               0.1308 |  0.0564 |  0.2089 |        0.1588 |        0.0435 |                   0.1153 |      0.0583 |      0.1833 |        0.1612 |        0.0238 |                   0.1374 |      0.0986 |      0.1897 |        0.0002 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | frq_dmd   |      30 |   12.174  |   22.0309 |              -9.857  | -10.8909 | -8.8214 |         3.947  |         4.0176 |                   -0.0706 |      -0.1412 |      -0.0183 |    0.2074 |    0.183  |               0.0244 | -0.0548 |  0.0993 |        0.9059 |        0.0851 |                   0.8208 |      0.7743 |      0.8641 |        1.1549 |        0.7519 |                   0.4029 |      0.2814 |      0.5392 |        0.3333 |
| C_third_a5e-3 | runs/gemma1b_v5/C_s2_abs5e-3 | frq_unemb |      30 |    2.1805 |    0.797  |               1.3836 |   1.1093 |  1.6315 |         1.8598 |         0.6953 |                    1.1645 |       0.9313 |       1.3731 |    0.1386 |    0.0066 |               0.132  |  0.0714 |  0.1921 |        0.0483 |        0.3282 |                  -0.2799 |     -0.3552 |     -0.2039 |        0.1464 |        0.1413 |                   0.0052 |     -0.0285 |      0.0428 |        0.0002 |

