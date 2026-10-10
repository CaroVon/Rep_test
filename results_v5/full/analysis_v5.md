# analysis_v5 (auto-generated)

convention: diff = a - b; lower is better for every metric; diff > 0 means b (adaptive) is better.

## metric_panel

| group                 | run                             | pair(a-b)             | metric   |   diff_mean |        lo |        hi |   n |
|:----------------------|:--------------------------------|:----------------------|:---------|------------:|----------:|----------:|----:|
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | euc_dmd - dua_dmd     | kl       |     0.16235 |   0.01915 |   0.31103 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | euc_dmd - dua_dmd     | kl_park  |     0.29029 |   0.21279 |   0.37294 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | euc_dmd - dua_dmd     | rd       |     0.12746 |   0.09589 |   0.16089 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | euc_dmd - dua_dmd     | cf_dev   |     0.11495 |   0.07777 |   0.16546 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | euc_dmd - dua_dmd     | kl_neu   |    -0.10327 |  -0.23684 |   0.05615 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | euc_dmd - dua_dmd     | kl       |     0.11344 |  -0.06632 |   0.30918 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | euc_dmd - dua_dmd     | kl_park  |     0.29947 |   0.20929 |   0.40681 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | euc_dmd - dua_dmd     | rd       |     0.12719 |   0.09922 |   0.16214 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | euc_dmd - dua_dmd     | cf_dev   |     0.15713 |   0.10763 |   0.21939 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | euc_dmd - dua_dmd     | kl_neu   |    -0.23305 |  -0.40411 |  -0.06531 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | euc_dmd - dua_dmd     | kl       |     0.24826 |   0.0511  |   0.48715 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | euc_dmd - dua_dmd     | kl_park  |     0.28075 |   0.19718 |   0.37075 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | euc_dmd - dua_dmd     | rd       |     0.11174 |   0.08184 |   0.14066 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | euc_dmd - dua_dmd     | cf_dev   |     0.11736 |   0.07835 |   0.16915 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | euc_dmd - dua_dmd     | kl_neu   |    -0.06783 |  -0.24365 |   0.09773 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | cau_unemb - dua_unemb | kl       |    -0.62962 |  -0.88896 |  -0.38286 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | cau_unemb - dua_unemb | kl_park  |     0.1589  |   0.09233 |   0.23382 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | cau_unemb - dua_unemb | rd       |     0.08497 |   0.0553  |   0.11783 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | cau_unemb - dua_unemb | cf_dev   |     0.06711 |   0.03382 |   0.10707 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | cau_unemb - dua_unemb | kl_neu   |    -0.70402 |  -0.96209 |  -0.45909 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | cau_unemb - dua_unemb | kl       |    -0.63936 |  -0.8431  |  -0.41625 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | cau_unemb - dua_unemb | kl_park  |     0.18145 |   0.10724 |   0.26872 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | cau_unemb - dua_unemb | rd       |     0.10319 |   0.07706 |   0.13629 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | cau_unemb - dua_unemb | cf_dev   |     0.10872 |   0.0543  |   0.17672 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | cau_unemb - dua_unemb | kl_neu   |    -0.79355 |  -1.01762 |  -0.56569 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | cau_unemb - dua_unemb | kl       |    -0.5804  |  -0.85059 |  -0.37998 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | cau_unemb - dua_unemb | kl_park  |     0.1546  |   0.09475 |   0.20827 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | cau_unemb - dua_unemb | rd       |     0.09379 |   0.06028 |   0.12731 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | cau_unemb - dua_unemb | cf_dev   |     0.08559 |   0.04439 |   0.13749 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | cau_unemb - dua_unemb | kl_neu   |    -0.69566 |  -0.94743 |  -0.5071  |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | frq_unemb - dua_unemb | kl       |    14.2801  |  13.1016  |  15.2816  |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | frq_unemb - dua_unemb | kl_park  |     1.50248 |   1.41382 |   1.58981 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | frq_unemb - dua_unemb | rd       |     0.12538 |   0.10266 |   0.14351 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | frq_unemb - dua_unemb | cf_dev   |     0.52676 |   0.47    |   0.57967 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | frq_unemb - dua_unemb | kl_neu   |     5.61904 |   4.6728  |   6.6298  |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | frq_unemb - dua_unemb | kl       |    15.6409  |  14.0003  |  17.4012  |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | frq_unemb - dua_unemb | kl_park  |     1.46237 |   1.37013 |   1.56826 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | frq_unemb - dua_unemb | rd       |     0.13075 |   0.11208 |   0.14783 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | frq_unemb - dua_unemb | cf_dev   |     0.54898 |   0.50563 |   0.59746 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | frq_unemb - dua_unemb | kl_neu   |     5.7681  |   5.07162 |   6.85059 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | frq_unemb - dua_unemb | kl       |     7.25771 |   5.8705  |   8.34443 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | frq_unemb - dua_unemb | kl_park  |     1.4741  |   1.37823 |   1.56154 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | frq_unemb - dua_unemb | rd       |     0.08325 |   0.06213 |   0.10522 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | frq_unemb - dua_unemb | cf_dev   |     0.51822 |   0.44971 |   0.58566 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | frq_unemb - dua_unemb | kl_neu   |     2.80875 |   1.7572  |   3.88438 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | cau_unemb - frq_unemb | kl       |   -14.9097  | -15.9053  | -13.711   |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | cau_unemb - frq_unemb | kl_park  |    -1.34358 |  -1.40706 |  -1.27452 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | cau_unemb - frq_unemb | rd       |    -0.04041 |  -0.07123 |  -0.00715 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | cau_unemb - frq_unemb | cf_dev   |    -0.45965 |  -0.51686 |  -0.40071 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | cau_unemb - frq_unemb | kl_neu   |    -6.32307 |  -7.21607 |  -5.4189  |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | cau_unemb - frq_unemb | kl       |   -16.2803  | -17.934   | -14.6453  |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | cau_unemb - frq_unemb | kl_park  |    -1.28092 |  -1.33804 |  -1.22257 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | cau_unemb - frq_unemb | rd       |    -0.02756 |  -0.05476 |   0.0061  |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | cau_unemb - frq_unemb | cf_dev   |    -0.44026 |  -0.48247 |  -0.39534 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | cau_unemb - frq_unemb | kl_neu   |    -6.56165 |  -7.39905 |  -5.93497 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | cau_unemb - frq_unemb | kl       |    -7.83811 |  -8.8525  |  -6.53273 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | cau_unemb - frq_unemb | kl_park  |    -1.31951 |  -1.39558 |  -1.23817 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | cau_unemb - frq_unemb | rd       |     0.01055 |  -0.02667 |   0.04186 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | cau_unemb - frq_unemb | cf_dev   |    -0.43263 |  -0.51432 |  -0.34881 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | cau_unemb - frq_unemb | kl_neu   |    -3.50441 |  -4.40723 |  -2.59066 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | frq_dmd - dua_dmd     | kl       |     1.45105 |   1.0377  |   1.97667 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | frq_dmd - dua_dmd     | kl_park  |     0.78412 |   0.63493 |   0.92984 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | frq_dmd - dua_dmd     | rd       |     0.1577  |   0.12811 |   0.19131 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | frq_dmd - dua_dmd     | cf_dev   |     0.3169  |   0.24799 |   0.38349 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | frq_dmd - dua_dmd     | kl_neu   |     0.58958 |   0.34858 |   0.88917 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | frq_dmd - dua_dmd     | kl       |     0.67378 |   0.44114 |   0.94442 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | frq_dmd - dua_dmd     | kl_park  |     0.56129 |   0.44351 |   0.69075 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | frq_dmd - dua_dmd     | rd       |     0.14981 |   0.1251  |   0.17664 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | frq_dmd - dua_dmd     | cf_dev   |     0.17286 |   0.13791 |   0.21346 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | frq_dmd - dua_dmd     | kl_neu   |    -0.07689 |  -0.25621 |   0.10389 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | frq_dmd - dua_dmd     | kl       |     6.73837 |   5.07503 |   8.31415 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | frq_dmd - dua_dmd     | kl_park  |     1.33122 |   1.15583 |   1.47097 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | frq_dmd - dua_dmd     | rd       |     0.12582 |   0.09677 |   0.15412 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | frq_dmd - dua_dmd     | cf_dev   |     0.47029 |   0.38966 |   0.55115 |  60 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | frq_dmd - dua_dmd     | kl_neu   |     2.65186 |   1.87563 |   3.50442 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | euc_dmd - dua_dmd     | kl       |    -0.80284 |  -1.06708 |  -0.5261  |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | euc_dmd - dua_dmd     | kl_park  |     0.64183 |   0.47437 |   0.80292 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | euc_dmd - dua_dmd     | rd       |     0.2683  |   0.20805 |   0.3261  |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | euc_dmd - dua_dmd     | cf_dev   |     0.10071 |   0.05809 |   0.15115 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | euc_dmd - dua_dmd     | kl_neu   |    -0.88161 |  -1.03798 |  -0.72429 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | euc_dmd - dua_dmd     | kl       |    -0.91145 |  -1.25394 |  -0.59725 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | euc_dmd - dua_dmd     | kl_park  |     0.72134 |   0.54881 |   0.90244 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | euc_dmd - dua_dmd     | rd       |     0.19326 |   0.13543 |   0.25774 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | euc_dmd - dua_dmd     | cf_dev   |     0.0732  |   0.03382 |   0.11885 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | euc_dmd - dua_dmd     | kl_neu   |    -1.01803 |  -1.19339 |  -0.84397 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | euc_dmd - dua_dmd     | kl       |    -0.75099 |  -1.0459  |  -0.46318 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | euc_dmd - dua_dmd     | kl_park  |     0.87684 |   0.69456 |   1.07415 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | euc_dmd - dua_dmd     | rd       |     0.26673 |   0.20651 |   0.32726 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | euc_dmd - dua_dmd     | cf_dev   |     0.12329 |   0.07252 |   0.17792 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | euc_dmd - dua_dmd     | kl_neu   |    -1.05975 |  -1.22092 |  -0.8988  |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | cau_unemb - dua_unemb | kl       |    -1.17025 |  -1.39293 |  -0.96488 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | cau_unemb - dua_unemb | kl_park  |     0.14836 |   0.07745 |   0.22895 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | cau_unemb - dua_unemb | rd       |     0.06856 |   0.0331  |   0.10847 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | cau_unemb - dua_unemb | cf_dev   |     0.13132 |   0.08487 |   0.17963 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | cau_unemb - dua_unemb | kl_neu   |    -1.17172 |  -1.37542 |  -0.97946 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | cau_unemb - dua_unemb | kl       |    -1.24094 |  -1.48131 |  -1.01044 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | cau_unemb - dua_unemb | kl_park  |     0.13129 |   0.05863 |   0.20703 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | cau_unemb - dua_unemb | rd       |     0.09483 |   0.04689 |   0.14403 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | cau_unemb - dua_unemb | cf_dev   |     0.10259 |   0.06433 |   0.14058 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | cau_unemb - dua_unemb | kl_neu   |    -1.22273 |  -1.43582 |  -1.02835 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | cau_unemb - dua_unemb | kl       |    -1.10674 |  -1.33706 |  -0.88558 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | cau_unemb - dua_unemb | kl_park  |     0.29078 |   0.18734 |   0.40834 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | cau_unemb - dua_unemb | rd       |     0.15054 |   0.10308 |   0.20382 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | cau_unemb - dua_unemb | cf_dev   |     0.15501 |   0.10667 |   0.20721 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | cau_unemb - dua_unemb | kl_neu   |    -1.23158 |  -1.44447 |  -1.04005 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | frq_unemb - dua_unemb | kl       |     0.66426 |   0.39972 |   0.92206 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | frq_unemb - dua_unemb | kl_park  |     1.69774 |   1.54823 |   1.8425  |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | frq_unemb - dua_unemb | rd       |     0.24884 |   0.18618 |   0.3045  |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | frq_unemb - dua_unemb | cf_dev   |     0.14707 |   0.10261 |   0.19861 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | frq_unemb - dua_unemb | kl_neu   |    -1.06581 |  -1.26476 |  -0.88094 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | frq_unemb - dua_unemb | kl       |     0.52826 |   0.25746 |   0.79523 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | frq_unemb - dua_unemb | kl_park  |     1.63995 |   1.54183 |   1.74176 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | frq_unemb - dua_unemb | rd       |     0.11468 |   0.05802 |   0.17428 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | frq_unemb - dua_unemb | cf_dev   |     0.00116 |  -0.03431 |   0.03883 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | frq_unemb - dua_unemb | kl_neu   |    -1.19039 |  -1.41655 |  -0.97407 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | frq_unemb - dua_unemb | kl       |     0.49873 |   0.18982 |   0.8263  |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | frq_unemb - dua_unemb | kl_park  |     1.62503 |   1.47688 |   1.78648 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | frq_unemb - dua_unemb | rd       |     0.10289 |   0.05565 |   0.15444 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | frq_unemb - dua_unemb | cf_dev   |     0.01252 |  -0.02399 |   0.06105 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | frq_unemb - dua_unemb | kl_neu   |    -1.22805 |  -1.44488 |  -1.01964 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | cau_unemb - frq_unemb | kl       |    -1.83452 |  -2.02266 |  -1.63302 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | cau_unemb - frq_unemb | kl_park  |    -1.54938 |  -1.72247 |  -1.35434 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | cau_unemb - frq_unemb | rd       |    -0.18028 |  -0.23827 |  -0.12094 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | cau_unemb - frq_unemb | cf_dev   |    -0.01575 |  -0.08486 |   0.05045 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | cau_unemb - frq_unemb | kl_neu   |    -0.10591 |  -0.14679 |  -0.06634 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | cau_unemb - frq_unemb | kl       |    -1.7692  |  -1.89796 |  -1.63314 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | cau_unemb - frq_unemb | kl_park  |    -1.50866 |  -1.62925 |  -1.38343 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | cau_unemb - frq_unemb | rd       |    -0.01986 |  -0.09238 |   0.05279 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | cau_unemb - frq_unemb | cf_dev   |     0.10143 |   0.05996 |   0.14155 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | cau_unemb - frq_unemb | kl_neu   |    -0.03234 |  -0.06514 |   0.00437 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | cau_unemb - frq_unemb | kl       |    -1.60547 |  -1.83584 |  -1.37589 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | cau_unemb - frq_unemb | kl_park  |    -1.33425 |  -1.53731 |  -1.1335  |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | cau_unemb - frq_unemb | rd       |     0.04765 |  -0.0244  |   0.12205 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | cau_unemb - frq_unemb | cf_dev   |     0.14249 |   0.07973 |   0.19823 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | cau_unemb - frq_unemb | kl_neu   |    -0.00353 |  -0.03748 |   0.03361 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | frq_dmd - dua_dmd     | kl       |     0.50065 |   0.25628 |   0.74722 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | frq_dmd - dua_dmd     | kl_park  |     1.76539 |   1.6807  |   1.85861 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | frq_dmd - dua_dmd     | rd       |     0.05653 |   0.00716 |   0.10383 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | frq_dmd - dua_dmd     | cf_dev   |     0.01685 |   0.00071 |   0.04066 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | frq_dmd - dua_dmd     | kl_neu   |    -0.97024 |  -1.15111 |  -0.80184 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | frq_dmd - dua_dmd     | kl       |    -0.34442 |  -0.76077 |   0.04891 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | frq_dmd - dua_dmd     | kl_park  |     1.36483 |   1.17368 |   1.52792 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | frq_dmd - dua_dmd     | rd       |     0.03879 |  -0.01782 |   0.09613 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | frq_dmd - dua_dmd     | cf_dev   |     0.01518 |   0.00713 |   0.02274 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | frq_dmd - dua_dmd     | kl_neu   |    -1.1233  |  -1.32021 |  -0.9345  |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | frq_dmd - dua_dmd     | kl       |     9.5587  |   8.47553 |  10.7271  |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | frq_dmd - dua_dmd     | kl_park  |     3.46169 |   3.29794 |   3.6334  |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | frq_dmd - dua_dmd     | rd       |     0.15303 |   0.10197 |   0.20202 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | frq_dmd - dua_dmd     | cf_dev   |     0.85838 |   0.83695 |   0.87955 |  60 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | frq_dmd - dua_dmd     | kl_neu   |    -0.06548 |  -0.23111 |   0.11969 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | euc_dmd - dua_dmd     | kl       |    -0.8416  |  -1.15007 |  -0.53785 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | euc_dmd - dua_dmd     | kl_park  |     0.73633 |   0.56805 |   0.90295 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | euc_dmd - dua_dmd     | rd       |     0.29457 |   0.23559 |   0.35034 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | euc_dmd - dua_dmd     | cf_dev   |     0.12057 |   0.07214 |   0.17825 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | euc_dmd - dua_dmd     | kl_neu   |    -1.08597 |  -1.30606 |  -0.88878 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | euc_dmd - dua_dmd     | kl       |    -0.60461 |  -0.96765 |  -0.25467 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | euc_dmd - dua_dmd     | kl_park  |     1.0966  |   0.92578 |   1.26142 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | euc_dmd - dua_dmd     | rd       |     0.29295 |   0.22971 |   0.35046 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | euc_dmd - dua_dmd     | cf_dev   |     0.10931 |   0.069   |   0.15171 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | euc_dmd - dua_dmd     | kl_neu   |    -1.0864  |  -1.30398 |  -0.87893 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | euc_dmd - dua_dmd     | kl       |    -0.59487 |  -1.01955 |  -0.18837 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | euc_dmd - dua_dmd     | kl_park  |     0.80526 |   0.59902 |   1.02163 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | euc_dmd - dua_dmd     | rd       |     0.22493 |   0.16392 |   0.28388 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | euc_dmd - dua_dmd     | cf_dev   |     0.1493  |   0.09356 |   0.21106 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | euc_dmd - dua_dmd     | kl_neu   |    -1.06617 |  -1.31175 |  -0.83964 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | cau_unemb - dua_unemb | kl       |    -1.33536 |  -1.5846  |  -1.09254 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | cau_unemb - dua_unemb | kl_park  |     0.10443 |   0.01571 |   0.21207 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | cau_unemb - dua_unemb | rd       |     0.1049  |   0.05333 |   0.15904 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | cau_unemb - dua_unemb | cf_dev   |     0.08152 |   0.03415 |   0.12798 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | cau_unemb - dua_unemb | kl_neu   |    -1.23164 |  -1.45161 |  -1.01813 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | cau_unemb - dua_unemb | kl       |    -1.11275 |  -1.37588 |  -0.85335 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | cau_unemb - dua_unemb | kl_park  |     0.30972 |   0.19253 |   0.43919 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | cau_unemb - dua_unemb | rd       |     0.14008 |   0.09409 |   0.18622 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | cau_unemb - dua_unemb | cf_dev   |     0.1645  |   0.11977 |   0.21303 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | cau_unemb - dua_unemb | kl_neu   |    -1.26129 |  -1.49686 |  -1.03569 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | cau_unemb - dua_unemb | kl       |    -1.09324 |  -1.38846 |  -0.79185 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | cau_unemb - dua_unemb | kl_park  |     0.2029  |   0.09508 |   0.32124 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | cau_unemb - dua_unemb | rd       |     0.09217 |   0.05291 |   0.13571 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | cau_unemb - dua_unemb | cf_dev   |     0.14452 |   0.09511 |   0.19784 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | cau_unemb - dua_unemb | kl_neu   |    -1.21249 |  -1.48258 |  -0.96699 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | frq_unemb - dua_unemb | kl       |     1.88765 |   1.31253 |   2.45522 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | frq_unemb - dua_unemb | kl_park  |     2.24707 |   1.98931 |   2.49372 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | frq_unemb - dua_unemb | rd       |     0.20114 |   0.14217 |   0.25968 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | frq_unemb - dua_unemb | cf_dev   |     0.42776 |   0.34249 |   0.51535 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | frq_unemb - dua_unemb | kl_neu   |    -0.96006 |  -1.17894 |  -0.76259 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | frq_unemb - dua_unemb | kl       |     0.60159 |   0.31276 |   0.90496 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | frq_unemb - dua_unemb | kl_park  |     1.74203 |   1.60985 |   1.86426 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | frq_unemb - dua_unemb | rd       |     0.18761 |   0.13763 |   0.23518 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | frq_unemb - dua_unemb | cf_dev   |     0.11256 |   0.06933 |   0.1581  |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | frq_unemb - dua_unemb | kl_neu   |    -1.19307 |  -1.41699 |  -0.96736 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | frq_unemb - dua_unemb | kl       |     1.20036 |   0.74691 |   1.65258 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | frq_unemb - dua_unemb | kl_park  |     2.08013 |   1.86544 |   2.28264 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | frq_unemb - dua_unemb | rd       |     0.23201 |   0.18185 |   0.28442 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | frq_unemb - dua_unemb | cf_dev   |     0.31534 |   0.2498  |   0.38342 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | frq_unemb - dua_unemb | kl_neu   |    -1.04713 |  -1.30545 |  -0.82646 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | cau_unemb - frq_unemb | kl       |    -3.223   |  -3.80894 |  -2.64922 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | cau_unemb - frq_unemb | kl_park  |    -2.14264 |  -2.43893 |  -1.82959 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | cau_unemb - frq_unemb | rd       |    -0.09623 |  -0.17299 |  -0.01154 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | cau_unemb - frq_unemb | cf_dev   |    -0.34624 |  -0.4379  |  -0.24779 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | cau_unemb - frq_unemb | kl_neu   |    -0.27159 |  -0.34542 |  -0.20219 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | cau_unemb - frq_unemb | kl       |    -1.71434 |  -1.89985 |  -1.51893 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | cau_unemb - frq_unemb | kl_park  |    -1.43231 |  -1.60283 |  -1.25965 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | cau_unemb - frq_unemb | rd       |    -0.04753 |  -0.11649 |   0.01777 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | cau_unemb - frq_unemb | cf_dev   |     0.05194 |  -0.01024 |   0.11474 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | cau_unemb - frq_unemb | kl_neu   |    -0.06823 |  -0.10475 |  -0.02951 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | cau_unemb - frq_unemb | kl       |    -2.2936  |  -2.59051 |  -1.99034 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | cau_unemb - frq_unemb | kl_park  |    -1.87723 |  -2.10479 |  -1.63128 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | cau_unemb - frq_unemb | rd       |    -0.13984 |  -0.21228 |  -0.06473 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | cau_unemb - frq_unemb | cf_dev   |    -0.17081 |  -0.25329 |  -0.08734 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | cau_unemb - frq_unemb | kl_neu   |    -0.16536 |  -0.2154  |  -0.12001 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | frq_dmd - dua_dmd     | kl       |     0.0504  |  -0.24483 |   0.32328 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | frq_dmd - dua_dmd     | kl_park  |     1.52407 |   1.43534 |   1.60625 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | frq_dmd - dua_dmd     | rd       |    -0.0144  |  -0.05387 |   0.02524 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | frq_dmd - dua_dmd     | cf_dev   |     0.01968 |   0.0026  |   0.03555 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | frq_dmd - dua_dmd     | kl_neu   |    -1.2052  |  -1.42799 |  -0.98863 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | frq_dmd - dua_dmd     | kl       |    -0.27492 |  -0.58097 |   0.03105 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | frq_dmd - dua_dmd     | kl_park  |     1.40827 |   1.30417 |   1.50522 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | frq_dmd - dua_dmd     | rd       |     0.28927 |   0.23781 |   0.33819 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | frq_dmd - dua_dmd     | cf_dev   |     0.00521 |  -0.00461 |   0.0146  |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | frq_dmd - dua_dmd     | kl_neu   |    -1.1597  |  -1.37993 |  -0.94955 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | frq_dmd - dua_dmd     | kl       |     0.45241 |  -0.0782  |   0.98636 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | frq_dmd - dua_dmd     | kl_park  |     1.66277 |   1.48888 |   1.84432 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | frq_dmd - dua_dmd     | rd       |     0.08351 |   0.02006 |   0.14398 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | frq_dmd - dua_dmd     | cf_dev   |     0.07584 |   0.02731 |   0.13179 |  60 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | frq_dmd - dua_dmd     | kl_neu   |    -1.02745 |  -1.27746 |  -0.80408 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | euc_dmd - dua_dmd     | kl       |     0.13937 |  -0.15799 |   0.35485 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | euc_dmd - dua_dmd     | kl_park  |     0.30816 |   0.2511  |   0.36856 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | euc_dmd - dua_dmd     | rd       |     0.0823  |   0.06151 |   0.10361 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | euc_dmd - dua_dmd     | cf_dev   |     0.20581 |   0.17591 |   0.23724 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | euc_dmd - dua_dmd     | kl_neu   |    -0.11727 |  -0.41398 |   0.0828  |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | euc_dmd - dua_dmd     | kl       |     0.03371 |  -0.30291 |   0.30458 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | euc_dmd - dua_dmd     | kl_park  |     0.23865 |   0.18353 |   0.30544 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | euc_dmd - dua_dmd     | rd       |     0.07643 |   0.05247 |   0.10668 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | euc_dmd - dua_dmd     | cf_dev   |     0.15011 |   0.09584 |   0.2146  |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | euc_dmd - dua_dmd     | kl_neu   |    -0.17497 |  -0.54209 |   0.11745 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | euc_dmd - dua_dmd     | kl       |     0.02381 |  -0.31293 |   0.31614 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | euc_dmd - dua_dmd     | kl_park  |     0.27792 |   0.20594 |   0.34228 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | euc_dmd - dua_dmd     | rd       |     0.07695 |   0.05039 |   0.10288 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | euc_dmd - dua_dmd     | cf_dev   |     0.16984 |   0.12789 |   0.20732 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | euc_dmd - dua_dmd     | kl_neu   |    -0.20258 |  -0.56621 |   0.12442 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | cau_unemb - dua_unemb | kl       |    -1.30901 |  -1.62919 |  -0.97974 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | cau_unemb - dua_unemb | kl_park  |     0.1026  |   0.0696  |   0.13871 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | cau_unemb - dua_unemb | rd       |     0.06103 |   0.04479 |   0.07964 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | cau_unemb - dua_unemb | cf_dev   |     0.09381 |   0.06529 |   0.12719 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | cau_unemb - dua_unemb | kl_neu   |    -1.34155 |  -1.68337 |  -1.02442 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | cau_unemb - dua_unemb | kl       |    -1.29755 |  -1.68552 |  -0.9717  |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | cau_unemb - dua_unemb | kl_park  |     0.07267 |   0.0357  |   0.11478 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | cau_unemb - dua_unemb | rd       |     0.05315 |   0.03008 |   0.08318 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | cau_unemb - dua_unemb | cf_dev   |     0.08636 |   0.04202 |   0.14346 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | cau_unemb - dua_unemb | kl_neu   |    -1.33138 |  -1.73567 |  -1.01888 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | cau_unemb - dua_unemb | kl       |    -1.36263 |  -1.79292 |  -0.95079 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | cau_unemb - dua_unemb | kl_park  |     0.10153 |   0.05314 |   0.15532 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | cau_unemb - dua_unemb | rd       |     0.07625 |   0.05457 |   0.09468 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | cau_unemb - dua_unemb | cf_dev   |     0.1197  |   0.08002 |   0.15745 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | cau_unemb - dua_unemb | kl_neu   |    -1.42704 |  -1.85941 |  -1.0054  |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | frq_unemb - dua_unemb | kl       |     3.3228  |   2.54527 |   4.06233 |  25 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | frq_unemb - dua_unemb | kl_park  |     0.63481 |   0.53127 |   0.76898 |  25 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | frq_unemb - dua_unemb | rd       |     0.08797 |   0.07173 |   0.10787 |  25 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | frq_unemb - dua_unemb | cf_dev   |     0.31454 |   0.2585  |   0.37876 |  25 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | frq_unemb - dua_unemb | kl_neu   |     1.5113  |   1.04885 |   1.99944 |  25 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | frq_unemb - dua_unemb | kl       |     5.40403 |   4.4475  |   6.47136 |  39 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | frq_unemb - dua_unemb | kl_park  |     0.71541 |   0.65384 |   0.78334 |  39 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | frq_unemb - dua_unemb | rd       |     0.08491 |   0.07597 |   0.09385 |  39 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | frq_unemb - dua_unemb | cf_dev   |     0.3262  |   0.28876 |   0.36958 |  39 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | frq_unemb - dua_unemb | kl_neu   |     2.78149 |   2.10884 |   3.48863 |  39 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | frq_unemb - dua_unemb | kl       |     4.94138 |   4.11213 |   5.6564  |  37 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | frq_unemb - dua_unemb | kl_park  |     0.76676 |   0.66383 |   0.8638  |  37 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | frq_unemb - dua_unemb | rd       |     0.10161 |   0.08587 |   0.11846 |  37 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | frq_unemb - dua_unemb | cf_dev   |     0.36355 |   0.30281 |   0.41584 |  37 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | frq_unemb - dua_unemb | kl_neu   |     2.09511 |   1.68198 |   2.50957 |  37 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | cau_unemb - frq_unemb | kl       |    -4.05218 |  -4.86455 |  -3.23887 |  25 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | cau_unemb - frq_unemb | kl_park  |    -0.57938 |  -0.69258 |  -0.49729 |  25 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | cau_unemb - frq_unemb | rd       |    -0.03715 |  -0.05227 |  -0.02306 |  25 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | cau_unemb - frq_unemb | cf_dev   |    -0.27722 |  -0.32366 |  -0.23593 |  25 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | cau_unemb - frq_unemb | kl_neu   |    -2.26408 |  -2.58686 |  -1.8773  |  25 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | cau_unemb - frq_unemb | kl       |    -6.08498 |  -7.06686 |  -5.16564 |  39 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | cau_unemb - frq_unemb | kl_park  |    -0.65066 |  -0.68844 |  -0.60875 |  39 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | cau_unemb - frq_unemb | rd       |    -0.04065 |  -0.05105 |  -0.03006 |  39 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | cau_unemb - frq_unemb | cf_dev   |    -0.28507 |  -0.31854 |  -0.25004 |  39 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | cau_unemb - frq_unemb | kl_neu   |    -3.49897 |  -4.10993 |  -2.90451 |  39 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | cau_unemb - frq_unemb | kl       |    -5.87911 |  -6.70395 |  -4.99262 |  37 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | cau_unemb - frq_unemb | kl_park  |    -0.69482 |  -0.79011 |  -0.60271 |  37 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | cau_unemb - frq_unemb | rd       |    -0.03805 |  -0.05147 |  -0.02299 |  37 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | cau_unemb - frq_unemb | cf_dev   |    -0.26147 |  -0.29049 |  -0.22505 |  37 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | cau_unemb - frq_unemb | kl_neu   |    -3.11317 |  -3.53254 |  -2.68694 |  37 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | frq_dmd - dua_dmd     | kl       |     0.05365 |  -0.27482 |   0.26544 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | frq_dmd - dua_dmd     | kl_park  |     0.29331 |   0.23284 |   0.35873 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | frq_dmd - dua_dmd     | rd       |     0.08183 |   0.05946 |   0.10476 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | frq_dmd - dua_dmd     | cf_dev   |     0.25522 |   0.22605 |   0.28616 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | frq_dmd - dua_dmd     | kl_neu   |    -0.21398 |  -0.53517 |  -0.01404 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | frq_dmd - dua_dmd     | kl       |    -0.20141 |  -0.50744 |   0.06792 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | frq_dmd - dua_dmd     | kl_park  |     0.1925  |   0.149   |   0.2391  |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | frq_dmd - dua_dmd     | rd       |     0.05426 |   0.03775 |   0.07332 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | frq_dmd - dua_dmd     | cf_dev   |     0.16712 |   0.12864 |   0.2118  |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | frq_dmd - dua_dmd     | kl_neu   |    -0.39023 |  -0.72173 |  -0.12691 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | frq_dmd - dua_dmd     | kl       |    -0.25799 |  -0.6443  |   0.03726 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | frq_dmd - dua_dmd     | kl_park  |     0.20232 |   0.14107 |   0.25107 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | frq_dmd - dua_dmd     | rd       |     0.05849 |   0.0367  |   0.07679 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | frq_dmd - dua_dmd     | cf_dev   |     0.15485 |   0.11559 |   0.18538 |  60 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | frq_dmd - dua_dmd     | kl_neu   |    -0.40404 |  -0.81909 |  -0.11536 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | euc_dmd - dua_dmd     | kl       |     0.31807 |   0.2284  |   0.41358 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | euc_dmd - dua_dmd     | kl_park  |     0.23499 |   0.17062 |   0.30203 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | euc_dmd - dua_dmd     | rd       |     0.09735 |   0.069   |   0.12308 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | euc_dmd - dua_dmd     | cf_dev   |     0.08725 |   0.06216 |   0.1207  |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | euc_dmd - dua_dmd     | kl_neu   |     0.08583 |   0.01921 |   0.17382 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | euc_dmd - dua_dmd     | kl       |     0.33196 |   0.21406 |   0.47927 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | euc_dmd - dua_dmd     | kl_park  |     0.2411  |   0.1696  |   0.33523 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | euc_dmd - dua_dmd     | rd       |     0.09333 |   0.06658 |   0.1273  |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | euc_dmd - dua_dmd     | cf_dev   |     0.11533 |   0.07505 |   0.1627  |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | euc_dmd - dua_dmd     | kl_neu   |     0.02812 |  -0.04349 |   0.11016 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | euc_dmd - dua_dmd     | kl       |     0.37071 |   0.24048 |   0.55368 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | euc_dmd - dua_dmd     | kl_park  |     0.23265 |   0.1627  |   0.31375 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | euc_dmd - dua_dmd     | rd       |     0.07759 |   0.05746 |   0.09988 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | euc_dmd - dua_dmd     | cf_dev   |     0.08859 |   0.06253 |   0.12356 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | euc_dmd - dua_dmd     | kl_neu   |     0.09851 |   0.00142 |   0.19647 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | cau_unemb - dua_unemb | kl       |     0.00375 |  -0.07414 |   0.0911  |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | cau_unemb - dua_unemb | kl_park  |     0.13064 |   0.08154 |   0.18883 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | cau_unemb - dua_unemb | rd       |     0.05744 |   0.03698 |   0.07914 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | cau_unemb - dua_unemb | cf_dev   |     0.08154 |   0.04958 |   0.11949 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | cau_unemb - dua_unemb | kl_neu   |    -0.06871 |  -0.14869 |   0.01859 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | cau_unemb - dua_unemb | kl       |     0.01575 |  -0.06532 |   0.12829 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | cau_unemb - dua_unemb | kl_park  |     0.15253 |   0.08777 |   0.22922 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | cau_unemb - dua_unemb | rd       |     0.06907 |   0.04033 |   0.10388 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | cau_unemb - dua_unemb | cf_dev   |     0.11196 |   0.06814 |   0.16962 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | cau_unemb - dua_unemb | kl_neu   |    -0.1296  |  -0.21422 |  -0.03234 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | cau_unemb - dua_unemb | kl       |     0.03049 |  -0.07999 |   0.13113 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | cau_unemb - dua_unemb | kl_park  |     0.12675 |   0.07896 |   0.1735  |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | cau_unemb - dua_unemb | rd       |     0.06067 |   0.03583 |   0.09413 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | cau_unemb - dua_unemb | cf_dev   |     0.08817 |   0.05427 |   0.13139 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | cau_unemb - dua_unemb | kl_neu   |    -0.07677 |  -0.16423 |   0.0002  |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | frq_unemb - dua_unemb | kl       |    14.9135  |  13.7467  |  15.9562  |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | frq_unemb - dua_unemb | kl_park  |     1.47422 |   1.38843 |   1.55472 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | frq_unemb - dua_unemb | rd       |     0.09785 |   0.07497 |   0.11696 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | frq_unemb - dua_unemb | cf_dev   |     0.54119 |   0.48721 |   0.58776 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | frq_unemb - dua_unemb | kl_neu   |     6.25435 |   5.27651 |   7.20477 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | frq_unemb - dua_unemb | kl       |    16.2961  |  14.6815  |  18.0181  |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | frq_unemb - dua_unemb | kl_park  |     1.43345 |   1.34944 |   1.52693 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | frq_unemb - dua_unemb | rd       |     0.09662 |   0.07445 |   0.11718 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | frq_unemb - dua_unemb | cf_dev   |     0.55222 |   0.51433 |   0.59109 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | frq_unemb - dua_unemb | kl_neu   |     6.43205 |   5.7682  |   7.3329  |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | frq_unemb - dua_unemb | kl       |     7.8686  |   6.48226 |   9.00128 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | frq_unemb - dua_unemb | kl_park  |     1.44626 |   1.35268 |   1.53528 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | frq_unemb - dua_unemb | rd       |     0.05012 |   0.02938 |   0.07787 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | frq_unemb - dua_unemb | cf_dev   |     0.5208  |   0.45127 |   0.58686 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | frq_unemb - dua_unemb | kl_neu   |     3.42764 |   2.44617 |   4.44813 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | cau_unemb - frq_unemb | kl       |   -14.9097  | -15.9964  | -13.7142  |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | cau_unemb - frq_unemb | kl_park  |    -1.34358 |  -1.40644 |  -1.27366 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | cau_unemb - frq_unemb | rd       |    -0.04041 |  -0.07249 |  -0.00905 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | cau_unemb - frq_unemb | cf_dev   |    -0.45965 |  -0.51705 |  -0.40217 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | cau_unemb - frq_unemb | kl_neu   |    -6.32307 |  -7.17084 |  -5.39164 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | cau_unemb - frq_unemb | kl       |   -16.2803  | -17.9928  | -14.7681  |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | cau_unemb - frq_unemb | kl_park  |    -1.28092 |  -1.34043 |  -1.2225  |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | cau_unemb - frq_unemb | rd       |    -0.02756 |  -0.05533 |   0.00671 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | cau_unemb - frq_unemb | cf_dev   |    -0.44026 |  -0.48323 |  -0.39521 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | cau_unemb - frq_unemb | kl_neu   |    -6.56165 |  -7.37441 |  -5.92832 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | cau_unemb - frq_unemb | kl       |    -7.83811 |  -8.88339 |  -6.48234 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | cau_unemb - frq_unemb | kl_park  |    -1.31951 |  -1.39197 |  -1.2423  |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | cau_unemb - frq_unemb | rd       |     0.01055 |  -0.0227  |   0.04243 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | cau_unemb - frq_unemb | cf_dev   |    -0.43263 |  -0.51408 |  -0.34623 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | cau_unemb - frq_unemb | kl_neu   |    -3.50441 |  -4.43747 |  -2.56939 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | frq_dmd - dua_dmd     | kl       |     1.60678 |   1.21907 |   2.10392 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | frq_dmd - dua_dmd     | kl_park  |     0.72882 |   0.5963  |   0.85347 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | frq_dmd - dua_dmd     | rd       |     0.1276  |   0.09969 |   0.15598 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | frq_dmd - dua_dmd     | cf_dev   |     0.2892  |   0.22956 |   0.34398 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s0_abs2e-2    | frq_dmd - dua_dmd     | kl_neu   |     0.77868 |   0.57203 |   1.02295 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | frq_dmd - dua_dmd     | kl       |     0.8923  |   0.6984  |   1.15351 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | frq_dmd - dua_dmd     | kl_park  |     0.50292 |   0.40334 |   0.61736 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | frq_dmd - dua_dmd     | rd       |     0.11596 |   0.09349 |   0.14378 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | frq_dmd - dua_dmd     | cf_dev   |     0.13107 |   0.10332 |   0.15903 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s1_abs2e-2    | frq_dmd - dua_dmd     | kl_neu   |     0.18428 |   0.08613 |   0.27052 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | frq_dmd - dua_dmd     | kl       |     6.86082 |   5.26689 |   8.41529 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | frq_dmd - dua_dmd     | kl_park  |     1.28311 |   1.11885 |   1.41692 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | frq_dmd - dua_dmd     | rd       |     0.09167 |   0.07337 |   0.11307 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | frq_dmd - dua_dmd     | cf_dev   |     0.44151 |   0.35629 |   0.52316 |  60 |
| A_third_a2e-2         | runs/gemma1b_v5/A_s2_abs2e-2    | frq_dmd - dua_dmd     | kl_neu   |     2.8182  |   2.06031 |   3.69231 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | euc_dmd - dua_dmd     | kl       |     0.34685 |   0.16064 |   0.54042 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | euc_dmd - dua_dmd     | kl_park  |     0.68298 |   0.52607 |   0.83897 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | euc_dmd - dua_dmd     | rd       |     0.27092 |   0.21005 |   0.33091 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | euc_dmd - dua_dmd     | cf_dev   |     0.12233 |   0.08071 |   0.16774 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | euc_dmd - dua_dmd     | kl_neu   |    -0.25918 |  -0.33593 |  -0.19061 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | euc_dmd - dua_dmd     | kl       |     0.30784 |   0.0554  |   0.56101 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | euc_dmd - dua_dmd     | kl_park  |     0.70841 |   0.54186 |   0.88263 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | euc_dmd - dua_dmd     | rd       |     0.16869 |   0.11572 |   0.22401 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | euc_dmd - dua_dmd     | cf_dev   |     0.08147 |   0.0443  |   0.12576 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | euc_dmd - dua_dmd     | kl_neu   |    -0.35077 |  -0.44856 |  -0.26225 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | euc_dmd - dua_dmd     | kl       |     0.38179 |   0.11778 |   0.64045 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | euc_dmd - dua_dmd     | kl_park  |     0.84667 |   0.6559  |   1.03951 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | euc_dmd - dua_dmd     | rd       |     0.24336 |   0.18626 |   0.30353 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | euc_dmd - dua_dmd     | cf_dev   |     0.13052 |   0.08199 |   0.18236 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | euc_dmd - dua_dmd     | kl_neu   |    -0.38779 |  -0.48671 |  -0.29789 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | cau_unemb - dua_unemb | kl       |    -0.23123 |  -0.33564 |  -0.12479 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | cau_unemb - dua_unemb | kl_park  |     0.18167 |   0.11224 |   0.25694 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | cau_unemb - dua_unemb | rd       |     0.05956 |   0.0266  |   0.09615 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | cau_unemb - dua_unemb | cf_dev   |     0.13576 |   0.09183 |   0.1793  |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | cau_unemb - dua_unemb | kl_neu   |    -0.39177 |  -0.46938 |  -0.32401 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | cau_unemb - dua_unemb | kl       |    -0.31392 |  -0.44232 |  -0.18867 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | cau_unemb - dua_unemb | kl_park  |     0.16179 |   0.10031 |   0.22233 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | cau_unemb - dua_unemb | rd       |     0.07753 |   0.03456 |   0.12724 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | cau_unemb - dua_unemb | cf_dev   |     0.11498 |   0.0814  |   0.15118 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | cau_unemb - dua_unemb | kl_neu   |    -0.45392 |  -0.55599 |  -0.36448 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | cau_unemb - dua_unemb | kl       |    -0.121   |  -0.26196 |   0.01906 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | cau_unemb - dua_unemb | kl_park  |     0.3304  |   0.22973 |   0.44087 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | cau_unemb - dua_unemb | rd       |     0.14188 |   0.09264 |   0.19342 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | cau_unemb - dua_unemb | cf_dev   |     0.16659 |   0.12074 |   0.21534 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | cau_unemb - dua_unemb | kl_neu   |    -0.4324  |  -0.52899 |  -0.34272 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | frq_unemb - dua_unemb | kl       |     1.60329 |   1.41023 |   1.78352 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | frq_unemb - dua_unemb | kl_park  |     1.73105 |   1.5802  |   1.87965 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | frq_unemb - dua_unemb | rd       |     0.23984 |   0.17934 |   0.30089 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | frq_unemb - dua_unemb | cf_dev   |     0.15151 |   0.1074  |   0.1976  |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | frq_unemb - dua_unemb | kl_neu   |    -0.28586 |  -0.35985 |  -0.20953 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | frq_unemb - dua_unemb | kl       |     1.45528 |   1.25332 |   1.64001 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | frq_unemb - dua_unemb | kl_park  |     1.67045 |   1.5666  |   1.76991 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | frq_unemb - dua_unemb | rd       |     0.09738 |   0.03524 |   0.15927 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | frq_unemb - dua_unemb | cf_dev   |     0.01356 |  -0.01948 |   0.05042 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | frq_unemb - dua_unemb | kl_neu   |    -0.42158 |  -0.52922 |  -0.32044 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | frq_unemb - dua_unemb | kl       |     1.48447 |   1.25163 |   1.73592 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | frq_unemb - dua_unemb | kl_park  |     1.66465 |   1.51676 |   1.82095 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | frq_unemb - dua_unemb | rd       |     0.09423 |   0.04451 |   0.14487 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | frq_unemb - dua_unemb | cf_dev   |     0.0241  |  -0.01225 |   0.07384 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | frq_unemb - dua_unemb | kl_neu   |    -0.42887 |  -0.55355 |  -0.31991 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | cau_unemb - frq_unemb | kl       |    -1.83452 |  -2.03024 |  -1.63495 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | cau_unemb - frq_unemb | kl_park  |    -1.54938 |  -1.72015 |  -1.35832 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | cau_unemb - frq_unemb | rd       |    -0.18028 |  -0.2414  |  -0.11897 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | cau_unemb - frq_unemb | cf_dev   |    -0.01575 |  -0.0831  |   0.05237 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | cau_unemb - frq_unemb | kl_neu   |    -0.10591 |  -0.14378 |  -0.0656  |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | cau_unemb - frq_unemb | kl       |    -1.7692  |  -1.90194 |  -1.64322 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | cau_unemb - frq_unemb | kl_park  |    -1.50866 |  -1.63524 |  -1.38028 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | cau_unemb - frq_unemb | rd       |    -0.01986 |  -0.08833 |   0.0488  |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | cau_unemb - frq_unemb | cf_dev   |     0.10143 |   0.05766 |   0.14101 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | cau_unemb - frq_unemb | kl_neu   |    -0.03234 |  -0.06572 |   0.00215 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | cau_unemb - frq_unemb | kl       |    -1.60547 |  -1.83586 |  -1.38604 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | cau_unemb - frq_unemb | kl_park  |    -1.33425 |  -1.54388 |  -1.13717 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | cau_unemb - frq_unemb | rd       |     0.04765 |  -0.02608 |   0.12236 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | cau_unemb - frq_unemb | cf_dev   |     0.14249 |   0.07907 |   0.20293 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | cau_unemb - frq_unemb | kl_neu   |    -0.00353 |  -0.0404  |   0.03269 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | frq_dmd - dua_dmd     | kl       |     1.65034 |   1.50447 |   1.79678 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | frq_dmd - dua_dmd     | kl_park  |     1.80655 |   1.72088 |   1.89801 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | frq_dmd - dua_dmd     | rd       |     0.05915 |   0.013   |   0.10709 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | frq_dmd - dua_dmd     | cf_dev   |     0.03848 |   0.02139 |   0.06235 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s0_abs2e-2    | frq_dmd - dua_dmd     | kl_neu   |    -0.34781 |  -0.44065 |  -0.26459 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | frq_dmd - dua_dmd     | kl       |     0.87487 |   0.54004 |   1.16065 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | frq_dmd - dua_dmd     | kl_park  |     1.3519  |   1.14275 |   1.51692 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | frq_dmd - dua_dmd     | rd       |     0.01423 |  -0.04389 |   0.07095 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | frq_dmd - dua_dmd     | cf_dev   |     0.02344 |   0.01508 |   0.03202 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s1_abs2e-2    | frq_dmd - dua_dmd     | kl_neu   |    -0.45604 |  -0.56817 |  -0.35824 |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | frq_dmd - dua_dmd     | kl       |    10.6915  |   9.6469  |  11.7524  |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | frq_dmd - dua_dmd     | kl_park  |     3.43152 |   3.25486 |   3.6093  |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | frq_dmd - dua_dmd     | rd       |     0.12966 |   0.07503 |   0.1867  |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | frq_dmd - dua_dmd     | cf_dev   |     0.86561 |   0.84573 |   0.8853  |  60 |
| C_third_a2e-2         | runs/gemma1b_v5/C_s2_abs2e-2    | frq_dmd - dua_dmd     | kl_neu   |     0.60648 |   0.41835 |   0.80001 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | euc_dmd - dua_dmd     | kl       |     0.1192  |   0.00834 |   0.23702 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | euc_dmd - dua_dmd     | kl_park  |     0.19398 |   0.13632 |   0.25834 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | euc_dmd - dua_dmd     | rd       |     0.08322 |   0.06116 |   0.10758 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | euc_dmd - dua_dmd     | cf_dev   |     0.11176 |   0.06976 |   0.15301 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | euc_dmd - dua_dmd     | kl_neu   |    -0.12291 |  -0.24933 |   0.00125 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | cau_unemb - dua_unemb | kl       |    -0.92224 |  -1.21755 |  -0.63176 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | cau_unemb - dua_unemb | kl_park  |     0.09343 |   0.03889 |   0.1457  |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | cau_unemb - dua_unemb | rd       |     0.08199 |   0.06063 |   0.10324 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | cau_unemb - dua_unemb | cf_dev   |     0.06234 |   0.01553 |   0.11009 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | cau_unemb - dua_unemb | kl_neu   |    -0.98362 |  -1.24031 |  -0.72896 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | frq_unemb - dua_unemb | kl       |     0.79483 |   0.54226 |   1.09692 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | frq_unemb - dua_unemb | kl_park  |     0.86519 |   0.81417 |   0.91843 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | frq_unemb - dua_unemb | rd       |     0.04045 |   0.01742 |   0.06269 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | frq_unemb - dua_unemb | cf_dev   |     0.10603 |   0.07443 |   0.13762 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | frq_unemb - dua_unemb | kl_neu   |    -0.49935 |  -0.76242 |  -0.20806 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | cau_unemb - frq_unemb | kl       |    -1.71706 |  -1.8679  |  -1.55442 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | cau_unemb - frq_unemb | kl_park  |    -0.77176 |  -0.83976 |  -0.70331 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | cau_unemb - frq_unemb | rd       |     0.04154 |   0.00673 |   0.07538 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | cau_unemb - frq_unemb | cf_dev   |    -0.04369 |  -0.09215 |   0.0102  |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | cau_unemb - frq_unemb | kl_neu   |    -0.48427 |  -0.63633 |  -0.31801 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | frq_dmd - dua_dmd     | kl       |     8.08127 |   6.51925 |   9.47062 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | frq_dmd - dua_dmd     | kl_park  |     1.38927 |   1.3036  |   1.47202 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | frq_dmd - dua_dmd     | rd       |     0.10211 |   0.07827 |   0.1259  |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | frq_dmd - dua_dmd     | cf_dev   |     0.53294 |   0.48168 |   0.57384 |  60 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | frq_dmd - dua_dmd     | kl_neu   |     3.39638 |   2.83849 |   4.00504 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | euc_dmd - dua_dmd     | kl       |     1.58536 |   1.04777 |   2.16902 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | euc_dmd - dua_dmd     | kl_park  |     0.71007 |   0.57961 |   0.85335 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | euc_dmd - dua_dmd     | rd       |     0.09055 |   0.0549  |   0.12591 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | euc_dmd - dua_dmd     | cf_dev   |     0.19761 |   0.15871 |   0.2381  |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | euc_dmd - dua_dmd     | kl_neu   |     0.3871  |  -0.00481 |   0.77736 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | euc_dmd - dua_dmd     | kl       |     0.97072 |   0.48377 |   1.43074 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | euc_dmd - dua_dmd     | kl_park  |     0.63204 |   0.53526 |   0.73137 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | euc_dmd - dua_dmd     | rd       |     0.07301 |   0.05364 |   0.0967  |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | euc_dmd - dua_dmd     | cf_dev   |     0.13886 |   0.10972 |   0.17035 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | euc_dmd - dua_dmd     | kl_neu   |     0.00411 |  -0.44341 |   0.40302 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | euc_dmd - dua_dmd     | kl       |     0.91699 |   0.23567 |   1.62855 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | euc_dmd - dua_dmd     | kl_park  |     0.56716 |   0.4515  |   0.67545 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | euc_dmd - dua_dmd     | rd       |     0.06266 |   0.0464  |   0.08233 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | euc_dmd - dua_dmd     | cf_dev   |     0.16693 |   0.12567 |   0.20361 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | euc_dmd - dua_dmd     | kl_neu   |    -0.08119 |  -0.56165 |   0.39665 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | cau_unemb - dua_unemb | kl       |    -0.91698 |  -1.23391 |  -0.64567 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | cau_unemb - dua_unemb | kl_park  |     0.20946 |   0.13922 |   0.27325 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | cau_unemb - dua_unemb | rd       |     0.13145 |   0.09898 |   0.16111 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | cau_unemb - dua_unemb | cf_dev   |     0.0461  |   0.02584 |   0.0654  |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | cau_unemb - dua_unemb | kl_neu   |    -1.13447 |  -1.43766 |  -0.84348 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | cau_unemb - dua_unemb | kl       |    -1.04528 |  -1.32759 |  -0.7678  |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | cau_unemb - dua_unemb | kl_park  |     0.17565 |   0.12165 |   0.22726 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | cau_unemb - dua_unemb | rd       |     0.0984  |   0.07946 |   0.11788 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | cau_unemb - dua_unemb | cf_dev   |     0.04939 |   0.03273 |   0.06695 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | cau_unemb - dua_unemb | kl_neu   |    -1.24273 |  -1.53621 |  -0.97899 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | cau_unemb - dua_unemb | kl       |    -1.08439 |  -1.46242 |  -0.76492 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | cau_unemb - dua_unemb | kl_park  |     0.16189 |   0.11186 |   0.213   |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | cau_unemb - dua_unemb | rd       |     0.10329 |   0.07708 |   0.12896 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | cau_unemb - dua_unemb | cf_dev   |     0.04963 |   0.03063 |   0.06821 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | cau_unemb - dua_unemb | kl_neu   |    -1.29701 |  -1.68589 |  -0.9863  |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | frq_unemb - dua_unemb | kl       |    -0.16815 |  -0.4818  |   0.1246  |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | frq_unemb - dua_unemb | kl_park  |     0.57603 |   0.53453 |   0.61311 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | frq_unemb - dua_unemb | rd       |     0.07657 |   0.05309 |   0.10029 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | frq_unemb - dua_unemb | cf_dev   |     0.25478 |   0.22544 |   0.29476 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | frq_unemb - dua_unemb | kl_neu   |    -1.46216 |  -1.74212 |  -1.18165 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | frq_unemb - dua_unemb | kl       |    -0.22544 |  -0.52813 |   0.05402 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | frq_unemb - dua_unemb | kl_park  |     0.6053  |   0.57034 |   0.64181 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | frq_unemb - dua_unemb | rd       |     0.07796 |   0.05884 |   0.10024 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | frq_unemb - dua_unemb | cf_dev   |     0.25382 |   0.22285 |   0.28397 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | frq_unemb - dua_unemb | kl_neu   |    -1.50768 |  -1.7793  |  -1.27902 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | frq_unemb - dua_unemb | kl       |    -0.33156 |  -0.74519 |   0.0158  |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | frq_unemb - dua_unemb | kl_park  |     0.55302 |   0.4912  |   0.61126 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | frq_unemb - dua_unemb | rd       |     0.07639 |   0.05678 |   0.09845 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | frq_unemb - dua_unemb | cf_dev   |     0.26163 |   0.23313 |   0.28913 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | frq_unemb - dua_unemb | kl_neu   |    -1.61525 |  -1.95695 |  -1.31647 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | cau_unemb - frq_unemb | kl       |    -0.74884 |  -0.86466 |  -0.64099 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | cau_unemb - frq_unemb | kl_park  |    -0.36657 |  -0.43783 |  -0.29914 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | cau_unemb - frq_unemb | rd       |     0.05488 |   0.02975 |   0.07614 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | cau_unemb - frq_unemb | cf_dev   |    -0.20868 |  -0.24332 |  -0.17763 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | cau_unemb - frq_unemb | kl_neu   |     0.32769 |   0.24347 |   0.40386 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | cau_unemb - frq_unemb | kl       |    -0.81984 |  -0.89894 |  -0.73657 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | cau_unemb - frq_unemb | kl_park  |    -0.42965 |  -0.4881  |  -0.36968 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | cau_unemb - frq_unemb | rd       |     0.02044 |  -0.0022  |   0.04568 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | cau_unemb - frq_unemb | cf_dev   |    -0.20443 |  -0.237   |  -0.17143 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | cau_unemb - frq_unemb | kl_neu   |     0.26496 |   0.17675 |   0.35845 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | cau_unemb - frq_unemb | kl       |    -0.75283 |  -0.85302 |  -0.66289 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | cau_unemb - frq_unemb | kl_park  |    -0.39114 |  -0.46438 |  -0.31946 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | cau_unemb - frq_unemb | rd       |     0.0269  |   0.00378 |   0.04671 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | cau_unemb - frq_unemb | cf_dev   |    -0.212   |  -0.24785 |  -0.18216 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | cau_unemb - frq_unemb | kl_neu   |     0.31824 |   0.25609 |   0.38486 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | frq_dmd - dua_dmd     | kl       |     6.44634 |   5.34258 |   7.50736 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | frq_dmd - dua_dmd     | kl_park  |     0.95931 |   0.84782 |   1.08602 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | frq_dmd - dua_dmd     | rd       |     0.0604  |   0.02525 |   0.09969 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | frq_dmd - dua_dmd     | cf_dev   |     0.29553 |   0.25907 |   0.32753 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | frq_dmd - dua_dmd     | kl_neu   |     2.64562 |   1.99983 |   3.31755 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | frq_dmd - dua_dmd     | kl       |     0.90021 |   0.23705 |   1.59266 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | frq_dmd - dua_dmd     | kl_park  |     0.61921 |   0.52668 |   0.71853 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | frq_dmd - dua_dmd     | rd       |     0.02031 |   0.00163 |   0.04097 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | frq_dmd - dua_dmd     | cf_dev   |     0.15398 |   0.10358 |   0.21241 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | frq_dmd - dua_dmd     | kl_neu   |    -0.10574 |  -0.53238 |   0.2843  |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | frq_dmd - dua_dmd     | kl       |     0.80631 |  -0.02353 |   1.84328 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | frq_dmd - dua_dmd     | kl_park  |     0.60181 |   0.46894 |   0.73714 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | frq_dmd - dua_dmd     | rd       |     0.0282  |   0.0115  |   0.04676 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | frq_dmd - dua_dmd     | cf_dev   |     0.18104 |   0.10727 |   0.24479 |  60 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | frq_dmd - dua_dmd     | kl_neu   |    -0.1811  |  -0.69653 |   0.35284 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | euc_dmd - dua_dmd     | kl       |    -1.24028 |  -1.73979 |  -0.84211 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | euc_dmd - dua_dmd     | kl_park  |     0.18905 |   0.11238 |   0.26725 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | euc_dmd - dua_dmd     | rd       |     0.04812 |   0.0297  |   0.06932 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | euc_dmd - dua_dmd     | cf_dev   |    -0.03633 |  -0.06291 |  -0.00538 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | euc_dmd - dua_dmd     | kl_neu   |    -1.25038 |  -1.70474 |  -0.86099 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | cau_unemb - dua_unemb | kl       |    -1.65011 |  -2.03547 |  -1.27142 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | cau_unemb - dua_unemb | kl_park  |     0.15796 |   0.11798 |   0.20023 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | cau_unemb - dua_unemb | rd       |     0.05683 |   0.03766 |   0.0772  |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | cau_unemb - dua_unemb | cf_dev   |     0.077   |   0.05539 |   0.09776 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | cau_unemb - dua_unemb | kl_neu   |    -1.69185 |  -2.06891 |  -1.34351 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | frq_unemb - dua_unemb | kl       |    -1.14396 |  -1.58051 |  -0.74637 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | frq_unemb - dua_unemb | kl_park  |     0.2521  |   0.21542 |   0.28365 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | frq_unemb - dua_unemb | rd       |     0.05763 |   0.04312 |   0.07505 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | frq_unemb - dua_unemb | cf_dev   |     0.24632 |   0.23215 |   0.2589  |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | frq_unemb - dua_unemb | kl_neu   |    -2.10276 |  -2.49915 |  -1.69679 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | cau_unemb - frq_unemb | kl       |    -0.50615 |  -0.57932 |  -0.43749 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | cau_unemb - frq_unemb | kl_park  |    -0.09414 |  -0.13392 |  -0.05683 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | cau_unemb - frq_unemb | rd       |    -0.0008  |  -0.01913 |   0.01536 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | cau_unemb - frq_unemb | cf_dev   |    -0.16933 |  -0.19771 |  -0.14219 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | cau_unemb - frq_unemb | kl_neu   |     0.41091 |   0.33818 |   0.48542 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | frq_dmd - dua_dmd     | kl       |    -2.57196 |  -3.24636 |  -1.95575 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | frq_dmd - dua_dmd     | kl_park  |     0.11829 |   0.06244 |   0.17358 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | frq_dmd - dua_dmd     | rd       |     0.0382  |   0.02188 |   0.05672 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | frq_dmd - dua_dmd     | cf_dev   |    -0.06676 |  -0.08989 |  -0.04128 |  60 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | frq_dmd - dua_dmd     | kl_neu   |    -2.35943 |  -2.98059 |  -1.81076 |  60 |

## capture_ratio

| group                 | probe   | metric   |   n |   gap_euc_minus_dua |   gap_lo |   gap_hi | gap_defined   |   rho_cau |   rho_cau_lo |   rho_cau_hi |   rho_frq |   rho_frq_lo |   rho_frq_hi |
|:----------------------|:--------|:---------|----:|--------------------:|---------:|---------:|:--------------|----------:|-------------:|-------------:|----------:|-------------:|-------------:|
| A_third_a5e-3         | ctx     | kl       | 180 |            -2.23059 |  -2.4441 |  -1.9902 | True          |    0.6044 |       0.4778 |       0.7544 |  nan      |     nan      |     nan      |
| A_third_a5e-3         | ctx     | kl_park  | 180 |            -0.00031 |  -0.0487 |   0.0529 | False         | 1600.25   |    -239.378  |     237.116  |  nan      |     nan      |     nan      |
| A_third_a5e-3         | ctx     | rd       | 180 |             0.0754  |   0.0617 |   0.0902 | True          |   -0.691  |      -0.997  |      -0.4731 |  nan      |     nan      |     nan      |
| A_third_a5e-3         | ctx     | cf_dev   | 180 |             0.01663 |  -0.0143 |   0.051  | False         |   -9.6894 |    -130.416  |     112.02   |  nan      |     nan      |     nan      |
| A_third_a5e-3         | ctx     | kl_neu   | 180 |            -1.98515 |  -2.144  |  -1.8038 | True          |    0.3863 |       0.3167 |       0.4779 |  nan      |     nan      |     nan      |
| A_third_a5e-3         | unemb   | kl       | 180 |            -0.51064 |  -0.6459 |  -0.3813 | True          |   -0.2072 |      -0.2705 |      -0.1646 |   25.2694 |      19.7844 |      34.1232 |
| A_third_a5e-3         | unemb   | kl_park  | 180 |             0.21663 |   0.1785 |   0.2578 | True          |    0.2384 |       0.1799 |       0.305  |   -5.8304 |      -7.1274 |      -4.9046 |
| A_third_a5e-3         | unemb   | rd       | 180 |             0.11296 |   0.0976 |   0.1297 | True          |    0.168  |       0.1055 |       0.2447 |   -0.0015 |      -0.1606 |       0.1416 |
| A_third_a5e-3         | unemb   | cf_dev   | 180 |             0.07849 |   0.0533 |   0.1067 | True          |   -0.1103 |      -0.1834 |      -0.0504 |   -5.7696 |      -8.9244 |      -4.0391 |
| A_third_a5e-3         | unemb   | kl_neu   | 180 |            -0.6913  |  -0.8359 |  -0.5615 | True          |   -0.0575 |      -0.0779 |      -0.0422 |    7.8451 |       6.2256 |       9.9612 |
| A_third_a5e-3         | dmd     | kl       | 180 |             0.17468 |   0.0714 |   0.2816 | True          |   -0.4518 |      -0.9785 |      -0.2699 |  -15.9131 |     -37.3067 |      -9.0615 |
| A_third_a5e-3         | dmd     | kl_park  | 180 |             0.29017 |   0.2385 |   0.3439 | True          |   -0.0632 |      -0.096  |      -0.0275 |   -2.0748 |      -2.7108 |      -1.5945 |
| A_third_a5e-3         | dmd     | rd       | 180 |             0.12213 |   0.1031 |   0.1406 | True          |    0.0067 |      -0.039  |       0.0543 |   -0.1827 |      -0.298  |      -0.0903 |
| A_third_a5e-3         | dmd     | cf_dev   | 180 |             0.12981 |   0.1032 |   0.16   | True          |   -0.1027 |      -0.1593 |      -0.0588 |   -1.4652 |      -2.2992 |      -0.9007 |
| A_third_a5e-3         | dmd     | kl_neu   | 180 |            -0.13472 |  -0.2246 |  -0.0412 | True          |    0.4589 |       0.2366 |       1.6624 |    8.8302 |       3.9775 |      31.3698 |
| C_third_a5e-3         | ctx     | kl       | 179 |            -1.32955 |  -1.516  |  -1.1373 | True          |    0.7825 |       0.6516 |       0.9452 |  nan      |     nan      |     nan      |
| C_third_a5e-3         | ctx     | kl_park  | 179 |             0.40055 |   0.3106 |   0.5009 | True          |   -2.0158 |      -2.6881 |      -1.5496 |  nan      |     nan      |     nan      |
| C_third_a5e-3         | ctx     | rd       | 179 |             0.18357 |   0.151  |   0.2149 | True          |   -0.3848 |      -0.5877 |      -0.2204 |  nan      |     nan      |     nan      |
| C_third_a5e-3         | ctx     | cf_dev   | 179 |             0.0901  |   0.0566 |   0.1249 | True          |   -3.276  |      -5.5369 |      -2.2071 |  nan      |     nan      |     nan      |
| C_third_a5e-3         | ctx     | kl_neu   | 179 |            -1.35354 |  -1.4813 |  -1.2312 | True          |    0.0913 |       0.0808 |       0.1024 |  nan      |     nan      |     nan      |
| C_third_a5e-3         | unemb   | kl       | 180 |            -1.09816 |  -1.2234 |  -0.9741 | True          |   -0.0678 |      -0.103  |      -0.0361 |    1.5134 |       1.3251 |       1.73   |
| C_third_a5e-3         | unemb   | kl_park  | 180 |             0.24088 |   0.1892 |   0.2955 | True          |    0.2106 |       0.0863 |       0.3344 |   -5.8675 |      -7.9215 |      -4.4715 |
| C_third_a5e-3         | unemb   | rd       | 180 |             0.12417 |   0.0975 |   0.1523 | True          |    0.1573 |       0.0134 |       0.2999 |   -0.2521 |      -0.7084 |       0.0901 |
| C_third_a5e-3         | unemb   | cf_dev   | 180 |             0.07676 |   0.0551 |   0.0996 | True          |   -0.689  |      -0.9711 |      -0.4986 |    0.3019 |      -0.1788 |       0.6468 |
| C_third_a5e-3         | unemb   | kl_neu   | 180 |            -1.19679 |  -1.3115 |  -1.0877 | True          |   -0.0099 |      -0.0133 |      -0.0067 |    0.0296 |       0.0114 |       0.048  |
| C_third_a5e-3         | dmd     | kl       | 180 |            -0.82176 |  -0.9978 |  -0.6474 | True          |    0.5435 |       0.4028 |       0.7377 |    4.9407 |       3.7168 |       6.721  |
| C_third_a5e-3         | dmd     | kl_park  | 180 |             0.74667 |   0.6471 |   0.8543 | True          |   -0.432  |      -0.5258 |      -0.3493 |   -1.9428 |      -2.4614 |      -1.541  |
| C_third_a5e-3         | dmd     | rd       | 180 |             0.24276 |   0.2077 |   0.2781 | True          |   -0.1895 |      -0.292  |      -0.0991 |    0.659  |       0.5261 |       0.7897 |
| C_third_a5e-3         | dmd     | cf_dev   | 180 |             0.09907 |   0.0735 |   0.1252 | True          |   -0.1775 |      -0.3417 |      -0.0501 |   -1.996  |      -3.1561 |      -1.1978 |
| C_third_a5e-3         | dmd     | kl_neu   | 180 |            -0.98646 |  -1.0866 |  -0.892  | True          |   -0.0067 |      -0.0126 |      -0.0008 |    0.2705 |       0.1812 |       0.3711 |
| Cbig_third_a5e-3      | ctx     | kl       | 178 |            -1.3072  |  -1.5055 |  -1.0958 | True          |    0.7807 |       0.6319 |       0.9831 |  nan      |     nan      |     nan      |
| Cbig_third_a5e-3      | ctx     | kl_park  | 178 |             0.44411 |   0.3481 |   0.5488 | True          |   -1.7678 |      -2.3268 |      -1.3796 |  nan      |     nan      |     nan      |
| Cbig_third_a5e-3      | ctx     | rd       | 178 |             0.20387 |   0.1686 |   0.2368 | True          |   -0.264  |      -0.4461 |      -0.1187 |  nan      |     nan      |     nan      |
| Cbig_third_a5e-3      | ctx     | cf_dev   | 178 |             0.0733  |   0.0393 |   0.1088 | True          |   -3.993  |      -7.7849 |      -2.5094 |  nan      |     nan      |     nan      |
| Cbig_third_a5e-3      | ctx     | kl_neu   | 178 |            -1.40143 |  -1.558  |  -1.2555 | True          |    0.0963 |       0.0831 |       0.1103 |  nan      |     nan      |     nan      |
| Cbig_third_a5e-3      | unemb   | kl       | 180 |            -1.12026 |  -1.2637 |  -0.9665 | True          |   -0.0537 |      -0.0908 |      -0.0168 |    2.0978 |       1.7863 |       2.5092 |
| Cbig_third_a5e-3      | unemb   | kl_park  | 180 |             0.24314 |   0.1863 |   0.301  | True          |    0.154  |      -0.0084 |       0.3181 |   -7.3206 |     -10.0733 |      -5.5341 |
| Cbig_third_a5e-3      | unemb   | rd       | 180 |             0.12837 |   0.1026 |   0.158  | True          |    0.1245 |      -0.0246 |       0.2652 |   -0.6119 |      -1.1373 |      -0.2431 |
| Cbig_third_a5e-3      | unemb   | cf_dev   | 180 |             0.07689 |   0.0552 |   0.0995 | True          |   -0.6931 |      -0.9482 |      -0.5208 |   -2.7095 |      -4.4247 |      -1.7288 |
| Cbig_third_a5e-3      | unemb   | kl_neu   | 180 |            -1.22344 |  -1.3579 |  -1.0854 | True          |   -0.0096 |      -0.0133 |      -0.0059 |    0.1281 |       0.1008 |       0.1582 |
| Cbig_third_a5e-3      | dmd     | kl       | 180 |            -0.68036 |  -0.8912 |  -0.4882 | True          |    0.5833 |       0.4124 |       0.8756 |    1.1117 |       0.8207 |       1.5508 |
| Cbig_third_a5e-3      | dmd     | kl_park  | 180 |             0.8794  |   0.7736 |   0.9912 | True          |   -0.3325 |      -0.4021 |      -0.2666 |   -0.7418 |      -0.9982 |      -0.532  |
| Cbig_third_a5e-3      | dmd     | rd       | 180 |             0.27081 |   0.238  |   0.3061 | True          |   -0.1055 |      -0.1833 |      -0.0362 |    0.5589 |       0.4201 |       0.6866 |
| Cbig_third_a5e-3      | dmd     | cf_dev   | 180 |             0.1264  |   0.0959 |   0.1567 | True          |   -0.455  |      -0.6338 |      -0.3239 |    0.7344 |       0.5562 |       0.8701 |
| Cbig_third_a5e-3      | dmd     | kl_neu   | 180 |            -1.07951 |  -1.2092 |  -0.9538 | True          |    0.0036 |      -0.0024 |       0.01   |   -0.0475 |      -0.0661 |      -0.0268 |
| gpt2_A_third_a5e-3    | unemb   | kl       | 180 |            -0.59319 |  -0.8514 |  -0.3539 | True          |   -1.2304 |      -2.1893 |      -0.8069 |  nan      |     nan      |     nan      |
| gpt2_A_third_a5e-3    | unemb   | kl_park  | 180 |             0.29466 |   0.2633 |   0.3285 | True          |    0.6869 |       0.6246 |       0.7516 |  nan      |     nan      |     nan      |
| gpt2_A_third_a5e-3    | unemb   | rd       | 180 |             0.09623 |   0.0858 |   0.1078 | True          |    0.3403 |       0.2514 |       0.4346 |  nan      |     nan      |     nan      |
| gpt2_A_third_a5e-3    | unemb   | cf_dev   | 180 |             0.0929  |   0.0717 |   0.1151 | True          |   -0.0759 |      -0.1605 |       0.0228 |  nan      |     nan      |     nan      |
| gpt2_A_third_a5e-3    | unemb   | kl_neu   | 180 |            -0.8055  |  -1.0719 |  -0.5688 | True          |   -0.6966 |      -1.0776 |      -0.4865 |  nan      |     nan      |     nan      |
| gpt2_A_third_a5e-3    | dmd     | kl       | 180 |             0.06563 |  -0.1102 |   0.2207 | False         |    4.057  |     -27.1702 |      37.1128 |    3.0608 |     -18.9008 |      26.5731 |
| gpt2_A_third_a5e-3    | dmd     | kl_park  | 180 |             0.27491 |   0.2386 |   0.3128 | True          |    0.1998 |       0.1107 |       0.2916 |    0.1656 |       0.1082 |       0.2225 |
| gpt2_A_third_a5e-3    | dmd     | rd       | 180 |             0.07856 |   0.0642 |   0.0944 | True          |    0.2929 |       0.218  |       0.3625 |    0.1744 |       0.0746 |       0.2699 |
| gpt2_A_third_a5e-3    | dmd     | cf_dev   | 180 |             0.17525 |   0.1486 |   0.2027 | True          |   -0.0482 |      -0.0991 |      -0.0052 |   -0.0978 |      -0.1872 |      -0.0209 |
| gpt2_A_third_a5e-3    | dmd     | kl_neu   | 180 |            -0.16494 |  -0.3546 |   0.0064 | False         |   -1.6451 |     -14.1697 |       5.4923 |   -1.0376 |      -8.9783 |       3.5803 |
| A_third_a2e-2         | ctx     | kl       | 180 |            -0.28001 |  -0.3709 |  -0.1808 | True          |    4.8146 |       3.2786 |       7.9713 |  nan      |     nan      |     nan      |
| A_third_a2e-2         | ctx     | kl_park  | 180 |             0.07791 |   0.0376 |   0.1242 | True          |   -6.3732 |     -12.8112 |      -4.1299 |  nan      |     nan      |     nan      |
| A_third_a2e-2         | ctx     | rd       | 180 |             0.05965 |   0.0478 |   0.0728 | True          |   -0.8734 |      -1.2603 |      -0.5837 |  nan      |     nan      |     nan      |
| A_third_a2e-2         | ctx     | cf_dev   | 180 |             0.06229 |   0.0412 |   0.0869 | True          |   -2.5875 |      -4.2008 |      -1.6595 |  nan      |     nan      |     nan      |
| A_third_a2e-2         | ctx     | kl_neu   | 180 |            -0.31304 |  -0.37   |  -0.2564 | True          |    2.45   |       1.8726 |       3.3163 |  nan      |     nan      |     nan      |
| A_third_a2e-2         | unemb   | kl       | 180 |             0.12248 |   0.0719 |   0.1745 | True          |    0.864  |       0.5795 |       1.5223 | -105.349  |    -182.637  |     -74.2929 |
| A_third_a2e-2         | unemb   | kl_park  | 180 |             0.18828 |   0.1569 |   0.2222 | True          |    0.2743 |       0.2117 |       0.3439 |   -6.7081 |      -8.0923 |      -5.6556 |
| A_third_a2e-2         | unemb   | rd       | 180 |             0.08136 |   0.068  |   0.0968 | True          |    0.2332 |       0.1417 |       0.3436 |   -0.0021 |      -0.2229 |       0.1924 |
| A_third_a2e-2         | unemb   | cf_dev   | 180 |             0.08524 |   0.0648 |   0.1084 | True          |   -0.1015 |      -0.1613 |      -0.048  |   -5.3127 |      -7.3163 |      -3.9599 |
| A_third_a2e-2         | unemb   | kl_neu   | 180 |            -0.05192 |  -0.0997 |  -0.0056 | True          |   -0.7662 |      -3.5603 |      -0.3592 |  104.463  |      48.7769 |     533.142  |
| A_third_a2e-2         | dmd     | kl       | 180 |             0.34025 |   0.2682 |   0.4241 | True          |   -0.232  |      -0.3061 |      -0.163  |   -8.1697 |     -11.7064 |      -5.4656 |
| A_third_a2e-2         | dmd     | kl_park  | 180 |             0.23625 |   0.1946 |   0.2794 | True          |   -0.0776 |      -0.1162 |      -0.0347 |   -2.5484 |      -3.3176 |      -1.9742 |
| A_third_a2e-2         | dmd     | rd       | 180 |             0.08942 |   0.0749 |   0.1059 | True          |    0.0092 |      -0.054  |       0.069  |   -0.2495 |      -0.4193 |      -0.1212 |
| A_third_a2e-2         | dmd     | cf_dev   | 180 |             0.09706 |   0.0782 |   0.1194 | True          |   -0.1373 |      -0.2089 |      -0.0808 |   -1.9597 |      -2.995  |      -1.2116 |
| A_third_a2e-2         | dmd     | kl_neu   | 180 |             0.07082 |   0.0235 |   0.1237 | True          |   -0.8729 |      -2.338  |      -0.5298 |  -16.7968 |     -45.3208 |      -9.4914 |
| C_third_a2e-2         | ctx     | kl       | 180 |             0.0459  |  -0.0741 |   0.1761 | False         |  -22.8909 |    -179.006  |     200.739  |  nan      |     nan      |     nan      |
| C_third_a2e-2         | ctx     | kl_park  | 180 |             0.49727 |   0.4025 |   0.5901 | True          |   -1.6438 |      -2.1478 |      -1.2899 |  nan      |     nan      |     nan      |
| C_third_a2e-2         | ctx     | rd       | 180 |             0.18075 |   0.1509 |   0.2127 | True          |   -0.3886 |      -0.603  |      -0.2257 |  nan      |     nan      |     nan      |
| C_third_a2e-2         | ctx     | cf_dev   | 180 |             0.1587  |   0.1282 |   0.192  | True          |   -1.8737 |      -2.4686 |      -1.4401 |  nan      |     nan      |     nan      |
| C_third_a2e-2         | ctx     | kl_neu   | 180 |            -0.46414 |  -0.5146 |  -0.4146 | True          |    0.2661 |       0.2277 |       0.3096 |  nan      |     nan      |     nan      |
| C_third_a2e-2         | unemb   | kl       | 180 |            -0.14756 |  -0.2111 |  -0.0849 | True          |   -0.5048 |      -0.9909 |      -0.2505 |   11.2623 |       7.9264 |      19.3286 |
| C_third_a2e-2         | unemb   | kl_park  | 180 |             0.27536 |   0.2292 |   0.3249 | True          |    0.1843 |       0.0783 |       0.2957 |   -5.1328 |      -6.5601 |      -4.0843 |
| C_third_a2e-2         | unemb   | rd       | 180 |             0.11252 |   0.0872 |   0.1383 | True          |    0.1736 |      -0.0063 |       0.3369 |   -0.2782 |      -0.8318 |       0.0883 |
| C_third_a2e-2         | unemb   | cf_dev   | 180 |             0.08623 |   0.0674 |   0.1074 | True          |   -0.6133 |      -0.8005 |      -0.466  |    0.2687 |      -0.1314 |       0.5702 |
| C_third_a2e-2         | unemb   | kl_neu   | 180 |            -0.41414 |  -0.4608 |  -0.3638 | True          |   -0.0287 |      -0.0402 |      -0.0182 |    0.0854 |       0.0306 |       0.1451 |
| C_third_a2e-2         | dmd     | kl       | 180 |             0.34549 |   0.2128 |   0.482  | True          |   -1.2928 |      -2.0416 |      -0.9196 |  -11.7516 |     -19.525  |      -8.0492 |
| C_third_a2e-2         | dmd     | kl_park  | 180 |             0.74602 |   0.6431 |   0.8443 | True          |   -0.4323 |      -0.5295 |      -0.3535 |   -1.9445 |      -2.4586 |      -1.5444 |
| C_third_a2e-2         | dmd     | rd       | 180 |             0.22766 |   0.1934 |   0.2633 | True          |   -0.2021 |      -0.3132 |      -0.1115 |    0.7027 |       0.5585 |       0.8412 |
| C_third_a2e-2         | dmd     | cf_dev   | 180 |             0.11144 |   0.0866 |   0.1379 | True          |   -0.1578 |      -0.2884 |      -0.0475 |   -1.7744 |      -2.7497 |      -1.0874 |
| C_third_a2e-2         | dmd     | kl_neu   | 180 |            -0.33258 |  -0.3857 |  -0.2856 | True          |   -0.0198 |      -0.0379 |      -0.0017 |    0.8022 |       0.5234 |       1.1312 |
| gemma4b_A_third_a5e-3 | ctx     | kl       |  60 |            -3.09206 |  -3.4691 |  -2.6752 | True          |    0.7545 |       0.6047 |       0.9322 |  nan      |     nan      |     nan      |
| gemma4b_A_third_a5e-3 | ctx     | kl_park  |  60 |            -0.17076 |  -0.2338 |  -0.0922 | True          |    4.1525 |       3.0822 |       7.3876 |  nan      |     nan      |     nan      |
| gemma4b_A_third_a5e-3 | ctx     | rd       |  60 |             0.04665 |   0.024  |   0.0709 | True          |   -2.1994 |      -5.3585 |      -1.0297 |  nan      |     nan      |     nan      |
| gemma4b_A_third_a5e-3 | ctx     | cf_dev   |  60 |            -0.00815 |  -0.0543 |   0.0375 | False         |    5.2302 |     -28.1151 |      30.7637 |  nan      |     nan      |     nan      |
| gemma4b_A_third_a5e-3 | ctx     | kl_neu   |  60 |            -2.72295 |  -3.0832 |  -2.3288 | True          |    0.4556 |       0.3751 |       0.5687 |  nan      |     nan      |     nan      |
| gemma4b_A_third_a5e-3 | unemb   | kl       |  60 |            -0.76473 |  -1.0276 |  -0.4802 | True          |   -0.206  |      -0.3268 |      -0.151  |    2.0394 |       1.5644 |       3.2101 |
| gemma4b_A_third_a5e-3 | unemb   | kl_park  |  60 |             0.14835 |   0.0938 |   0.2075 | True          |    0.3702 |       0.2447 |       0.6009 |   -4.8321 |      -8.1146 |      -3.2551 |
| gemma4b_A_third_a5e-3 | unemb   | rd       |  60 |             0.09159 |   0.0706 |   0.1137 | True          |    0.1048 |      -0.0246 |       0.2129 |    0.5583 |       0.1925 |       0.8075 |
| gemma4b_A_third_a5e-3 | unemb   | cf_dev   |  60 |             0.03045 |  -0.0061 |   0.067  | False         |   -1.0473 |      -7.1926 |       3.7259 |   -2.4822 |     -28.8952 |      18.0408 |
| gemma4b_A_third_a5e-3 | unemb   | kl_neu   |  60 |            -0.88485 |  -1.1148 |  -0.6363 | True          |   -0.1116 |      -0.1601 |      -0.0869 |    0.4357 |       0.2451 |       0.7231 |
| gemma4b_A_third_a5e-3 | dmd     | kl       |  60 |             0.1192  |   0.0087 |   0.2406 | True          |   -0.4599 |      -1.6661 |       0.0156 |  -66.7956 |    -353.553  |     -31.5476 |
| gemma4b_A_third_a5e-3 | dmd     | kl_park  |  60 |             0.19398 |   0.1332 |   0.2583 | True          |   -0.1487 |      -0.2034 |      -0.0856 |   -6.1618 |      -9.3095 |      -4.4323 |
| gemma4b_A_third_a5e-3 | dmd     | rd       |  60 |             0.08322 |   0.0608 |   0.109  | True          |    0.0164 |      -0.0588 |       0.0742 |   -0.227  |      -0.5998 |       0.0278 |
| gemma4b_A_third_a5e-3 | dmd     | cf_dev   |  60 |             0.11176 |   0.0697 |   0.1525 | True          |   -0.2532 |      -0.3944 |      -0.1709 |   -3.7687 |      -6.4728 |      -2.4995 |
| gemma4b_A_third_a5e-3 | dmd     | kl_neu   |  60 |            -0.12291 |  -0.246  |   0.0047 | False         |   -0.2259 |      -2.2879 |       0.5357 |   28.6337 |     -73.8851 |     200.224  |
| A_ing_a5e-3           | ctx     | kl       | 180 |            -2.78953 |  -3.0755 |  -2.4834 | True          |    0.757  |       0.6426 |       0.9058 |  nan      |     nan      |     nan      |
| A_ing_a5e-3           | ctx     | kl_park  | 180 |             0.25681 |   0.1976 |   0.3169 | True          |   -1.2834 |      -1.6773 |      -1.0234 |  nan      |     nan      |     nan      |
| A_ing_a5e-3           | ctx     | rd       | 180 |             0.09155 |   0.0755 |   0.1097 | True          |   -0.0556 |      -0.1185 |      -0.0093 |  nan      |     nan      |     nan      |
| A_ing_a5e-3           | ctx     | cf_dev   | 180 |            -0.02374 |  -0.0444 |  -0.004  | True          |    6.3643 |       3.3761 |      25.8724 |  nan      |     nan      |     nan      |
| A_ing_a5e-3           | ctx     | kl_neu   | 180 |            -2.67089 |  -2.9295 |  -2.411  | True          |    0.4004 |       0.3399 |       0.4756 |  nan      |     nan      |     nan      |
| A_ing_a5e-3           | unemb   | kl       | 180 |            -0.9171  |  -1.0967 |  -0.7457 | True          |   -0.1074 |      -0.1313 |      -0.089  |    0.7364 |       0.5981 |       0.9154 |
| A_ing_a5e-3           | unemb   | kl_park  | 180 |             0.25377 |   0.2214 |   0.286  | True          |    0.2815 |       0.2237 |       0.3495 |   -1.2781 |      -1.5973 |      -1.0246 |
| A_ing_a5e-3           | unemb   | rd       | 180 |             0.13602 |   0.1208 |   0.1501 | True          |    0.1836 |       0.1247 |       0.2525 |    0.4341 |       0.3682 |       0.4966 |
| A_ing_a5e-3           | unemb   | cf_dev   | 180 |             0.04098 |   0.0307 |   0.0512 | True          |   -0.1803 |      -0.4344 |       0.0188 |   -5.2646 |      -7.193  |      -3.9827 |
| A_ing_a5e-3           | unemb   | kl_neu   | 180 |            -1.15764 |  -1.3371 |  -0.9855 | True          |   -0.058  |      -0.07   |      -0.0481 |   -0.3202 |      -0.3987 |      -0.2547 |
| A_ing_a5e-3           | dmd     | kl       | 180 |             1.15769 |   0.8108 |   1.4998 | True          |   -1.8586 |      -2.582  |      -1.4762 |   -1.3475 |      -2.1463 |      -0.6692 |
| A_ing_a5e-3           | dmd     | kl_park  | 180 |             0.63642 |   0.5655 |   0.7129 | True          |   -0.3034 |      -0.3613 |      -0.2541 |   -0.142  |      -0.24   |      -0.0468 |
| A_ing_a5e-3           | dmd     | rd       | 180 |             0.0754  |   0.0599 |   0.093  | True          |   -0.0063 |      -0.0288 |       0.0147 |    0.5186 |       0.4038 |       0.6689 |
| A_ing_a5e-3           | dmd     | cf_dev   | 180 |             0.1678  |   0.1457 |   0.1903 | True          |   -0.6051 |      -0.7764 |      -0.4628 |   -0.2526 |      -0.4837 |      -0.0424 |
| A_ing_a5e-3           | dmd     | kl_neu   | 180 |             0.10334 |  -0.1542 |   0.3701 | False         |   -8.2317 |     -72.6135 |      66.1308 |   -6.6084 |     -48.8745 |      50.8614 |
| gpt2_A_ing_a5e-3      | unemb   | kl       |  60 |            -1.02189 |  -1.4517 |  -0.6018 | True          |   -0.6148 |      -1.1953 |      -0.3812 |   -0.1195 |      -0.3735 |       0.0539 |
| gpt2_A_ing_a5e-3      | unemb   | kl_park  |  60 |             0.26222 |   0.2194 |   0.3074 | True          |    0.3976 |       0.3332 |       0.4887 |    0.0386 |      -0.1683 |       0.1883 |
| gpt2_A_ing_a5e-3      | unemb   | rd       |  60 |             0.06734 |   0.0462 |   0.0889 | True          |    0.1562 |       0.0438 |       0.2911 |    0.1443 |      -0.1167 |       0.3042 |
| gpt2_A_ing_a5e-3      | unemb   | cf_dev   |  60 |             0.05548 |   0.0262 |   0.0859 | True          |   -0.3877 |      -1.9067 |       0.1107 |   -3.4395 |      -8.1518 |      -1.8459 |
| gpt2_A_ing_a5e-3      | unemb   | kl_neu   |  60 |            -1.09283 |  -1.511  |  -0.6584 | True          |   -0.5481 |      -1.0592 |      -0.3379 |   -0.9241 |      -1.6115 |      -0.628  |
| gpt2_A_ing_a5e-3      | dmd     | kl       |  60 |            -1.24028 |  -1.7205 |  -0.8101 | True          |    2.3442 |       1.6508 |       3.6072 |   -1.0737 |      -1.5409 |      -0.7589 |
| gpt2_A_ing_a5e-3      | dmd     | kl_park  |  60 |             0.18905 |   0.1165 |   0.273  | True          |   -1.5961 |      -2.6123 |      -1.1271 |    0.3743 |       0.2625 |       0.5062 |
| gpt2_A_ing_a5e-3      | dmd     | rd       |  60 |             0.04812 |   0.0306 |   0.0683 | True          |   -0.0503 |      -0.1904 |       0.0301 |    0.2061 |       0.1221 |       0.3233 |
| gpt2_A_ing_a5e-3      | dmd     | cf_dev   |  60 |            -0.03633 |  -0.0634 |  -0.0058 | True          |    7.8693 |       4.7128 |      30.4518 |   -0.8376 |      -4.4228 |      -0.2424 |
| gpt2_A_ing_a5e-3      | dmd     | kl_neu   |  60 |            -1.25038 |  -1.6979 |  -0.8494 | True          |    1.205  |       0.8036 |       1.8861 |   -0.887  |      -1.2384 |      -0.6317 |

## advantage_regression

| group                 | pair(a-b)             | metric   | model      | term   |   coef_per_SD |       lo |       hi |     R2 |   n |   n_clusters |
|:----------------------|:----------------------|:---------|:-----------|:-------|--------------:|---------:|---------:|-------:|----:|-------------:|
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.01832 | -0.13099 |  0.11801 | 0.001  | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |      -0.16413 | -0.24626 | -0.06956 | 0.0841 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |       0.00381 | -0.09892 |  0.12365 | 0      | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl       | joint      | H0     |      -0.40097 | -0.69876 | -0.08199 | 0.1364 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl       | joint      | cf0    |      -0.21152 | -0.29645 | -0.10042 | 0.1364 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl       | joint      | log_pr |       0.42543 |  0.18691 |  0.68556 | 0.1364 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.15747 | -0.1979  | -0.10312 | 0.3765 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |      -0.0576  | -0.10692 |  0.00011 | 0.0504 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.15074 | -0.18716 | -0.10369 | 0.345  | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.18417 | -0.31301 | -0.06646 | 0.4061 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl_park  | joint      | cf0    |      -0.04689 | -0.08729 | -0.00177 | 0.4061 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.03288 | -0.06804 |  0.15061 | 0.4061 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.05079 | -0.06745 | -0.03329 | 0.2886 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.02364 | -0.04209 | -0.00188 | 0.0625 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.05184 | -0.06722 | -0.03502 | 0.3007 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | rd       | joint      | H0     |      -0.03203 | -0.06975 |  0.0054  | 0.3322 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | rd       | joint      | cf0    |      -0.017   | -0.03407 |  0.0012  | 0.3322 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | rd       | joint      | log_pr |      -0.01814 | -0.05365 |  0.01817 | 0.3322 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.04575 | -0.06954 | -0.02062 | 0.123  | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |      -2e-05   | -0.02149 |  0.02171 | 0      | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.05104 | -0.07506 | -0.02764 | 0.153  | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | cf_dev   | joint      | H0     |       0.03713 | -0.02287 |  0.08757 | 0.1671 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.01429 | -0.01235 |  0.03532 | 0.1671 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | cf_dev   | joint      | log_pr |      -0.08902 | -0.13984 | -0.02428 | 0.1671 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |       0.02741 | -0.11962 |  0.17905 | 0.0028 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.23673 | -0.30101 | -0.15343 | 0.206  | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |       0.03757 | -0.10203 |  0.17499 | 0.0052 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.33899 | -0.5967  | -0.04763 | 0.2739 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -0.28802 | -0.36696 | -0.18045 | 0.2739 | 180 |           47 |
| A_third_a5e-3         | euc_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.41584 |  0.18296 |  0.65359 | 0.2739 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl       | uni_H0     | H0     |       0.10072 | -0.0536  |  0.26751 | 0.018  | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl       | uni_cf0    | cf0    |      -0.25618 | -0.37193 | -0.13069 | 0.1166 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl       | uni_log_pr | log_pr |       0.17713 |  0.02073 |  0.37078 | 0.0558 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl       | joint      | H0     |      -1.00334 | -1.22712 | -0.74198 | 0.3839 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl       | joint      | cf0    |      -0.40323 | -0.51778 | -0.2791  | 0.3839 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl       | joint      | log_pr |       1.20696 |  0.9293  |  1.45269 | 0.3839 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.09393 | -0.13842 | -0.04509 | 0.2064 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |      -0.02739 | -0.0729  |  0.02471 | 0.0175 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.08039 | -0.12298 | -0.03327 | 0.1512 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.19898 | -0.31029 | -0.09865 | 0.2427 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl_park  | joint      | cf0    |      -0.03153 | -0.07132 |  0.00948 | 0.2427 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.11416 |  0.02309 |  0.21857 | 0.2427 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | rd       | uni_H0     | H0     |      -0.0397  | -0.05817 | -0.01404 | 0.1922 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.0166  | -0.03543 |  0.00442 | 0.0336 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.0374  | -0.05396 | -0.01341 | 0.1706 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | rd       | joint      | H0     |      -0.05466 | -0.09646 | -0.00845 | 0.216  | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | rd       | joint      | cf0    |      -0.01493 | -0.03173 |  0.00258 | 0.216  | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | rd       | joint      | log_pr |       0.0173  | -0.02311 |  0.05887 | 0.216  | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |      -0.04468 | -0.06849 | -0.01943 | 0.1247 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |       0.02395 |  0.00541 |  0.04642 | 0.0358 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |      -0.03648 | -0.06194 | -0.01119 | 0.0831 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.07404 | -0.13503 | -0.02332 | 0.1793 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | cf_dev   | joint      | cf0    |       0.0252  |  0.00337 |  0.04724 | 0.1793 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.02853 | -0.02623 |  0.09632 | 0.1793 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |       0.11239 | -0.04547 |  0.29427 | 0.0256 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -0.30386 | -0.40798 | -0.19551 | 0.1868 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |       0.17402 |  0.00894 |  0.34678 | 0.0613 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl_neu   | joint      | H0     |      -0.89915 | -1.10159 | -0.64683 | 0.459  | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -0.44191 | -0.54249 | -0.33416 | 0.459  | 180 |           47 |
| A_third_a5e-3         | cau_unemb - dua_unemb | kl_neu   | joint      | log_pr |       1.11301 |  0.85146 |  1.33796 | 0.459  | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl       | uni_H0     | H0     |      -1.9459  | -2.41101 | -1.49379 | 0.2753 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl       | uni_cf0    | cf0    |      -0.1337  | -0.6514  |  0.56278 | 0.0013 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl       | uni_log_pr | log_pr |      -1.73081 | -2.12921 | -1.29944 | 0.2178 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl       | joint      | H0     |      -3.01001 | -4.54865 | -1.44888 | 0.2841 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl       | joint      | cf0    |      -0.07754 | -0.58266 |  0.45265 | 0.2841 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl       | joint      | log_pr |       1.13243 | -0.35718 |  2.62977 | 0.2841 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.30947 | -0.33891 | -0.27806 | 0.8254 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |      -0.03569 | -0.09176 |  0.03904 | 0.011  | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.30794 | -0.33494 | -0.27911 | 0.8173 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.16306 | -0.24518 | -0.0691  | 0.8451 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.01075 | -0.01451 |  0.0428  | 0.8451 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl_park  | joint      | log_pr |      -0.15582 | -0.23757 | -0.08052 | 0.8451 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | rd       | uni_H0     | H0     |      -0.01489 | -0.02858 | -0.00085 | 0.0328 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | rd       | uni_cf0    | cf0    |       0.00995 |  0.00105 |  0.02065 | 0.0147 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.02585 | -0.03906 | -0.0127  | 0.0988 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | rd       | joint      | H0     |       0.11596 |  0.08509 |  0.14609 | 0.3239 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | rd       | joint      | cf0    |       0.02725 |  0.01758 |  0.0393  | 0.3239 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | rd       | joint      | log_pr |      -0.141   | -0.1735  | -0.1094  | 0.3239 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |       0.00932 | -0.01958 |  0.03701 | 0.0038 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |       0.14722 |  0.13997 |  0.15644 | 0.9415 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.03077 |  0.00224 |  0.05976 | 0.0411 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.06076 | -0.07785 | -0.04126 | 0.9569 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | cf_dev   | joint      | cf0    |       0.14091 |  0.13518 |  0.14815 | 0.9569 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.06009 |  0.04146 |  0.07762 | 0.9569 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |      -0.88846 | -1.41773 | -0.31946 | 0.1109 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -2.08844 | -2.4257  | -1.68925 | 0.6126 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |      -0.95454 | -1.50005 | -0.40677 | 0.128  | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl_neu   | joint      | H0     |      -1.81865 | -2.56666 | -1.1213  | 0.6992 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -2.15701 | -2.52351 | -1.81346 | 0.6992 | 180 |           47 |
| A_third_a5e-3         | frq_unemb - dua_unemb | kl_neu   | joint      | log_pr |       1.19715 |  0.50181 |  1.90744 | 0.6992 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl       | uni_H0     | H0     |       2.04662 |  1.57266 |  2.53282 | 0.2979 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl       | uni_cf0    | cf0    |      -0.12248 | -0.744   |  0.38081 | 0.0011 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl       | uni_log_pr | log_pr |       1.90794 |  1.51247 |  2.35709 | 0.2589 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl       | joint      | H0     |       2.00667 |  0.46761 |  3.65289 | 0.305  | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl       | joint      | cf0    |      -0.32569 | -0.80248 |  0.15144 | 0.305  | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl       | joint      | log_pr |       0.07453 | -1.50158 |  1.5574  | 0.305  | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl_park  | uni_H0     | H0     |       0.21554 |  0.17457 |  0.26215 | 0.5037 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl_park  | uni_cf0    | cf0    |       0.00831 | -0.04389 |  0.05171 | 0.0007 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl_park  | uni_log_pr | log_pr |       0.22755 |  0.18833 |  0.27193 | 0.5614 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl_park  | joint      | H0     |      -0.03592 | -0.13071 |  0.06631 | 0.5783 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl_park  | joint      | cf0    |      -0.04227 | -0.08616 |  0.00152 | 0.5783 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl_park  | joint      | log_pr |       0.26998 |  0.17389 |  0.36982 | 0.5783 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | rd       | uni_H0     | H0     |      -0.02481 | -0.04655 |  0.00302 | 0.0481 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | rd       | uni_cf0    | cf0    |      -0.02656 | -0.04609 | -0.00448 | 0.0551 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | rd       | uni_log_pr | log_pr |      -0.01155 | -0.03251 |  0.01704 | 0.0104 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | rd       | joint      | H0     |      -0.17062 | -0.2223  | -0.12067 | 0.2755 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | rd       | joint      | cf0    |      -0.04218 | -0.06229 | -0.02262 | 0.2755 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | rd       | joint      | log_pr |       0.1583  |  0.1067  |  0.21698 | 0.2755 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | cf_dev   | uni_H0     | H0     |      -0.05401 | -0.07663 | -0.02431 | 0.1026 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | cf_dev   | uni_cf0    | cf0    |      -0.12326 | -0.14082 | -0.10444 | 0.5346 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | cf_dev   | uni_log_pr | log_pr |      -0.06726 | -0.08658 | -0.04228 | 0.1592 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | cf_dev   | joint      | H0     |      -0.01328 | -0.06696 |  0.02782 | 0.6018 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | cf_dev   | joint      | cf0    |      -0.11571 | -0.13606 | -0.09698 | 0.6018 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | cf_dev   | joint      | log_pr |      -0.03157 | -0.078   |  0.02483 | 0.6018 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl_neu   | uni_H0     | H0     |       1.00085 |  0.58659 |  1.39591 | 0.1704 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl_neu   | uni_cf0    | cf0    |       1.78458 |  1.44446 |  2.08603 | 0.5416 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl_neu   | uni_log_pr | log_pr |       1.12855 |  0.71309 |  1.51773 | 0.2166 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl_neu   | joint      | H0     |       0.9195  |  0.22472 |  1.6573  | 0.6609 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl_neu   | joint      | cf0    |       1.7151  |  1.40266 |  2.04925 | 0.6609 | 180 |           47 |
| A_third_a5e-3         | cau_unemb - frq_unemb | kl_neu   | joint      | log_pr |      -0.08414 | -0.77216 |  0.60618 | 0.6609 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.57987 | -1.08553 | -0.11195 | 0.0504 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |       0.42044 | -0.04567 |  0.94776 | 0.0265 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |      -0.32941 | -0.79105 |  0.10226 | 0.0163 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl       | joint      | H0     |      -2.30448 | -3.91026 | -0.97208 | 0.1291 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl       | joint      | cf0    |       0.27792 | -0.17652 |  0.76136 | 0.1291 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl       | joint      | log_pr |       1.7953  |  0.62121 |  3.2191  | 0.1291 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.28303 | -0.34183 | -0.2249  | 0.4384 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |      -0.00739 | -0.07924 |  0.08892 | 0.0003 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.26672 | -0.32177 | -0.20682 | 0.3893 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.27375 | -0.43484 | -0.11107 | 0.4405 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl_park  | joint      | cf0    |       0.02067 | -0.03062 |  0.07927 | 0.4405 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl_park  | joint      | log_pr |      -0.01186 | -0.15806 |  0.12875 | 0.4405 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.04446 | -0.05806 | -0.02671 | 0.236  | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.02321 | -0.03726 | -0.00556 | 0.0643 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.05083 | -0.06314 | -0.03506 | 0.3085 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | rd       | joint      | H0     |       0.02449 | -0.01386 |  0.0664  | 0.3365 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | rd       | joint      | cf0    |      -0.01116 | -0.02427 |  0.00269 | 0.3365 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | rd       | joint      | log_pr |      -0.07177 | -0.10554 | -0.03596 | 0.3365 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.00881 | -0.04199 |  0.02152 | 0.0025 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.10453 |  0.07935 |  0.12392 | 0.3506 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |       0.00215 | -0.02925 |  0.03417 | 0.0001 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.00539 | -0.08761 |  0.07357 | 0.3625 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.1079  |  0.08282 |  0.12921 | 0.3625 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | cf_dev   | joint      | log_pr |      -0.01431 | -0.09376 |  0.06465 | 0.3625 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |      -0.30112 | -0.61986 |  0.03562 | 0.0564 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.50411 | -0.8051  | -0.22063 | 0.158  | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |      -0.25614 | -0.57361 |  0.08496 | 0.0408 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -1.08644 | -1.76502 | -0.48205 | 0.2438 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -0.57953 | -0.86672 | -0.30919 | 0.2438 | 180 |           47 |
| A_third_a5e-3         | frq_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.88755 |  0.43436 |  1.38676 | 0.2438 | 180 |           47 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.28045 | -0.44385 | -0.11918 | 0.0535 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |       0.41068 |  0.25425 |  0.57052 | 0.1147 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |      -0.26018 | -0.42838 | -0.07414 | 0.0461 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl       | joint      | H0     |       0.102   | -0.16347 |  0.36605 | 0.1175 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl       | joint      | cf0    |       0.47639 |  0.17558 |  0.77201 | 0.1175 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl       | joint      | log_pr |      -0.02161 | -0.22609 |  0.19987 | 0.1175 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |       0.06942 | -0.04845 |  0.17041 | 0.0094 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |      -0.01406 | -0.11849 |  0.08597 | 0.0004 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |       0.0365  | -0.06155 |  0.14344 | 0.0026 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl_park  | joint      | H0     |       0.14178 | -0.06409 |  0.31447 | 0.0179 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl_park  | joint      | cf0    |       0.11076 | -0.07478 |  0.27576 | 0.0179 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.02355 | -0.10986 |  0.17184 | 0.0179 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | rd       | uni_H0     | H0     |       0.04013 |  0.00412 |  0.06796 | 0.0291 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.02009 | -0.05849 |  0.01198 | 0.0073 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |       0.02786 | -0.0042  |  0.06191 | 0.014  | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | rd       | joint      | H0     |       0.05797 |  0.00176 |  0.10841 | 0.0375 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | rd       | joint      | cf0    |       0.03502 | -0.02622 |  0.08813 | 0.0375 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | rd       | joint      | log_pr |       0.01615 | -0.0304  |  0.06082 | 0.0375 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.01171 | -0.03724 |  0.01076 | 0.0039 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.00757 | -0.01773 |  0.03143 | 0.0016 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.01092 | -0.03898 |  0.01901 | 0.0034 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.01276 | -0.0633  |  0.03389 | 0.0052 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | cf_dev   | joint      | cf0    |      -0.00744 | -0.06064 |  0.03989 | 0.0052 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | cf_dev   | joint      | log_pr |      -0.00818 | -0.04385 |  0.02872 | 0.0052 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |      -0.35997 | -0.43626 | -0.28243 | 0.2931 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |       0.45929 |  0.36142 |  0.5686  | 0.4772 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |      -0.25576 | -0.34288 | -0.17428 | 0.148  | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.02132 | -0.11816 |  0.0865  | 0.4812 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl_neu   | joint      | cf0    |       0.47681 |  0.32976 |  0.65323 | 0.4812 | 180 |          177 |
| C_third_a5e-3         | euc_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.05454 | -0.00853 |  0.12252 | 0.4812 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl       | uni_H0     | H0     |      -0.40324 | -0.50859 | -0.3027  | 0.2127 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl       | uni_cf0    | cf0    |       0.56713 |  0.44668 |  0.68125 | 0.4208 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl       | uni_log_pr | log_pr |      -0.33479 | -0.45902 | -0.21966 | 0.1466 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl       | joint      | H0     |       0.0892  | -0.05967 |  0.22707 | 0.4256 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl       | joint      | cf0    |       0.64786 |  0.44545 |  0.84378 | 0.4256 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl       | joint      | log_pr |       0.01835 | -0.10239 |  0.12779 | 0.4256 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl_park  | uni_H0     | H0     |       0.0345  | -0.00997 |  0.07191 | 0.0101 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |      -0.01354 | -0.06087 |  0.0327  | 0.0016 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |       0.01667 | -0.0522  |  0.07609 | 0.0024 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl_park  | joint      | H0     |       0.05939 | -0.02375 |  0.13072 | 0.0139 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.03526 | -0.05418 |  0.10959 | 0.0139 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.00429 | -0.0878  |  0.08143 | 0.0139 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | rd       | uni_H0     | H0     |       0.01826 | -0.00204 |  0.0368  | 0.01   | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.00964 | -0.03181 |  0.01144 | 0.0028 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.00908 | -0.03598 |  0.0161  | 0.0025 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | rd       | joint      | H0     |       0.0343  | -0.00671 |  0.07266 | 0.0274 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | rd       | joint      | cf0    |      -0.0018  | -0.04419 |  0.04054 | 0.0274 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | rd       | joint      | log_pr |      -0.03008 | -0.07121 |  0.00397 | 0.0274 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |       0.03833 |  0.0152  |  0.06119 | 0.0449 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |      -0.03906 | -0.06457 | -0.01672 | 0.0466 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.03607 |  0.01382 |  0.06061 | 0.0397 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | cf_dev   | joint      | H0     |       0.01619 | -0.03028 |  0.05705 | 0.0565 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | cf_dev   | joint      | cf0    |      -0.01609 | -0.06664 |  0.02555 | 0.0565 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.01663 | -0.01153 |  0.04676 | 0.0565 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |      -0.48663 | -0.56964 | -0.40469 | 0.378  | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |       0.63381 |  0.53617 |  0.73515 | 0.6411 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |      -0.34936 | -0.44649 | -0.25485 | 0.1948 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl_neu   | joint      | H0     |      -0.0044  | -0.1116  |  0.10162 | 0.6469 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl_neu   | joint      | cf0    |       0.6787  |  0.51343 |  0.85077 | 0.6469 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - dua_unemb | kl_neu   | joint      | log_pr |       0.07729 |  0.0185  |  0.14364 | 0.6469 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl       | uni_H0     | H0     |      -0.54633 | -0.71387 | -0.37668 | 0.2327 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl       | uni_cf0    | cf0    |       0.7133  |  0.56168 |  0.86024 | 0.3967 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl       | uni_log_pr | log_pr |      -0.32322 | -0.49057 | -0.16864 | 0.0814 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl       | joint      | H0     |      -0.02976 | -0.26779 |  0.21736 | 0.4161 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl       | joint      | cf0    |       0.81865 |  0.57774 |  1.0467  | 0.4161 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl       | joint      | log_pr |       0.20558 |  0.07052 |  0.34706 | 0.4161 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.17854 | -0.27516 | -0.07734 | 0.1101 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |       0.18172 |  0.09782 |  0.26758 | 0.1141 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.04386 | -0.12862 |  0.03738 | 0.0066 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.12606 | -0.27209 |  0.00435 | 0.1626 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.16745 |  0.07616 |  0.26115 | 0.1626 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.13383 |  0.03742 |  0.23742 | 0.1626 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | rd       | uni_H0     | H0     |       0.06342 |  0.03903 |  0.08519 | 0.0871 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.05734 | -0.08842 | -0.02787 | 0.0712 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | rd       | uni_log_pr | log_pr |       0.05956 |  0.02647 |  0.09095 | 0.0768 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | rd       | joint      | H0     |       0.03981 | -0.00299 |  0.08266 | 0.1043 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | rd       | joint      | cf0    |      -0.00595 | -0.05644 |  0.04246 | 0.1043 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | rd       | joint      | log_pr |       0.03277 | -0.00928 |  0.07561 | 0.1043 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |       0.00547 | -0.03224 |  0.03969 | 0.0011 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |      -0.0148  | -0.04013 |  0.01368 | 0.0078 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.02593 |  0.00337 |  0.04919 | 0.0238 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.0225  | -0.075   |  0.02417 | 0.0308 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | cf_dev   | joint      | cf0    |      -0.01299 | -0.04896 |  0.02238 | 0.0308 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.03085 |  0.00404 |  0.05905 | 0.0308 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |      -0.4637  | -0.54812 | -0.37574 | 0.3396 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |       0.61318 |  0.50072 |  0.72035 | 0.5938 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |      -0.31903 | -0.42741 | -0.21887 | 0.1607 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl_neu   | joint      | H0     |       0.00663 | -0.11393 |  0.12982 | 0.6045 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl_neu   | joint      | cf0    |       0.68344 |  0.48932 |  0.88134 | 0.6045 | 180 |          177 |
| C_third_a5e-3         | frq_unemb - dua_unemb | kl_neu   | joint      | log_pr |       0.1042  |  0.03523 |  0.17977 | 0.6045 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl       | uni_H0     | H0     |       0.14308 | -0.00309 |  0.28268 | 0.0359 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl       | uni_cf0    | cf0    |      -0.14617 | -0.26403 | -0.04095 | 0.0375 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl       | uni_log_pr | log_pr |      -0.01157 | -0.13179 |  0.11396 | 0.0002 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl       | joint      | H0     |       0.11896 | -0.08386 |  0.32276 | 0.0775 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl       | joint      | cf0    |      -0.17079 | -0.32246 | -0.01328 | 0.0775 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl       | joint      | log_pr |      -0.18723 | -0.33665 | -0.04358 | 0.0775 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl_park  | uni_H0     | H0     |       0.21303 |  0.09681 |  0.32746 | 0.097  | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl_park  | uni_cf0    | cf0    |      -0.19525 | -0.29143 | -0.09795 | 0.0815 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl_park  | uni_log_pr | log_pr |       0.06053 | -0.04833 |  0.17273 | 0.0078 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl_park  | joint      | H0     |       0.18545 |  0.01494 |  0.35154 | 0.1229 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl_park  | joint      | cf0    |      -0.13219 | -0.26746 | -0.00451 | 0.1229 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl_park  | joint      | log_pr |      -0.12954 | -0.26346 | -0.00308 | 0.1229 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | rd       | uni_H0     | H0     |      -0.04516 | -0.07421 | -0.01692 | 0.0281 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | rd       | uni_cf0    | cf0    |       0.04771 |  0.0143  |  0.08163 | 0.0313 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | rd       | uni_log_pr | log_pr |      -0.06864 | -0.10995 | -0.02855 | 0.0648 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | rd       | joint      | H0     |      -0.00552 | -0.06005 |  0.05185 | 0.0655 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | rd       | joint      | cf0    |       0.00415 | -0.0579  |  0.06347 | 0.0655 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | rd       | joint      | log_pr |      -0.06285 | -0.11939 | -0.00369 | 0.0655 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | cf_dev   | uni_H0     | H0     |       0.03286 | -0.00783 |  0.07724 | 0.0206 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | cf_dev   | uni_cf0    | cf0    |      -0.02426 | -0.06405 |  0.00795 | 0.0112 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | cf_dev   | uni_log_pr | log_pr |       0.01014 | -0.02413 |  0.04481 | 0.002  | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | cf_dev   | joint      | H0     |       0.03869 | -0.02438 |  0.09983 | 0.023  | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | cf_dev   | joint      | cf0    |      -0.00311 | -0.05706 |  0.04764 | 0.023  | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | cf_dev   | joint      | log_pr |      -0.01422 | -0.05613 |  0.02545 | 0.023  | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl_neu   | uni_H0     | H0     |      -0.02293 | -0.04324 | -0.00345 | 0.0247 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl_neu   | uni_cf0    | cf0    |       0.02063 | -0.01295 |  0.05287 | 0.02   | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl_neu   | uni_log_pr | log_pr |      -0.03033 | -0.05145 | -0.00989 | 0.0432 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl_neu   | joint      | H0     |      -0.01102 | -0.0492  |  0.02807 | 0.0455 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl_neu   | joint      | cf0    |      -0.00475 | -0.06459 |  0.05926 | 0.0455 | 180 |          177 |
| C_third_a5e-3         | cau_unemb - frq_unemb | kl_neu   | joint      | log_pr |      -0.02691 | -0.05212 | -0.00313 | 0.0455 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.9416  | -1.37427 | -0.55012 | 0.1162 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |       0.8389  |  0.42716 |  1.2844  | 0.0923 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |      -0.77433 | -1.15386 | -0.37235 | 0.0786 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl       | joint      | H0     |      -0.6576  | -1.3807  |  0.05214 | 0.1274 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl       | joint      | cf0    |       0.13538 | -0.53216 |  0.79905 | 0.1274 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl       | joint      | log_pr |      -0.30866 | -0.94626 |  0.29464 | 0.1274 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.30282 | -0.37917 | -0.21157 | 0.2552 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |       0.24648 |  0.1746  |  0.31846 | 0.1691 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.15126 | -0.22108 | -0.08614 | 0.0637 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.29247 | -0.42384 | -0.13308 | 0.2601 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl_park  | joint      | cf0    |       0.05045 | -0.04523 |  0.15117 | 0.2601 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.04974 | -0.03771 |  0.13932 | 0.2601 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | rd       | uni_H0     | H0     |       0.05091 |  0.0277  |  0.07474 | 0.0619 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.04118 | -0.07094 | -0.01457 | 0.0405 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |       0.06439 |  0.03428 |  0.09236 | 0.099  | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | rd       | joint      | H0     |       0.03389 | -0.00954 |  0.07529 | 0.1095 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | rd       | joint      | cf0    |       0.02149 | -0.02807 |  0.06315 | 0.1095 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | rd       | joint      | log_pr |       0.05818 |  0.02194 |  0.09516 | 0.1095 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.02005 | -0.03724 | -0.00547 | 0.08   | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.02157 |  0.00778 |  0.0358  | 0.0926 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.0125  | -0.02326 | -0.00296 | 0.0311 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.00902 | -0.03172 |  0.00922 | 0.0991 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.01644 |  0.00017 |  0.03423 | 0.0991 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | cf_dev   | joint      | log_pr |       0.00299 | -0.00786 |  0.01432 | 0.0991 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |      -0.26496 | -0.35667 | -0.17586 | 0.1366 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |       0.31101 |  0.17419 |  0.45899 | 0.1882 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |      -0.16731 | -0.27614 | -0.07131 | 0.0545 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.07224 | -0.22646 |  0.09318 | 0.1944 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl_neu   | joint      | cf0    |       0.28961 |  0.06001 |  0.54703 | 0.1944 | 180 |          177 |
| C_third_a5e-3         | frq_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.05553 | -0.02878 |  0.14017 | 0.1944 | 180 |          177 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.5242  | -0.70356 | -0.33916 | 0.1401 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |       0.69677 |  0.51382 |  0.88231 | 0.2475 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |      -0.45793 | -0.64492 | -0.28235 | 0.1069 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl       | joint      | H0     |       0.00936 | -0.32775 |  0.33261 | 0.2479 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl       | joint      | cf0    |       0.7255  |  0.39895 |  1.06393 | 0.2479 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl       | joint      | log_pr |       0.03155 | -0.21359 |  0.29904 | 0.2479 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.06234 | -0.17606 |  0.04602 | 0.0073 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |       0.09348 | -0.0214  |  0.20774 | 0.0164 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.00043 | -0.10473 |  0.10111 | 0      | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.02622 | -0.22148 |  0.15264 | 0.0311 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl_park  | joint      | cf0    |       0.16012 |  0.00969 |  0.30924 | 0.0311 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.12686 | -0.02877 |  0.29166 | 0.0311 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | rd       | uni_H0     | H0     |       0.01801 | -0.01894 |  0.05125 | 0.006  | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.00724 | -0.03822 |  0.02658 | 0.001  | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |       0.03645 |  0.0016  |  0.06524 | 0.0247 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | rd       | joint      | H0     |       0.0085  | -0.05316 |  0.0617  | 0.0361 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | rd       | joint      | cf0    |       0.03795 | -0.00658 |  0.08777 | 0.0361 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | rd       | joint      | log_pr |       0.0566  |  0.01039 |  0.10813 | 0.0361 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.01851 | -0.0517  |  0.01271 | 0.0081 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.0138  | -0.01382 |  0.04196 | 0.0045 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |       0.00625 | -0.01708 |  0.0321  | 0.0009 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.03426 | -0.09432 |  0.01894 | 0.0255 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.01464 | -0.02999 |  0.05848 | 0.0255 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | cf_dev   | joint      | log_pr |       0.03958 | -0.00054 |  0.08702 | 0.0255 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |      -0.51268 | -0.59664 | -0.4308  | 0.3663 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |       0.7046  |  0.61769 |  0.79563 | 0.6918 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |      -0.48579 | -0.5794  | -0.40031 | 0.3289 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl_neu   | joint      | H0     |       0.07511 | -0.0237  |  0.17884 | 0.6948 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl_neu   | joint      | cf0    |       0.74142 |  0.57803 |  0.91494 | 0.6948 | 180 |          178 |
| Cbig_third_a5e-3      | euc_dmd - dua_dmd     | kl_neu   | joint      | log_pr |      -0.0302  | -0.10616 |  0.04931 | 0.6948 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl       | uni_H0     | H0     |      -0.55459 | -0.68049 | -0.42637 | 0.2655 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl       | uni_cf0    | cf0    |       0.69479 |  0.5394  |  0.85698 | 0.4166 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl       | uni_log_pr | log_pr |      -0.48399 | -0.61967 | -0.36177 | 0.2022 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl       | joint      | H0     |      -0.05528 | -0.23355 |  0.13246 | 0.4178 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl       | joint      | cf0    |       0.65199 |  0.39476 |  0.90619 | 0.4178 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl       | joint      | log_pr |      -0.00074 | -0.15088 |  0.14857 | 0.4178 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.02241 | -0.09884 |  0.04934 | 0.0026 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |      -0.00632 | -0.07339 |  0.06016 | 0.0002 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |       0.02216 | -0.03552 |  0.07733 | 0.0025 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.08845 | -0.20748 |  0.01778 | 0.0182 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl_park  | joint      | cf0    |      -0.03318 | -0.137   |  0.0535  | 0.0182 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.05971 | -0.02234 |  0.15302 | 0.0182 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | rd       | uni_H0     | H0     |       0.01545 | -0.01289 |  0.0417  | 0.0066 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.01973 | -0.04572 |  0.00698 | 0.0108 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.00446 | -0.03265 |  0.02061 | 0.0005 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | rd       | joint      | H0     |       0.01544 | -0.03    |  0.05564 | 0.0299 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | rd       | joint      | cf0    |      -0.03406 | -0.07839 |  0.00918 | 0.0299 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | rd       | joint      | log_pr |      -0.03825 | -0.07581 | -0.00537 | 0.0299 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |       0.03758 |  0.00452 |  0.06929 | 0.0372 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |      -0.04856 | -0.07728 | -0.01878 | 0.0621 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.05313 |  0.02885 |  0.0772  | 0.0743 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.01492 | -0.06704 |  0.03772 | 0.0839 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | cf_dev   | joint      | cf0    |      -0.03138 | -0.07195 |  0.00789 | 0.0839 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.04183 |  0.00199 |  0.08408 | 0.0839 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |      -0.57157 | -0.66177 | -0.4779  | 0.3781 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |       0.77209 |  0.65505 |  0.89355 | 0.6899 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |      -0.52777 | -0.62868 | -0.43062 | 0.3224 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl_neu   | joint      | H0     |       0.05203 | -0.04381 |  0.15594 | 0.6911 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl_neu   | joint      | cf0    |       0.80125 |  0.6133  |  1.02182 | 0.6911 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - dua_unemb | kl_neu   | joint      | log_pr |      -0.01557 | -0.09897 |  0.07121 | 0.6911 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl       | uni_H0     | H0     |      -0.81785 | -1.02888 | -0.59652 | 0.2038 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl       | uni_cf0    | cf0    |       1.04899 |  0.81158 |  1.28641 | 0.3353 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl       | uni_log_pr | log_pr |      -0.69564 | -0.89708 | -0.49127 | 0.1474 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl       | joint      | H0     |      -0.05881 | -0.45979 |  0.34377 | 0.3359 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl       | joint      | cf0    |       1.04323 |  0.62631 |  1.48761 | 0.3359 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl       | joint      | log_pr |       0.05741 | -0.20333 |  0.30246 | 0.3359 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.32485 | -0.41668 | -0.21773 | 0.164  | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |       0.32659 |  0.22123 |  0.43533 | 0.1657 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.23271 | -0.32514 | -0.12844 | 0.0841 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.1962  | -0.36952 | -0.01171 | 0.188  | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.20407 |  0.0297  |  0.37729 | 0.188  | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.04035 | -0.08097 |  0.16984 | 0.188  | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | rd       | uni_H0     | H0     |       0.05719 |  0.02903 |  0.0816  | 0.0677 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.05382 | -0.08098 | -0.02761 | 0.0599 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | rd       | uni_log_pr | log_pr |       0.06914 |  0.03966 |  0.09705 | 0.0989 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | rd       | joint      | H0     |       0.01746 | -0.03313 |  0.06092 | 0.1029 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | rd       | joint      | cf0    |      -0.0025  | -0.04461 |  0.03738 | 0.1029 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | rd       | joint      | log_pr |       0.05554 |  0.01362 |  0.10078 | 0.1029 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |      -0.03965 | -0.07472 |  0.00086 | 0.021  | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |       0.04554 |  0.00884 |  0.08231 | 0.0277 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |      -0.03697 | -0.07392 |  0.00396 | 0.0182 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.00836 | -0.07365 |  0.05743 | 0.0289 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | cf_dev   | joint      | cf0    |       0.03335 | -0.03198 |  0.09624 | 0.0289 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | cf_dev   | joint      | log_pr |      -0.00848 | -0.05917 |  0.04559 | 0.0289 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |      -0.50939 | -0.60645 | -0.41255 | 0.3183 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |       0.69423 |  0.56178 |  0.83016 | 0.5913 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |      -0.4673  | -0.57476 | -0.3764  | 0.2679 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl_neu   | joint      | H0     |       0.0533  | -0.05671 |  0.16987 | 0.5927 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl_neu   | joint      | cf0    |       0.73341 |  0.50613 |  0.98142 | 0.5927 | 180 |          178 |
| Cbig_third_a5e-3      | frq_unemb - dua_unemb | kl_neu   | joint      | log_pr |      -0.00234 | -0.09263 |  0.09175 | 0.5927 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl       | uni_H0     | H0     |       0.26325 |  0.04415 |  0.47635 | 0.0306 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl       | uni_cf0    | cf0    |      -0.3542  | -0.57318 | -0.154   | 0.0553 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl       | uni_log_pr | log_pr |       0.21165 |  0.04116 |  0.38953 | 0.0198 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl       | joint      | H0     |       0.00352 | -0.39809 |  0.38549 | 0.0561 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl       | joint      | cf0    |      -0.39124 | -0.77275 | -0.04413 | 0.0561 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl       | joint      | log_pr |      -0.05815 | -0.3171  |  0.16412 | 0.0561 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl_park  | uni_H0     | H0     |       0.30244 |  0.16544 |  0.42785 | 0.0992 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl_park  | uni_cf0    | cf0    |      -0.33291 | -0.46512 | -0.20789 | 0.1202 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl_park  | uni_log_pr | log_pr |       0.25488 |  0.12942 |  0.36574 | 0.0704 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl_park  | joint      | H0     |       0.10775 | -0.11889 |  0.33758 | 0.1263 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl_park  | joint      | cf0    |      -0.23725 | -0.4329  | -0.04119 | 0.1263 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl_park  | joint      | log_pr |       0.01936 | -0.14085 |  0.16464 | 0.1263 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | rd       | uni_H0     | H0     |      -0.04174 | -0.07893 | -0.00208 | 0.0203 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | rd       | uni_cf0    | cf0    |       0.03409 | -0.00511 |  0.07425 | 0.0136 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | rd       | uni_log_pr | log_pr |      -0.0736  | -0.11329 | -0.03651 | 0.0632 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | rd       | joint      | H0     |      -0.00202 | -0.06608 |  0.06319 | 0.069  | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | rd       | joint      | cf0    |      -0.03156 | -0.09195 |  0.02964 | 0.069  | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | rd       | joint      | log_pr |      -0.09379 | -0.15437 | -0.04162 | 0.069  | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | cf_dev   | uni_H0     | H0     |       0.07723 |  0.03165 |  0.1204  | 0.0586 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | cf_dev   | uni_cf0    | cf0    |      -0.09411 | -0.13819 | -0.05217 | 0.0869 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | cf_dev   | uni_log_pr | log_pr |       0.09009 |  0.04575 |  0.13263 | 0.0797 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | cf_dev   | joint      | H0     |      -0.00656 | -0.07621 |  0.06149 | 0.0993 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | cf_dev   | joint      | cf0    |      -0.06474 | -0.13187 |  0.00115 | 0.0993 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | cf_dev   | joint      | log_pr |       0.05031 | -0.00887 |  0.10886 | 0.0993 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl_neu   | uni_H0     | H0     |      -0.06218 | -0.08901 | -0.03629 | 0.0818 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl_neu   | uni_cf0    | cf0    |       0.07786 |  0.03737 |  0.11966 | 0.1283 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl_neu   | uni_log_pr | log_pr |      -0.06047 | -0.08957 | -0.03391 | 0.0774 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl_neu   | joint      | H0     |      -0.00127 | -0.03973 |  0.03699 | 0.1304 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl_neu   | joint      | cf0    |       0.06784 |  0.00228 |  0.13485 | 0.1304 | 180 |          178 |
| Cbig_third_a5e-3      | cau_unemb - frq_unemb | kl_neu   | joint      | log_pr |      -0.01323 | -0.04461 |  0.01775 | 0.1304 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.68096 | -0.86714 | -0.50991 | 0.2021 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |       0.79256 |  0.60998 |  0.99607 | 0.2738 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |      -0.626   | -0.90978 | -0.36565 | 0.1708 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl       | joint      | H0     |      -0.13486 | -0.47019 |  0.15475 | 0.2826 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl       | joint      | cf0    |       0.60859 |  0.28093 |  0.90861 | 0.2826 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl       | joint      | log_pr |      -0.11823 | -0.54269 |  0.24946 | 0.2826 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.1903  | -0.27548 | -0.12097 | 0.1444 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |       0.17537 |  0.10221 |  0.25314 | 0.1226 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.12547 | -0.25359 | -0.00809 | 0.0628 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.14808 | -0.26097 | -0.04151 | 0.155  | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl_park  | joint      | cf0    |       0.0849  | -0.01871 |  0.1733  | 0.155  | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.03338 | -0.16445 |  0.20974 | 0.155  | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.01111 | -0.04063 |  0.01797 | 0.003  | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |       0.01564 | -0.01541 |  0.04873 | 0.006  | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |       0.00309 | -0.03136 |  0.03882 | 0.0002 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | rd       | joint      | H0     |      -0.00878 | -0.06054 |  0.03769 | 0.0154 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | rd       | joint      | cf0    |       0.02837 | -0.02501 |  0.08247 | 0.0154 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | rd       | joint      | log_pr |       0.02846 | -0.01895 |  0.07767 | 0.0154 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |       0.01768 | -0.00418 |  0.03562 | 0.0186 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |      -0.02043 | -0.03761 |  0.00104 | 0.0248 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |       0.0104  | -0.02783 |  0.04277 | 0.0064 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | cf_dev   | joint      | H0     |       0.00846 | -0.0203  |  0.03602 | 0.0277 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | cf_dev   | joint      | cf0    |      -0.02023 | -0.04706 |  0.00471 | 0.0277 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | cf_dev   | joint      | log_pr |      -0.00919 | -0.06748 |  0.03832 | 0.0277 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |      -0.5347  | -0.62302 | -0.44565 | 0.3649 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |       0.73355 |  0.64305 |  0.8269  | 0.6867 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |      -0.49577 | -0.60168 | -0.40771 | 0.3137 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl_neu   | joint      | H0     |       0.06755 | -0.02832 |  0.17485 | 0.6889 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl_neu   | joint      | cf0    |       0.7787  |  0.61111 |  0.96473 | 0.6889 | 180 |          178 |
| Cbig_third_a5e-3      | frq_dmd - dua_dmd     | kl_neu   | joint      | log_pr |      -0.00956 | -0.09345 |  0.07269 | 0.6889 | 180 |          178 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl       | uni_H0     | H0     |       0.59893 |  0.37411 |  0.80057 | 0.3805 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |      -0.42655 | -0.58592 | -0.28719 | 0.193  | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |       0.58458 |  0.35447 |  0.78254 | 0.3625 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl       | joint      | H0     |      -0.23    | -0.79642 |  0.33408 | 0.4875 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl       | joint      | cf0    |      -0.38619 | -0.53415 | -0.2338  | 0.4875 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl       | joint      | log_pr |       0.74013 |  0.20843 |  1.32268 | 0.4875 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.12262 | -0.14937 | -0.09732 | 0.4803 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |       0.01256 | -0.02893 |  0.05138 | 0.005  | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.11504 | -0.14029 | -0.09254 | 0.4227 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.20697 | -0.29096 | -0.10571 | 0.5239 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl_park  | joint      | cf0    |      -0.04563 | -0.07843 | -0.0067  | 0.5239 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.07305 | -0.00757 |  0.14371 | 0.5239 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.03998 | -0.05437 | -0.02362 | 0.2616 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.00496 | -0.02362 |  0.01472 | 0.004  | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.03928 | -0.05386 | -0.02335 | 0.2525 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | rd       | joint      | H0     |      -0.06914 | -0.11565 | -0.01361 | 0.3309 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | rd       | joint      | cf0    |      -0.02478 | -0.04227 | -0.00691 | 0.3309 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | rd       | joint      | log_pr |       0.02204 | -0.02501 |  0.06681 | 0.3309 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.05874 | -0.07755 | -0.0378  | 0.2529 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.06175 |  0.04643 |  0.07724 | 0.2795 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.047   | -0.06821 | -0.02306 | 0.1619 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.05417 | -0.10645 | -0.00103 | 0.399  | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.04528 |  0.02746 |  0.05964 | 0.399  | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | cf_dev   | joint      | log_pr |       0.01135 | -0.04306 |  0.05761 | 0.399  | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |       0.6281  |  0.38724 |  0.82284 | 0.4119 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.45165 | -0.61341 | -0.31004 | 0.213  | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |       0.6032  |  0.35657 |  0.79848 | 0.3799 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.12951 | -0.68608 |  0.43958 | 0.5165 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -0.38962 | -0.53441 | -0.22234 | 0.5165 | 180 |           48 |
| gpt2_A_third_a5e-3    | euc_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.66335 |  0.14215 |  1.24226 | 0.5165 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl       | uni_H0     | H0     |       0.84428 |  0.64102 |  1.04041 | 0.4277 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl       | uni_cf0    | cf0    |      -0.70245 | -0.84624 | -0.55309 | 0.2961 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl       | uni_log_pr | log_pr |       0.82067 |  0.60745 |  1.00388 | 0.4041 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl       | joint      | H0     |      -0.54734 | -1.12771 |  0.05272 | 0.6184 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl       | joint      | cf0    |      -0.69155 | -0.84315 | -0.52605 | 0.6184 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl       | joint      | log_pr |       1.22711 |  0.69855 |  1.78772 | 0.6184 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.05862 | -0.07972 | -0.03519 | 0.2392 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |       0.00358 | -0.0255  |  0.03169 | 0.0009 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.04989 | -0.07118 | -0.02974 | 0.1732 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.16916 | -0.22819 | -0.09905 | 0.3202 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl_park  | joint      | cf0    |      -0.03694 | -0.06533 | -0.0049  | 0.3202 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.1039  |  0.05217 |  0.1554  | 0.3202 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | rd       | uni_H0     | H0     |      -0.03731 | -0.04834 | -0.02366 | 0.3178 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | rd       | uni_cf0    | cf0    |       0.00145 | -0.01408 |  0.01734 | 0.0005 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.03635 | -0.04742 | -0.02448 | 0.3017 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | rd       | joint      | H0     |      -0.05237 | -0.0846  | -0.01503 | 0.3519 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | rd       | joint      | cf0    |      -0.01451 | -0.02701 | -0.00192 | 0.3519 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | rd       | joint      | log_pr |       0.01077 | -0.01956 |  0.04089 | 0.3519 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |      -0.06587 | -0.0834  | -0.04525 | 0.419  | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |       0.06491 |  0.05207 |  0.08048 | 0.4068 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |      -0.05252 | -0.07241 | -0.02749 | 0.2663 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.07459 | -0.12207 | -0.02841 | 0.6223 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | cf_dev   | joint      | cf0    |       0.0437  |  0.02914 |  0.05642 | 0.6223 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.02485 | -0.01923 |  0.06557 | 0.6223 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |       0.84789 |  0.64489 |  1.04398 | 0.4466 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -0.71419 | -0.86035 | -0.5646  | 0.3169 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |       0.81621 |  0.60109 |  1.00364 | 0.4139 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl_neu   | joint      | H0     |      -0.47313 | -1.06742 |  0.1086  | 0.6415 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -0.69008 | -0.83986 | -0.5162  | 0.6415 | 180 |           48 |
| gpt2_A_third_a5e-3    | cau_unemb - dua_unemb | kl_neu   | joint      | log_pr |       1.15283 |  0.64043 |  1.73048 | 0.6415 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl       | uni_H0     | H0     |      -0.60041 | -1.1732  | -0.19121 | 0.0846 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl       | uni_cf0    | cf0    |       0.30307 |  0.01669 |  0.62867 | 0.0216 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl       | uni_log_pr | log_pr |      -0.43634 | -1.06979 | -0.01141 | 0.0447 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl       | joint      | H0     |      -1.11601 | -2.2844  | -0.08317 | 0.0957 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl       | joint      | cf0    |      -0.0813  | -0.60959 |  0.34785 | 0.0957 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl       | joint      | log_pr |       0.54454 | -0.56558 |  1.5551  | 0.0957 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.21777 | -0.23895 | -0.19659 | 0.8396 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |       0.09336 |  0.05363 |  0.13278 | 0.1543 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.19158 | -0.22922 | -0.14758 | 0.6498 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.21346 | -0.29111 | -0.13598 | 0.8405 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.00788 | -0.03499 |  0.04026 | 0.8405 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl_park  | joint      | log_pr |      -0.00131 | -0.07684 |  0.07983 | 0.8405 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | rd       | uni_H0     | H0     |      -0.03203 | -0.03987 | -0.02549 | 0.4804 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | rd       | uni_cf0    | cf0    |       0.01887 |  0.01014 |  0.02681 | 0.1667 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.03005 | -0.03926 | -0.02391 | 0.4227 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | rd       | joint      | H0     |      -0.00563 | -0.02315 |  0.01127 | 0.538  | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | rd       | joint      | cf0    |       0.01396 |  0.00651 |  0.02108 | 0.538  | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | rd       | joint      | log_pr |      -0.02347 | -0.04015 | -0.00691 | 0.538  | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |      -0.0866  | -0.12176 | -0.05886 | 0.2544 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |       0.14879 |  0.13844 |  0.15929 | 0.7509 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |      -0.038   | -0.07555 | -0.01    | 0.049  | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.07445 | -0.13026 | -0.01873 | 0.7892 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | cf_dev   | joint      | cf0    |       0.1238  |  0.0995  |  0.14314 | 0.7892 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.04209 | -0.00646 |  0.08563 | 0.7892 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |       0.19101 | -0.14329 |  0.44583 | 0.0204 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -0.61841 | -0.81524 | -0.42306 | 0.2136 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |       0.07012 | -0.2991  |  0.33802 | 0.0027 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl_neu   | joint      | H0     |      -0.4597  | -1.17941 |  0.1739  | 0.228  | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -0.75772 | -1.12206 | -0.45867 | 0.228  | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_unemb - dua_unemb | kl_neu   | joint      | log_pr |       0.39207 | -0.24497 |  1.01275 | 0.228  | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl       | uni_H0     | H0     |       1.09644 |  0.71256 |  1.58033 | 0.2463 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl       | uni_cf0    | cf0    |      -0.71159 | -1.07001 | -0.37659 | 0.1037 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl       | uni_log_pr | log_pr |       0.89924 |  0.48058 |  1.50004 | 0.1657 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl       | joint      | H0     |       0.93157 | -0.22666 |  2.12208 | 0.2645 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl       | joint      | cf0    |      -0.33529 | -0.75974 |  0.16951 | 0.2645 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl       | joint      | log_pr |       0.03477 | -1.03963 |  1.33664 | 0.2645 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl_park  | uni_H0     | H0     |       0.18132 |  0.15187 |  0.20648 | 0.7177 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl_park  | uni_cf0    | cf0    |      -0.06729 | -0.1066  | -0.02566 | 0.0989 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl_park  | uni_log_pr | log_pr |       0.16724 |  0.12626 |  0.2049  | 0.6106 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl_park  | joint      | H0     |       0.1497  |  0.05709 |  0.23376 | 0.722  | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl_park  | joint      | cf0    |      -0.0036  | -0.04399 |  0.03893 | 0.722  | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl_park  | joint      | log_pr |       0.03402 | -0.0567  |  0.13763 | 0.722  | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | rd       | uni_H0     | H0     |       0.0015  | -0.00829 |  0.01514 | 0.0013 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | rd       | uni_cf0    | cf0    |      -0.00834 | -0.01758 |  0.00035 | 0.0418 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | rd       | uni_log_pr | log_pr |       0.00127 | -0.00765 |  0.01413 | 0.001  | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | rd       | joint      | H0     |      -0.01729 | -0.03812 |  0.00458 | 0.0638 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | rd       | joint      | cf0    |      -0.01354 | -0.02651 | -0.00271 | 0.0638 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | rd       | joint      | log_pr |       0.01508 | -0.00214 |  0.03602 | 0.0638 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | cf_dev   | uni_H0     | H0     |       0.04749 |  0.02615 |  0.07081 | 0.1662 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | cf_dev   | uni_cf0    | cf0    |      -0.09554 | -0.10647 | -0.08349 | 0.6727 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | cf_dev   | uni_log_pr | log_pr |       0.01909 | -0.00588 |  0.04267 | 0.0269 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | cf_dev   | joint      | H0     |       0.01845 | -0.02389 |  0.06382 | 0.6808 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | cf_dev   | joint      | cf0    |      -0.08899 | -0.10501 | -0.06914 | 0.6808 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | cf_dev   | joint      | log_pr |      -0.00737 | -0.04472 |  0.02813 | 0.6808 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl_neu   | uni_H0     | H0     |       0.30623 |  0.07279 |  0.56539 | 0.0678 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl_neu   | uni_cf0    | cf0    |       0.19038 | -0.04156 |  0.40882 | 0.0262 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl_neu   | uni_log_pr | log_pr |       0.38014 |  0.14362 |  0.71554 | 0.1045 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl_neu   | joint      | H0     |       0.32501 | -0.37644 |  1.06955 | 0.1538 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl_neu   | joint      | cf0    |       0.335   |  0.04793 |  0.68629 | 0.1538 | 101 |           42 |
| gpt2_A_third_a5e-3    | cau_unemb - frq_unemb | kl_neu   | joint      | log_pr |       0.12977 | -0.50309 |  0.86386 | 0.1538 | 101 |           42 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl       | uni_H0     | H0     |       0.5816  |  0.32522 |  0.79114 | 0.3518 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |      -0.36106 | -0.51143 | -0.22106 | 0.1356 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |       0.57424 |  0.31045 |  0.79448 | 0.343  | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl       | joint      | H0     |      -0.16602 | -0.79823 |  0.40237 | 0.4226 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl       | joint      | cf0    |      -0.3084  | -0.46996 | -0.14812 | 0.4226 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl       | joint      | log_pr |       0.68179 |  0.13443 |  1.34094 | 0.4226 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.09588 | -0.13054 | -0.06851 | 0.378  | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |       0.02616 | -0.00926 |  0.05681 | 0.0281 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.08554 | -0.11734 | -0.06062 | 0.3008 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.17411 | -0.28825 | -0.04836 | 0.3986 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl_park  | joint      | cf0    |      -0.02055 | -0.0589  |  0.0267  | 0.3986 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.07553 | -0.02287 |  0.17258 | 0.3986 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.0295  | -0.04488 | -0.01649 | 0.183  | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.00786 | -0.02391 |  0.00686 | 0.013  | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.02951 | -0.04406 | -0.01801 | 0.1832 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | rd       | joint      | H0     |      -0.0554  | -0.09944 | -0.00172 | 0.2645 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | rd       | joint      | cf0    |      -0.02352 | -0.03989 | -0.0038  | 0.2645 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | rd       | joint      | log_pr |       0.01903 | -0.02277 |  0.05646 | 0.2645 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.04515 | -0.05868 | -0.02926 | 0.1867 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.06688 |  0.05767 |  0.07646 | 0.4098 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.0298  | -0.04604 | -0.0108  | 0.0814 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.06966 | -0.11825 | -0.02657 | 0.4768 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.05039 |  0.03287 |  0.06432 | 0.4768 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | cf_dev   | joint      | log_pr |       0.04398 |  0.00377 |  0.08312 | 0.4768 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |       0.59748 |  0.3495  |  0.8035  | 0.3768 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.38706 | -0.53349 | -0.24249 | 0.1581 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |       0.57904 |  0.31624 |  0.79799 | 0.3539 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.07707 | -0.73762 |  0.50212 | 0.4485 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -0.31724 | -0.47488 | -0.15044 | 0.4485 | 180 |           48 |
| gpt2_A_third_a5e-3    | frq_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.60123 |  0.00945 |  1.26812 | 0.4485 | 180 |           48 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.1275  | -0.18213 | -0.06199 | 0.1254 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |      -0.09398 | -0.15382 | -0.02702 | 0.0681 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |      -0.11655 | -0.16243 | -0.06093 | 0.1048 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl       | joint      | H0     |      -0.25395 | -0.46602 | -0.06686 | 0.1924 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl       | joint      | cf0    |      -0.09882 | -0.15282 | -0.03711 | 0.1924 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl       | joint      | log_pr |       0.14346 | -0.01745 |  0.33166 | 0.1924 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.1451  | -0.18169 | -0.10042 | 0.4315 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |      -0.0459  | -0.08573 |  0.00204 | 0.0432 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.14021 | -0.17309 | -0.10034 | 0.403  | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.14896 | -0.26361 | -0.05064 | 0.4532 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl_park  | joint      | cf0    |      -0.0334  | -0.06743 |  0.00388 | 0.4532 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.00739 | -0.08108 |  0.11282 | 0.4532 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.03654 | -0.05747 | -0.01526 | 0.1841 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.00655 | -0.02571 |  0.01346 | 0.0059 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.03779 | -0.05923 | -0.01705 | 0.1968 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | rd       | joint      | H0     |      -0.00728 | -0.04701 |  0.03488 | 0.1977 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | rd       | joint      | cf0    |       0.00032 | -0.01945 |  0.01981 | 0.1977 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | rd       | joint      | log_pr |      -0.03097 | -0.07332 |  0.00968 | 0.1977 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.03738 | -0.05791 | -0.01783 | 0.1457 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.00045 | -0.0147  |  0.0173  | 0      | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.04158 | -0.06102 | -0.02276 | 0.1803 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | cf_dev   | joint      | H0     |       0.02968 | -0.01349 |  0.06459 | 0.1974 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.01207 | -0.00673 |  0.02764 | 0.1974 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | cf_dev   | joint      | log_pr |      -0.07207 | -0.10733 | -0.02424 | 0.1974 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |      -0.06594 | -0.14591 |  0.01095 | 0.0651 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.15116 | -0.18705 | -0.10909 | 0.342  | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |      -0.06213 | -0.13404 |  0.00477 | 0.0578 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.21918 | -0.37518 | -0.05254 | 0.4265 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -0.16625 | -0.19981 | -0.12044 | 0.4265 | 180 |           47 |
| A_third_a2e-2         | euc_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.17845 |  0.04358 |  0.31779 | 0.4265 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl       | uni_H0     | H0     |      -0.06525 | -0.12368 |  0.00405 | 0.0505 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl       | uni_cf0    | cf0    |      -0.08255 | -0.13193 | -0.01909 | 0.0808 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl       | uni_log_pr | log_pr |      -0.03572 | -0.09324 |  0.03443 | 0.0151 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl       | joint      | H0     |      -0.40787 | -0.51821 | -0.29358 | 0.2737 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl       | joint      | cf0    |      -0.11901 | -0.16894 | -0.06272 | 0.2737 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl       | joint      | log_pr |       0.37395 |  0.26068 |  0.48362 | 0.2737 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.09606 | -0.13178 | -0.0538  | 0.3052 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |      -0.02242 | -0.05633 |  0.01605 | 0.0166 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.08516 | -0.11736 | -0.04513 | 0.2399 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.16791 | -0.26605 | -0.07205 | 0.3299 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl_park  | joint      | cf0    |      -0.02228 | -0.05432 |  0.01052 | 0.3299 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.07816 | -0.00226 |  0.16802 | 0.3299 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | rd       | uni_H0     | H0     |      -0.04026 | -0.05761 | -0.01765 | 0.225  | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.01361 | -0.0282  |  0.00178 | 0.0257 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.03873 | -0.05591 | -0.01899 | 0.2082 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | rd       | joint      | H0     |      -0.04408 | -0.08956 |  0.00169 | 0.2389 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | rd       | joint      | cf0    |      -0.01049 | -0.02594 |  0.00465 | 0.2389 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | rd       | joint      | log_pr |       0.00507 | -0.03714 |  0.0508  | 0.2389 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |      -0.04548 | -0.06869 | -0.02143 | 0.1787 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |       0.01311 | -0.00163 |  0.02979 | 0.0148 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |      -0.0416  | -0.0645  | -0.01912 | 0.1495 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.04189 | -0.09038 | -0.00283 | 0.2053 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | cf_dev   | joint      | cf0    |       0.01816 | -5e-05   |  0.03416 | 0.2053 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | cf_dev   | joint      | log_pr |      -0.00559 | -0.04607 |  0.04384 | 0.2053 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |      -0.02718 | -0.10489 |  0.04634 | 0.0121 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -0.11853 | -0.16063 | -0.07352 | 0.2298 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |      -0.00624 | -0.07786 |  0.06286 | 0.0006 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl_neu   | joint      | H0     |      -0.34471 | -0.45848 | -0.22652 | 0.4205 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -0.15636 | -0.19875 | -0.10879 | 0.4205 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - dua_unemb | kl_neu   | joint      | log_pr |       0.35114 |  0.24598 |  0.45718 | 0.4205 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl       | uni_H0     | H0     |      -2.11187 | -2.56709 | -1.64672 | 0.3091 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl       | uni_cf0    | cf0    |       0.03992 | -0.4721  |  0.6886  | 0.0001 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl       | uni_log_pr | log_pr |      -1.94366 | -2.36079 | -1.53996 | 0.2618 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl       | joint      | H0     |      -2.41454 | -4.02594 | -0.90999 | 0.3136 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl       | joint      | cf0    |       0.20668 | -0.27187 |  0.69727 | 0.3136 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl       | joint      | log_pr |       0.29941 | -1.17323 |  1.86257 | 0.3136 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.3116  | -0.34077 | -0.28351 | 0.8226 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |      -0.03073 | -0.08394 |  0.03709 | 0.008  | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.31271 | -0.34    | -0.28415 | 0.8284 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.132   | -0.21562 | -0.04583 | 0.8514 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.02    | -0.00526 |  0.04732 | 0.8514 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl_park  | joint      | log_pr |      -0.19182 | -0.27019 | -0.11281 | 0.8514 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | rd       | uni_H0     | H0     |      -0.01546 | -0.03302 |  0.00221 | 0.0279 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | rd       | uni_cf0    | cf0    |       0.01294 | -1e-05   |  0.02526 | 0.0195 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.02718 | -0.04441 | -0.00905 | 0.0862 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | rd       | joint      | H0     |       0.12654 |  0.09628 |  0.15948 | 0.3056 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | rd       | joint      | cf0    |       0.03169 |  0.01832 |  0.04497 | 0.3056 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | rd       | joint      | log_pr |      -0.15323 | -0.18905 | -0.12041 | 0.3056 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |       0.00853 | -0.01856 |  0.03465 | 0.0037 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |       0.13637 |  0.13214 |  0.14168 | 0.9452 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.02566 | -0.00066 |  0.05213 | 0.0335 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.02861 | -0.04719 | -0.00911 | 0.9493 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | cf_dev   | joint      | cf0    |       0.13387 |  0.13012 |  0.13845 | 0.9493 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.02597 |  0.00583 |  0.04268 | 0.9493 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |      -1.02803 | -1.49233 | -0.54389 | 0.1652 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -1.90311 | -2.2162  | -1.54016 | 0.5661 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |      -1.1348  | -1.57301 | -0.67743 | 0.2013 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl_neu   | joint      | H0     |      -1.26422 | -1.97609 | -0.58149 | 0.6827 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -1.87146 | -2.219   | -1.55175 | 0.6827 | 180 |           47 |
| A_third_a2e-2         | frq_unemb - dua_unemb | kl_neu   | joint      | log_pr |       0.43528 | -0.25614 |  1.11441 | 0.6827 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl       | uni_H0     | H0     |       2.04662 |  1.57099 |  2.54195 | 0.2979 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl       | uni_cf0    | cf0    |      -0.12248 | -0.75696 |  0.37485 | 0.0011 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl       | uni_log_pr | log_pr |       1.90794 |  1.49205 |  2.35025 | 0.2589 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl       | joint      | H0     |       2.00667 |  0.44218 |  3.56792 | 0.305  | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl       | joint      | cf0    |      -0.32569 | -0.81374 |  0.16301 | 0.305  | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl       | joint      | log_pr |       0.07453 | -1.43838 |  1.59487 | 0.305  | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl_park  | uni_H0     | H0     |       0.21554 |  0.17322 |  0.26401 | 0.5037 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl_park  | uni_cf0    | cf0    |       0.00831 | -0.0428  |  0.05361 | 0.0007 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl_park  | uni_log_pr | log_pr |       0.22755 |  0.18624 |  0.27148 | 0.5614 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl_park  | joint      | H0     |      -0.03592 | -0.13598 |  0.06128 | 0.5783 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl_park  | joint      | cf0    |      -0.04227 | -0.0851  |  0.00237 | 0.5783 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl_park  | joint      | log_pr |       0.26998 |  0.1781  |  0.37019 | 0.5783 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | rd       | uni_H0     | H0     |      -0.02481 | -0.04635 |  0.00306 | 0.0481 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | rd       | uni_cf0    | cf0    |      -0.02656 | -0.04648 | -0.0045  | 0.0551 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | rd       | uni_log_pr | log_pr |      -0.01155 | -0.03344 |  0.01607 | 0.0104 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | rd       | joint      | H0     |      -0.17062 | -0.22503 | -0.11925 | 0.2755 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | rd       | joint      | cf0    |      -0.04218 | -0.06199 | -0.02384 | 0.2755 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | rd       | joint      | log_pr |       0.1583  |  0.10656 |  0.21785 | 0.2755 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | cf_dev   | uni_H0     | H0     |      -0.05401 | -0.0762  | -0.02511 | 0.1026 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | cf_dev   | uni_cf0    | cf0    |      -0.12326 | -0.14108 | -0.10445 | 0.5346 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | cf_dev   | uni_log_pr | log_pr |      -0.06726 | -0.08748 | -0.04124 | 0.1592 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | cf_dev   | joint      | H0     |      -0.01328 | -0.06728 |  0.02734 | 0.6018 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | cf_dev   | joint      | cf0    |      -0.11571 | -0.13635 | -0.09642 | 0.6018 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | cf_dev   | joint      | log_pr |      -0.03157 | -0.07656 |  0.02297 | 0.6018 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl_neu   | uni_H0     | H0     |       1.00085 |  0.60419 |  1.41281 | 0.1704 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl_neu   | uni_cf0    | cf0    |       1.78458 |  1.44681 |  2.08906 | 0.5416 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl_neu   | uni_log_pr | log_pr |       1.12855 |  0.7149  |  1.52747 | 0.2166 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl_neu   | joint      | H0     |       0.9195  |  0.24798 |  1.66388 | 0.6609 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl_neu   | joint      | cf0    |       1.7151  |  1.41503 |  2.04115 | 0.6609 | 180 |           47 |
| A_third_a2e-2         | cau_unemb - frq_unemb | kl_neu   | joint      | log_pr |      -0.08414 | -0.80382 |  0.5962  | 0.6609 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.68905 | -1.1924  | -0.248   | 0.0724 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |       0.49058 |  0.06922 |  0.95136 | 0.0367 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |      -0.44977 | -0.8768  | -0.03905 | 0.0308 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl       | joint      | H0     |      -2.15746 | -3.7524  | -0.8358  | 0.1521 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl       | joint      | cf0    |       0.39062 | -0.07907 |  0.82286 | 0.1521 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl       | joint      | log_pr |       1.51333 |  0.35639 |  2.90845 | 0.1521 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.27066 | -0.33112 | -0.20998 | 0.4485 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |       0.00431 | -0.06152 |  0.08936 | 0.0001 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.2562  | -0.30835 | -0.19955 | 0.4018 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.23853 | -0.38677 | -0.09104 | 0.4547 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl_park  | joint      | cf0    |       0.03416 | -0.01777 |  0.08897 | 0.4547 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl_park  | joint      | log_pr |      -0.03735 | -0.17122 |  0.09689 | 0.4547 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.03022 | -0.04821 | -0.01193 | 0.1269 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.00612 | -0.02082 |  0.00989 | 0.0052 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.03678 | -0.05198 | -0.02063 | 0.188  | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | rd       | joint      | H0     |       0.04924 |  0.00541 |  0.09507 | 0.2204 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | rd       | joint      | cf0    |       0.00617 | -0.00871 |  0.02222 | 0.2204 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | rd       | joint      | log_pr |      -0.0846  | -0.12636 | -0.04466 | 0.2204 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.00043 | -0.03091 |  0.02482 | 0      | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.105   |  0.08125 |  0.12497 | 0.3993 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |       0.0116  | -0.01854 |  0.03874 | 0.0049 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.01284 | -0.08662 |  0.06468 | 0.4032 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.10568 |  0.08139 |  0.12754 | 0.4032 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | cf_dev   | joint      | log_pr |       0.00263 | -0.07314 |  0.07507 | 0.4032 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |      -0.39447 | -0.71102 | -0.10721 | 0.111  | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.41854 | -0.70695 | -0.14223 | 0.1249 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |      -0.35584 | -0.64439 | -0.07976 | 0.0903 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.96663 | -1.65824 | -0.38299 | 0.2436 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -0.45776 | -0.73185 | -0.20738 | 0.2436 | 180 |           47 |
| A_third_a2e-2         | frq_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.65017 |  0.23785 |  1.15107 | 0.2436 | 180 |           47 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl       | uni_H0     | H0     |       0.06533 | -0.06683 |  0.18922 | 0.0048 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |       0.02589 | -0.09328 |  0.14077 | 0.0008 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |       0.01716 | -0.12948 |  0.17361 | 0.0003 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl       | joint      | H0     |       0.20992 | -0.02652 |  0.41668 | 0.0219 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl       | joint      | cf0    |       0.20279 | -0.04022 |  0.41587 | 0.0219 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl       | joint      | log_pr |       0.02222 | -0.1606  |  0.20701 | 0.0219 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |       0.06359 | -0.04238 |  0.16165 | 0.0087 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |      -0.02685 | -0.13281 |  0.06969 | 0.0016 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |       0.04881 | -0.04473 |  0.15394 | 0.0051 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl_park  | joint      | H0     |       0.09879 | -0.096   |  0.26312 | 0.0132 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl_park  | joint      | cf0    |       0.07315 | -0.12407 |  0.24373 | 0.0132 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.03727 | -0.09197 |  0.17901 | 0.0132 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | rd       | uni_H0     | H0     |       0.03761 |  0.00521 |  0.06823 | 0.027  | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.02558 | -0.06312 |  0.00618 | 0.0125 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |       0.03572 |  0.00317 |  0.06925 | 0.0243 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | rd       | joint      | H0     |       0.03843 | -0.01943 |  0.089   | 0.0354 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | rd       | joint      | cf0    |       0.02079 | -0.03935 |  0.07411 | 0.0354 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | rd       | joint      | log_pr |       0.02644 | -0.01811 |  0.07192 | 0.0354 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.00689 | -0.03032 |  0.01591 | 0.0015 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |      -0.00141 | -0.02728 |  0.02089 | 0.0001 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.00593 | -0.03243 |  0.01988 | 0.0011 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.01814 | -0.06595 |  0.02504 | 0.0064 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | cf_dev   | joint      | cf0    |      -0.02074 | -0.06982 |  0.02409 | 0.0064 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | cf_dev   | joint      | log_pr |      -0.00838 | -0.04083 |  0.02506 | 0.0064 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |      -0.05001 | -0.08856 | -0.00533 | 0.0207 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |       0.08412 |  0.03514 |  0.13673 | 0.0586 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |      -0.02727 | -0.07446 |  0.01894 | 0.0062 | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl_neu   | joint      | H0     |       0.0298  | -0.03899 |  0.106   | 0.07   | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl_neu   | joint      | cf0    |       0.1303  |  0.05165 |  0.22607 | 0.07   | 180 |          177 |
| C_third_a2e-2         | euc_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.03688 | -0.01097 |  0.08962 | 0.07   | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl       | uni_H0     | H0     |      -0.05024 | -0.10755 |  0.00536 | 0.0105 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl       | uni_cf0    | cf0    |       0.10799 |  0.0388  |  0.17408 | 0.0487 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl       | uni_log_pr | log_pr |      -0.04757 | -0.12396 |  0.02114 | 0.0094 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl       | joint      | H0     |       0.07986 | -0.02908 |  0.18587 | 0.0616 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl       | joint      | cf0    |       0.1827  |  0.05671 |  0.29783 | 0.0616 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl       | joint      | log_pr |       0.02033 | -0.07988 |  0.10494 | 0.0616 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl_park  | uni_H0     | H0     |       0.03239 | -0.00866 |  0.06784 | 0.0103 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |      -0.01677 | -0.06299 |  0.02668 | 0.0027 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |       0.02252 | -0.04101 |  0.0741  | 0.005  | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl_park  | joint      | H0     |       0.04578 | -0.03593 |  0.12085 | 0.0129 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.0267  | -0.05583 |  0.09658 | 0.0129 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.01268 | -0.06754 |  0.07992 | 0.0129 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | rd       | uni_H0     | H0     |       0.01262 | -0.00775 |  0.03055 | 0.0052 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.00985 | -0.03121 |  0.01089 | 0.0032 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.00559 | -0.03129 |  0.01756 | 0.001  | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | rd       | joint      | H0     |       0.01775 | -0.01857 |  0.05511 | 0.0145 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | rd       | joint      | cf0    |      -0.00983 | -0.04942 |  0.03137 | 0.0145 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | rd       | joint      | log_pr |      -0.02202 | -0.05765 |  0.0084  | 0.0145 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |       0.02964 |  0.00771 |  0.05087 | 0.0321 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |      -0.03292 | -0.05586 | -0.01254 | 0.0396 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.03003 |  0.01046 |  0.05174 | 0.033  | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | cf_dev   | joint      | H0     |       0.00683 | -0.03419 |  0.04355 | 0.0457 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | cf_dev   | joint      | cf0    |      -0.01857 | -0.06241 |  0.02011 | 0.0457 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.01447 | -0.01141 |  0.04133 | 0.0457 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |      -0.09917 | -0.13931 | -0.05637 | 0.0802 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |       0.14473 |  0.09541 |  0.19804 | 0.1708 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |      -0.06789 | -0.11361 | -0.02469 | 0.0376 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl_neu   | joint      | H0     |       0.02546 | -0.04511 |  0.10445 | 0.1796 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl_neu   | joint      | cf0    |       0.18516 |  0.10071 |  0.28426 | 0.1796 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - dua_unemb | kl_neu   | joint      | log_pr |       0.03306 | -0.01595 |  0.0836  | 0.1796 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl       | uni_H0     | H0     |      -0.19332 | -0.33119 | -0.04389 | 0.0557 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl       | uni_cf0    | cf0    |       0.25416 |  0.13431 |  0.37488 | 0.0962 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl       | uni_log_pr | log_pr |      -0.03599 | -0.15507 |  0.07409 | 0.0019 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl       | joint      | H0     |      -0.0391  | -0.24787 |  0.16183 | 0.1339 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl       | joint      | cf0    |       0.3535  |  0.17835 |  0.53196 | 0.1339 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl       | joint      | log_pr |       0.20756 |  0.07651 |  0.33367 | 0.1339 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.18064 | -0.28417 | -0.08631 | 0.1079 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |       0.17849 |  0.09416 |  0.25939 | 0.1053 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.03801 | -0.12571 |  0.0418  | 0.0048 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.13968 | -0.28639 | -0.00247 | 0.1593 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.1589  |  0.05958 |  0.25268 | 0.1593 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.14223 |  0.04345 |  0.24138 | 0.1593 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | rd       | uni_H0     | H0     |       0.05779 |  0.03242 |  0.08066 | 0.0691 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.05756 | -0.08812 | -0.02958 | 0.0685 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | rd       | uni_log_pr | log_pr |       0.06305 |  0.02687 |  0.09603 | 0.0822 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | rd       | joint      | H0     |       0.02327 | -0.02085 |  0.06832 | 0.0977 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | rd       | joint      | cf0    |      -0.01398 | -0.06664 |  0.03697 | 0.0977 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | rd       | joint      | log_pr |       0.04083 | -0.00274 |  0.08556 | 0.0977 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |      -0.00322 | -0.03903 |  0.02981 | 0.0004 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |      -0.00866 | -0.03192 |  0.01748 | 0.0028 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.01989 | -0.00344 |  0.04414 | 0.015  | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.03185 | -0.08068 |  0.01419 | 0.0307 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | cf_dev   | joint      | cf0    |      -0.01547 | -0.04996 |  0.0196  | 0.0307 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.02869 |  0.00058 |  0.0559  | 0.0307 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |      -0.07623 | -0.12322 | -0.02768 | 0.0358 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |       0.1241  |  0.05833 |  0.18908 | 0.0948 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |      -0.03756 | -0.09083 |  0.01768 | 0.0087 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl_neu   | joint      | H0     |       0.03648 | -0.04927 |  0.12698 | 0.1141 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl_neu   | joint      | cf0    |       0.18991 |  0.06989 |  0.31302 | 0.1141 | 180 |          177 |
| C_third_a2e-2         | frq_unemb - dua_unemb | kl_neu   | joint      | log_pr |       0.05997 |  0.00032 |  0.12648 | 0.1141 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl       | uni_H0     | H0     |       0.14308 |  0.01144 |  0.28006 | 0.0359 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl       | uni_cf0    | cf0    |      -0.14617 | -0.26752 | -0.03425 | 0.0375 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl       | uni_log_pr | log_pr |      -0.01157 | -0.12629 |  0.11078 | 0.0002 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl       | joint      | H0     |       0.11896 | -0.07588 |  0.31337 | 0.0775 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl       | joint      | cf0    |      -0.17079 | -0.32571 | -0.02256 | 0.0775 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl       | joint      | log_pr |      -0.18723 | -0.33331 | -0.03041 | 0.0775 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl_park  | uni_H0     | H0     |       0.21303 |  0.09843 |  0.32564 | 0.097  | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl_park  | uni_cf0    | cf0    |      -0.19525 | -0.30782 | -0.09716 | 0.0815 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl_park  | uni_log_pr | log_pr |       0.06053 | -0.04782 |  0.16742 | 0.0078 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl_park  | joint      | H0     |       0.18545 |  0.00985 |  0.35462 | 0.1229 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl_park  | joint      | cf0    |      -0.13219 | -0.27138 | -0.00249 | 0.1229 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl_park  | joint      | log_pr |      -0.12954 | -0.26867 |  0.00685 | 0.1229 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | rd       | uni_H0     | H0     |      -0.04516 | -0.07497 | -0.01599 | 0.0281 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | rd       | uni_cf0    | cf0    |       0.04771 |  0.01582 |  0.08055 | 0.0313 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | rd       | uni_log_pr | log_pr |      -0.06864 | -0.10701 | -0.02557 | 0.0648 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | rd       | joint      | H0     |      -0.00552 | -0.06035 |  0.05146 | 0.0655 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | rd       | joint      | cf0    |       0.00415 | -0.05956 |  0.06648 | 0.0655 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | rd       | joint      | log_pr |      -0.06285 | -0.11825 | -0.00724 | 0.0655 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | cf_dev   | uni_H0     | H0     |       0.03286 | -0.0072  |  0.07721 | 0.0206 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | cf_dev   | uni_cf0    | cf0    |      -0.02426 | -0.06187 |  0.00728 | 0.0112 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | cf_dev   | uni_log_pr | log_pr |       0.01014 | -0.022   |  0.04358 | 0.002  | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | cf_dev   | joint      | H0     |       0.03869 | -0.02216 |  0.1033  | 0.023  | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | cf_dev   | joint      | cf0    |      -0.00311 | -0.05632 |  0.04632 | 0.023  | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | cf_dev   | joint      | log_pr |      -0.01422 | -0.05295 |  0.02374 | 0.023  | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl_neu   | uni_H0     | H0     |      -0.02293 | -0.04337 | -0.00442 | 0.0247 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl_neu   | uni_cf0    | cf0    |       0.02063 | -0.01182 |  0.05379 | 0.02   | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl_neu   | uni_log_pr | log_pr |      -0.03033 | -0.05295 | -0.00881 | 0.0432 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl_neu   | joint      | H0     |      -0.01102 | -0.04751 |  0.02811 | 0.0455 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl_neu   | joint      | cf0    |      -0.00475 | -0.06364 |  0.05801 | 0.0455 | 180 |          177 |
| C_third_a2e-2         | cau_unemb - frq_unemb | kl_neu   | joint      | log_pr |      -0.02691 | -0.05204 | -0.00298 | 0.0455 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.59582 | -1.02207 | -0.22392 | 0.0547 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |       0.45411 |  0.06635 |  0.86107 | 0.0318 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |      -0.497   | -0.87888 | -0.11279 | 0.038  | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl       | joint      | H0     |      -0.54968 | -1.23385 |  0.12063 | 0.061  | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl       | joint      | cf0    |      -0.13822 | -0.76045 |  0.48458 | 0.061  | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl       | joint      | log_pr |      -0.26483 | -0.81343 |  0.32318 | 0.061  | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.30866 | -0.38668 | -0.21311 | 0.2443 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |       0.23368 |  0.15368 |  0.31372 | 0.1401 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.13896 | -0.21006 | -0.06628 | 0.0495 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.33546 | -0.47925 | -0.17798 | 0.2506 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl_park  | joint      | cf0    |       0.01284 | -0.09612 |  0.12037 | 0.2506 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.06346 | -0.02916 |  0.15907 | 0.2506 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | rd       | uni_H0     | H0     |       0.04839 |  0.02451 |  0.0717  | 0.0527 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.04667 | -0.0736  | -0.0209  | 0.049  | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |       0.07225 |  0.03998 |  0.10085 | 0.1175 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | rd       | joint      | H0     |       0.01436 | -0.03191 |  0.05812 | 0.1193 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | rd       | joint      | cf0    |       0.00727 | -0.0382  |  0.05007 | 0.1193 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | rd       | joint      | log_pr |       0.06847 |  0.02909 |  0.10793 | 0.1193 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.01522 | -0.03214 | -0.00108 | 0.0476 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.01258 | -0.00245 |  0.02877 | 0.0325 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.00752 | -0.01871 |  0.00268 | 0.0116 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.0144  | -0.03669 |  0.00533 | 0.0488 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.00314 | -0.01472 |  0.02274 | 0.0488 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | cf_dev   | joint      | log_pr |       0.00279 | -0.00759 |  0.01414 | 0.0488 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |       0.045   | -0.02102 |  0.11422 | 0.007  | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.06416 | -0.17865 |  0.04136 | 0.0142 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |       0.06118 | -0.01461 |  0.13767 | 0.0129 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.02113 | -0.16029 |  0.12188 | 0.0173 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -0.0569  | -0.26245 |  0.15291 | 0.0173 | 180 |          177 |
| C_third_a2e-2         | frq_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.03786 | -0.04019 |  0.11144 | 0.0173 | 180 |          177 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl       | uni_H0     | H0     |       0.13233 |  0.01208 |  0.2191  | 0.1268 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |      -0.15312 | -0.20846 | -0.08035 | 0.1698 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |       0.17313 |  0.07569 |  0.27235 | 0.2171 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl       | joint      | H0     |      -0.26852 | -0.4914  | -0.09946 | 0.411  |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl       | joint      | cf0    |      -0.16844 | -0.23172 | -0.09471 | 0.411  |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl       | joint      | log_pr |       0.38403 |  0.22179 |  0.54971 | 0.411  |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.07567 | -0.12978 | -0.00832 | 0.1747 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |      -0.00661 | -0.06099 |  0.06302 | 0.0013 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.07169 | -0.12927 | -0.00325 | 0.1568 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.08806 | -0.22873 |  0.04175 | 0.2076 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | joint      | cf0    |      -0.03482 | -0.07715 |  0.00704 | 0.2076 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.00127 | -0.13694 |  0.14479 | 0.2076 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.03521 | -0.0564  | -0.01047 | 0.176  |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.00518 | -0.0336  |  0.02621 | 0.0038 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.04387 | -0.05997 | -0.02154 | 0.2732 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | rd       | joint      | H0     |       0.01376 | -0.055   |  0.07934 | 0.3036 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | rd       | joint      | cf0    |      -0.0116  | -0.0328  |  0.01784 | 0.3036 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | rd       | joint      | log_pr |      -0.05844 | -0.12547 |  0.00882 | 0.3036 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.03048 | -0.06507 |  0.00924 | 0.0825 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.011   | -0.0159  |  0.03958 | 0.0108 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.02634 | -0.06307 |  0.01197 | 0.0616 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.03554 | -0.12057 |  0.05702 | 0.0832 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.00061 | -0.02762 |  0.02429 | 0.0832 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | cf_dev   | joint      | log_pr |       0.00583 | -0.07526 |  0.08713 | 0.0832 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |       0.18129 |  0.00081 |  0.27849 | 0.2197 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.21168 | -0.29114 | -0.12946 | 0.2995 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |       0.20604 |  0.0374  |  0.32229 | 0.2838 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.20123 | -0.40089 | -0.09477 | 0.5355 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -0.21194 | -0.30261 | -0.1221  | 0.5355 |  60 |           16 |
| gemma4b_A_third_a5e-3 | euc_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.34815 |  0.22599 |  0.5109  | 0.5355 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl       | uni_H0     | H0     |       0.22237 |  0.01357 |  0.51765 | 0.0708 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl       | uni_cf0    | cf0    |      -0.30891 | -0.44178 | -0.16282 | 0.1366 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl       | uni_log_pr | log_pr |       0.3257  |  0.11165 |  0.63044 | 0.1518 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl       | joint      | H0     |      -0.69061 | -1.17525 | -0.26283 | 0.3533 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl       | joint      | cf0    |      -0.3683  | -0.55447 | -0.18308 | 0.3533 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl       | joint      | log_pr |       0.8802  |  0.45656 |  1.3381  | 0.3533 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.02412 | -0.07088 |  0.03374 | 0.0245 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |      -0.00051 | -0.0454  |  0.04511 | 0      |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.01508 | -0.05943 |  0.04138 | 0.0096 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.06854 | -0.17807 |  0.02617 | 0.0419 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | joint      | cf0    |      -0.01445 | -0.05985 |  0.03046 | 0.0419 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.04406 | -0.05701 |  0.14961 | 0.0419 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | rd       | uni_H0     | H0     |      -0.01073 | -0.03353 |  0.02339 | 0.0199 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | rd       | uni_cf0    | cf0    |       0.00658 | -0.01518 |  0.03362 | 0.0075 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.00909 | -0.03379 |  0.02182 | 0.0143 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | rd       | joint      | H0     |      -0.01083 | -0.05165 |  0.03026 | 0.0218 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | rd       | joint      | cf0    |       0.00332 | -0.02004 |  0.02919 | 0.0218 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | rd       | joint      | log_pr |       0.00131 | -0.04264 |  0.04405 | 0.0218 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |      -0.00836 | -0.04307 |  0.03249 | 0.0053 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |       0.02002 | -0.00427 |  0.04837 | 0.0302 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.00294 | -0.03529 |  0.04586 | 0.0007 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.04779 | -0.14553 |  0.04971 | 0.0614 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | joint      | cf0    |       0.01362 | -0.00857 |  0.04241 | 0.0614 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.04859 | -0.04472 |  0.13947 | 0.0614 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |       0.21046 |  0.00978 |  0.4603  | 0.0797 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -0.32189 | -0.44273 | -0.20552 | 0.1864 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |       0.29493 |  0.1154  |  0.56504 | 0.1565 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | joint      | H0     |      -0.61103 | -1.02159 | -0.26564 | 0.3976 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -0.37487 | -0.54216 | -0.19363 | 0.3976 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - dua_unemb | kl_neu   | joint      | log_pr |       0.77642 |  0.40895 |  1.17112 | 0.3976 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl       | uni_H0     | H0     |       0.34055 |  0.13859 |  0.61916 | 0.1446 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl       | uni_cf0    | cf0    |      -0.32587 | -0.51278 | -0.12625 | 0.1324 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl       | uni_log_pr | log_pr |       0.36032 |  0.18539 |  0.62859 | 0.1619 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl       | joint      | H0     |      -0.16199 | -1.02247 |  0.49769 | 0.2537 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl       | joint      | cf0    |      -0.29419 | -0.41597 | -0.119   | 0.2537 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl       | joint      | log_pr |       0.45174 | -0.17146 |  1.23082 | 0.2537 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.07536 | -0.11669 | -0.0161  | 0.1528 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |       0.05009 |  0.01208 |  0.09412 | 0.0675 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.08058 | -0.11969 | -0.02129 | 0.1747 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | joint      | H0     |       0.01845 | -0.13917 |  0.16863 | 0.2106 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.03933 | -0.01941 |  0.09994 | 0.2106 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl_park  | joint      | log_pr |      -0.08992 | -0.2279  |  0.07072 | 0.2106 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | rd       | uni_H0     | H0     |       0.02389 |  0.00115 |  0.03705 | 0.0794 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.00905 | -0.02554 |  0.01241 | 0.0114 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | rd       | uni_log_pr | log_pr |       0.00221 | -0.02303 |  0.01867 | 0.0007 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | rd       | joint      | H0     |       0.12719 |  0.07958 |  0.17835 | 0.3744 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | rd       | joint      | cf0    |       0.01151 | -0.00795 |  0.0359  | 0.3744 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | rd       | joint      | log_pr |      -0.11039 | -0.15881 | -0.07394 | 0.3744 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |       0.00424 | -0.04258 |  0.02688 | 0.001  |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |      -0.00451 | -0.02456 |  0.0163  | 0.0012 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.01672 | -0.01682 |  0.03746 | 0.0162 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.06867 | -0.18294 |  0.00156 | 0.0604 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | joint      | cf0    |      -0.0125  | -0.0314  |  0.01903 | 0.0604 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.07635 |  0.01269 |  0.16569 | 0.0604 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |       0.40651 |  0.16885 |  0.73267 | 0.1924 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -0.60245 | -0.77991 | -0.41653 | 0.4226 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |       0.36698 |  0.1648  |  0.68664 | 0.1568 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | joint      | H0     |      -0.06478 | -0.7721  |  0.52774 | 0.5018 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -0.56376 | -0.68252 | -0.40904 | 0.5018 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_unemb - dua_unemb | kl_neu   | joint      | log_pr |       0.32057 | -0.23746 |  0.96483 | 0.5018 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl       | uni_H0     | H0     |      -0.11818 | -0.3317  |  0.06407 | 0.0334 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl       | uni_cf0    | cf0    |       0.01696 | -0.18253 |  0.23551 | 0.0007 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl       | uni_log_pr | log_pr |      -0.03463 | -0.20783 |  0.13379 | 0.0029 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl       | joint      | H0     |      -0.52863 | -1.00658 |  0.11123 | 0.1108 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl       | joint      | cf0    |      -0.07411 | -0.24823 |  0.12895 | 0.1108 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl       | joint      | log_pr |       0.42846 | -0.14062 |  0.8829  | 0.1108 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | uni_H0     | H0     |       0.05124 | -0.03323 |  0.12138 | 0.0481 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | uni_cf0    | cf0    |      -0.0506  | -0.11079 | -0.00339 | 0.0469 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | uni_log_pr | log_pr |       0.06551 | -0.01204 |  0.12939 | 0.0786 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | joint      | H0     |      -0.08699 | -0.27433 |  0.09289 | 0.1289 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | joint      | cf0    |      -0.05378 | -0.14    |  0.03149 | 0.1289 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl_park  | joint      | log_pr |       0.13398 | -0.03662 |  0.30423 | 0.1289 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | rd       | uni_H0     | H0     |      -0.03462 | -0.06825 |  0.01549 | 0.0868 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | rd       | uni_cf0    | cf0    |       0.01563 | -0.02028 |  0.04852 | 0.0177 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | rd       | uni_log_pr | log_pr |      -0.0113  | -0.05134 |  0.0417  | 0.0092 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | rd       | joint      | H0     |      -0.13803 | -0.21333 | -0.07325 | 0.2455 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | rd       | joint      | cf0    |      -0.00818 | -0.04045 |  0.0199  | 0.2455 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | rd       | joint      | log_pr |       0.1117  |  0.05345 |  0.18286 | 0.2455 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | uni_H0     | H0     |      -0.0126  | -0.05778 |  0.05462 | 0.0082 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | uni_cf0    | cf0    |       0.02453 | -0.01061 |  0.05683 | 0.0311 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | uni_log_pr | log_pr |      -0.01378 | -0.05804 |  0.0477  | 0.0098 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | joint      | H0     |       0.02088 | -0.05224 |  0.13326 | 0.0393 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | joint      | cf0    |       0.02612 | -0.01931 |  0.05791 | 0.0393 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | cf_dev   | joint      | log_pr |      -0.02776 | -0.11142 |  0.04619 | 0.0393 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | uni_H0     | H0     |      -0.19605 | -0.4362  | -0.0241  | 0.0917 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | uni_cf0    | cf0    |       0.28056 |  0.07493 |  0.47701 | 0.1878 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | uni_log_pr | log_pr |      -0.07205 | -0.28118 |  0.08163 | 0.0124 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | joint      | H0     |      -0.54625 | -1.04185 |  0.02342 | 0.3036 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | joint      | cf0    |       0.18889 | -0.00967 |  0.41451 | 0.3036 |  60 |           16 |
| gemma4b_A_third_a5e-3 | cau_unemb - frq_unemb | kl_neu   | joint      | log_pr |       0.45585 | -0.08268 |  0.8929  | 0.3036 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.53811 | -1.54543 |  0.37498 | 0.0196 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |       1.01899 | -0.08143 |  2.02565 | 0.0702 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |      -0.08719 | -0.95492 |  1.04179 | 0.0005 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl       | joint      | H0     |      -1.84912 | -6.65754 |  2.29116 | 0.1082 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl       | joint      | cf0    |       0.74133 | -0.37203 |  1.82417 | 0.1082 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl       | joint      | log_pr |       1.71875 | -2.28851 |  5.95343 | 0.1082 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.26501 | -0.33691 | -0.21161 | 0.7498 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |       0.11386 |  0.03091 |  0.20483 | 0.1384 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.25489 | -0.31821 | -0.18907 | 0.6936 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.15125 | -0.30455 | -0.03178 | 0.7818 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | joint      | cf0    |       0.04452 |  0.00903 |  0.08845 | 0.7818 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl_park  | joint      | log_pr |      -0.11017 | -0.23716 |  0.0256  | 0.7818 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.01327 | -0.03957 |  0.01833 | 0.0229 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.02365 | -0.05269 |  0.00778 | 0.0729 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.02126 | -0.04372 |  0.00627 | 0.0589 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | rd       | joint      | H0     |       0.00915 | -0.04139 |  0.06407 | 0.1635 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | rd       | joint      | cf0    |      -0.02712 | -0.05169 |  0.00615 | 0.1635 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | rd       | joint      | log_pr |      -0.03456 | -0.09626 |  0.02015 | 0.1635 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.0637  | -0.11059 | -0.018   | 0.1786 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.14428 |  0.13146 |  0.16245 | 0.9164 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.04519 | -0.09753 |  0.00709 | 0.0899 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.00669 | -0.04213 |  0.01921 | 0.9321 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.13966 |  0.12882 |  0.15172 | 0.9321 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | cf_dev   | joint      | log_pr |      -0.01318 | -0.04438 |  0.01733 | 0.9321 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |       0.32233 | -0.40158 |  1.08559 | 0.0274 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.81741 | -1.54979 | -0.09273 | 0.1763 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |       0.33892 | -0.14278 |  1.05352 | 0.0303 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.64939 | -2.97375 |  1.49769 | 0.2038 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -0.88584 | -1.62757 | -0.22992 | 0.2038 |  60 |           16 |
| gemma4b_A_third_a5e-3 | frq_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.75999 | -1.30863 |  2.80905 | 0.2038 |  60 |           16 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl       | uni_H0     | H0     |       0.03579 | -0.2804  |  0.41102 | 0.0004 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |      -0.27916 | -0.55894 |  0.05355 | 0.0215 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |       0.06785 | -0.18784 |  0.38141 | 0.0013 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl       | joint      | H0     |      -0.47523 | -1.4947  |  0.72419 | 0.0314 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl       | joint      | cf0    |      -0.33323 | -0.62614 |  0.01779 | 0.0314 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl       | joint      | log_pr |       0.55687 | -0.47347 |  1.52969 | 0.0314 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.24058 | -0.29219 | -0.18937 | 0.4747 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |      -0.11281 | -0.18057 | -0.05272 | 0.1044 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.25115 | -0.29997 | -0.20511 | 0.5173 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.10468 | -0.2477  |  0.04406 | 0.5815 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl_park  | joint      | cf0    |      -0.09096 | -0.13336 | -0.04668 | 0.5815 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl_park  | joint      | log_pr |      -0.14118 | -0.26459 | -0.01607 | 0.5815 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.05014 | -0.06827 | -0.03367 | 0.359  | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.02996 | -0.04841 | -0.01288 | 0.1282 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.04969 | -0.0683  | -0.03216 | 0.3525 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | rd       | joint      | H0     |      -0.04961 | -0.08323 | -0.01378 | 0.4723 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | rd       | joint      | cf0    |      -0.02824 | -0.04187 | -0.01293 | 0.4723 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | rd       | joint      | log_pr |       0.00052 | -0.03116 |  0.03059 | 0.4723 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.00092 | -0.01704 |  0.01805 | 0      | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.02819 |  0.00803 |  0.04477 | 0.0453 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.00156 | -0.01698 |  0.01756 | 0.0001 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | cf_dev   | joint      | H0     |       0.02688 | -0.02793 |  0.0836  | 0.0514 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.03116 |  0.0103  |  0.04668 | 0.0514 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | cf_dev   | joint      | log_pr |      -0.0308  | -0.08346 |  0.02755 | 0.0514 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |       0.08763 | -0.23786 |  0.43184 | 0.0035 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.67123 | -0.86995 | -0.43402 | 0.2081 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |       0.09181 | -0.2091  |  0.37251 | 0.0039 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.51518 | -1.20868 |  0.33159 | 0.2365 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -0.73835 | -0.95281 | -0.46411 | 0.2365 | 180 |           46 |
| A_ing_a5e-3           | euc_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.67018 | -0.01848 |  1.31165 | 0.2365 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl       | uni_H0     | H0     |       0.25368 |  0.02416 |  0.48986 | 0.064  | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl       | uni_cf0    | cf0    |      -0.43359 | -0.54024 | -0.32777 | 0.187  | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl       | uni_log_pr | log_pr |       0.3558  |  0.14179 |  0.58794 | 0.1259 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl       | joint      | H0     |      -1.09878 | -1.3459  | -0.81573 | 0.4907 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl       | joint      | cf0    |      -0.58095 | -0.68173 | -0.47467 | 0.4907 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl       | joint      | log_pr |       1.46221 |  1.17346 |  1.74449 | 0.4907 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.0929  | -0.13391 | -0.05293 | 0.2329 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |      -0.04918 | -0.08287 | -0.01997 | 0.0653 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.09013 | -0.12672 | -0.05454 | 0.2193 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.10364 | -0.20516 |  0.00343 | 0.2902 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl_park  | joint      | cf0    |      -0.04713 | -0.07178 | -0.02115 | 0.2902 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.01325 | -0.07384 |  0.09711 | 0.2902 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | rd       | uni_H0     | H0     |      -0.03602 | -0.0539  | -0.01697 | 0.1526 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.00975 | -0.02709 |  0.00765 | 0.0112 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.03444 | -0.05287 | -0.01651 | 0.1395 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | rd       | joint      | H0     |      -0.03731 | -0.07961 |  0.01214 | 0.161  | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | rd       | joint      | cf0    |      -0.00862 | -0.02481 |  0.00846 | 0.161  | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | rd       | joint      | log_pr |       0.00171 | -0.04321 |  0.04337 | 0.161  | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |      -0.00587 | -0.01691 |  0.00595 | 0.0063 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |       0.01072 | -0.00045 |  0.02303 | 0.021  | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |      -0.00227 | -0.01362 |  0.00867 | 0.0009 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.0253  | -0.06538 |  0.0145  | 0.0365 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | cf_dev   | joint      | cf0    |       0.00903 | -0.00211 |  0.02135 | 0.0365 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.02034 | -0.01809 |  0.06157 | 0.0365 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |       0.23982 |  0.03144 |  0.46851 | 0.0612 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -0.4693  | -0.56981 | -0.36916 | 0.2343 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |       0.32154 |  0.10578 |  0.54816 | 0.11   | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl_neu   | joint      | H0     |      -0.9572  | -1.23759 | -0.66267 | 0.4996 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -0.6007  | -0.69879 | -0.49437 | 0.4996 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - dua_unemb | kl_neu   | joint      | log_pr |       1.2975  |  1.01308 |  1.58037 | 0.4996 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl       | uni_H0     | H0     |       0.40515 |  0.21868 |  0.61004 | 0.1628 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl       | uni_cf0    | cf0    |      -0.25201 | -0.35771 | -0.12957 | 0.063  | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl       | uni_log_pr | log_pr |       0.50759 |  0.33227 |  0.70508 | 0.2555 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl       | joint      | H0     |      -0.89301 | -1.18012 | -0.57849 | 0.4443 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl       | joint      | cf0    |      -0.39851 | -0.51543 | -0.27774 | 0.4443 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl       | joint      | log_pr |       1.39739 |  1.09888 |  1.69964 | 0.4443 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.02279 | -0.04377 |  0.00147 | 0.021  | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |       0.0577  |  0.03458 |  0.08549 | 0.1346 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.01015 | -0.02938 |  0.01294 | 0.0042 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.07435 | -0.1365  | -0.00411 | 0.1719 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.05363 |  0.03301 |  0.08253 | 0.1719 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.05283 | -0.0053  |  0.10797 | 0.1719 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | rd       | uni_H0     | H0     |      -0.03212 | -0.0463  | -0.01887 | 0.1416 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | rd       | uni_cf0    | cf0    |       0.00993 | -0.00406 |  0.02417 | 0.0135 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.03629 | -0.0501  | -0.02322 | 0.1807 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | rd       | joint      | H0     |       0.02906 | -0.00713 |  0.06827 | 0.2231 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | rd       | joint      | cf0    |       0.0173  |  0.00566 |  0.03008 | 0.2231 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | rd       | joint      | log_pr |      -0.0658  | -0.10493 | -0.02926 | 0.2231 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |       0.01138 | -0.00585 |  0.02878 | 0.019  | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |      -0.06227 | -0.07214 | -0.05206 | 0.5678 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.00825 | -0.01095 |  0.02465 | 0.01   | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.01602 | -0.03554 |  0.00602 | 0.6111 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | cf_dev   | joint      | cf0    |      -0.06575 | -0.07685 | -0.05318 | 0.6111 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | cf_dev   | joint      | log_pr |       0.03171 |  0.01146 |  0.05094 | 0.6111 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |       0.28744 |  0.11534 |  0.48334 | 0.0951 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -0.47025 | -0.56618 | -0.37345 | 0.2546 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |       0.34506 |  0.17248 |  0.53614 | 0.1371 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl_neu   | joint      | H0     |      -0.72935 | -0.97079 | -0.47506 | 0.5145 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -0.58526 | -0.67217 | -0.48824 | 0.5145 | 180 |           46 |
| A_ing_a5e-3           | frq_unemb - dua_unemb | kl_neu   | joint      | log_pr |       1.10502 |  0.83498 |  1.37514 | 0.5145 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl       | uni_H0     | H0     |      -0.15148 | -0.20021 | -0.0998  | 0.1997 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl       | uni_cf0    | cf0    |      -0.18158 | -0.22597 | -0.14126 | 0.287  | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl       | uni_log_pr | log_pr |      -0.1518  | -0.20632 | -0.09455 | 0.2006 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl       | joint      | H0     |      -0.20576 | -0.3116  | -0.09939 | 0.4741 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl       | joint      | cf0    |      -0.18243 | -0.22894 | -0.14462 | 0.4741 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl       | joint      | log_pr |       0.06482 | -0.04914 |  0.17931 | 0.4741 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl_park  | uni_H0     | H0     |      -0.07011 | -0.10467 | -0.03329 | 0.1006 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl_park  | uni_cf0    | cf0    |      -0.10688 | -0.14289 | -0.07744 | 0.2338 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl_park  | uni_log_pr | log_pr |      -0.07998 | -0.12044 | -0.04422 | 0.1309 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl_park  | joint      | H0     |      -0.02929 | -0.12121 |  0.07468 | 0.3272 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl_park  | joint      | cf0    |      -0.10076 | -0.13783 | -0.07071 | 0.3272 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl_park  | joint      | log_pr |      -0.03958 | -0.13688 |  0.04977 | 0.3272 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | rd       | uni_H0     | H0     |      -0.0039  | -0.02268 |  0.01462 | 0.0024 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | rd       | uni_cf0    | cf0    |      -0.01968 | -0.03399 | -0.00501 | 0.0598 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | rd       | uni_log_pr | log_pr |       0.00184 | -0.01701 |  0.02101 | 0.0005 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | rd       | joint      | H0     |      -0.06638 | -0.09882 | -0.03064 | 0.138  | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | rd       | joint      | cf0    |      -0.02592 | -0.04015 | -0.01019 | 0.138  | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | rd       | joint      | log_pr |       0.06751 |  0.02323 |  0.10614 | 0.138  | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | cf_dev   | uni_H0     | H0     |      -0.01725 | -0.03498 |  0.00097 | 0.0263 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | cf_dev   | uni_cf0    | cf0    |       0.07299 |  0.06338 |  0.08374 | 0.4715 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | cf_dev   | uni_log_pr | log_pr |      -0.01051 | -0.02622 |  0.00627 | 0.0098 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | cf_dev   | joint      | H0     |      -0.00928 | -0.04735 |  0.02636 | 0.5078 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | cf_dev   | joint      | cf0    |       0.07478 |  0.06389 |  0.08571 | 0.5078 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | cf_dev   | joint      | log_pr |      -0.01137 | -0.04683 |  0.02524 | 0.5078 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl_neu   | uni_H0     | H0     |      -0.04761 | -0.09566 | -0.00035 | 0.0385 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl_neu   | uni_cf0    | cf0    |       0.00095 | -0.05434 |  0.04534 | 0      | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl_neu   | uni_log_pr | log_pr |      -0.02352 | -0.07381 |  0.02308 | 0.0094 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl_neu   | joint      | H0     |      -0.22785 | -0.32845 | -0.12949 | 0.1071 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl_neu   | joint      | cf0    |      -0.01544 | -0.06739 |  0.03046 | 0.1071 | 180 |           46 |
| A_ing_a5e-3           | cau_unemb - frq_unemb | kl_neu   | joint      | log_pr |       0.19247 |  0.10437 |  0.29011 | 0.1071 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl       | uni_H0     | H0     |      -0.30388 | -0.78164 |  0.17561 | 0.0154 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |      -0.0179  | -0.41621 |  0.36548 | 0.0001 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |      -0.05083 | -0.53178 |  0.38613 | 0.0004 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl       | joint      | H0     |      -2.32615 | -3.61046 | -1.16665 | 0.0999 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl       | joint      | cf0    |      -0.21029 | -0.59405 |  0.20994 | 0.0999 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl       | joint      | log_pr |       2.16104 |  1.06556 |  3.44727 | 0.0999 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.24251 | -0.31019 | -0.178   | 0.4334 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |      -0.07826 | -0.1442  | -0.00239 | 0.0451 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.23125 | -0.30224 | -0.16866 | 0.3941 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.26644 | -0.41344 | -0.09968 | 0.4697 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl_park  | joint      | cf0    |      -0.07224 | -0.1252  | -0.013   | 0.4697 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.02826 | -0.12003 |  0.16858 | 0.4697 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.03574 | -0.05402 | -0.0182  | 0.2144 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.03209 | -0.04988 | -0.01378 | 0.1728 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.03471 | -0.05549 | -0.01676 | 0.2022 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | rd       | joint      | H0     |      -0.04975 | -0.07689 | -0.01673 | 0.3786 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | rd       | joint      | cf0    |      -0.03236 | -0.04614 | -0.01697 | 0.3786 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | rd       | joint      | log_pr |       0.01615 | -0.01381 |  0.0444  | 0.3786 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.01059 | -0.03657 |  0.01258 | 0.0051 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |       0.06531 |  0.04257 |  0.08253 | 0.1921 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |       0.00266 | -0.02138 |  0.02562 | 0.0003 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.06815 | -0.1339  | -0.00553 | 0.2168 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | cf_dev   | joint      | cf0    |       0.06023 |  0.03464 |  0.07905 | 0.2168 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | cf_dev   | joint      | log_pr |       0.05897 | -0.00071 |  0.11998 | 0.2168 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |      -0.15179 | -0.51735 |  0.243   | 0.0077 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.80096 | -1.1259  | -0.48747 | 0.2146 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |      -0.08129 | -0.43569 |  0.24663 | 0.0022 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -1.2934  | -2.03463 | -0.48433 | 0.2766 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -0.91419 | -1.23034 | -0.58869 | 0.2766 | 180 |           46 |
| A_ing_a5e-3           | frq_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       1.25057 |  0.58735 |  1.92543 | 0.2766 | 180 |           46 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl       | uni_H0     | H0     |       0.2903  | -0.10785 |  0.66311 | 0.0291 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |      -1.07319 | -1.3397  | -0.84382 | 0.3975 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |       0.12686 | -0.27809 |  0.45926 | 0.0056 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl       | joint      | H0     |      -0.73092 | -3.26692 |  0.34044 | 0.416  |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl       | joint      | cf0    |      -1.23283 | -1.86616 | -0.87662 | 0.416  |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl       | joint      | log_pr |       0.74332 | -0.29589 |  3.35535 | 0.416  |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.22558 | -0.32094 | -0.13683 | 0.5604 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |      -0.08789 | -0.1923  | -0.04035 | 0.0851 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.23995 | -0.34617 | -0.16376 | 0.634  |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.28176 | -0.52224 | -0.07478 | 0.8228 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl_park  | joint      | cf0    |      -0.16306 | -0.23786 | -0.10072 | 0.8228 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.01326 | -0.14148 |  0.22772 | 0.8228 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.0485  | -0.08236 | -0.01974 | 0.4095 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.00373 | -0.03067 |  0.01631 | 0.0024 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.04691 | -0.08641 | -0.02162 | 0.3831 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | rd       | joint      | H0     |      -0.07058 | -0.17736 |  0.0264  | 0.4675 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | rd       | joint      | cf0    |      -0.02186 | -0.05152 |  0.00553 | 0.4675 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | rd       | joint      | log_pr |       0.01747 | -0.05825 |  0.11955 | 0.4675 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |      -0.00118 | -0.0273  |  0.0277  | 0.0002 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |      -0.02743 | -0.04249 | -0.01117 | 0.1083 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |      -0.00515 | -0.02891 |  0.02025 | 0.0038 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.02878 | -0.08946 |  0.04672 | 0.1251 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | cf_dev   | joint      | cf0    |      -0.03418 | -0.05002 | -0.01444 | 0.1251 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | cf_dev   | joint      | log_pr |       0.01984 | -0.05455 |  0.071   | 0.1251 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |       0.37713 |  0.0066  |  0.72024 | 0.0553 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -0.98167 | -1.22545 | -0.74404 | 0.3746 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |       0.22159 | -0.17092 |  0.54128 | 0.0191 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.50335 | -3.01407 |  0.70623 | 0.3951 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -1.08551 | -1.6912  | -0.737   | 0.3951 |  60 |           16 |
| gpt2_A_ing_a5e-3      | euc_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.63432 | -0.4477  |  3.21207 | 0.3951 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl       | uni_H0     | H0     |       0.81648 |  0.50229 |  1.17114 | 0.3922 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl       | uni_cf0    | cf0    |      -0.52974 | -0.70112 | -0.20373 | 0.1651 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl       | uni_log_pr | log_pr |       0.77366 |  0.48629 |  1.07301 | 0.3522 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl       | joint      | H0     |      -0.1205  | -1.74166 |  0.98316 | 0.4952 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl       | joint      | cf0    |      -0.51932 | -0.93998 | -0.22409 | 0.4952 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl       | joint      | log_pr |       0.85953 | -0.11819 |  2.635   | 0.4952 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.07353 | -0.14567 | -0.01364 | 0.2698 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |      -0.00175 | -0.04581 |  0.01851 | 0.0002 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |      -0.06306 | -0.13538 | -0.0125  | 0.1984 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.17939 | -0.38586 | -0.00393 | 0.344  |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl_park  | joint      | cf0    |      -0.04499 | -0.12845 |  0.0074  | 0.344  |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.10108 | -0.02121 |  0.29729 | 0.344  |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | rd       | uni_H0     | H0     |      -0.03549 | -0.0612  | -0.0104  | 0.2595 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | rd       | uni_cf0    | cf0    |      -0.00884 | -0.0247  | -0.00157 | 0.0161 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.03356 | -0.05987 | -0.01238 | 0.2321 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | rd       | joint      | H0     |      -0.07465 | -0.12891 | -0.01098 | 0.3582 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | rd       | joint      | cf0    |      -0.02722 | -0.05107 | -0.00986 | 0.3582 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | rd       | joint      | log_pr |       0.03432 | -0.01052 |  0.08462 | 0.3582 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |       0.02558 |  0.00448 |  0.04525 | 0.0929 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |       0.04579 |  0.03554 |  0.06433 | 0.2975 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |       0.03442 |  0.01694 |  0.04902 | 0.1681 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | cf_dev   | joint      | H0     |       0.04751 |  0.00085 |  0.10198 | 0.518  |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | cf_dev   | joint      | cf0    |       0.05824 |  0.04332 |  0.08407 | 0.518  |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | cf_dev   | joint      | log_pr |      -0.00674 | -0.06099 |  0.0406  | 0.518  |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |       0.76609 |  0.45844 |  1.10255 | 0.371  |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -0.52579 | -0.70656 | -0.25035 | 0.1747 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |       0.72108 |  0.43572 |  0.99028 | 0.3287 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl_neu   | joint      | H0     |      -0.13517 | -1.72248 |  0.98744 | 0.4817 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -0.52125 | -0.92546 | -0.23304 | 0.4817 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - dua_unemb | kl_neu   | joint      | log_pr |       0.82046 | -0.17408 |  2.53649 | 0.4817 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl       | uni_H0     | H0     |       0.96908 |  0.66393 |  1.31281 | 0.4706 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl       | uni_cf0    | cf0    |      -0.39887 | -0.58415 | -0.04053 | 0.0797 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl       | uni_log_pr | log_pr |       0.94139 |  0.63596 |  1.22626 | 0.4441 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl       | joint      | H0     |       0.19232 | -1.65118 |  1.45621 | 0.508  |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl       | joint      | cf0    |      -0.30984 | -0.77623 |  0.00876 | 0.508  |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl       | joint      | log_pr |       0.74757 | -0.35409 |  2.70385 | 0.508  |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl_park  | uni_H0     | H0     |      -0.00038 | -0.05259 |  0.05232 | 0      |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl_park  | uni_cf0    | cf0    |       0.04813 |  0.02691 |  0.07165 | 0.1631 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl_park  | uni_log_pr | log_pr |       0.01468 | -0.04435 |  0.06369 | 0.0152 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl_park  | joint      | H0     |      -0.03429 | -0.24485 |  0.12672 | 0.1911 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl_park  | joint      | cf0    |       0.04132 | -0.01749 |  0.09355 | 0.1911 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl_park  | joint      | log_pr |       0.04855 | -0.08341 |  0.26504 | 0.1911 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | rd       | uni_H0     | H0     |      -0.02522 | -0.05558 | -0.00131 | 0.1645 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | rd       | uni_cf0    | cf0    |       0.00552 | -0.01452 |  0.01927 | 0.0079 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | rd       | uni_log_pr | log_pr |      -0.02133 | -0.05246 |  0.00039 | 0.1176 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | rd       | joint      | H0     |      -0.04942 | -0.13344 |  0.03226 | 0.1795 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | rd       | joint      | cf0    |      -0.00657 | -0.03465 |  0.01794 | 0.1795 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | rd       | joint      | log_pr |       0.02419 | -0.038   |  0.10552 | 0.1795 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | cf_dev   | uni_H0     | H0     |      -0.01499 | -0.02984 | -0.00163 | 0.1606 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | cf_dev   | uni_cf0    | cf0    |       0.01056 | -0.005   |  0.0194  | 0.0796 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | cf_dev   | uni_log_pr | log_pr |      -0.01269 | -0.02698 | -0.00028 | 0.115  |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | cf_dev   | joint      | H0     |      -0.01121 | -0.05345 |  0.02531 | 0.1936 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | cf_dev   | joint      | cf0    |       0.00744 | -0.01287 |  0.01806 | 0.1936 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | cf_dev   | joint      | log_pr |      -0.00192 | -0.03428 |  0.04252 | 0.1936 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl_neu   | uni_H0     | H0     |       0.90559 |  0.61053 |  1.23556 | 0.4562 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl_neu   | uni_cf0    | cf0    |      -0.58699 | -0.75919 | -0.28705 | 0.1917 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl_neu   | uni_log_pr | log_pr |       0.83632 |  0.56456 |  1.10025 | 0.3891 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl_neu   | joint      | H0     |       0.08965 | -1.43904 |  1.16745 | 0.5553 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl_neu   | joint      | cf0    |      -0.52662 | -0.91412 | -0.2374  | 0.5553 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_unemb - dua_unemb | kl_neu   | joint      | log_pr |       0.72691 | -0.2289  |  2.34158 | 0.5553 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl       | uni_H0     | H0     |      -0.15259 | -0.22871 | -0.0606  | 0.2782 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl       | uni_cf0    | cf0    |      -0.13087 | -0.21574 | -0.09164 | 0.2047 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl       | uni_log_pr | log_pr |      -0.16773 | -0.21595 | -0.09479 | 0.3362 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl       | joint      | H0     |      -0.31282 | -0.5729  | -0.07272 | 0.6736 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl       | joint      | cf0    |      -0.20948 | -0.32123 | -0.13908 | 0.6736 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl       | joint      | log_pr |       0.11197 | -0.09956 |  0.31382 | 0.6736 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl_park  | uni_H0     | H0     |      -0.07315 | -0.11526 | -0.02687 | 0.2254 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl_park  | uni_cf0    | cf0    |      -0.04988 | -0.09958 | -0.02268 | 0.1048 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl_park  | uni_log_pr | log_pr |      -0.07774 | -0.11176 | -0.03832 | 0.2546 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl_park  | joint      | H0     |      -0.14509 | -0.26974 |  0.02764 | 0.4563 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl_park  | joint      | cf0    |      -0.0863  | -0.15701 | -0.03588 | 0.4563 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl_park  | joint      | log_pr |       0.05253 | -0.09494 |  0.15988 | 0.4563 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | rd       | uni_H0     | H0     |      -0.01027 | -0.0272  |  0.01232 | 0.0366 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | rd       | uni_cf0    | cf0    |      -0.01436 | -0.03039 | -0.00086 | 0.0716 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | rd       | uni_log_pr | log_pr |      -0.01223 | -0.02432 |  0.00854 | 0.0519 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | rd       | joint      | H0     |      -0.02522 | -0.07091 |  0.01619 | 0.1498 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | rd       | joint      | cf0    |      -0.02065 | -0.03711 | -0.00346 | 0.1498 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | rd       | joint      | log_pr |       0.01013 | -0.02798 |  0.04603 | 0.1498 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | cf_dev   | uni_H0     | H0     |       0.04058 |  0.01624 |  0.05977 | 0.2148 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | cf_dev   | uni_cf0    | cf0    |       0.03524 |  0.02128 |  0.06468 | 0.162  |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | cf_dev   | uni_log_pr | log_pr |       0.04711 |  0.02999 |  0.06359 | 0.2895 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | cf_dev   | joint      | H0     |       0.05872 |  0.02433 |  0.09946 | 0.5147 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | cf_dev   | joint      | cf0    |       0.0508  |  0.03792 |  0.08393 | 0.5147 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | cf_dev   | joint      | log_pr |      -0.00482 | -0.04509 |  0.02656 | 0.5147 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl_neu   | uni_H0     | H0     |      -0.13949 | -0.19486 | -0.09375 | 0.4711 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl_neu   | uni_cf0    | cf0    |       0.0612  | -0.00864 |  0.0914  | 0.0907 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl_neu   | uni_log_pr | log_pr |      -0.11524 | -0.16499 | -0.06585 | 0.3215 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl_neu   | joint      | H0     |      -0.22482 | -0.40903 | -0.10171 | 0.5062 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl_neu   | joint      | cf0    |       0.00536 | -0.08595 |  0.04689 | 0.5062 |  60 |           16 |
| gpt2_A_ing_a5e-3      | cau_unemb - frq_unemb | kl_neu   | joint      | log_pr |       0.09355 | -0.01577 |  0.25756 | 0.5062 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl       | uni_H0     | H0     |       0.89537 |  0.39031 |  1.34285 | 0.2175 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl       | uni_cf0    | cf0    |      -1.17071 | -1.45689 | -0.70851 | 0.3719 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl       | uni_log_pr | log_pr |       0.72216 |  0.19626 |  1.09776 | 0.1415 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl       | joint      | H0     |      -0.31098 | -3.15115 |  1.36435 | 0.4941 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl       | joint      | cf0    |      -1.20701 | -1.81021 | -0.70167 | 0.4941 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl       | joint      | log_pr |       0.95042 | -0.53181 |  3.90144 | 0.4941 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl_park  | uni_H0     | H0     |      -0.12408 | -0.18981 | -0.06071 | 0.4179 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl_park  | uni_cf0    | cf0    |      -0.07493 | -0.12823 | -0.04042 | 0.1524 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl_park  | uni_log_pr | log_pr |      -0.13463 | -0.19941 | -0.08184 | 0.492  |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl_park  | joint      | H0     |      -0.19402 | -0.35528 | -0.07752 | 0.7653 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl_park  | joint      | cf0    |      -0.1252  | -0.16499 | -0.08691 | 0.7653 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl_park  | joint      | log_pr |       0.03908 | -0.06279 |  0.20432 | 0.7653 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | rd       | uni_H0     | H0     |      -0.04048 | -0.07161 | -0.01215 | 0.3446 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | rd       | uni_cf0    | cf0    |      -0.00691 | -0.03293 |  0.01052 | 0.01   |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | rd       | uni_log_pr | log_pr |      -0.03998 | -0.0747  | -0.01632 | 0.3361 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | rd       | joint      | H0     |      -0.05995 | -0.16338 |  0.02678 | 0.4208 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | rd       | joint      | cf0    |      -0.02232 | -0.05054 |  0.0026  | 0.4208 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | rd       | joint      | log_pr |       0.01451 | -0.05222 |  0.11312 | 0.4208 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | cf_dev   | uni_H0     | H0     |       0.00695 | -0.01672 |  0.03195 | 0.0142 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | cf_dev   | uni_cf0    | cf0    |      -0.03113 | -0.04058 | -0.01808 | 0.2855 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | cf_dev   | uni_log_pr | log_pr |       0.00028 | -0.01956 |  0.02421 | 0      |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | cf_dev   | joint      | H0     |      -0.00295 | -0.03194 |  0.06507 | 0.2862 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | cf_dev   | joint      | cf0    |      -0.03185 | -0.04226 | -0.01479 | 0.2862 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | cf_dev   | joint      | log_pr |       0.00142 | -0.07171 |  0.03136 | 0.2862 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl_neu   | uni_H0     | H0     |       0.86707 |  0.3688  |  1.30965 | 0.2316 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl_neu   | uni_cf0    | cf0    |      -1.03499 | -1.28922 | -0.5999  | 0.3301 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl_neu   | uni_log_pr | log_pr |       0.70987 |  0.18546 |  1.08204 | 0.1553 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl_neu   | joint      | H0     |      -0.16319 | -2.85703 |  1.61477 | 0.4646 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl_neu   | joint      | cf0    |      -1.03855 | -1.62773 | -0.513   | 0.4646 |  60 |           16 |
| gpt2_A_ing_a5e-3      | frq_dmd - dua_dmd     | kl_neu   | joint      | log_pr |       0.80944 | -0.76354 |  3.57137 | 0.4646 |  60 |           16 |

## predictor_corr

| group                 | a         | b         | pred_i   | pred_j   |   corr |
|:----------------------|:----------|:----------|:---------|:---------|-------:|
| A_third_a5e-3         | euc_dmd   | dua_dmd   | H0       | cf0      |  0.094 |
| A_third_a5e-3         | euc_dmd   | dua_dmd   | H0       | log_pr   |  0.946 |
| A_third_a5e-3         | euc_dmd   | dua_dmd   | cf0      | log_pr   |  0.2   |
| A_third_a5e-3         | cau_unemb | dua_unemb | H0       | cf0      |  0.094 |
| A_third_a5e-3         | cau_unemb | dua_unemb | H0       | log_pr   |  0.946 |
| A_third_a5e-3         | cau_unemb | dua_unemb | cf0      | log_pr   |  0.2   |
| A_third_a5e-3         | frq_unemb | dua_unemb | H0       | cf0      |  0.094 |
| A_third_a5e-3         | frq_unemb | dua_unemb | H0       | log_pr   |  0.946 |
| A_third_a5e-3         | frq_unemb | dua_unemb | cf0      | log_pr   |  0.2   |
| A_third_a5e-3         | cau_unemb | frq_unemb | H0       | cf0      |  0.094 |
| A_third_a5e-3         | cau_unemb | frq_unemb | H0       | log_pr   |  0.946 |
| A_third_a5e-3         | cau_unemb | frq_unemb | cf0      | log_pr   |  0.2   |
| A_third_a5e-3         | frq_dmd   | dua_dmd   | H0       | cf0      |  0.094 |
| A_third_a5e-3         | frq_dmd   | dua_dmd   | H0       | log_pr   |  0.946 |
| A_third_a5e-3         | frq_dmd   | dua_dmd   | cf0      | log_pr   |  0.2   |
| C_third_a5e-3         | euc_dmd   | dua_dmd   | H0       | cf0      | -0.777 |
| C_third_a5e-3         | euc_dmd   | dua_dmd   | H0       | log_pr   |  0.579 |
| C_third_a5e-3         | euc_dmd   | dua_dmd   | cf0      | log_pr   | -0.625 |
| C_third_a5e-3         | cau_unemb | dua_unemb | H0       | cf0      | -0.777 |
| C_third_a5e-3         | cau_unemb | dua_unemb | H0       | log_pr   |  0.579 |
| C_third_a5e-3         | cau_unemb | dua_unemb | cf0      | log_pr   | -0.625 |
| C_third_a5e-3         | frq_unemb | dua_unemb | H0       | cf0      | -0.777 |
| C_third_a5e-3         | frq_unemb | dua_unemb | H0       | log_pr   |  0.579 |
| C_third_a5e-3         | frq_unemb | dua_unemb | cf0      | log_pr   | -0.625 |
| C_third_a5e-3         | cau_unemb | frq_unemb | H0       | cf0      | -0.777 |
| C_third_a5e-3         | cau_unemb | frq_unemb | H0       | log_pr   |  0.579 |
| C_third_a5e-3         | cau_unemb | frq_unemb | cf0      | log_pr   | -0.625 |
| C_third_a5e-3         | frq_dmd   | dua_dmd   | H0       | cf0      | -0.777 |
| C_third_a5e-3         | frq_dmd   | dua_dmd   | H0       | log_pr   |  0.579 |
| C_third_a5e-3         | frq_dmd   | dua_dmd   | cf0      | log_pr   | -0.625 |
| Cbig_third_a5e-3      | euc_dmd   | dua_dmd   | H0       | cf0      | -0.765 |
| Cbig_third_a5e-3      | euc_dmd   | dua_dmd   | H0       | log_pr   |  0.681 |
| Cbig_third_a5e-3      | euc_dmd   | dua_dmd   | cf0      | log_pr   | -0.683 |
| Cbig_third_a5e-3      | cau_unemb | dua_unemb | H0       | cf0      | -0.765 |
| Cbig_third_a5e-3      | cau_unemb | dua_unemb | H0       | log_pr   |  0.681 |
| Cbig_third_a5e-3      | cau_unemb | dua_unemb | cf0      | log_pr   | -0.683 |
| Cbig_third_a5e-3      | frq_unemb | dua_unemb | H0       | cf0      | -0.765 |
| Cbig_third_a5e-3      | frq_unemb | dua_unemb | H0       | log_pr   |  0.681 |
| Cbig_third_a5e-3      | frq_unemb | dua_unemb | cf0      | log_pr   | -0.683 |
| Cbig_third_a5e-3      | cau_unemb | frq_unemb | H0       | cf0      | -0.765 |
| Cbig_third_a5e-3      | cau_unemb | frq_unemb | H0       | log_pr   |  0.681 |
| Cbig_third_a5e-3      | cau_unemb | frq_unemb | cf0      | log_pr   | -0.683 |
| Cbig_third_a5e-3      | frq_dmd   | dua_dmd   | H0       | cf0      | -0.765 |
| Cbig_third_a5e-3      | frq_dmd   | dua_dmd   | H0       | log_pr   |  0.681 |
| Cbig_third_a5e-3      | frq_dmd   | dua_dmd   | cf0      | log_pr   | -0.683 |
| gpt2_A_third_a5e-3    | euc_dmd   | dua_dmd   | H0       | cf0      | -0.337 |
| gpt2_A_third_a5e-3    | euc_dmd   | dua_dmd   | H0       | log_pr   |  0.944 |
| gpt2_A_third_a5e-3    | euc_dmd   | dua_dmd   | cf0      | log_pr   | -0.159 |
| gpt2_A_third_a5e-3    | cau_unemb | dua_unemb | H0       | cf0      | -0.337 |
| gpt2_A_third_a5e-3    | cau_unemb | dua_unemb | H0       | log_pr   |  0.944 |
| gpt2_A_third_a5e-3    | cau_unemb | dua_unemb | cf0      | log_pr   | -0.159 |
| gpt2_A_third_a5e-3    | frq_unemb | dua_unemb | H0       | cf0      | -0.4   |
| gpt2_A_third_a5e-3    | frq_unemb | dua_unemb | H0       | log_pr   |  0.887 |
| gpt2_A_third_a5e-3    | frq_unemb | dua_unemb | cf0      | log_pr   | -0.113 |
| gpt2_A_third_a5e-3    | cau_unemb | frq_unemb | H0       | cf0      | -0.4   |
| gpt2_A_third_a5e-3    | cau_unemb | frq_unemb | H0       | log_pr   |  0.887 |
| gpt2_A_third_a5e-3    | cau_unemb | frq_unemb | cf0      | log_pr   | -0.113 |
| gpt2_A_third_a5e-3    | frq_dmd   | dua_dmd   | H0       | cf0      | -0.337 |
| gpt2_A_third_a5e-3    | frq_dmd   | dua_dmd   | H0       | log_pr   |  0.944 |
| gpt2_A_third_a5e-3    | frq_dmd   | dua_dmd   | cf0      | log_pr   | -0.159 |
| A_third_a2e-2         | euc_dmd   | dua_dmd   | H0       | cf0      |  0.094 |
| A_third_a2e-2         | euc_dmd   | dua_dmd   | H0       | log_pr   |  0.946 |
| A_third_a2e-2         | euc_dmd   | dua_dmd   | cf0      | log_pr   |  0.2   |
| A_third_a2e-2         | cau_unemb | dua_unemb | H0       | cf0      |  0.094 |
| A_third_a2e-2         | cau_unemb | dua_unemb | H0       | log_pr   |  0.946 |
| A_third_a2e-2         | cau_unemb | dua_unemb | cf0      | log_pr   |  0.2   |
| A_third_a2e-2         | frq_unemb | dua_unemb | H0       | cf0      |  0.094 |
| A_third_a2e-2         | frq_unemb | dua_unemb | H0       | log_pr   |  0.946 |
| A_third_a2e-2         | frq_unemb | dua_unemb | cf0      | log_pr   |  0.2   |
| A_third_a2e-2         | cau_unemb | frq_unemb | H0       | cf0      |  0.094 |
| A_third_a2e-2         | cau_unemb | frq_unemb | H0       | log_pr   |  0.946 |
| A_third_a2e-2         | cau_unemb | frq_unemb | cf0      | log_pr   |  0.2   |
| A_third_a2e-2         | frq_dmd   | dua_dmd   | H0       | cf0      |  0.094 |
| A_third_a2e-2         | frq_dmd   | dua_dmd   | H0       | log_pr   |  0.946 |
| A_third_a2e-2         | frq_dmd   | dua_dmd   | cf0      | log_pr   |  0.2   |
| C_third_a2e-2         | euc_dmd   | dua_dmd   | H0       | cf0      | -0.777 |
| C_third_a2e-2         | euc_dmd   | dua_dmd   | H0       | log_pr   |  0.579 |
| C_third_a2e-2         | euc_dmd   | dua_dmd   | cf0      | log_pr   | -0.625 |
| C_third_a2e-2         | cau_unemb | dua_unemb | H0       | cf0      | -0.777 |
| C_third_a2e-2         | cau_unemb | dua_unemb | H0       | log_pr   |  0.579 |
| C_third_a2e-2         | cau_unemb | dua_unemb | cf0      | log_pr   | -0.625 |
| C_third_a2e-2         | frq_unemb | dua_unemb | H0       | cf0      | -0.777 |
| C_third_a2e-2         | frq_unemb | dua_unemb | H0       | log_pr   |  0.579 |
| C_third_a2e-2         | frq_unemb | dua_unemb | cf0      | log_pr   | -0.625 |
| C_third_a2e-2         | cau_unemb | frq_unemb | H0       | cf0      | -0.777 |
| C_third_a2e-2         | cau_unemb | frq_unemb | H0       | log_pr   |  0.579 |
| C_third_a2e-2         | cau_unemb | frq_unemb | cf0      | log_pr   | -0.625 |
| C_third_a2e-2         | frq_dmd   | dua_dmd   | H0       | cf0      | -0.777 |
| C_third_a2e-2         | frq_dmd   | dua_dmd   | H0       | log_pr   |  0.579 |
| C_third_a2e-2         | frq_dmd   | dua_dmd   | cf0      | log_pr   | -0.625 |
| gemma4b_A_third_a5e-3 | euc_dmd   | dua_dmd   | H0       | cf0      | -0.323 |
| gemma4b_A_third_a5e-3 | euc_dmd   | dua_dmd   | H0       | log_pr   |  0.902 |
| gemma4b_A_third_a5e-3 | euc_dmd   | dua_dmd   | cf0      | log_pr   | -0.186 |
| gemma4b_A_third_a5e-3 | cau_unemb | dua_unemb | H0       | cf0      | -0.323 |
| gemma4b_A_third_a5e-3 | cau_unemb | dua_unemb | H0       | log_pr   |  0.902 |
| gemma4b_A_third_a5e-3 | cau_unemb | dua_unemb | cf0      | log_pr   | -0.186 |
| gemma4b_A_third_a5e-3 | frq_unemb | dua_unemb | H0       | cf0      | -0.323 |
| gemma4b_A_third_a5e-3 | frq_unemb | dua_unemb | H0       | log_pr   |  0.902 |
| gemma4b_A_third_a5e-3 | frq_unemb | dua_unemb | cf0      | log_pr   | -0.186 |
| gemma4b_A_third_a5e-3 | cau_unemb | frq_unemb | H0       | cf0      | -0.323 |
| gemma4b_A_third_a5e-3 | cau_unemb | frq_unemb | H0       | log_pr   |  0.902 |
| gemma4b_A_third_a5e-3 | cau_unemb | frq_unemb | cf0      | log_pr   | -0.186 |
| gemma4b_A_third_a5e-3 | frq_dmd   | dua_dmd   | H0       | cf0      | -0.323 |
| gemma4b_A_third_a5e-3 | frq_dmd   | dua_dmd   | H0       | log_pr   |  0.902 |
| gemma4b_A_third_a5e-3 | frq_dmd   | dua_dmd   | cf0      | log_pr   | -0.186 |
| A_ing_a5e-3           | euc_dmd   | dua_dmd   | H0       | cf0      |  0.036 |
| A_ing_a5e-3           | euc_dmd   | dua_dmd   | H0       | log_pr   |  0.939 |
| A_ing_a5e-3           | euc_dmd   | dua_dmd   | cf0      | log_pr   |  0.128 |
| A_ing_a5e-3           | cau_unemb | dua_unemb | H0       | cf0      |  0.036 |
| A_ing_a5e-3           | cau_unemb | dua_unemb | H0       | log_pr   |  0.939 |
| A_ing_a5e-3           | cau_unemb | dua_unemb | cf0      | log_pr   |  0.128 |
| A_ing_a5e-3           | frq_unemb | dua_unemb | H0       | cf0      |  0.036 |
| A_ing_a5e-3           | frq_unemb | dua_unemb | H0       | log_pr   |  0.939 |
| A_ing_a5e-3           | frq_unemb | dua_unemb | cf0      | log_pr   |  0.128 |
| A_ing_a5e-3           | cau_unemb | frq_unemb | H0       | cf0      |  0.036 |
| A_ing_a5e-3           | cau_unemb | frq_unemb | H0       | log_pr   |  0.939 |
| A_ing_a5e-3           | cau_unemb | frq_unemb | cf0      | log_pr   |  0.128 |
| A_ing_a5e-3           | frq_dmd   | dua_dmd   | H0       | cf0      |  0.036 |
| A_ing_a5e-3           | frq_dmd   | dua_dmd   | H0       | log_pr   |  0.939 |
| A_ing_a5e-3           | frq_dmd   | dua_dmd   | cf0      | log_pr   |  0.128 |
| gpt2_A_ing_a5e-3      | euc_dmd   | dua_dmd   | H0       | cf0      | -0.269 |
| gpt2_A_ing_a5e-3      | euc_dmd   | dua_dmd   | H0       | log_pr   |  0.928 |
| gpt2_A_ing_a5e-3      | euc_dmd   | dua_dmd   | cf0      | log_pr   | -0.05  |
| gpt2_A_ing_a5e-3      | cau_unemb | dua_unemb | H0       | cf0      | -0.269 |
| gpt2_A_ing_a5e-3      | cau_unemb | dua_unemb | H0       | log_pr   |  0.928 |
| gpt2_A_ing_a5e-3      | cau_unemb | dua_unemb | cf0      | log_pr   | -0.05  |
| gpt2_A_ing_a5e-3      | frq_unemb | dua_unemb | H0       | cf0      | -0.269 |
| gpt2_A_ing_a5e-3      | frq_unemb | dua_unemb | H0       | log_pr   |  0.928 |
| gpt2_A_ing_a5e-3      | frq_unemb | dua_unemb | cf0      | log_pr   | -0.05  |
| gpt2_A_ing_a5e-3      | cau_unemb | frq_unemb | H0       | cf0      | -0.269 |
| gpt2_A_ing_a5e-3      | cau_unemb | frq_unemb | H0       | log_pr   |  0.928 |
| gpt2_A_ing_a5e-3      | cau_unemb | frq_unemb | cf0      | log_pr   | -0.05  |
| gpt2_A_ing_a5e-3      | frq_dmd   | dua_dmd   | H0       | cf0      | -0.269 |
| gpt2_A_ing_a5e-3      | frq_dmd   | dua_dmd   | H0       | log_pr   |  0.928 |
| gpt2_A_ing_a5e-3      | frq_dmd   | dua_dmd   | cf0      | log_pr   | -0.05  |

## null_control_summary

| group                 | run                             | method    |   n_ctx |   kl_real |   kl_null |   kl_real_minus_null |    kl_lo |    kl_hi |   kl_park_real |   kl_park_null |   kl_park_real_minus_null |   kl_park_lo |   kl_park_hi |   rd_real |   rd_null |   rd_real_minus_null |   rd_lo |   rd_hi |   cf_dev_real |   cf_dev_null |   cf_dev_real_minus_null |   cf_dev_lo |   cf_dev_hi |   kl_neu_real |   kl_neu_null |   kl_neu_real_minus_null |   kl_neu_lo |   kl_neu_hi |   P1_null_end |
|:----------------------|:--------------------------------|:----------|--------:|----------:|----------:|---------------------:|---------:|---------:|---------------:|---------------:|--------------------------:|-------------:|-------------:|----------:|----------:|---------------------:|--------:|--------:|--------------:|--------------:|-------------------------:|------------:|------------:|--------------:|--------------:|-------------------------:|------------:|------------:|--------------:|
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | cau_ctx   |      30 |    2.4998 |    3.0196 |              -0.5198 |  -0.8332 |  -0.2828 |         1.0897 |         1.0228 |                    0.0669 |      -0.0074 |       0.1386 |    0.2236 |    0.1855 |               0.0381 |  0.0088 |  0.0597 |        0.3103 |        0.3769 |                  -0.0667 |     -0.1023 |     -0.0198 |        1.6201 |        1.4713 |                   0.1489 |      0.066  |      0.2151 |        0.0456 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | cau_dmd   |      30 |    1.3013 |    1.8693 |              -0.5681 |  -0.7533 |  -0.329  |         0.6928 |         0.8515 |                   -0.1588 |      -0.2617 |      -0.0283 |    0.1993 |    0.2296 |              -0.0303 | -0.0608 |  0.002  |        0.1754 |        0.1977 |                  -0.0223 |     -0.068  |      0.0358 |        0.8789 |        0.8101 |                   0.0688 |     -0.0374 |      0.1818 |        0.1851 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | cau_unemb |      30 |    0.8821 |    0.1035 |               0.7787 |   0.6519 |   0.9264 |         0.4988 |         0.0543 |                    0.4445 |       0.323  |       0.5871 |    0.1615 |    0.0575 |               0.104  |  0.0583 |  0.1629 |        0.1098 |        0.0325 |                   0.0773 |      0.039  |      0.1301 |        0.6668 |        0.0394 |                   0.6274 |      0.5062 |      0.7605 |        0.0084 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | dua_ctx   |      30 |    3.3574 |    2.2566 |               1.1008 |   0.7251 |   1.4278 |         0.5164 |         0.3631 |                    0.1533 |       0.0952 |       0.2325 |    0.0746 |    0.0664 |               0.0081 | -0.0108 |  0.0306 |        0.1513 |        0.161  |                  -0.0098 |     -0.0265 |      0.0071 |        2.8725 |        1.5015 |                   1.371  |      1.007  |      1.6631 |        0.0849 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | dua_dmd   |      30 |    0.9191 |    0.7427 |               0.1764 |   0.095  |   0.2524 |         0.3056 |         0.2318 |                    0.0738 |       0.0311 |       0.1087 |    0.0577 |    0.0796 |              -0.0219 | -0.0336 | -0.0104 |        0.0481 |        0.0575 |                  -0.0094 |     -0.0193 |      0.0011 |        0.8062 |        0.3777 |                   0.4285 |      0.3193 |      0.5306 |        0.2339 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | dua_unemb |      30 |    1.36   |    0.1791 |               1.1808 |   0.9538 |   1.4139 |         0.2938 |         0.0602 |                    0.2337 |       0.1893 |       0.2785 |    0.0674 |    0.0213 |               0.046  |  0.0334 |  0.0584 |        0.0374 |        0.025  |                   0.0124 |      0.0025 |      0.0228 |        1.2363 |        0.1146 |                   1.1217 |      0.9139 |      1.3364 |        0.0124 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | euc_ctx   |      30 |    1.0062 |    0.5958 |               0.4105 |   0.3134 |   0.5231 |         0.5585 |         0.3284 |                    0.2301 |       0.1368 |       0.3491 |    0.157  |    0.1495 |               0.0075 | -0.0204 |  0.0429 |        0.1283 |        0.1321 |                  -0.0037 |     -0.0425 |      0.0496 |        0.8315 |        0.3649 |                   0.4667 |      0.3819 |      0.5661 |        0.0364 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | euc_dmd   |      30 |    1.1643 |    1.5278 |              -0.3635 |  -0.5273 |  -0.1583 |         0.6415 |         0.7822 |                   -0.1407 |      -0.2369 |      -0.0125 |    0.1937 |    0.2314 |              -0.0377 | -0.0734 |  0.0006 |        0.1519 |        0.192  |                  -0.0401 |     -0.0755 |     -0.0013 |        0.7867 |        0.7375 |                   0.0492 |     -0.0715 |      0.1687 |        0.286  |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | euc_unemb |      30 |    0.9762 |    0.1936 |               0.7826 |   0.6663 |   0.9245 |         0.5372 |         0.1506 |                    0.3867 |       0.2643 |       0.5304 |    0.1886 |    0.0822 |               0.1064 |  0.067  |  0.1581 |        0.093  |        0.0556 |                   0.0374 |      0.0007 |      0.0913 |        0.6934 |        0.0912 |                   0.6022 |      0.4893 |      0.7288 |        0.0101 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | frq_dmd   |      30 |    2.7929 |    1.8674 |               0.9255 |   0.7311 |   1.1846 |         1.2268 |         0.8475 |                    0.3793 |       0.2636 |       0.5246 |    0.227  |    0.149  |               0.078  |  0.0416 |  0.1207 |        0.3878 |        0.3294 |                   0.0583 |      0.0336 |      0.0898 |        1.5645 |        0.8749 |                   0.6896 |      0.4929 |      0.9451 |        0.0225 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s0_abs5e-3    | frq_unemb |      30 |   16.2469 |   19.7485 |              -3.5016 |  -4.0834 |  -2.8708 |         1.8716 |         1.8715 |                    0.0001 |      -0.0001 |       0.0004 |    0.1921 |    0.1726 |               0.0194 |  0.0002 |  0.0386 |        0.5786 |        0.5787 |                  -0.0001 |     -0.0002 |     -0      |        7.0746 |        8.5004 |                  -1.4259 |     -1.8698 |     -1.0498 |        0.008  |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | cau_ctx   |      30 |    1.816  |    0.8975 |               0.9185 |   0.6549 |   1.2696 |         0.7786 |         0.4052 |                    0.3733 |       0.2649 |       0.498  |    0.186  |    0.1786 |               0.0074 | -0.0092 |  0.0244 |        0.2466 |        0.1356 |                   0.111  |      0.0533 |      0.1765 |        1.29   |        0.4447 |                   0.8453 |      0.6738 |      1.0369 |        0.0243 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | cau_dmd   |      30 |    1.1367 |    1.9229 |              -0.7862 |  -0.9299 |  -0.616  |         0.5525 |         0.633  |                   -0.0805 |      -0.1359 |      -0.0176 |    0.1796 |    0.1652 |               0.0144 | -0.0043 |  0.0393 |        0.1945 |        0.1807 |                   0.0137 |     -0.0315 |      0.0756 |        0.7581 |        0.6709 |                   0.0873 |     -0.0035 |      0.1963 |        0.3222 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | cau_unemb |      30 |    0.8247 |    0.1031 |               0.7215 |   0.6261 |   0.8293 |         0.4326 |         0.0389 |                    0.3937 |       0.3201 |       0.486  |    0.1551 |    0.0667 |               0.0884 |  0.059  |  0.127  |        0.1321 |        0.0352 |                   0.0969 |      0.0568 |      0.1476 |        0.6018 |        0.0487 |                   0.5531 |      0.4854 |      0.6376 |        0.0075 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | dua_ctx   |      30 |    3.1867 |    2.0779 |               1.1088 |   0.8151 |   1.4495 |         0.4699 |         0.3243 |                    0.1455 |       0.1011 |       0.2134 |    0.0843 |    0.0689 |               0.0155 | -0.0064 |  0.0467 |        0.1181 |        0.1039 |                   0.0141 |      0.0033 |      0.031  |        2.7667 |        1.3685 |                   1.3981 |      1.0976 |      1.7417 |        0.1341 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | dua_dmd   |      30 |    0.9468 |    0.7323 |               0.2145 |   0.1218 |   0.2934 |         0.3092 |         0.1846 |                    0.1247 |       0.0909 |       0.1577 |    0.059  |    0.0948 |              -0.0357 | -0.0487 | -0.0173 |        0.0488 |        0.0619 |                  -0.0131 |     -0.0268 |      0.0015 |        0.8491 |        0.3675 |                   0.4816 |      0.407  |      0.5818 |        0.2811 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | dua_unemb |      30 |    1.5313 |    0.165  |               1.3662 |   1.0805 |   1.663  |         0.3033 |         0.0273 |                    0.276  |       0.229  |       0.3304 |    0.067  |    0.0234 |               0.0436 |  0.028  |  0.0647 |        0.0402 |        0.0159 |                   0.0243 |      0.0142 |      0.0364 |        1.4175 |        0.1084 |                   1.3091 |      1.0329 |      1.5977 |        0.009  |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | euc_ctx   |      30 |    0.9426 |    0.6248 |               0.3178 |   0.2118 |   0.4316 |         0.4539 |         0.3116 |                    0.1423 |       0.0797 |       0.2198 |    0.1357 |    0.1603 |              -0.0246 | -0.0458 |  0.0014 |        0.1556 |        0.1313 |                   0.0243 |     -0.0049 |      0.0548 |        0.7454 |        0.3178 |                   0.4276 |      0.3376 |      0.5328 |        0.0569 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | euc_dmd   |      30 |    1.105  |    1.6807 |              -0.5757 |  -0.7039 |  -0.4425 |         0.5515 |         0.5944 |                   -0.0429 |      -0.0861 |       0.0133 |    0.183  |    0.1595 |               0.0236 |  0.0001 |  0.0469 |        0.1865 |        0.1889 |                  -0.0024 |     -0.0436 |      0.0477 |        0.7201 |        0.6325 |                   0.0877 |      0.0141 |      0.1756 |        0.4268 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | euc_unemb |      30 |    0.9346 |    0.1075 |               0.8271 |   0.7375 |   0.9326 |         0.4807 |         0.0336 |                    0.4471 |       0.3851 |       0.5326 |    0.1728 |    0.0718 |               0.101  |  0.0754 |  0.1352 |        0.121  |        0.0375 |                   0.0835 |      0.0483 |      0.1212 |        0.6477 |        0.0549 |                   0.5928 |      0.5279 |      0.6658 |        0.0079 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | frq_dmd   |      30 |    1.6052 |    0.434  |               1.1712 |   1.0164 |   1.385  |         0.7898 |         0.2295 |                    0.5603 |       0.4728 |       0.6787 |    0.201  |    0.1182 |               0.0828 |  0.0687 |  0.095  |        0.2089 |        0.0814 |                   0.1276 |      0.0847 |      0.1733 |        0.8854 |        0.2183 |                   0.6671 |      0.5673 |      0.7918 |        0.028  |
| A_third_a5e-3         | runs/gemma1b_v5/A_s1_abs5e-3    | frq_unemb |      30 |   17.3528 |   17.2451 |               0.1078 |  -0.4342 |   0.7132 |         1.7107 |         1.7092 |                    0.0014 |       0.0001 |       0.0035 |    0.1981 |    0.1464 |               0.0518 |  0.0358 |  0.0671 |        0.5644 |        0.5643 |                   0.0001 |      0      |      0.0002 |        7.6251 |        7.6393 |                  -0.0143 |     -0.2803 |      0.2672 |        0.0078 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | cau_ctx   |      30 |    2.8065 |    2.0803 |               0.7262 |   0.3998 |   1.1603 |         1.1089 |         0.8032 |                    0.3058 |       0.2154 |       0.4107 |    0.1971 |    0.1785 |               0.0186 |  0.0012 |  0.0362 |        0.3653 |        0.2657 |                   0.0996 |      0.0524 |      0.1497 |        1.6805 |        1.0405 |                   0.64   |      0.4152 |      0.8539 |        0.0061 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | cau_dmd   |      30 |    1.2864 |    2.5611 |              -1.2748 |  -1.5065 |  -1.0398 |         0.6174 |         0.8276 |                   -0.2101 |      -0.2763 |      -0.1383 |    0.1796 |    0.1992 |              -0.0196 | -0.0496 |  0.0076 |        0.1926 |        0.3048 |                  -0.1122 |     -0.1778 |     -0.0351 |        0.8061 |        0.3844 |                   0.4217 |      0.3389 |      0.5097 |        0.0105 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | cau_unemb |      30 |    0.8693 |    0.1085 |               0.7608 |   0.6648 |   0.8667 |         0.4739 |         0.0695 |                    0.4044 |       0.3352 |       0.4759 |    0.1669 |    0.0819 |               0.085  |  0.0484 |  0.1199 |        0.1492 |        0.0317 |                   0.1175 |      0.0675 |      0.1759 |        0.6249 |        0.0455 |                   0.5793 |      0.4919 |      0.6774 |        0.0095 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | dua_ctx   |      30 |    3.1011 |    2.1893 |               0.9118 |   0.5035 |   1.2773 |         0.4651 |         0.3685 |                    0.0966 |       0.0513 |       0.1409 |    0.0761 |    0.0647 |               0.0114 | -0.0167 |  0.0471 |        0.1314 |        0.1463 |                  -0.0149 |     -0.026  |     -0.0045 |        2.6381 |        1.3418 |                   1.2963 |      0.8267 |      1.6946 |        0.0011 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | dua_dmd   |      30 |    0.978  |    0.6143 |               0.3636 |   0.258  |   0.4813 |         0.3049 |         0.177  |                    0.1279 |       0.0865 |       0.1676 |    0.0619 |    0.0834 |              -0.0215 | -0.0444 |  0.0038 |        0.0494 |        0.135  |                  -0.0856 |     -0.099  |     -0.0732 |        0.8693 |        0.2697 |                   0.5996 |      0.4421 |      0.8105 |        0.0096 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | dua_unemb |      30 |    1.4522 |    0.1394 |               1.3127 |   1.0949 |   1.5777 |         0.3099 |         0.0385 |                    0.2715 |       0.2347 |       0.3119 |    0.0632 |    0.0208 |               0.0425 |  0.0281 |  0.0571 |        0.0396 |        0.0111 |                   0.0285 |      0.0202 |      0.038  |        1.3306 |        0.0837 |                   1.2469 |      1.0313 |      1.5069 |        0.0095 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | euc_ctx   |      30 |    0.9273 |    0.6219 |               0.3054 |   0.2266 |   0.3737 |         0.4692 |         0.3106 |                    0.1586 |       0.1073 |       0.2179 |    0.1499 |    0.1425 |               0.0074 | -0.0195 |  0.0375 |        0.1414 |        0.1192 |                   0.0222 |     -0.0142 |      0.0582 |        0.7153 |        0.2778 |                   0.4375 |      0.3258 |      0.5292 |        0.006  |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | euc_dmd   |      30 |    1.215  |    2.1697 |              -0.9546 |  -1.1818 |  -0.7284 |         0.6005 |         0.8059 |                   -0.2054 |      -0.2747 |      -0.131  |    0.1746 |    0.1976 |              -0.0231 | -0.0538 |  0.006  |        0.1855 |        0.2995 |                  -0.114  |     -0.1688 |     -0.0533 |        0.7668 |        0.4482 |                   0.3186 |      0.2519 |      0.38   |        0.0137 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | euc_unemb |      30 |    0.99   |    0.1036 |               0.8864 |   0.7915 |   0.9829 |         0.5391 |         0.0653 |                    0.4738 |       0.402  |       0.5465 |    0.1801 |    0.0818 |               0.0983 |  0.0645 |  0.1334 |        0.1407 |        0.0345 |                   0.1062 |      0.0619 |      0.1615 |        0.6854 |        0.0411 |                   0.6443 |      0.5775 |      0.7144 |        0.0098 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | frq_dmd   |      30 |    8.1177 |    3.3446 |               4.7731 |   3.4105 |   6.097  |         1.6771 |         0.8021 |                    0.875  |       0.731  |       0.9861 |    0.1947 |    0.1036 |               0.0911 |  0.074  |  0.1103 |        0.5283 |        0.2801 |                   0.2482 |      0.1676 |      0.3115 |        3.6088 |        1.5619 |                   2.0469 |      1.5151 |      2.6192 |        0.0082 |
| A_third_a5e-3         | runs/gemma1b_v5/A_s2_abs5e-3    | frq_unemb |      30 |    8.6042 |   18.1314 |              -9.5272 | -10.2974 |  -8.3933 |         1.7875 |         1.8039 |                   -0.0164 |      -0.0364 |      -0.0046 |    0.1347 |    0.0839 |               0.0508 |  0.026  |  0.0754 |        0.5625 |        0.5737 |                  -0.0112 |     -0.0275 |     -0.0027 |        4.0474 |        7.9472 |                  -3.8998 |     -4.4304 |     -3.3876 |        0.0094 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | cau_ctx   |      30 |    1.7971 |    5.6965 |              -3.8995 |  -4.607  |  -3.2492 |         1.4677 |         2.3143 |                   -0.8466 |      -1.1677 |      -0.5232 |    0.2771 |    0.3138 |              -0.0367 | -0.1241 |  0.0501 |        0.5009 |        0.4215 |                   0.0793 |     -0.0146 |      0.1698 |        0.2801 |        0.496  |                  -0.2159 |     -0.3028 |     -0.1428 |        0.0004 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | cau_dmd   |      30 |    1.9753 |    7.1167 |              -5.1414 |  -6.3082 |  -4.1975 |         1.6262 |         3.0146 |                   -1.3884 |      -1.874  |      -0.8824 |    0.4217 |    0.4284 |              -0.0067 | -0.1043 |  0.083  |        0.2182 |        0.0667 |                   0.1515 |      0.0716 |      0.2399 |        0.1349 |        0.1238 |                   0.011  |     -0.0248 |      0.0474 |        0      |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | cau_unemb |      30 |    0.6107 |    0.1324 |               0.4783 |   0.3538 |   0.6113 |         0.5265 |         0.1145 |                    0.412  |       0.2929 |       0.5502 |    0.103  |    0.0669 |               0.0361 | -0.0119 |  0.098  |        0.2214 |        0.0297 |                   0.1917 |      0.1323 |      0.2606 |        0.1389 |        0.0178 |                   0.121  |      0.0931 |      0.1508 |        0.0003 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | dua_ctx   |      30 |    2.1891 |    2.2911 |              -0.102  |  -0.3306 |   0.1557 |         0.4048 |         0.393  |                    0.0118 |      -0.0408 |       0.0583 |    0.0349 |    0.0401 |              -0.0052 | -0.0443 |  0.0325 |        0.15   |        0.0962 |                   0.0538 |      0.0295 |      0.0755 |        1.4338 |        0.9785 |                   0.4553 |      0.2724 |      0.667  |        0.0001 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | dua_dmd   |      30 |    2.063  |    3.7071 |              -1.6441 |  -2.1086 |  -1.2307 |         0.4225 |         0.6778 |                   -0.2553 |      -0.4401 |      -0.1167 |    0.0565 |    0.0655 |              -0.009  | -0.0376 |  0.022  |        0.0628 |        0.0695 |                  -0.0066 |     -0.017  |      0.0066 |        1.0059 |        0.5439 |                   0.462  |      0.3101 |      0.6451 |        0      |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | dua_unemb |      30 |    1.7761 |    0.4528 |               1.3233 |   1.0867 |   1.58   |         0.3589 |         0.1068 |                    0.2521 |       0.1751 |       0.3451 |    0.0444 |    0.0121 |               0.0322 |  0.0047 |  0.0711 |        0.0729 |        0.0567 |                   0.0162 |     -0.0058 |      0.0438 |        1.2953 |        0.2437 |                   1.0516 |      0.797  |      1.3211 |        0.001  |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | euc_ctx   |      30 |    0.9034 |    1.0959 |              -0.1925 |  -0.4848 |   0.1002 |         0.7513 |         0.8348 |                   -0.0835 |      -0.34   |       0.1613 |    0.2033 |    0.2255 |              -0.0222 | -0.1017 |  0.0568 |        0.2853 |        0.0735 |                   0.2118 |      0.1238 |      0.3021 |        0.1851 |        0.0795 |                   0.1055 |      0.0733 |      0.1396 |        0.0002 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | euc_dmd   |      30 |    1.3055 |    5.6618 |              -4.3563 |  -5.3679 |  -3.4689 |         1.1495 |         2.738  |                   -1.5885 |      -1.9636 |      -1.2499 |    0.3297 |    0.3941 |              -0.0644 | -0.1593 |  0.0288 |        0.2077 |        0.0649 |                   0.1429 |      0.0751 |      0.2169 |        0.1276 |        0.1048 |                   0.0228 |     -0.0091 |      0.0557 |        0.0001 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | euc_unemb |      30 |    0.6973 |    0.1748 |               0.5226 |   0.3469 |   0.7383 |         0.5914 |         0.1495 |                    0.442  |       0.2765 |       0.6515 |    0.1097 |    0.0827 |               0.027  | -0.0241 |  0.084  |        0.1783 |        0.0347 |                   0.1436 |      0.093  |      0.196  |        0.1556 |        0.0248 |                   0.1308 |      0.0995 |      0.1646 |        0.0003 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | frq_dmd   |      30 |    2.6042 |    0.4602 |               2.144  |   1.9194 |   2.3234 |         2.241  |         0.3657 |                    1.8753 |       1.7464 |       1.9892 |    0.1043 |    0.0104 |               0.0939 |  0.034  |  0.156  |        0.0782 |        0.1491 |                  -0.0709 |     -0.1183 |     -0.0222 |        0.0573 |        0.0592 |                  -0.002  |     -0.0312 |      0.0258 |        0.0003 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s0_abs5e-3    | frq_unemb |      30 |    2.5915 |    2.5559 |               0.0355 |  -0.5717 |   0.5403 |         2.1962 |         1.7741 |                    0.4221 |       0.1466 |       0.6926 |    0.2417 |    0.0015 |               0.2402 |  0.1609 |  0.3172 |        0.2744 |        0.6121 |                  -0.3378 |     -0.4257 |     -0.245  |        0.2759 |        0.2899 |                  -0.014  |     -0.0666 |      0.043  |        0.0003 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | cau_ctx   |      30 |    2.3683 |    1.5629 |               0.8055 |   0.3365 |   1.2662 |         1.9637 |         1.1405 |                    0.8233 |       0.4531 |       1.1828 |    0.2752 |    0.2471 |               0.0282 | -0.0719 |  0.1314 |        0.6555 |        0.2857 |                   0.3699 |      0.2719 |      0.4661 |        0.2633 |        0.1947 |                   0.0686 |      0.0275 |      0.108  |        0.0008 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | cau_dmd   |      30 |    2.1026 |    5.0325 |              -2.9299 |  -3.8931 |  -1.9741 |         1.6124 |         2.4395 |                   -0.8271 |      -1.3454 |      -0.3386 |    0.3248 |    0.356  |              -0.0312 | -0.1214 |  0.054  |        0.1702 |        0.0596 |                   0.1106 |      0.0488 |      0.1798 |        0.1022 |        0.0825 |                   0.0196 |      0.0009 |      0.0392 |        0.0006 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | cau_unemb |      30 |    0.5045 |    0.1798 |               0.3247 |   0.2066 |   0.458  |         0.4446 |         0.1545 |                    0.2901 |       0.1715 |       0.4233 |    0.1329 |    0.0811 |               0.0518 | -0.0097 |  0.1223 |        0.1615 |        0.0408 |                   0.1207 |      0.0774 |      0.1697 |        0.1028 |        0.0173 |                   0.0855 |      0.064  |      0.1088 |        0.0018 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | dua_ctx   |      29 |    2.1857 |    1.7651 |               0.4206 |   0.0988 |   0.7359 |         0.4406 |         0.3021 |                    0.1385 |       0.0932 |       0.1874 |    0.0211 |    0.0318 |              -0.0107 | -0.03   |  0.0009 |        0.2484 |        0.1438 |                   0.1046 |      0.0834 |      0.1279 |        1.3106 |        0.7557 |                   0.5549 |      0.3881 |      0.7205 |        0.0002 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | dua_dmd   |      30 |    2.2706 |    3.2813 |              -1.0107 |  -1.6239 |  -0.5044 |         0.5333 |         0.5561 |                   -0.0228 |      -0.1101 |       0.0584 |    0.0856 |    0.0777 |               0.0079 | -0.0186 |  0.0444 |        0.0433 |        0.0618 |                  -0.0185 |     -0.0292 |     -0.0075 |        0.8946 |        0.4331 |                   0.4615 |      0.3568 |      0.5662 |        0.0042 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | dua_unemb |      30 |    1.4809 |    0.5768 |               0.9042 |   0.706  |   1.1045 |         0.3201 |         0.121  |                    0.1991 |       0.1326 |       0.2801 |    0.0158 |    0.0127 |               0.0032 |  0.0009 |  0.0058 |        0.0704 |        0.0671 |                   0.0033 |     -0.0125 |      0.02   |        1.0597 |        0.2628 |                   0.797  |      0.6132 |      0.9825 |        0.0023 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | euc_ctx   |      30 |    0.7893 |    0.5533 |               0.236  |   0.018  |   0.4735 |         0.6812 |         0.4234 |                    0.2578 |       0.061  |       0.4671 |    0.1691 |    0.1544 |               0.0148 | -0.0679 |  0.1015 |        0.2506 |        0.0622 |                   0.1883 |      0.1222 |      0.2543 |        0.136  |        0.0643 |                   0.0716 |      0.0522 |      0.0942 |        0.0009 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | euc_dmd   |      30 |    1.6229 |    3.9805 |              -2.3576 |  -3.2097 |  -1.6014 |         1.286  |         2.1009 |                   -0.8149 |      -1.3141 |      -0.3776 |    0.3069 |    0.3393 |              -0.0324 | -0.1247 |  0.0639 |        0.1468 |        0.0583 |                   0.0885 |      0.031  |      0.1541 |        0.1063 |        0.0756 |                   0.0307 |      0.0181 |      0.0442 |        0.0006 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | euc_unemb |      30 |    0.6046 |    0.1931 |               0.4115 |   0.2587 |   0.5871 |         0.5146 |         0.1612 |                    0.3534 |       0.2054 |       0.5169 |    0.1895 |    0.0758 |               0.1137 |  0.0278 |  0.202  |        0.0986 |        0.05   |                   0.0485 |      0.0099 |      0.0971 |        0.1126 |        0.0248 |                   0.0878 |      0.0659 |      0.1142 |        0.0019 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | frq_dmd   |      30 |    2.2306 |    4.799  |              -2.5684 |  -3.2393 |  -1.9182 |         1.9205 |         2.2737 |                   -0.3532 |      -0.5687 |      -0.138  |    0.1005 |    0.0357 |               0.0648 |  0.0128 |  0.1222 |        0.0541 |        0.1008 |                  -0.0467 |     -0.0785 |     -0.0157 |        0.02   |        0.0968 |                  -0.0768 |     -0.1127 |     -0.0445 |        0.0006 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s1_abs5e-3    | frq_unemb |      30 |    2.3141 |    4.7039 |              -2.3899 |  -3.0175 |  -1.8035 |         2.0026 |         2.8743 |                   -0.8717 |      -1.174  |      -0.5851 |    0.1635 |    0.0063 |               0.1571 |  0.0925 |  0.2243 |        0.0819 |        0.8373 |                  -0.7555 |     -0.8126 |     -0.6863 |        0.1449 |        0.4338 |                  -0.2889 |     -0.3584 |     -0.2214 |        0.0016 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | cau_ctx   |      30 |    1.7776 |    4.0876 |              -2.31   |  -2.7694 |  -1.8427 |         1.4023 |         2.3207 |                   -0.9184 |      -1.2357 |      -0.584  |    0.2849 |    0.3445 |              -0.0596 | -0.1373 |  0.0105 |        0.5163 |        0.4963 |                   0.02   |     -0.0875 |      0.1282 |        0.3467 |        0.4753 |                  -0.1286 |     -0.1923 |     -0.07   |        0.0007 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | cau_dmd   |      30 |    1.8755 |    4.8648 |              -2.9893 |  -3.7763 |  -2.1966 |         1.4875 |         2.5285 |                   -1.041  |      -1.4132 |      -0.6793 |    0.3374 |    0.3459 |              -0.0085 | -0.0889 |  0.0705 |        0.17   |        0.0741 |                   0.0959 |      0.0261 |      0.1786 |        0.1271 |        0.0492 |                   0.0779 |      0.0529 |      0.1022 |        0      |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | cau_unemb |      30 |    0.737  |    0.1295 |               0.6075 |   0.4269 |   0.8141 |         0.6511 |         0.1064 |                    0.5448 |       0.3701 |       0.739  |    0.1999 |    0.0697 |               0.1302 |  0.0557 |  0.2013 |        0.2141 |        0.0362 |                   0.1779 |      0.1165 |      0.2393 |        0.1497 |        0.0238 |                   0.1258 |      0.0888 |      0.1753 |        0.0002 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | dua_ctx   |      30 |    2.3899 |    2.1751 |               0.2149 |  -0.1148 |   0.5825 |         0.4154 |         0.385  |                    0.0305 |      -0.0115 |       0.0718 |    0.0493 |    0.0372 |               0.0121 | -0.0128 |  0.0447 |        0.1601 |        0.1238 |                   0.0363 |      0.0171 |      0.0548 |        1.6537 |        0.965  |                   0.6887 |      0.4104 |      1.0057 |        0.019  |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | dua_dmd   |      30 |    2.3305 |    3.2244 |              -0.894  |  -1.3022 |  -0.4952 |         0.4955 |         0.5541 |                   -0.0586 |      -0.1366 |       0.022  |    0.0666 |    0.0882 |              -0.0216 | -0.0639 |  0.0207 |        0.0527 |        0.078  |                  -0.0253 |     -0.0376 |     -0.0131 |        1.1369 |        0.5411 |                   0.5958 |      0.4334 |      0.7986 |        0.001  |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | dua_unemb |      30 |    1.904  |    0.3856 |               1.5183 |   1.1982 |   1.8549 |         0.3556 |         0.0978 |                    0.2577 |       0.211  |       0.3125 |    0.039  |    0.0217 |               0.0173 |  0.0086 |  0.0298 |        0.0715 |        0.0576 |                   0.0139 |     -0.0027 |      0.0308 |        1.4365 |        0.2049 |                   1.2316 |      0.9032 |      1.6066 |        0.0003 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | euc_ctx   |      30 |    1.204  |    1.0983 |               0.1057 |  -0.1898 |   0.4433 |         0.9752 |         0.8071 |                    0.168  |      -0.1115 |       0.4563 |    0.2385 |    0.2374 |               0.0011 | -0.0864 |  0.0842 |        0.2889 |        0.1078 |                   0.1811 |      0.0971 |      0.2623 |        0.2221 |        0.1075 |                   0.1146 |      0.0746 |      0.1592 |        0.0006 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | euc_dmd   |      30 |    1.6778 |    4.4214 |              -2.7436 |  -3.3972 |  -2.1015 |         1.3002 |         2.389  |                   -1.0888 |      -1.4424 |      -0.7407 |    0.3174 |    0.3415 |              -0.0241 | -0.1136 |  0.07   |        0.1643 |        0.0774 |                   0.0869 |      0.0253 |      0.1571 |        0.1519 |        0.0693 |                   0.0827 |      0.0556 |      0.1102 |        0.0001 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | euc_unemb |      30 |    0.8201 |    0.1269 |               0.6932 |   0.5037 |   0.9296 |         0.7124 |         0.1026 |                    0.6098 |       0.4305 |       0.8244 |    0.2035 |    0.0728 |               0.1308 |  0.0564 |  0.2089 |        0.1588 |        0.0435 |                   0.1153 |      0.0583 |      0.1833 |        0.1612 |        0.0238 |                   0.1374 |      0.0986 |      0.1897 |        0.0002 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | frq_dmd   |      30 |   12.174  |   22.0309 |              -9.857  | -10.8909 |  -8.8214 |         3.947  |         4.0176 |                   -0.0706 |      -0.1412 |      -0.0183 |    0.2074 |    0.183  |               0.0244 | -0.0548 |  0.0993 |        0.9059 |        0.0851 |                   0.8208 |      0.7743 |      0.8641 |        1.1549 |        0.7519 |                   0.4029 |      0.2814 |      0.5392 |        0.3333 |
| C_third_a5e-3         | runs/gemma1b_v5/C_s2_abs5e-3    | frq_unemb |      30 |    2.1805 |    0.797  |               1.3836 |   1.1093 |   1.6315 |         1.8598 |         0.6953 |                    1.1645 |       0.9313 |       1.3731 |    0.1386 |    0.0066 |               0.132  |  0.0714 |  0.1921 |        0.0483 |        0.3282 |                  -0.2799 |     -0.3552 |     -0.2039 |        0.1464 |        0.1413 |                   0.0052 |     -0.0285 |      0.0428 |        0.0002 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | cau_ctx   |      30 |    1.8059 |    0.7034 |               1.1025 |   0.7514 |   1.4885 |         1.429  |         0.5466 |                    0.8824 |       0.6037 |       1.161  |    0.2798 |    0.1669 |               0.1129 |  0.0498 |  0.1771 |        0.574  |        0.1039 |                   0.4701 |      0.38   |      0.558  |        0.384  |        0.0966 |                   0.2873 |      0.2042 |      0.3715 |        0.0001 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | cau_dmd   |      30 |    1.438  |    6.3735 |              -4.9355 |  -5.6387 |  -4.2441 |         1.2459 |         2.4768 |                   -1.2309 |      -1.5374 |      -0.9245 |    0.3767 |    0.3233 |               0.0534 | -0.0408 |  0.1362 |        0.1569 |        0.0644 |                   0.0925 |      0.0369 |      0.1513 |        0.1271 |        0.1409 |                  -0.0139 |     -0.0657 |      0.0352 |        0.0001 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | cau_unemb |      30 |    0.5603 |    0.1344 |               0.4259 |   0.3084 |   0.5693 |         0.4727 |         0.1052 |                    0.3674 |       0.2533 |       0.4938 |    0.1567 |    0.0614 |               0.0953 |  0.0329 |  0.1665 |        0.1359 |        0.0396 |                   0.0963 |      0.0706 |      0.1288 |        0.1429 |        0.0193 |                   0.1236 |      0.0925 |      0.1584 |        0.0002 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | dua_ctx   |      29 |    2.4236 |    1.8632 |               0.5604 |   0.2526 |   0.8637 |         0.4536 |         0.3389 |                    0.1147 |       0.0835 |       0.1458 |    0.0359 |    0.0327 |               0.0032 | -0.0147 |  0.0285 |        0.2155 |        0.0904 |                   0.1251 |      0.1074 |      0.1427 |        1.7212 |        0.8944 |                   0.8268 |      0.5727 |      1.0991 |        0      |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | dua_dmd   |      30 |    2.2894 |    3.681  |              -1.3916 |  -1.8077 |  -0.9846 |         0.4514 |         0.686  |                   -0.2346 |      -0.3013 |      -0.1784 |    0.0763 |    0.0751 |               0.0013 | -0.0402 |  0.0457 |        0.0492 |        0.0824 |                  -0.0332 |     -0.0578 |     -0.0065 |        1.3196 |        0.577  |                   0.7426 |      0.5375 |      0.9787 |        0      |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | dua_unemb |      30 |    2.0859 |    0.5191 |               1.5668 |   1.2897 |   1.8709 |         0.4224 |         0.1085 |                    0.3139 |       0.2369 |       0.4175 |    0.0637 |    0.0146 |               0.049  |  0.0147 |  0.0891 |        0.0986 |        0.0618 |                   0.0367 |      0.0146 |      0.064  |        1.4932 |        0.2922 |                   1.201  |      0.8633 |      1.5475 |        0.0015 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | euc_ctx   |      30 |    0.8237 |    0.5258 |               0.2978 |   0.0683 |   0.546  |         0.6856 |         0.4174 |                    0.2682 |       0.0535 |       0.491  |    0.2313 |    0.1293 |               0.102  |  0.0195 |  0.1879 |        0.2669 |        0.0727 |                   0.1942 |      0.1209 |      0.2705 |        0.2055 |        0.0702 |                   0.1352 |      0.1027 |      0.1667 |        0.0001 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | euc_dmd   |      30 |    1.319  |    5.0983 |              -3.7793 |  -4.2539 |  -3.3066 |         1.1371 |         2.3017 |                   -1.1646 |      -1.4494 |      -0.9271 |    0.3876 |    0.334  |               0.0536 | -0.0292 |  0.1368 |        0.1226 |        0.0625 |                   0.0601 |      0.0111 |      0.1214 |        0.1336 |        0.0934 |                   0.0402 |      0.0042 |      0.0791 |        0      |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | euc_unemb |      30 |    0.6906 |    0.2008 |               0.4898 |   0.3225 |   0.6918 |         0.5764 |         0.1562 |                    0.4202 |       0.2536 |       0.6115 |    0.2144 |    0.097  |               0.1174 |  0.038  |  0.1996 |        0.099  |        0.0439 |                   0.0551 |      0.0258 |      0.0892 |        0.1522 |        0.0375 |                   0.1148 |      0.0828 |      0.149  |        0.0002 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | frq_dmd   |      30 |    2.296  |   10.8654 |              -8.5694 |  -9.2643 |  -7.9108 |         1.9439 |         2.966  |                   -1.0221 |      -1.2136 |      -0.8428 |    0.0508 |    0.071  |              -0.0202 | -0.0583 |  0.0165 |        0.07   |        0.1861 |                  -0.116  |     -0.1615 |     -0.0723 |        0.0372 |        0.5722 |                  -0.535  |     -0.6398 |     -0.4296 |        0.0002 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s0_abs5e-3 | frq_unemb |      30 |    3.686  |    5.5352 |              -1.8492 |  -2.4117 |  -1.2763 |         2.5716 |         2.2538 |                    0.3178 |       0.0567 |       0.5554 |    0.2681 |    0.0231 |               0.245  |  0.1708 |  0.3176 |        0.4906 |        0.5899 |                  -0.0993 |     -0.2145 |      0.0141 |        0.4046 |        0.5529 |                  -0.1483 |     -0.2104 |     -0.0877 |        0.0002 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | cau_ctx   |      30 |    2.5251 |    1.6445 |               0.8806 |   0.3245 |   1.4605 |         1.945  |         1.1177 |                    0.8273 |       0.443  |       1.2455 |    0.3242 |    0.2498 |               0.0744 | -0.0127 |  0.1605 |        0.6399 |        0.2232 |                   0.4167 |      0.3305 |      0.5028 |        0.4197 |        0.2055 |                   0.2142 |      0.1586 |      0.2754 |        0.0003 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | cau_dmd   |      30 |    2.655  |    5.9308 |              -3.2758 |  -4.0868 |  -2.4912 |         2.113  |         2.71   |                   -0.597  |      -0.9152 |      -0.2974 |    0.4465 |    0.4142 |               0.0324 | -0.0434 |  0.1072 |        0.221  |        0.0936 |                   0.1274 |      0.0671 |      0.1885 |        0.1834 |        0.1074 |                   0.0759 |      0.0379 |      0.1169 |        0.0004 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | cau_unemb |      30 |    0.798  |    0.1714 |               0.6266 |   0.4489 |   0.823  |         0.6876 |         0.14   |                    0.5476 |       0.3553 |       0.7526 |    0.1531 |    0.0735 |               0.0795 |  0.0089 |  0.1483 |        0.2478 |        0.0463 |                   0.2016 |      0.147  |      0.2583 |        0.1961 |        0.0242 |                   0.172  |      0.1292 |      0.2161 |        0.0001 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | dua_ctx   |      30 |    2.5771 |    2.5945 |              -0.0174 |  -0.2946 |   0.2509 |         0.4585 |         0.4488 |                    0.0097 |      -0.0271 |       0.0441 |    0.0395 |    0.0403 |              -0.0008 | -0.0214 |  0.0283 |        0.2129 |        0.1558 |                   0.0571 |      0.0378 |      0.0769 |        1.8879 |        1.1746 |                   0.7133 |      0.5056 |      0.932  |        0.0393 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | dua_dmd   |      30 |    2.6294 |    3.1099 |              -0.4805 |  -0.7824 |  -0.1773 |         0.4971 |         0.5819 |                   -0.0848 |      -0.1651 |      -0.011  |    0.0694 |    0.061  |               0.0084 | -0.0261 |  0.0464 |        0.0696 |        0.0811 |                  -0.0115 |     -0.0272 |      0.0051 |        1.4897 |        0.7194 |                   0.7703 |      0.5563 |      1.0005 |        0.0989 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | dua_unemb |      30 |    2.0842 |    0.4222 |               1.662  |   1.3119 |   2.0555 |         0.3511 |         0.106  |                    0.2451 |       0.1922 |       0.3075 |    0.0213 |    0.017  |               0.0042 | -0.0048 |  0.0108 |        0.0752 |        0.06   |                   0.0152 |     -0.0012 |      0.0346 |        1.682  |        0.226  |                   1.4559 |      1.104  |      1.8167 |        0.0002 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | euc_ctx   |      30 |    1.1089 |    1.2384 |              -0.1295 |  -0.4482 |   0.1863 |         0.9186 |         0.9322 |                   -0.0136 |      -0.2628 |       0.2451 |    0.2561 |    0.2535 |               0.0026 | -0.0856 |  0.0899 |        0.286  |        0.1653 |                   0.1207 |      0.0536 |      0.1921 |        0.232  |        0.1153 |                   0.1167 |      0.0832 |      0.1531 |        0.001  |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | euc_dmd   |      30 |    1.982  |    4.5981 |              -2.6162 |  -3.356  |  -1.9577 |         1.6544 |         2.4392 |                   -0.7847 |      -1.0734 |      -0.5294 |    0.3605 |    0.3897 |              -0.0292 | -0.1219 |  0.0581 |        0.1708 |        0.0927 |                   0.078  |      0.0349 |      0.1277 |        0.1765 |        0.1086 |                   0.068  |      0.0355 |      0.0997 |        0.0011 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | euc_unemb |      30 |    0.8667 |    0.1653 |               0.7015 |   0.5043 |   0.9228 |         0.7271 |         0.1386 |                    0.5885 |       0.3915 |       0.8094 |    0.1369 |    0.0794 |               0.0575 | -0.012  |  0.1306 |        0.1856 |        0.0451 |                   0.1405 |      0.0926 |      0.19   |        0.2127 |        0.0252 |                   0.1876 |      0.1393 |      0.2392 |        0.0001 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | frq_dmd   |      30 |    2.1863 |    8.3175 |              -6.1312 |  -7.2726 |  -5.068  |         1.8559 |         3.1581 |                   -1.3022 |      -1.5585 |      -1.0399 |    0.3568 |    0.0824 |               0.2744 |  0.2021 |  0.3378 |        0.0721 |        0.5396 |                  -0.4675 |     -0.5206 |     -0.4067 |        0.0834 |        0.5479 |                  -0.4644 |     -0.5768 |     -0.3576 |        0.3289 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s1_abs5e-3 | frq_unemb |      30 |    2.4894 |    0.3651 |               2.1243 |   1.9376 |   2.3077 |         2.0867 |         0.3307 |                    1.7561 |       1.5832 |       1.9263 |    0.2583 |    0.0067 |               0.2516 |  0.1828 |  0.3203 |        0.2256 |        0.2156 |                   0.0099 |     -0.0731 |      0.0882 |        0.2681 |        0.1002 |                   0.1679 |      0.1101 |      0.2317 |        0.0002 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | cau_ctx   |      30 |    1.6272 |    2.2653 |              -0.6381 |  -1.1769 |  -0.0541 |         1.3914 |         1.385  |                    0.0064 |      -0.3672 |       0.3911 |    0.2449 |    0.2423 |               0.0026 | -0.0875 |  0.0979 |        0.482  |        0.3522 |                   0.1298 |      0.0267 |      0.235  |        0.2953 |        0.2695 |                   0.0258 |     -0.0365 |      0.109  |        0.0003 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | cau_dmd   |      30 |    1.8494 |    5.8423 |              -3.9929 |  -4.8489 |  -3.1739 |         1.5281 |         2.6254 |                   -1.0973 |      -1.4474 |      -0.7253 |    0.289  |    0.293  |              -0.004  | -0.0848 |  0.0731 |        0.2839 |        0.0746 |                   0.2093 |      0.1175 |      0.311  |        0.1464 |        0.0844 |                   0.062  |      0.0329 |      0.0923 |        0.0001 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | cau_unemb |      30 |    0.5839 |    0.1905 |               0.3935 |   0.2379 |   0.5649 |         0.5014 |         0.1491 |                    0.3523 |       0.2119 |       0.5134 |    0.0957 |    0.0856 |               0.0101 | -0.0427 |  0.0656 |        0.1894 |        0.0373 |                   0.1521 |      0.0963 |      0.2188 |        0.1656 |        0.0206 |                   0.1449 |      0.0937 |      0.2054 |        0.0001 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | dua_ctx   |      30 |    2.5147 |    1.9462 |               0.5684 |   0.1978 |   0.948  |         0.4797 |         0.3364 |                    0.1434 |       0.1025 |       0.1921 |    0.0297 |    0.0354 |              -0.0057 | -0.0102 | -0.0014 |        0.2043 |        0.1487 |                   0.0557 |      0.0383 |      0.0732 |        1.7337 |        0.879  |                   0.8547 |      0.5456 |      1.2248 |        0.0087 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | dua_dmd   |      30 |    1.9376 |    2.7589 |              -0.8213 |  -1.2573 |  -0.4252 |         0.3941 |         0.5229 |                   -0.1288 |      -0.1934 |      -0.0592 |    0.0721 |    0.0822 |              -0.0101 | -0.0444 |  0.0266 |        0.0313 |        0.0792 |                  -0.0479 |     -0.0676 |     -0.0302 |        1.2166 |        0.4823 |                   0.7343 |      0.468  |      1.0136 |        0.0039 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | dua_unemb |      30 |    1.7638 |    0.3781 |               1.3857 |   0.973  |   1.8705 |         0.31   |         0.0803 |                    0.2296 |       0.177  |       0.2958 |    0.0303 |    0.0168 |               0.0135 |  0.0049 |  0.0249 |        0.0495 |        0.0305 |                   0.019  |      0.008  |      0.0309 |        1.4576 |        0.212  |                   1.2457 |      0.8229 |      1.6871 |        0.0003 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | euc_ctx   |      30 |    1.0692 |    0.7858 |               0.2834 |   0.0452 |   0.5648 |         0.9191 |         0.5804 |                    0.3388 |       0.1219 |       0.5952 |    0.1926 |    0.1801 |               0.0125 | -0.0623 |  0.0971 |        0.297  |        0.1173 |                   0.1798 |      0.1089 |      0.2584 |        0.2163 |        0.0871 |                   0.1292 |      0.0873 |      0.1734 |        0.0003 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | euc_dmd   |      30 |    1.4265 |    5.2805 |              -3.854  |  -4.6157 |  -3.1035 |         1.1874 |         2.4199 |                   -1.2325 |      -1.5454 |      -0.9183 |    0.2628 |    0.2978 |              -0.0349 | -0.104  |  0.0314 |        0.1836 |        0.0736 |                   0.1099 |      0.036  |      0.1899 |        0.1465 |        0.1025 |                   0.044  |      0.0105 |      0.0824 |        0.0002 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | euc_unemb |      30 |    0.6258 |    0.1636 |               0.4622 |   0.3192 |   0.6285 |         0.5227 |         0.1252 |                    0.3976 |       0.2597 |       0.5488 |    0.121  |    0.0771 |               0.044  | -0.0158 |  0.1134 |        0.1243 |        0.0345 |                   0.0899 |      0.0548 |      0.1303 |        0.1798 |        0.0211 |                   0.1587 |      0.102  |      0.2212 |        0.0001 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | frq_dmd   |      30 |    2.5501 |    7.1178 |              -4.5677 |  -5.1124 |  -3.9541 |         2.1133 |         3.6442 |                   -1.5308 |      -1.8    |      -1.2537 |    0.167  |    0.1237 |               0.0434 | -0.0056 |  0.0948 |        0.1206 |        0.176  |                  -0.0554 |     -0.1064 |      0.005  |        0.1634 |        0.4027 |                  -0.2393 |     -0.3203 |     -0.1621 |        0.9251 |
| Cbig_third_a5e-3      | runs/gemma1b_v5/Cbig_s2_abs5e-3 | frq_unemb |      30 |    3.0974 |    7.6389 |              -4.5415 |  -5.9339 |  -3.4308 |         2.5125 |         3.6146 |                   -1.1022 |      -1.3483 |      -0.8133 |    0.2943 |    0.0021 |               0.2922 |  0.2206 |  0.3581 |        0.401  |        0.8819 |                  -0.481  |     -0.5655 |     -0.3944 |        0.3521 |        0.719  |                  -0.3669 |     -0.5145 |     -0.2355 |        0.0001 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | cau_dmd   |      30 |    1.3291 |    9.266  |              -7.9368 |  -8.4049 |  -7.482  |         0.4959 |         0.872  |                   -0.3761 |      -0.431  |      -0.3229 |    0.1345 |    0.1587 |              -0.0242 | -0.0356 | -0.0145 |        0.238  |        0.3834 |                  -0.1455 |     -0.1664 |     -0.1185 |        0.9841 |        3.199  |                  -2.2149 |     -2.3496 |     -2.0492 |        0.1317 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | cau_unemb |      30 |    0.7484 |    1.275  |              -0.5266 |  -0.6269 |  -0.4288 |         0.3292 |         0.4028 |                   -0.0736 |      -0.1185 |      -0.0201 |    0.1113 |    0.1336 |              -0.0223 | -0.0348 | -0.0071 |        0.1517 |        0.1584 |                  -0.0067 |     -0.0318 |      0.0221 |        0.6034 |        0.7776 |                  -0.1742 |     -0.2394 |     -0.0988 |        0.0067 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | dua_ctx   |      30 |    8.982  |   13.3862 |              -4.4042 |  -4.8688 |  -3.8501 |         0.3865 |         0.5846 |                   -0.1982 |      -0.2292 |      -0.1703 |    0.1033 |    0.1201 |              -0.0169 | -0.0302 | -0.0011 |        0.0604 |        0.1979 |                  -0.1375 |     -0.1545 |     -0.1206 |        7.3806 |        8.401  |                  -1.0204 |     -1.6897 |     -0.343  |        0.1756 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | dua_dmd   |      30 |    1.3302 |    1.0901 |               0.2401 |   0.1187 |   0.3521 |         0.2301 |         0.1227 |                    0.1073 |       0.0639 |       0.1541 |    0.0619 |    0.0559 |               0.006  | -0.0068 |  0.0188 |        0.0354 |        0.0869 |                  -0.0516 |     -0.0628 |     -0.0387 |        1.2302 |        0.7455 |                   0.4847 |      0.3769 |      0.6086 |        0.1148 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | dua_unemb |      30 |    2.0112 |    0.7043 |               1.3069 |   1.1312 |   1.5069 |         0.2173 |         0.0485 |                    0.1688 |       0.1415 |       0.2025 |    0.0465 |    0.017  |               0.0295 |  0.0203 |  0.0422 |        0.0591 |        0.0353 |                   0.0238 |      0.0047 |      0.0421 |        1.8965 |        0.583  |                   1.3135 |      1.1263 |      1.5272 |        0.0059 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | euc_ctx   |      30 |    1.1472 |    1.8493 |              -0.7021 |  -0.8412 |  -0.5755 |         0.4004 |         0.5391 |                   -0.1387 |      -0.1737 |      -0.1114 |    0.1228 |    0.1473 |              -0.0245 | -0.0443 | -0.007  |        0.1651 |        0.2966 |                  -0.1314 |     -0.1549 |     -0.1078 |        0.9991 |        1.0584 |                  -0.0594 |     -0.1618 |      0.0392 |        0.1567 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | euc_dmd   |      30 |    1.5544 |    2.6609 |              -1.1064 |  -1.2343 |  -0.9641 |         0.548  |         0.6049 |                   -0.0569 |      -0.1066 |      -0.002  |    0.1508 |    0.1492 |               0.0016 | -0.0157 |  0.0197 |        0.2359 |        0.3602 |                  -0.1243 |     -0.1548 |     -0.0904 |        1.203  |        1.0522 |                   0.1509 |      0.0398 |      0.2565 |        0.2137 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | euc_unemb |      30 |    1.5122 |    0.3018 |               1.2104 |   1.1027 |   1.3335 |         0.5587 |         0.1466 |                    0.4121 |       0.3103 |       0.5413 |    0.1568 |    0.0802 |               0.0766 |  0.0454 |  0.1137 |        0.1426 |        0.0949 |                   0.0476 |      0.0165 |      0.0858 |        1.1897 |        0.1885 |                   1.0012 |      0.8946 |      1.0984 |        0.0074 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | frq_dmd   |      30 |    1.4654 |    2.9769 |              -1.5114 |  -1.9167 |  -1.1989 |         0.5313 |         0.6181 |                   -0.0868 |      -0.1499 |      -0.0191 |    0.1534 |    0.1197 |               0.0337 |  0.0102 |  0.0641 |        0.2804 |        0.2318 |                   0.0486 |      0.0029 |      0.0908 |        1.1127 |        1.7973 |                  -0.6846 |     -0.8929 |     -0.4838 |        0.0057 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s0_abs5e-3       | frq_unemb |      12 |    4.4916 |   21.858  |             -17.3663 | -18.0091 | -16.7424 |         0.782  |         0.8902 |                   -0.1082 |      -0.1822 |      -0.0358 |    0.1279 |    0      |               0.1279 |  0.116  |  0.1386 |        0.3989 |        0.4646 |                  -0.0656 |     -0.1336 |     -0.0201 |        2.672  |       11.5165 |                  -8.8445 |     -9.7638 |     -7.7236 |        0      |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | cau_dmd   |      30 |    1.1293 |    1.2849 |              -0.1556 |  -0.2895 |  -0.0155 |         0.4193 |         0.2893 |                    0.13   |       0.0645 |       0.2157 |    0.1185 |    0.1067 |               0.0118 | -0.0053 |  0.0361 |        0.2057 |        0.1762 |                   0.0295 |     -0.0238 |      0.0976 |        0.7854 |        0.8116 |                  -0.0262 |     -0.1467 |      0.076  |        0.1642 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | cau_unemb |      30 |    0.7102 |    0.4472 |               0.263  |   0.2162 |   0.3232 |         0.3015 |         0.1485 |                    0.153  |       0.1135 |       0.2009 |    0.1074 |    0.1038 |               0.0036 | -0.0053 |  0.0136 |        0.148  |        0.0496 |                   0.0984 |      0.0509 |      0.1589 |        0.554  |        0.2793 |                   0.2748 |      0.229  |      0.3255 |        0.0074 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | dua_ctx   |      30 |    8.9479 |   11.6299 |              -2.682  |  -3.254  |  -2.1149 |         0.3979 |         0.4257 |                   -0.0278 |      -0.0642 |       0.0054 |    0.0931 |    0.0951 |              -0.002  | -0.0132 |  0.0082 |        0.067  |        0.139  |                  -0.072  |     -0.0964 |     -0.0496 |        7.3048 |        7.7338 |                  -0.429  |     -1.0823 |      0.2549 |        0.2033 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | dua_dmd   |      30 |    1.3696 |    0.7593 |               0.6103 |   0.5147 |   0.7176 |         0.2287 |         0.0656 |                    0.1631 |       0.1263 |       0.2046 |    0.0648 |    0.0386 |               0.0262 |  0.0125 |  0.0372 |        0.0478 |        0.0596 |                  -0.0118 |     -0.0264 |      0.0046 |        1.2577 |        0.5535 |                   0.7042 |      0.5772 |      0.8542 |        0.1714 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | dua_unemb |      30 |    1.9373 |    0.6275 |               1.3097 |   1.0012 |   1.6277 |         0.2168 |         0.038  |                    0.1788 |       0.1406 |       0.222  |    0.0413 |    0.012  |               0.0293 |  0.0204 |  0.0395 |        0.0654 |        0.0198 |                   0.0455 |      0.0298 |      0.061  |        1.8272 |        0.5147 |                   1.3125 |      1.0101 |      1.6819 |        0.0068 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | euc_ctx   |      30 |    1.0191 |    1.7584 |              -0.7393 |  -1.0003 |  -0.5279 |         0.3345 |         0.3747 |                   -0.0402 |      -0.0898 |       0.0028 |    0.1102 |    0.1154 |              -0.0052 | -0.0216 |  0.0139 |        0.1366 |        0.1887 |                  -0.0521 |     -0.0818 |     -0.016  |        0.8758 |        1.3472 |                  -0.4715 |     -0.7402 |     -0.2604 |        0.1697 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | euc_dmd   |      30 |    1.5191 |    1.5188 |               0.0002 |  -0.18   |   0.1949 |         0.4654 |         0.2642 |                    0.2012 |       0.1539 |       0.2667 |    0.1375 |    0.112  |               0.0255 |  0.0077 |  0.0464 |        0.1802 |        0.2191 |                  -0.0389 |     -0.1046 |      0.0489 |        1.209  |        1.0045 |                   0.2044 |      0.012  |      0.3782 |        0.3124 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | euc_unemb |      30 |    1.5497 |    0.3047 |               1.2451 |   1.0742 |   1.4146 |         0.4848 |         0.0548 |                    0.43   |       0.3713 |       0.4899 |    0.1346 |    0.0704 |               0.0642 |  0.0507 |  0.0763 |        0.1377 |        0.0598 |                   0.0779 |      0.0368 |      0.1301 |        1.2376 |        0.1978 |                   1.0398 |      0.8559 |      1.2173 |        0.005  |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | frq_dmd   |      30 |    1.2441 |    0.064  |               1.1801 |   1.0748 |   1.292  |         0.4297 |         0.0276 |                    0.4021 |       0.3095 |       0.4984 |    0.1308 |    0.0396 |               0.0912 |  0.0682 |  0.1236 |        0.2067 |        0.0245 |                   0.1821 |      0.13   |      0.2414 |        0.9397 |        0.0405 |                   0.8992 |      0.8304 |      0.9734 |        0.0072 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s1_abs5e-3       | frq_unemb |      21 |    6.3904 |   21.5864 |             -15.196  | -16.1278 | -14.0503 |         0.8843 |         0.9334 |                   -0.0491 |      -0.0908 |      -0.0088 |    0.1289 |    0.1295 |              -0.0006 | -0.0057 |  0.0086 |        0.4016 |        0.4334 |                  -0.0318 |     -0.06   |     -0.0043 |        3.8545 |       12.0858 |                  -8.2313 |     -8.9471 |     -7.2837 |        0.0307 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | cau_dmd   |      30 |    1.1938 |    2.9648 |              -1.771  |  -1.9559 |  -1.5832 |         0.4487 |         0.4942 |                   -0.0455 |      -0.12   |       0.0315 |    0.1302 |    0.1422 |              -0.012  | -0.0314 |  0.0036 |        0.2429 |        0.2971 |                  -0.0542 |     -0.0895 |     -0.0146 |        0.8269 |        1.5805 |                  -0.7536 |     -0.8657 |     -0.647  |        0.2496 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | cau_unemb |      30 |    0.726  |    1.7439 |              -1.0178 |  -1.1495 |  -0.8763 |         0.3204 |         0.4093 |                   -0.0888 |      -0.1248 |      -0.049  |    0.1249 |    0.1269 |              -0.0021 | -0.0155 |  0.0117 |        0.1815 |        0.0767 |                   0.1048 |      0.0806 |      0.1333 |        0.5479 |        1.0862 |                  -0.5382 |     -0.6264 |     -0.4538 |        0.0047 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | dua_ctx   |      30 |    8.6099 |   11.101  |              -2.4912 |  -2.9635 |  -1.9399 |         0.3516 |         0.4432 |                   -0.0916 |      -0.1212 |      -0.0632 |    0.0875 |    0.0913 |              -0.0038 | -0.0131 |  0.0062 |        0.0514 |        0.0951 |                  -0.0437 |     -0.0552 |     -0.0334 |        7.2193 |        7.4054 |                  -0.1861 |     -0.7292 |      0.3039 |        0.3318 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | dua_dmd   |      30 |    1.5396 |    0.8681 |               0.6715 |   0.559  |   0.8003 |         0.2186 |         0.0883 |                    0.1303 |       0.1035 |       0.1581 |    0.0727 |    0.0402 |               0.0325 |  0.0226 |  0.043  |        0.0502 |        0.066  |                  -0.0158 |     -0.0356 |      0.0021 |        1.4112 |        0.6428 |                   0.7684 |      0.6114 |      0.9515 |        0.1172 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | dua_unemb |      30 |    2.2913 |    0.8606 |               1.4308 |   1.1255 |   1.7262 |         0.2324 |         0.0521 |                    0.1804 |       0.1509 |       0.2173 |    0.0486 |    0.0245 |               0.024  |  0.0144 |  0.0357 |        0.0553 |        0.0222 |                   0.0332 |      0.0217 |      0.0467 |        2.1621 |        0.7122 |                   1.4499 |      1.1359 |      1.7894 |        0.0046 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | euc_ctx   |      30 |    1.0091 |    2.0962 |              -1.0871 |  -1.2129 |  -0.9495 |         0.3375 |         0.3933 |                   -0.0557 |      -0.1035 |      -0.0047 |    0.1154 |    0.1162 |              -0.0009 | -0.0192 |  0.0172 |        0.1693 |        0.1796 |                  -0.0103 |     -0.0365 |      0.0172 |        0.86   |        1.2652 |                  -0.4052 |     -0.4737 |     -0.3395 |        0.3315 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | euc_dmd   |      30 |    1.4039 |    1.969  |              -0.5652 |  -0.7363 |  -0.3887 |         0.4854 |         0.4247 |                    0.0606 |      -0.0008 |       0.1172 |    0.1491 |    0.14   |               0.0091 | -0.005  |  0.0236 |        0.2257 |        0.326  |                  -0.1003 |     -0.1377 |     -0.0609 |        1.0727 |        1.1641 |                  -0.0914 |     -0.2195 |      0.0354 |        0.2188 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | euc_unemb |      30 |    1.3806 |    0.3371 |               1.0435 |   0.944  |   1.1897 |         0.5036 |         0.133  |                    0.3706 |       0.2964 |       0.4557 |    0.139  |    0.0746 |               0.0644 |  0.0376 |  0.0974 |        0.1717 |        0.0974 |                   0.0743 |      0.0438 |      0.1093 |        1.0487 |        0.2223 |                   0.8265 |      0.7417 |      0.9491 |        0.005  |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | frq_dmd   |      30 |    1.1259 |    0.3179 |               0.8081 |   0.7301 |   0.8781 |         0.4094 |         0.1458 |                    0.2636 |       0.2162 |       0.3139 |    0.1307 |    0.0758 |               0.0549 |  0.0401 |  0.0706 |        0.2137 |        0.0858 |                   0.1279 |      0.1036 |      0.1538 |        0.8668 |        0.1917 |                   0.6751 |      0.5935 |      0.7496 |        0.0046 |
| gpt2_A_third_a5e-3    | runs/gpt2_v5/A_s2_abs5e-3       | frq_unemb |      16 |    6.5638 |   21.758  |             -15.1942 | -15.9396 | -14.3524 |         0.8957 |         0.9392 |                   -0.0435 |      -0.097  |      -0.0049 |    0.1286 |    0.0926 |               0.036  |  0.0297 |  0.041  |        0.4115 |        0.4466 |                  -0.0351 |     -0.1008 |     -0.003  |        3.6873 |       11.8438 |                  -8.1565 |     -9.2362 |     -7.1784 |        0.0017 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | cau_ctx   |      30 |    3.1167 |    5.6447 |              -2.528  |  -2.8623 |  -2.1956 |         1.1179 |         1.4106 |                   -0.2926 |      -0.3513 |      -0.2281 |    0.2376 |    0.2517 |              -0.0141 | -0.025  | -0.0046 |        0.1833 |        0.4054 |                  -0.222  |     -0.2829 |     -0.1564 |        1.9328 |        2.7248 |                  -0.7919 |     -0.9274 |     -0.6956 |        0.144  |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | cau_dmd   |      30 |    0.8267 |    1.4377 |              -0.611  |  -0.7686 |  -0.5044 |         0.3817 |         0.6587 |                   -0.277  |      -0.3309 |      -0.216  |    0.119  |    0.1921 |              -0.073  | -0.1023 | -0.0399 |        0.12   |        0.2519 |                  -0.132  |     -0.1598 |     -0.1125 |        0.4937 |        0.4519 |                   0.0418 |     -0.012  |      0.0947 |        0.1727 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | cau_unemb |      30 |    0.6402 |    0.0537 |               0.5865 |   0.5058 |   0.665  |         0.3408 |         0.0335 |                    0.3072 |       0.2569 |       0.3584 |    0.1471 |    0.0561 |               0.0911 |  0.0698 |  0.1139 |        0.0923 |        0.0211 |                   0.0713 |      0.042  |      0.1083 |        0.4397 |        0.0243 |                   0.4154 |      0.3545 |      0.472  |        0.011  |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | dua_ctx   |      30 |    4.4123 |    4.135  |               0.2773 |  -0.0158 |   0.6358 |         0.6144 |         0.5394 |                    0.075  |       0.0318 |       0.1272 |    0.09   |    0.0836 |               0.0063 | -0.01   |  0.0254 |        0.1542 |        0.237  |                  -0.0828 |     -0.098  |     -0.0626 |        3.8483 |        2.5536 |                   1.2946 |      1.0175 |      1.5543 |        0.1452 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | dua_dmd   |      30 |    0.6883 |    0.5705 |               0.1177 |   0.0732 |   0.1627 |         0.2157 |         0.1982 |                    0.0175 |      -0.0132 |       0.0446 |    0.0587 |    0.0733 |              -0.0145 | -0.0372 |  0.0065 |        0.0313 |        0.1025 |                  -0.0712 |     -0.0836 |     -0.0624 |        0.6001 |        0.2538 |                   0.3463 |      0.2885 |      0.4202 |        0.1125 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | dua_unemb |      30 |    1.7075 |    0.1024 |               1.6052 |   1.3678 |   1.8186 |         0.2835 |         0.0295 |                    0.254  |       0.2216 |       0.2794 |    0.0728 |    0.0213 |               0.0514 |  0.0315 |  0.073  |        0.0723 |        0.0105 |                   0.0618 |      0.0467 |      0.0779 |        1.5261 |        0.0741 |                   1.452  |      1.2244 |      1.6301 |        0.0128 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | euc_ctx   |      30 |    0.8335 |    0.7996 |               0.0339 |  -0.0432 |   0.1199 |         0.3803 |         0.4043 |                   -0.024  |      -0.0915 |       0.0461 |    0.1116 |    0.1588 |              -0.0472 | -0.0833 | -0.0023 |        0.1025 |        0.1572 |                  -0.0547 |     -0.081  |     -0.0211 |        0.709  |        0.4077 |                   0.3013 |      0.2566 |      0.3519 |        0.1155 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | euc_dmd   |      30 |    0.8    |    1.2817 |              -0.4817 |  -0.5951 |  -0.377  |         0.3599 |         0.6497 |                   -0.2898 |      -0.3439 |      -0.2252 |    0.115  |    0.2029 |              -0.0879 | -0.1185 | -0.053  |        0.0983 |        0.2696 |                  -0.1713 |     -0.1979 |     -0.1424 |        0.5407 |        0.458  |                   0.0828 |      0.0111 |      0.1553 |        0.1739 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | euc_unemb |      30 |    0.7957 |    0.0694 |               0.7263 |   0.6308 |   0.8114 |         0.3912 |         0.0503 |                    0.3409 |       0.2937 |       0.3908 |    0.1474 |    0.056  |               0.0914 |  0.0743 |  0.1114 |        0.0685 |        0.0296 |                   0.0389 |      0.021  |      0.0645 |        0.5389 |        0.0345 |                   0.5044 |      0.4414 |      0.5637 |        0.0119 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | frq_dmd   |      30 |    7.839  |    8.4261 |              -0.5871 |  -1.3185 |   0.0091 |         1.5999 |         1.4063 |                    0.1936 |       0.141  |       0.2463 |    0.1537 |    0.1017 |               0.052  |  0.0243 |  0.0846 |        0.5806 |        0.5424 |                   0.0381 |      0.0168 |      0.057  |        3.4913 |        3.5036 |                  -0.0123 |     -0.4285 |      0.3042 |        0.0184 |
| gemma4b_A_third_a5e-3 | runs/gemma4b_v5/A_s0_abs5e-3    | frq_unemb |      30 |    2.2906 |    8.9255 |              -6.6349 |  -7.5582 |  -5.5289 |         1.1151 |         1.6731 |                   -0.558  |      -0.6152 |      -0.4872 |    0.1168 |    0.0143 |               0.1025 |  0.0816 |  0.1186 |        0.1714 |        0.592  |                  -0.4205 |     -0.477  |     -0.3557 |        0.7933 |        3.9309 |                  -3.1376 |     -3.55   |     -2.7185 |        0.0117 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | cau_ctx   |      30 |    4.4422 |    6.314  |              -1.8718 |  -3.1224 |  -0.7474 |         1.5255 |         1.5031 |                    0.0224 |      -0.046  |       0.0962 |    0.2668 |    0.2376 |               0.0292 |  0.0111 |  0.0481 |        0.4669 |        0.5054 |                  -0.0385 |     -0.0651 |     -0.0144 |        2.5813 |        2.8692 |                  -0.288  |     -0.5804 |     -0.0385 |        0.0036 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | cau_dmd   |      30 |    6.3263 |    7.7934 |              -1.4671 |  -2.2031 |  -0.7877 |         1.746  |         1.1997 |                    0.5463 |       0.4302 |       0.682  |    0.2786 |    0.2201 |               0.0585 |  0.0386 |  0.0854 |        0.5408 |        0.2982 |                   0.2426 |      0.1158 |      0.347  |        2.8947 |        1.9559 |                   0.9388 |      0.7514 |      1.1181 |        0.0013 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | cau_unemb |      30 |    1.0534 |    0.1655 |               0.8879 |   0.7536 |   1.0079 |         0.6201 |         0.0915 |                    0.5286 |       0.3953 |       0.6619 |    0.226  |    0.0852 |               0.1408 |  0.0849 |  0.1852 |        0.095  |        0.0602 |                   0.0347 |      0.0077 |      0.0641 |        0.5877 |        0.0579 |                   0.5297 |      0.423  |      0.6322 |        0.0071 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | dua_ctx   |      30 |    5.2505 |    2.5439 |               2.7066 |   2.3223 |   3.133  |         0.8834 |         0.4    |                    0.4834 |       0.4317 |       0.5422 |    0.1318 |    0.0826 |               0.0492 |  0.0208 |  0.0805 |        0.3563 |        0.1763 |                   0.1801 |      0.1539 |      0.2105 |        4.0664 |        1.593  |                   2.4734 |      2.0978 |      2.9063 |        0.0125 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | dua_dmd   |      30 |    2.7396 |    1.9464 |               0.7932 |   0.5517 |   1.0666 |         0.7779 |         0.3307 |                    0.4472 |       0.3763 |       0.5242 |    0.165  |    0.1132 |               0.0518 |  0.0195 |  0.0866 |        0.2661 |        0.0645 |                   0.2016 |      0.1553 |      0.2464 |        1.6523 |        0.7119 |                   0.9404 |      0.7149 |      1.148  |        0.0074 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | dua_unemb |      30 |    1.7817 |    0.2514 |               1.5303 |   1.2423 |   1.8455 |         0.3736 |         0.0603 |                    0.3133 |       0.2717 |       0.3546 |    0.0664 |    0.0226 |               0.0438 |  0.0322 |  0.0584 |        0.0414 |        0.0374 |                   0.004  |     -0.0049 |      0.014  |        1.5417 |        0.1485 |                   1.3932 |      1.109  |      1.6815 |        0.0071 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | euc_ctx   |      30 |    2.5402 |    1.1681 |               1.3722 |   1.1706 |   1.5925 |         1.2151 |         0.5596 |                    0.6554 |       0.5192 |       0.8152 |    0.2634 |    0.1961 |               0.0673 |  0.0348 |  0.0985 |        0.3062 |        0.1856 |                   0.1206 |      0.0612 |      0.1889 |        1.6314 |        0.5622 |                   1.0692 |      0.8916 |      1.2654 |        0.0081 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | euc_dmd   |      30 |    4.6258 |    6.9467 |              -2.321  |  -3.0775 |  -1.6228 |         1.5839 |         1.1307 |                    0.4532 |       0.3439 |       0.5906 |    0.2779 |    0.2202 |               0.0577 |  0.0351 |  0.085  |        0.4597 |        0.2892 |                   0.1705 |      0.0464 |      0.2736 |        2.3026 |        1.7392 |                   0.5634 |      0.4091 |      0.7122 |        0.0014 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | euc_unemb |      30 |    1.1465 |    0.171  |               0.9755 |   0.8549 |   1.0922 |         0.6859 |         0.0922 |                    0.5937 |       0.4726 |       0.7088 |    0.2408 |    0.0884 |               0.1524 |  0.1064 |  0.1937 |        0.1065 |        0.0581 |                   0.0484 |      0.0302 |      0.0656 |        0.6445 |        0.0614 |                   0.5831 |      0.4763 |      0.6824 |        0.0068 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | frq_dmd   |      30 |    9.4911 |    1.6857 |               7.8054 |   6.7184 |   8.8866 |         1.8299 |         0.7756 |                    1.0543 |       0.8387 |       1.2002 |    0.249  |    0.1697 |               0.0793 |  0.0524 |  0.0964 |        0.5627 |        0.2733 |                   0.2894 |      0.1937 |      0.3859 |        4.4429 |        0.8599 |                   3.5829 |      3.1471 |      3.9652 |        0.0066 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s0_abs5e-3  | frq_unemb |      30 |    1.7896 |    0.5276 |               1.262  |   1.1127 |   1.3884 |         0.9838 |         0.2835 |                    0.7003 |       0.6337 |       0.762  |    0.1554 |    0.0101 |               0.1452 |  0.13   |  0.1609 |        0.2965 |        0.1508 |                   0.1457 |      0.0719 |      0.2356 |        0.2099 |        0.3147 |                  -0.1048 |     -0.1941 |     -0.0229 |        0.0064 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | cau_ctx   |      30 |    5.11   |    2.7383 |               2.3717 |   2.0669 |   2.735  |         1.6188 |         1.0684 |                    0.5503 |       0.4456 |       0.6609 |    0.266  |    0.221  |               0.045  |  0.028  |  0.0615 |        0.4824 |        0.3442 |                   0.1382 |      0.105  |      0.1735 |        2.9264 |        1.3913 |                   1.535  |      1.2869 |      1.8361 |        0.1086 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | cau_dmd   |      30 |    6.4019 |    4.7021 |               1.6998 |   1.1107 |   2.3728 |         1.7315 |         1.0247 |                    0.7068 |       0.5809 |       0.8356 |    0.2699 |    0.1919 |               0.078  |  0.057  |  0.0994 |        0.5031 |        0.2015 |                   0.3016 |      0.2423 |      0.3614 |        3.0323 |        1.8084 |                   1.2239 |      0.8882 |      1.6245 |        0.0853 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | cau_unemb |      30 |    1.0417 |    0.1412 |               0.9005 |   0.8026 |   1.0059 |         0.6267 |         0.082  |                    0.5448 |       0.4443 |       0.6497 |    0.1807 |    0.0961 |               0.0846 |  0.0483 |  0.1251 |        0.0919 |        0.0425 |                   0.0494 |      0.0326 |      0.0667 |        0.5514 |        0.0636 |                   0.4878 |      0.4034 |      0.5791 |        0.0047 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | dua_ctx   |      30 |    5.3285 |    3.6203 |               1.7082 |   1.4855 |   1.9421 |         0.948  |         0.5819 |                    0.3661 |       0.3046 |       0.4547 |    0.151  |    0.0964 |               0.0546 |  0.0225 |  0.0847 |        0.334  |        0.2385 |                   0.0955 |      0.0757 |      0.1141 |        4.2842 |        2.3169 |                   1.9673 |      1.7483 |      2.1964 |        0.1311 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | dua_dmd   |      30 |    3.3316 |    2.7122 |               0.6194 |   0.3578 |   0.8345 |         0.9057 |         0.4451 |                    0.4606 |       0.3929 |       0.5435 |    0.1999 |    0.1326 |               0.0673 |  0.0465 |  0.0926 |        0.2502 |        0.0745 |                   0.1757 |      0.1449 |      0.2046 |        2.1544 |        1.2484 |                   0.906  |      0.7074 |      1.1079 |        0.204  |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | dua_unemb |      30 |    2.1141 |    0.3216 |               1.7925 |   1.4609 |   2.1604 |         0.4269 |         0.067  |                    0.3599 |       0.3108 |       0.4147 |    0.086  |    0.0313 |               0.0547 |  0.0362 |  0.0741 |        0.0423 |        0.0255 |                   0.0168 |      0.0018 |      0.0346 |        1.8289 |        0.2053 |                   1.6235 |      1.3385 |      1.952  |        0.0035 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | euc_ctx   |      30 |    2.7164 |    1.3377 |               1.3787 |   1.2203 |   1.5861 |         1.2822 |         0.6573 |                    0.6249 |       0.4919 |       0.7856 |    0.2613 |    0.1797 |               0.0815 |  0.0541 |  0.1091 |        0.3279 |        0.2267 |                   0.1012 |      0.0552 |      0.14   |        1.6887 |        0.7421 |                   0.9467 |      0.8258 |      1.1009 |        0.0846 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | euc_dmd   |      30 |    4.3766 |    4.6855 |              -0.3089 |  -0.8267 |   0.2985 |         1.5526 |         1.025  |                    0.5275 |       0.4018 |       0.6621 |    0.2725 |    0.1951 |               0.0774 |  0.0576 |  0.1    |        0.3845 |        0.1706 |                   0.2139 |      0.1322 |      0.2871 |        2.1799 |        1.9806 |                   0.1993 |     -0.1122 |      0.5636 |        0.1149 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | euc_unemb |      30 |    1.1702 |    0.1741 |               0.9961 |   0.8777 |   1.1306 |         0.7192 |         0.1021 |                    0.617  |       0.499  |       0.7529 |    0.2211 |    0.1013 |               0.1198 |  0.0848 |  0.159  |        0.0854 |        0.051  |                   0.0344 |      0.0171 |      0.0542 |        0.635  |        0.0822 |                   0.5528 |      0.4625 |      0.6366 |        0.0049 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | frq_dmd   |      30 |    4.3629 |    3.3472 |               1.0157 |   0.5824 |   1.485  |         1.5391 |         1.2627 |                    0.2764 |       0.1689 |       0.391  |    0.2164 |    0.1651 |               0.0513 |  0.0319 |  0.0692 |        0.4149 |        0.4513 |                  -0.0365 |     -0.0709 |      0.0066 |        2.172  |        1.7506 |                   0.4214 |      0.2001 |      0.6563 |        0.0205 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s1_abs5e-3  | frq_unemb |      30 |    1.7846 |    0.3371 |               1.4475 |   1.3384 |   1.5626 |         1.003  |         0.2199 |                    0.7831 |       0.73   |       0.8418 |    0.1564 |    0.011  |               0.1453 |  0.1155 |  0.1748 |        0.3035 |        0.1316 |                   0.1719 |      0.0956 |      0.2395 |        0.2609 |        0.2439 |                   0.017  |     -0.0354 |      0.0771 |        0.0045 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | cau_ctx   |      30 |    4.4552 |    4.0737 |               0.3814 |  -0.0877 |   0.8149 |         1.4007 |         1.0481 |                    0.3526 |       0.2959 |       0.4322 |    0.2362 |    0.2067 |               0.0295 |  0.0165 |  0.0458 |        0.4224 |        0.3391 |                   0.0833 |      0.0444 |      0.1263 |        2.6502 |        2.1701 |                   0.4801 |      0.245  |      0.7411 |        0.1995 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | cau_dmd   |      30 |    6.3774 |    6.073  |               0.3044 |  -0.0934 |   0.6921 |         1.5352 |         1.1708 |                    0.3644 |       0.2854 |       0.4503 |    0.2438 |    0.2078 |               0.036  |  0.0202 |  0.0526 |        0.462  |        0.3619 |                   0.1001 |      0.0423 |      0.15   |        3.1757 |        2.6513 |                   0.5244 |      0.2716 |      0.8205 |        0.068  |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | cau_unemb |      30 |    0.951  |    0.1503 |               0.8007 |   0.7226 |   0.8829 |         0.5216 |         0.0883 |                    0.4333 |       0.3602 |       0.5147 |    0.1833 |    0.0938 |               0.0895 |  0.0579 |  0.1244 |        0.0742 |        0.0444 |                   0.0298 |      0.0148 |      0.049  |        0.5215 |        0.069  |                   0.4526 |      0.3941 |      0.5247 |        0.0084 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | dua_ctx   |      30 |    5.2173 |    2.848  |               2.3693 |   1.9921 |   2.8523 |         0.9153 |         0.415  |                    0.5003 |       0.4524 |       0.552  |    0.1644 |    0.0843 |               0.08   |  0.0604 |  0.1021 |        0.3352 |        0.1629 |                   0.1723 |      0.1449 |      0.1975 |        4.2227 |        2.0323 |                   2.1903 |      1.8413 |      2.7096 |        0.1457 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | dua_dmd   |      30 |    3.0135 |    2.6144 |               0.3991 |   0.221  |   0.5872 |         0.7894 |         0.4553 |                    0.3341 |       0.2778 |       0.3939 |    0.1742 |    0.1427 |               0.0315 |  0.0143 |  0.0477 |        0.2282 |        0.118  |                   0.1102 |      0.0705 |      0.1481 |        2.0617 |        1.424  |                   0.6377 |      0.4795 |      0.8209 |        0.1401 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | dua_unemb |      30 |    1.8899 |    0.2496 |               1.6403 |   1.3538 |   2.0316 |         0.3804 |         0.0624 |                    0.3181 |       0.2786 |       0.3688 |    0.0727 |    0.0303 |               0.0424 |  0.0245 |  0.063  |        0.0408 |        0.0204 |                   0.0204 |      0.005  |      0.0423 |        1.6638 |        0.1663 |                   1.4975 |      1.2161 |      1.8638 |        0.0106 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | euc_ctx   |      30 |    2.48   |    1.4973 |               0.9827 |   0.8175 |   1.1754 |         1.0986 |         0.6063 |                    0.4923 |       0.415  |       0.5894 |    0.2375 |    0.1841 |               0.0534 |  0.0364 |  0.0754 |        0.2821 |        0.2276 |                   0.0545 |      0.019  |      0.0937 |        1.5881 |        0.8684 |                   0.7196 |      0.6088 |      0.8625 |        0.1359 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | euc_dmd   |      30 |    3.8607 |    4.2026 |              -0.342  |  -0.7224 |   0.0446 |         1.3257 |         1.0122 |                    0.3135 |       0.2225 |       0.4043 |    0.2431 |    0.2146 |               0.0285 |  0.0144 |  0.0448 |        0.3459 |        0.2845 |                   0.0614 |      0.0045 |      0.1152 |        2.0573 |        1.9756 |                   0.0817 |     -0.1336 |      0.2863 |        0.1138 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | euc_unemb |      30 |    1.0296 |    0.1901 |               0.8395 |   0.7603 |   0.9252 |         0.584  |         0.1199 |                    0.464  |       0.3857 |       0.5426 |    0.1982 |    0.1098 |               0.0884 |  0.0636 |  0.1164 |        0.07   |        0.0524 |                   0.0176 |      0.0019 |      0.0409 |        0.5764 |        0.09   |                   0.4864 |      0.4283 |      0.5577 |        0.0085 |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | frq_dmd   |      30 |    4.2785 |    2.2349 |               2.0436 |   1.5091 |   2.5046 |         1.4166 |         0.878  |                    0.5386 |       0.3609 |       0.7168 |    0.2068 |    0.1701 |               0.0367 |  0.0239 |  0.0546 |        0.4211 |        0.317  |                   0.104  |      0.0169 |      0.198  |        2.1369 |        1.2114 |                   0.9255 |      0.7228 |      1.0951 |        0.01   |
| A_ing_a5e-3           | runs/gemma1b_v5/ing_s2_abs5e-3  | frq_unemb |      30 |    1.6987 |    0.5982 |               1.1005 |   0.8781 |   1.2921 |         0.9189 |         0.3252 |                    0.5937 |       0.488  |       0.675  |    0.1549 |    0.0091 |               0.1458 |  0.127  |  0.1693 |        0.3123 |        0.1668 |                   0.1456 |      0.0841 |      0.2079 |        0.2256 |        0.3726 |                  -0.147  |     -0.2471 |     -0.0469 |        0.0067 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | cau_dmd   |      30 |    6.1496 |    8.4865 |              -2.3369 |  -2.7058 |  -1.9536 |         1.0705 |         0.7092 |                    0.3612 |       0.2847 |       0.4511 |    0.1738 |    0.1387 |               0.0351 |  0.0208 |  0.0487 |        0.4348 |        0.3021 |                   0.1327 |      0.1082 |      0.1559 |        3.9975 |        4.9186 |                  -0.9211 |     -1.3171 |     -0.4848 |        0.3337 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | cau_unemb |      30 |    0.9186 |    0.4673 |               0.4513 |   0.3536 |   0.5396 |         0.4295 |         0.1984 |                    0.2312 |       0.1466 |       0.3121 |    0.1175 |    0.0892 |               0.0283 |  0.0074 |  0.0509 |        0.1498 |        0.0628 |                   0.0871 |      0.0682 |      0.1073 |        0.6849 |        0.2738 |                   0.4111 |      0.3212 |      0.4891 |        0.003  |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | dua_ctx   |      29 |   14.0008 |   14.9777 |              -0.9769 |  -1.4752 |  -0.3914 |         0.7522 |         0.6276 |                    0.1245 |       0.0755 |       0.1669 |    0.1344 |    0.1115 |               0.0229 |  0.01   |  0.036  |        0.2964 |        0.2362 |                   0.0602 |      0.0496 |      0.0704 |        9.6673 |        8.976  |                   0.6913 |      0.1719 |      1.2239 |        0.2239 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | dua_dmd   |      30 |    4.452  |    2.7917 |               1.6603 |   1.3907 |   2.0062 |         0.5519 |         0.1974 |                    0.3545 |       0.3072 |       0.3997 |    0.1153 |    0.0633 |               0.0521 |  0.0337 |  0.0665 |        0.1902 |        0.0506 |                   0.1397 |      0.1192 |      0.1586 |        3.6882 |        1.8375 |                   1.8507 |      1.5347 |      2.2488 |        0.129  |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | dua_unemb |      30 |    2.4987 |    1.0054 |               1.4933 |   1.3233 |   1.6983 |         0.254  |         0.0625 |                    0.1915 |       0.16   |       0.2259 |    0.0452 |    0.0218 |               0.0234 |  0.0157 |  0.03   |        0.0667 |        0.038  |                   0.0286 |      0.0134 |      0.0454 |        2.3126 |        0.8428 |                   1.4698 |      1.2912 |      1.6773 |        0.001  |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | euc_ctx   |      30 |    2.5198 |    2.8627 |              -0.3429 |  -0.6095 |  -0.0849 |         0.769  |         0.715  |                    0.0539 |      -0.0273 |       0.1328 |    0.163  |    0.1516 |               0.0114 | -0.0094 |  0.0327 |        0.2313 |        0.3017 |                  -0.0704 |     -0.0871 |     -0.0536 |        1.928  |        1.7067 |                   0.2212 |      0.0082 |      0.4194 |        0.1973 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | euc_dmd   |      30 |    3.2539 |    3.7986 |              -0.5447 |  -0.8483 |  -0.24   |         0.7673 |         0.662  |                    0.1053 |       0.0196 |       0.2122 |    0.1698 |    0.1413 |               0.0285 |  0.0134 |  0.0459 |        0.1506 |        0.2403 |                  -0.0897 |     -0.131  |     -0.042  |        2.4947 |        2.2693 |                   0.2254 |     -0.0346 |      0.4766 |        0.2174 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | euc_unemb |      30 |    1.5542 |    0.4139 |               1.1403 |   0.9956 |   1.2894 |         0.5245 |         0.1862 |                    0.3384 |       0.2408 |       0.4337 |    0.1262 |    0.083  |               0.0432 |  0.0148 |  0.0687 |        0.1184 |        0.1295 |                  -0.0111 |     -0.0503 |      0.0272 |        1.2952 |        0.2615 |                   1.0336 |      0.9017 |      1.1718 |        0.0027 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | frq_dmd   |      30 |    1.8858 |    0.2162 |               1.6696 |   1.5606 |   1.7686 |         0.6836 |         0.0644 |                    0.6192 |       0.5069 |       0.7366 |    0.1587 |    0.0646 |               0.0941 |  0.068  |  0.1184 |        0.1146 |        0.044  |                   0.0706 |      0.0511 |      0.0916 |        1.3562 |        0.1108 |                   1.2454 |      1.184  |      1.3005 |        0.0025 |
| gpt2_A_ing_a5e-3      | runs/gpt2_v5/ing_s0_abs5e-3     | frq_unemb |      30 |    1.4283 |   18.9396 |             -17.5114 | -17.9416 | -17.187  |         0.5304 |         1.1369 |                   -0.6064 |      -0.7304 |      -0.4919 |    0.1211 |    0.0546 |               0.0665 |  0.0526 |  0.0835 |        0.3256 |        0.4533 |                  -0.1277 |     -0.1724 |     -0.0904 |        0.2572 |       10.3594 |                 -10.1022 |    -10.8535 |     -9.4052 |        0.0016 |

