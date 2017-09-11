from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'T0032   ._SN',
        MapName             = 'map1',
        Location            = 'T0030.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'CH02350クラウス市長',                  # 9
        'CH02360メイベル市長',                  # 10
        'CH02370リラ',                          # 11
        'CH02380ルグラン老人',                  # 12
        'CH02390ジル',                          # 13
        'CH02400ジャン',                        # 14
        'CH02410ダルモア市長',                  # 15
        'CH02420ギルバート',                    # 16
        'CH02430マオ婆さん',                    # 17
        'CH02440グスタフ整備長',                # 18
        'CH02450シード少佐',                    # 19
        'CH02460ヒルダ夫人',                    # 20
        'CH02470執事フィリップ',                # 21
        'CH02480ティオ',                        # 22
        'CH02490エリッサ',                      # 23
        'CH02500ポーリィ',                      # 24
        'CH02510ディン',                        # 25
        'CH02520レイス',                        # 26
        'CH02530ロッコ',                        # 27
        'CH02540テス',                          # 28
        'CH02550ハンス',                        # 29
        'CH02560アイナ',                        # 30
        'CH02570テレサ院長',                    # 31
        'CH02580エルナン',                      # 32
        'CH02590クラム',                        # 33
        'CH02600コリンズ校長',                  # 34
        'CH02610キリカ',                        # 35
        'CH02620マードック工房長',              # 36
        'CH02630マリィ',                        # 37
        'CH02640ダニエル',                      # 38
        'CH01600王国軍将校Ｂ',                  # 39
        'CH01610特務兵Ｂ',                      # 40
        'CH01620男ブレイサー２',                # 41
        'CH01630女ブレイサー２',                # 42
        'CH01640王国軍兵士',                    # 43
        'CH01650王国軍兵士',                    # 44
        'CH01660男性学者３',                    # 45
        'CH01670若い神父',                      # 46
        'CH01680街中年男２',                    # 47
        'CH01690街中年女２',                    # 48
        'CH01700ネコ\u3000\u3000',              # 49
        'CH01710牛\u3000\u3000\u3000',          # 50
        'CH01720にわとり',                      # 51
        'CH01730はと\u3000\u3000',              # 52
        'CH01740かもめ\u3000',                  # 53
        'CH01750男ブレイサー３',                # 54
        'CH01760男ブレイサー４',                # 55
        'CH01770ウェイトレス１',                # 56
        'CH01780ウェイトレス２',                # 57
        'CH01790特務兵Ｃ中隊長',                # 58
        'CH20020  0',                           # 59
        'CH20020  1',                           # 60
        'CH20020  2',                           # 61
        'CH20020  3',                           # 62
        'CH20020  4',                           # 63
        'CH20020  5',                           # 64
        'CH20020  6',                           # 65
        'CH20020  7',                           # 66
        'CH20020  8',                           # 67
        'CH20020  9',                           # 68
        'CH20020  10',                          # 69
        'CH20020  11',                          # 70
        'CH20020  12',                          # 71
        'CH20020  13',                          # 72
        'CH20020  14',                          # 73
        'CH20020  15',                          # 74
        'CH20020  16',                          # 75
        'CH20020  17',                          # 76
        'CH20020  18',                          # 77
        'CH20020  19',                          # 78
        'CH20020  20',                          # 79
        'CH20020  21',                          # 80
        'CH20020  22',                          # 81
        'CH20020  23',                          # 82
        'CH20020  24',                          # 83
        'CH20020  25',                          # 84
        'CH20020  26',                          # 85
        'CH20020  27',                          # 86
        'CH20020  28',                          # 87
        'CH20020  29',                          # 88
        'CH20020  30',                          # 89
        'CH20020  31',                          # 90
        'CH20021  0',                           # 91
        'CH20021  1',                           # 92
        'CH20021  2',                           # 93
        'CH20021  3',                           # 94
        'CH20021  4',                           # 95
        'CH20021  5',                           # 96
        'CH20021  6',                           # 97
        'CH20021  7',                           # 98
        'CH20021  8',                           # 99
        'CH20021  9',                           # 100
        'CH20021  10',                          # 101
        'CH20021  11',                          # 102
        'CH20021  12',                          # 103
        'CH20021  13',                          # 104
        'CH20021  14',                          # 105
        'CH20021  15',                          # 106
        'CH20021  16',                          # 107
        'CH20021  17',                          # 108
        'CH20021  18',                          # 109
        'CH20021  19',                          # 110
        'CH20021  20',                          # 111
        'CH20021  21',                          # 112
        'CH20021  22',                          # 113
        'CH20021  23',                          # 114
        'CH20021  24',                          # 115
        'CH20021  25',                          # 116
        'CH20021  26',                          # 117
        'CH20021  27',                          # 118
        'CH20021  28',                          # 119
        'CH20021  29',                          # 120
        'CH20021  30',                          # 121
        'CH20021  31',                          # 122
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02350 ._CH',             # 00
        'ED6_DT07/CH02360 ._CH',             # 01
        'ED6_DT07/CH02370 ._CH',             # 02
        'ED6_DT07/CH02380 ._CH',             # 03
        'ED6_DT07/CH02390 ._CH',             # 04
        'ED6_DT07/CH02400 ._CH',             # 05
        'ED6_DT07/CH02410 ._CH',             # 06
        'ED6_DT07/CH02420 ._CH',             # 07
        'ED6_DT07/CH02430 ._CH',             # 08
        'ED6_DT07/CH02440 ._CH',             # 09
        'ED6_DT07/CH02450 ._CH',             # 0A
        'ED6_DT07/CH02460 ._CH',             # 0B
        'ED6_DT07/CH02470 ._CH',             # 0C
        'ED6_DT07/CH02480 ._CH',             # 0D
        'ED6_DT07/CH02490 ._CH',             # 0E
        'ED6_DT07/CH02500 ._CH',             # 0F
        'ED6_DT07/CH02510 ._CH',             # 10
        'ED6_DT07/CH02520 ._CH',             # 11
        'ED6_DT07/CH02530 ._CH',             # 12
        'ED6_DT07/CH02540 ._CH',             # 13
        'ED6_DT07/CH02550 ._CH',             # 14
        'ED6_DT07/CH02560 ._CH',             # 15
        'ED6_DT07/CH02570 ._CH',             # 16
        'ED6_DT07/CH02580 ._CH',             # 17
        'ED6_DT07/CH02590 ._CH',             # 18
        'ED6_DT07/CH02600 ._CH',             # 19
        'ED6_DT07/CH02610 ._CH',             # 1A
        'ED6_DT07/CH02620 ._CH',             # 1B
        'ED6_DT07/CH02630 ._CH',             # 1C
        'ED6_DT07/CH02640 ._CH',             # 1D
        'ED6_DT07/CH01600 ._CH',             # 1E
        'ED6_DT07/CH01610 ._CH',             # 1F
        'ED6_DT07/CH01620 ._CH',             # 20
        'ED6_DT07/CH01630 ._CH',             # 21
        'ED6_DT07/CH01640 ._CH',             # 22
        'ED6_DT07/CH01650 ._CH',             # 23
        'ED6_DT07/CH01660 ._CH',             # 24
        'ED6_DT07/CH01670 ._CH',             # 25
        'ED6_DT07/CH01680 ._CH',             # 26
        'ED6_DT07/CH01690 ._CH',             # 27
        'ED6_DT07/CH01700 ._CH',             # 28
        'ED6_DT07/CH01710 ._CH',             # 29
        'ED6_DT07/CH01720 ._CH',             # 2A
        'ED6_DT07/CH01730 ._CH',             # 2B
        'ED6_DT07/CH01740 ._CH',             # 2C
        'ED6_DT07/CH01750 ._CH',             # 2D
        'ED6_DT07/CH01760 ._CH',             # 2E
        'ED6_DT07/CH01770 ._CH',             # 2F
        'ED6_DT07/CH01780 ._CH',             # 30
        'ED6_DT07/CH01790 ._CH',             # 31
        'ED6_DT06/CH20020 ._CH',             # 32
        'ED6_DT06/CH20021 ._CH',             # 33
    )

    AddCharChipPat(
        'ED6_DT07/CH02350P._CP',             # 00
        'ED6_DT07/CH02360P._CP',             # 01
        'ED6_DT07/CH02370P._CP',             # 02
        'ED6_DT07/CH02380P._CP',             # 03
        'ED6_DT07/CH02390P._CP',             # 04
        'ED6_DT07/CH02400P._CP',             # 05
        'ED6_DT07/CH02410P._CP',             # 06
        'ED6_DT07/CH02420P._CP',             # 07
        'ED6_DT07/CH02430P._CP',             # 08
        'ED6_DT07/CH02440P._CP',             # 09
        'ED6_DT07/CH02450P._CP',             # 0A
        'ED6_DT07/CH02460P._CP',             # 0B
        'ED6_DT07/CH02470P._CP',             # 0C
        'ED6_DT07/CH02480P._CP',             # 0D
        'ED6_DT07/CH02490P._CP',             # 0E
        'ED6_DT07/CH02500P._CP',             # 0F
        'ED6_DT07/CH02510P._CP',             # 10
        'ED6_DT07/CH02520P._CP',             # 11
        'ED6_DT07/CH02530P._CP',             # 12
        'ED6_DT07/CH02540P._CP',             # 13
        'ED6_DT07/CH02550P._CP',             # 14
        'ED6_DT07/CH02560P._CP',             # 15
        'ED6_DT07/CH02570P._CP',             # 16
        'ED6_DT07/CH02580P._CP',             # 17
        'ED6_DT07/CH02590P._CP',             # 18
        'ED6_DT07/CH02600P._CP',             # 19
        'ED6_DT07/CH02610P._CP',             # 1A
        'ED6_DT07/CH02620P._CP',             # 1B
        'ED6_DT07/CH02630P._CP',             # 1C
        'ED6_DT07/CH02640P._CP',             # 1D
        'ED6_DT07/CH01600P._CP',             # 1E
        'ED6_DT07/CH01610P._CP',             # 1F
        'ED6_DT07/CH01620P._CP',             # 20
        'ED6_DT07/CH01630P._CP',             # 21
        'ED6_DT07/CH01640P._CP',             # 22
        'ED6_DT07/CH01650P._CP',             # 23
        'ED6_DT07/CH01660P._CP',             # 24
        'ED6_DT07/CH01670P._CP',             # 25
        'ED6_DT07/CH01680P._CP',             # 26
        'ED6_DT07/CH01690P._CP',             # 27
        'ED6_DT07/CH01700P._CP',             # 28
        'ED6_DT07/CH01710P._CP',             # 29
        'ED6_DT07/CH01720P._CP',             # 2A
        'ED6_DT07/CH01730P._CP',             # 2B
        'ED6_DT07/CH01740P._CP',             # 2C
        'ED6_DT07/CH01750P._CP',             # 2D
        'ED6_DT07/CH01760P._CP',             # 2E
        'ED6_DT07/CH01770P._CP',             # 2F
        'ED6_DT07/CH01780P._CP',             # 30
        'ED6_DT07/CH01790P._CP',             # 31
        'ED6_DT06/CH20020P._CP',             # 32
        'ED6_DT06/CH20021P._CP',             # 33
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 40000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 40000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 40000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 47,
        ChipIndex           = 0x2F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 40000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 40000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 49,
        ChipIndex           = 0x31,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 50,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65586,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131122,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196658,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262194,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327730,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 393266,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458802,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 18000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 524338,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589874,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 22000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 655410,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 720946,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 26000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 786482,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 852018,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917554,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 48000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 983090,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1048626,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1114162,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1179698,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1245234,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1310770,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1376306,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1441842,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1507378,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 18000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572914,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638450,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 22000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703986,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1769522,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 26000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835058,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1900594,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966130,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2031666,
        ChipIndex           = 0x32,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 51,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65587,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131123,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196659,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262195,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327731,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 393267,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458803,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 18000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 524339,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589875,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 22000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 655411,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 720947,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 26000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 786483,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 852019,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917555,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 52000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 983091,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1048627,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1114163,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1179699,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1245235,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1310771,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1376307,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1441843,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1507379,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 18000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572915,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638451,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 22000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703987,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1769523,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 26000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835059,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1900595,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966131,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2031667,
        ChipIndex           = 0x33,
        NpcIndex            = 0x142,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )


    ScpFunction(
        "Function_0_108A",         # 00, 0
        "Function_1_108B",         # 01, 1
        "Function_2_108C",         # 02, 2
        "Function_3_10A2",         # 03, 3
        "Function_4_10B8",         # 04, 4
        "Function_5_10CE",         # 05, 5
        "Function_6_10F2",         # 06, 6
        "Function_7_1116",         # 07, 7
        "Function_8_1168",         # 08, 8
        "Function_9_11EB",         # 09, 9
        "Function_10_123D",        # 0A, 10
        "Function_11_128F",        # 0B, 11
        "Function_12_1351",        # 0C, 12
        "Function_13_13A3",        # 0D, 13
        "Function_14_1471",        # 0E, 14
        "Function_15_152A",        # 0F, 15
        "Function_16_157C",        # 10, 16
        "Function_17_15C3",        # 11, 17
        "Function_18_1615",        # 12, 18
        "Function_19_1658",        # 13, 19
        "Function_20_169B",        # 14, 20
        "Function_21_16B4",        # 15, 21
        "Function_22_16CD",        # 16, 22
        "Function_23_16E6",        # 17, 23
        "Function_24_16FF",        # 18, 24
        "Function_25_1718",        # 19, 25
        "Function_26_1731",        # 1A, 26
        "Function_27_174A",        # 1B, 27
        "Function_28_179C",        # 1C, 28
        "Function_29_17FD",        # 1D, 29
        "Function_30_1891",        # 1E, 30
        "Function_31_18E3",        # 1F, 31
        "Function_32_1971",        # 20, 32
        "Function_33_19A5",        # 21, 33
        "Function_34_19D9",        # 22, 34
        "Function_35_1A4B",        # 23, 35
    )


    def Function_0_108A(): pass

    label("Function_0_108A")

    Return()

    # Function_0_108A end

    def Function_1_108B(): pass

    label("Function_1_108B")

    Return()

    # Function_1_108B end

    def Function_2_108C(): pass

    label("Function_2_108C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10A1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_108C")

    label("loc_10A1")

    Return()

    # Function_2_108C end

    def Function_3_10A2(): pass

    label("Function_3_10A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10B7")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("Function_3_10A2")

    label("loc_10B7")

    Return()

    # Function_3_10A2 end

    def Function_4_10B8(): pass

    label("Function_4_10B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10CD")
    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("Function_4_10B8")

    label("loc_10CD")

    Return()

    # Function_4_10B8 end

    def Function_5_10CE(): pass

    label("Function_5_10CE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10F1")
    OP_8D(0xFE, 4000, 20000, 24000, 30000, 1500)
    Jump("Function_5_10CE")

    label("loc_10F1")

    Return()

    # Function_5_10CE end

    def Function_6_10F2(): pass

    label("Function_6_10F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1115")
    OP_8D(0xFE, 22000, 20000, 42000, 30000, 1500)
    Jump("Function_6_10F2")

    label("loc_1115")

    Return()

    # Function_6_10F2 end

    def Function_7_1116(): pass

    label("Function_7_1116")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "#600F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "#601F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "#602F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "#603F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "#604F慌て\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1116 end

    def Function_8_1168(): pass

    label("Function_8_1168")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0xFE,
        "#610F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "#611F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "#612F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "#613F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "#614F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "#615F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "#616F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "#617F困り笑顔\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_1168 end

    def Function_9_11EB(): pass

    label("Function_9_11EB")

    TalkBegin(0xFE)

    ChrTalk(    #13
        0xFE,
        "#620F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "#621F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "#622F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "#623F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "#624F睨み\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_11EB end

    def Function_10_123D(): pass

    label("Function_10_123D")

    TalkBegin(0xFE)

    ChrTalk(    #18
        0xFE,
        "#630F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "#631F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "#632F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "#633F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "#634F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_123D end

    def Function_11_128F(): pass

    label("Function_11_128F")

    TalkBegin(0xFE)

    ChrTalk(    #23
        0xFE,
        "#640F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "#641F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "#642F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "#643F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "#644F自信\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "#645F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "#646Fムッ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "#647F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "#648Fウインク\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "#649Fからかい\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "#659Fにやり（…使う？）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_128F end

    def Function_12_1351(): pass

    label("Function_12_1351")

    TalkBegin(0xFE)

    ChrTalk(    #34
        0xFE,
        "#650F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "#651F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "#652F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "#653F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "#654F溜息\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1351 end

    def Function_13_13A3(): pass

    label("Function_13_13A3")

    TalkBegin(0xFE)

    ChrTalk(    #39
        0xFE,
        "#660F通常（表）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "#661F笑顔（表）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "#662F真剣（表裏兼用）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "#663F驚愕１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "#664F瞑目（表裏兼用）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "#665F叫び（表裏兼用）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "#666Fくっ（裏）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "#667F笑顔（裏）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "#668F驚愕２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_13A3 end

    def Function_14_1471(): pass

    label("Function_14_1471")

    TalkBegin(0xFE)

    ChrTalk(    #48
        0xFE,
        "#670F通常（表）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "#671F真剣（表裏兼用）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "#672F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "#673F瞑目（表裏兼用）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "#674F叫び（表裏兼用）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "#675F笑顔（裏）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "#676F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "#677F叫び２（ケガ）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1471 end

    def Function_15_152A(): pass

    label("Function_15_152A")

    TalkBegin(0xFE)

    ChrTalk(    #56
        0xFE,
        "#680F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "#681F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "#682F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "#683F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "#684F怒り\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_152A end

    def Function_16_157C(): pass

    label("Function_16_157C")

    TalkBegin(0xFE)

    ChrTalk(    #61
        0xFE,
        "#690F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "#691F笑顔１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "#692F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "#693F笑顔２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_157C end

    def Function_17_15C3(): pass

    label("Function_17_15C3")

    TalkBegin(0xFE)

    ChrTalk(    #65
        0xFE,
        "#700F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "#701F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "#702F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "#703F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "#704F叫び\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_15C3 end

    def Function_18_1615(): pass

    label("Function_18_1615")

    TalkBegin(0xFE)

    ChrTalk(    #70
        0xFE,
        "#710F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "#711F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "#712F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "#713F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1615 end

    def Function_19_1658(): pass

    label("Function_19_1658")

    TalkBegin(0xFE)

    ChrTalk(    #74
        0xFE,
        "#720F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "#721F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "#722F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "#723F叫び\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_1658 end

    def Function_20_169B(): pass

    label("Function_20_169B")

    TalkBegin(0xFE)

    ChrTalk(    #78
        0xFE,
        "フェイスなし\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_169B end

    def Function_21_16B4(): pass

    label("Function_21_16B4")

    TalkBegin(0xFE)

    ChrTalk(    #79
        0xFE,
        "フェイスなし\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_16B4 end

    def Function_22_16CD(): pass

    label("Function_22_16CD")

    TalkBegin(0xFE)

    ChrTalk(    #80
        0xFE,
        "フェイスなし\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_16CD end

    def Function_23_16E6(): pass

    label("Function_23_16E6")

    TalkBegin(0xFE)

    ChrTalk(    #81
        0xFE,
        "フェイスなし\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_16E6 end

    def Function_24_16FF(): pass

    label("Function_24_16FF")

    TalkBegin(0xFE)

    ChrTalk(    #82
        0xFE,
        "フェイスなし\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_16FF end

    def Function_25_1718(): pass

    label("Function_25_1718")

    TalkBegin(0xFE)

    ChrTalk(    #83
        0xFE,
        "フェイスなし\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_1718 end

    def Function_26_1731(): pass

    label("Function_26_1731")

    TalkBegin(0xFE)

    ChrTalk(    #84
        0xFE,
        "フェイスなし\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_1731 end

    def Function_27_174A(): pass

    label("Function_27_174A")

    TalkBegin(0xFE)

    ChrTalk(    #85
        0xFE,
        "#730F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "#731F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "#732F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "#733F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "#734F溜息\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_174A end

    def Function_28_179C(): pass

    label("Function_28_179C")

    TalkBegin(0xFE)

    ChrTalk(    #90
        0xFE,
        "#740F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "#741F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "#742F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "#743F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "#744F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "#745F溜息\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_179C end

    def Function_29_17FD(): pass

    label("Function_29_17FD")

    TalkBegin(0xFE)

    ChrTalk(    #96
        0xFE,
        "#750F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "#751F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "#752F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "#753F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "#754F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "#755F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "#756F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "#757F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "#758Fうれし泣き\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_17FD end

    def Function_30_1891(): pass

    label("Function_30_1891")

    TalkBegin(0xFE)

    ChrTalk(    #105
        0xFE,
        "#760F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "#761F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "#762F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "#763F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "#764F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_1891 end

    def Function_31_18E3(): pass

    label("Function_31_18E3")

    TalkBegin(0xFE)

    ChrTalk(    #110
        0xFE,
        "#770F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "#771F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "#772F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "#773F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "#774F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "#775F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "#776F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "#777F泣き\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "#778F叫び\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_18E3 end

    def Function_32_1971(): pass

    label("Function_32_1971")

    TalkBegin(0xFE)

    ChrTalk(    #119
        0xFE,
        "#780F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "#781F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "#782F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_1971 end

    def Function_33_19A5(): pass

    label("Function_33_19A5")

    TalkBegin(0xFE)

    ChrTalk(    #122
        0xFE,
        "#790F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "#791F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "#792F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_19A5 end

    def Function_34_19D9(): pass

    label("Function_34_19D9")

    TalkBegin(0xFE)

    ChrTalk(    #125
        0xFE,
        "#800F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "#801F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "#802F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "#803F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "#804F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "#805F慌て\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "#806F遠い目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_19D9 end

    def Function_35_1A4B(): pass

    label("Function_35_1A4B")

    TalkBegin(0xFE)

    ChrTalk(    #132
        0xFE,
        "はにゃ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_1A4B end

    SaveToFile()

Try(main)
